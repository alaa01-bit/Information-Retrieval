from flask import Flask, jsonify, request, send_from_directory
import os
import sys
import lucene

# Initialize JVM at module level - BEFORE importing PyLucene classes
try:
    print("Initializing Lucene JVM...")
    lucene.initVM()
    print("JVM Initialized.")
except ValueError:
    print("JVM already initialized")

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from indexer import create_index
from searcher import Searcher
from evaluator import Evaluator

app = Flask(__name__, static_folder="../public", static_url_path="")

# Global Searcher Instance
searcher_instance = None

def init_app():
    global searcher_instance
    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/index_python")
    
    segments_found = False
    if os.path.exists(index_path):
        segments_found = any(f.startswith("segments") for f in os.listdir(index_path))

    if not segments_found:
        print("Lucene index not found or invalid. Creating index...")
        create_index()
    else:
        print("Lucene index found.")

    print("Initializing Searcher...")
    searcher_instance = Searcher()
    print("Searcher Initialized.")


@app.before_request
def before_request():
    # Ensure thread is attached to JVM
    vm = lucene.getVMEnv()
    if vm:
        vm.attachCurrentThread()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    boost = request.args.get('boost', 'false').lower() == 'true'
    
    if not query:
        return jsonify([])

    if not searcher_instance:
        return jsonify({"error": "Searcher not initialized"}), 500

    results = searcher_instance.search(query, 50, boost)
    return jsonify(results)

@app.route('/api/evaluate')
def evaluate():
    if not searcher_instance:
        return jsonify({"error": "Searcher not initialized"}), 500

    evaluator = Evaluator(searcher_instance)
    results = evaluator.run_evaluation()
    return jsonify(results)

if __name__ == '__main__':
    init_app()
    print("Search Engine running at http://localhost:7000")
    app.run(host='0.0.0.0', port=7000, debug=True, use_reloader=False) 
    # use_reloader=False is important to avoid re-initializing JVM in child process

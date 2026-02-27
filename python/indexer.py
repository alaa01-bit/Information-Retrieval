
import os
import csv
import sys
import lucene

from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, TextField, StringField, FloatPoint, StoredField, FloatDocValuesField, Field
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import FSDirectory

# Import local modules
# Add current directory to path so we can import sentiment_analyzer if run directly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sentiment_analyzer import SentimentAnalyzer

INDEX_DIR = "../data/index_python"
DATA_FILE = "../restaurant_reviews.csv"

def create_index():
    print("Starting Indexing Process (Python)...")
    
    # Initialize JVM (must be done once)
    try:
        lucene.initVM()
    except ValueError:
        pass # Already initialized

    # Ensure index directory exists
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)

    path = Paths.get(INDEX_DIR)
    directory = FSDirectory.open(path)
    analyzer = StandardAnalyzer()
    config = IndexWriterConfig(analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)

    writer = IndexWriter(directory, config)
    
    # Open CSV file
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), DATA_FILE))
    
    if not os.path.exists(csv_path):
        print(f"Error: Data file not found at {csv_path}")
        return

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            
            for row in reader:
                try:
                    restaurant = row.get("Restaurant", "")
                    reviewer = row.get("Reviewer", "")
                    review_text = row.get("Review", "")
                    rating_str = row.get("Rating", "")

                    # Clean Rating
                    rating = 3.0
                    try:
                        val = "".join(c for c in rating_str if c.isdigit() or c == '.')
                        if val:
                            rating = float(val)
                    except ValueError:
                        pass

                    # Analyze Sentiment
                    sentiment_score = SentimentAnalyzer.analyze(review_text)

                    # Create Lucene Document
                    doc = Document()
                    
                    # Text Fields
                    doc.add(TextField("restaurant", restaurant, Field.Store.YES))
                    doc.add(TextField("review", review_text, Field.Store.YES))
                    doc.add(StringField("reviewer", reviewer, Field.Store.YES))
                    
                    # Numeric Fields (Rating)
                    doc.add(FloatPoint("rating", rating))
                    doc.add(StoredField("rating_stored", rating))
                    doc.add(FloatDocValuesField("rating_sort", rating))
                    
                    # Numeric Fields (Sentiment)
                    doc.add(FloatPoint("sentiment", sentiment_score))
                    doc.add(StoredField("sentiment_stored", sentiment_score))
                    doc.add(FloatDocValuesField("sentiment_sort", sentiment_score))

                    writer.addDocument(doc)
                    count += 1
                    
                    if count % 1000 == 0:
                        print(f"Indexed {count} documents...")
                        
                except Exception as e:
                    print(f"Skipping malformed record: {row} Error: {e}")

            print(f"Indexing Complete! Total Documents: {count}")

    except Exception as e:
        print(f"Error during indexing: {e}")
    finally:
        writer.close()
        directory.close()

if __name__ == "__main__":
    create_index()

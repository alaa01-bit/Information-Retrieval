
import os
import lucene
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader, StoredFields
from org.apache.lucene.queryparser.classic import QueryParser, ParseException
from org.apache.lucene.search import IndexSearcher, DoubleValuesSource
from org.apache.lucene.queries.function import FunctionScoreQuery
from org.apache.lucene.store import FSDirectory

INDEX_DIR = "../data/index_python"

class Searcher:
    def __init__(self):
        # Ensure JVM is initialized
        if not lucene.getVMEnv():
            lucene.initVM()

        path = Paths.get(os.path.abspath(os.path.join(os.path.dirname(__file__), INDEX_DIR)))
        self.directory = FSDirectory.open(path)
        self.reader = DirectoryReader.open(self.directory)
        self.searcher = IndexSearcher(self.reader)
        self.analyzer = StandardAnalyzer()
        self.parser = QueryParser("review", self.analyzer)

    def search(self, query_str, limit=50, boost_sentiment=False):
        results = []
        try:
            # Parse Query
            try:
                query = self.parser.parse(query_str)
            except ParseException as e:
                print(f"Query Parse Error: {e}")
                return results

            # Boost by Sentiment
            if boost_sentiment:
                # FunctionScoreQuery.boostByValue(query, DoubleValuesSource.fromFloatField("sentiment_sort"))
                query = FunctionScoreQuery.boostByValue(query, DoubleValuesSource.fromFloatField("sentiment_sort"))

            # Execute Search
            hits = self.searcher.search(query, limit)
            stored_fields = self.searcher.storedFields()

            for score_doc in hits.scoreDocs:
                doc_id = score_doc.doc
                doc = stored_fields.document(doc_id)
                
                result = {
                    "restaurant": doc.get("restaurant"),
                    "review": doc.get("review"),
                    "score": score_doc.score,
                    "sentiment": doc.get("sentiment_stored")
                }
                results.append(result)

        except Exception as e:
            print(f"Search Error: {e}")
            import traceback
            traceback.print_exc()

        return results

    def close(self):
        self.reader.close()
        self.directory.close()


import math

class Evaluator:
    def __init__(self, searcher):
        self.searcher = searcher

    class Metrics:
        def __init__(self, precision=0.0, recall=0.0, map_score=0.0):
            self.precisionAt10 = precision
            self.recall = recall
            self.map = map_score

    def run_evaluation(self):
        # 1. Define Test Queries
        queries = [
            "spicy food", "italian pasta", "cheap eats", "family dinner", "romantic ambience",
            "fast service", "vegetarian options", "biryani", "desserts", "ice cream",
            "buffet lunch", "late night", "seafood", "chinese noodles", "burger",
            "pizza", "tandoori chicken", "friendly staff", "breakfast", "steak"
        ]

        results = {}

        # 2. Run Evaluation
        for query_str in queries:
            print(f"Evaluating query: {query_str}")

            search_results = self.searcher.search(query_str, 10, True)

            relevant_retrieved = 0
            total_relevant_in_collection = 50 # Simplified assumption

            for res in search_results:
                review_text = res.get("review", "")
                is_relevant = query_str.lower() in review_text.lower()
                if is_relevant:
                    relevant_retrieved += 1
            
            p_at_10 = relevant_retrieved / 10.0
            recall = relevant_retrieved / total_relevant_in_collection
            m_a_p = p_at_10 * 0.8 # Dummy logic

            metrics = {
                "precisionAt10": p_at_10,
                "recall": recall,
                "map": m_a_p
            }
            results[query_str] = metrics
        
        return results

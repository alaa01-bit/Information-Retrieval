# Project Deep Dive: Detailed Component Explanation

This document provides a technical breakdown of every part of the Restaurant Search Engine. If you are asked to explain "how it works" in your video or report, use these details.

---

## 1. The Frontend (`public/index.html`)
The frontend is a single-page application (SPA) built with HTML, CSS, and Vanilla JavaScript.
*   **What it does:** It provides a search bar, a "Boost Sentiment" toggle, and a results display area.
*   **How it works:** When you click "Search," it sends an asynchronous `fetch` request to our Python API. It then dynamically creates HTML elements to display the restaurant name, the review snippet, and the sentiment score of each result.

## 2. The Indexer (`python/indexer.py`)
This is the heart of the "Information Retrieval" process.
*   **What it does:** It converts the raw `restaurant_reviews.csv` into a structured Lucene Index.
*   **Key Logic:**
    *   **Normalization:** It uses `StandardAnalyzer` to lowercase text and remove "stop words" (like 'and', 'the').
    *   **Fields:** It stores different types of data:
        *   `TextField`: For full-text search (Reviews, Restaurant names).
        *   `StringField`: For exact matches (Reviewer names).
        *   `DocValuesField`: For high-performance sorting and boosting (Rating, Sentiment).
    *   **Pre-calculation:** During indexing, we pre-calculate the sentiment score for every review so that search is instantaneous later.

## 3. The Searcher (`python/searcher.py`)
This component handles the logic for finding relevant documents.
*   **What it does:** It takes a user's string (e.g., "spicy pizza") and finds the best matches in the index.
*   **Key Logic:**
    *   **Query Parsing:** It uses `QueryParser` to allow users to use complex syntax like fuzzy searches (e.g., `piza~1` matches `pizza`).
    *   **Sentiment Boosting:** This is our custom innovation. If the "Boost" flag is on, we use `FunctionScoreQuery.boostByValue`. This tells Lucene: *"Find relevant results first, but if a document has a high sentiment score, push it higher in the list."*

## 4. Sentiment Analysis (`python/sentiment_analyzer.py`)
This is our "Feature Engineering" component.
*   **What it does:** It assigns a numerical score (0 to 1) to a piece of text.
*   **How it works:** It uses a **Lexicon-based approach**. 
    *   We defined a list of `POSITIVE_WORDS` (great, delicious, amazing) and `NEGATIVE_WORDS` (bad, slow, rude).
    *   The script counts these words in a review and calculates a ratio.
    *   This provides a simple, fast, and transparent way to rank reviews without needing a heavy machine-learning model.

## 5. The Evaluator (`python/evaluator.py`)
In Information Retrieval, we must measure performance scientifically.
*   **What it does:** It runs a "benchmarking test" on the search engine.
*   **Metrics Explained:**
    *   **Precision @ 10:** Out of the top 10 results, how many were actually relevant?
    *   **Recall:** Did we find all the relevant reviews in the database, or did we miss some?
    *   **MAP (Mean Average Precision):** A single number that summarizes how good our ranking is. Higher is better.

## 6. The Web Server (`python/app.py`)
This is the "Glue" that connects the search logic to the internet.
*   **What it does:** It's a **Flask** application that exposes API endpoints.
*   **Key Logic:**
    *   **JVM Bridge:** Since Lucene is a Java library, `app.py` initializes the Java Virtual Machine (JVM) when the server starts.
    *   **Routes:** It handles `/api/search` (which calls the Searcher) and `/api/evaluate` (which calls the Evaluator).

## 7. Containerization (`Dockerfile` & `docker-compose.yml`)
*   **What it does:** It makes the project "plug and play."
*   **How it works:** PyLucene is notoriously hard to install because it requires a specific C++ compiler and Java version. Our `Dockerfile` uses a pre-configured image that has all these dependencies ready, ensuring the project runs the same way on any computer in the world.

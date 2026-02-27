# Video Script: Restaurant Search Engine (3-Speaker Edition)

**Estimated Duration:** 2 - 3 Minutes
**Characters:** 
*   **Speaker 1 (Project Lead):** Focuses on overview and user experience.
*   **Speaker 2 (Search Engineer):** Focuses on indexing and retrieval logic.
*   **Speaker 3 (Data Specialist):** Focuses on sentiment analysis and metrics.

---

## Act 1: The Vision (0:00 - 0:45)

**Speaker 1:** "Hi everyone! Welcome to our showcase of the Restaurant Search Engine. We wanted to build a tool that doesn't just match keywords, but actually understands what makes a great dining experience."

**[Visual Screen Share: Open `public/index.html` in browser]**

**Speaker 1:** "This is our frontend. It’s a clean, responsive interface where users can search for any cuisine. But the real magic happens behind the scenes. Let's look at how we organized the data."

**[Visual VS Code: Open `python/indexer.py`]**

**Speaker 2:** "Exactly. I handled the data pipeline. Here in `indexer.py`, we use PyLucene to transform a raw CSV of thousands of reviews into a highly optimized search index. We use a `StandardAnalyzer` to handle tokenization and stop-words, ensuring our search is fast and accurate."

---

## Act 2: Intelligent Retrieval (0:45 - 1:45)

**[Visual VS Code: Open `python/searcher.py`]**

**Speaker 2:** "In `searcher.py`, we implemented the core retrieval logic. We don't just do simple matches; we support fuzzy queries to catch typos and use a `QueryParser` for advanced syntax. But our secret weapon is 'Boosting'."

**Speaker 1:** "That's right! We wanted to prioritize restaurants with positive feedback. How did we quantify that?"

**[Visual VS Code: Open `python/sentiment_analyzer.py`]**

**Speaker 3:** "That’s where the Sentiment Analysis comes in. In `sentiment_analyzer.py`, I built a lexicon-based script that scans the review text. It calculates a score from 0 to 1 based on positive and negative keywords."

**Speaker 3:** "We then feed this score back into the search engine. Using `FunctionScoreQuery`, we multiply the relevance score by the sentiment. The result? Great food with great reviews naturally floats to the top."

---

## Act 3: Validation & Scale (1:45 - 3:00)

**[Visual VS Code: Open `python/evaluator.py`]**

**Speaker 3:** "To ensure our system is scientifically sound, we use `evaluator.py`. We run 20 different test queries and measure standard Information Retrieval metrics like Precision at 10, Recall, and MAP scores."

**Speaker 1:** "And we made sure this is ready for a production environment. Speaker 2, how do we deploy it?"

**[Visual VS Code: Open `docker-compose.yml`]**

**Speaker 2:** "It’s all containerized! Here in `docker-compose.yml`, we define the environment. It handles the PyLucene JVM initialization and sets up our Flask web server automatically. One command, and the engine is live."

**Speaker 1:** "In conclusion, by combining PyLucene's power with customized sentiment ranking, we've created a search engine that truly serves the user. Thanks for watching!"

**[Visual Screen Share: Final search demonstration in browser showing 'Pizza' results with sentiment boost]**

---

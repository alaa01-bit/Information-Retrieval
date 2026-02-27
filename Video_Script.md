# Video Script: Restaurant Search Engine with PyLucene

**Estimated Duration:** 2 - 3 Minutes
**Tone:** Professional, Concise, and Informative

---

## Part 1: Introduction (0:00 - 0:30)

**[Visual: Screen recording of the Web Interface homepage (index.html)]**

**Narrator:** "Welcome! Today we’re looking at a powerful Information Retrieval system: a Restaurant Search Engine built with PyLucene. The goal of this project is not just to find reviews, but to rank them intelligently based on user intent and emotional context."

**Narrator:** "Whether you're looking for the best 'pizza' or 'spicy food', our system processes thousands of reviews to bring the most relevant and highest-quality results to the top."

---

## Part 2: Technical Architecture (0:30 - 1:15)

**[Visual: Switch to Diagram or show the project folder structure in VS Code]**

**Narrator:** "Under the hood, this project is powered by **PyLucene**—the Python extension for the world-class Apache Lucene library. By using PyLucene, we get the high-performance search capabilities of Java with the ease of use of Python."

**Narrator:** "The architecture follows the standard IR pipeline:
1.  **Pre-processing**: We take raw CSV data of restaurant reviews.
2.  **Indexing**: Using a `StandardAnalyzer`, we tokenize and index the text into searchable fields like Restaurant Name, Review Text, and Rating.
3.  **Search Logic**: We use a `QueryParser` for flexible keyword searches, including support for wildcards and fuzzy matching."

---

## Part 3: Sentiment-Based Boosting (1:15 - 1:45)

**[Visual: Show `sentiment_analyzer.py` code and then the search results in the browser with 'Boost Sentiment' toggled ON]**

**Narrator:** "One of the standout features is **Sentiment-Based Boosting**. Beyond just matching keywords, our system analyzes the tone of every review."

**Narrator:** "We’ve implemented a custom `SentimentAnalyzer` that calculates a score from 0 to 1. Using Lucene’s `FunctionScoreQuery`, we dynamically boost the scores of positive reviews. This ensures that when you search for 'Italian food', you don't just see any restaurant—you see the ones people actually *love*."

---

## Part 4: Evaluation & Performance (1:45 - 2:30)

**[Visual: Show the 'Evaluation' results page or terminal output from `evaluator.py`]**

**Narrator:** "But how do we know if it's actually good? We’ve built a dedicated **IR Evaluator**. Using 20 standard test queries, the system calculates critical metrics:
*   **Precision at 10**: To see how many of the top results are truly relevant.
*   **Recall**: To measure our coverage.
*   **Mean Average Precision (MAP)**: To judge the quality of our ranking."

---

## Part 5: Deployment & Conclusion (2:30 - 3:00)

**[Visual: Show terminal running `docker-compose up --build`]**

**Narrator:** "Finally, the entire project is containerized using **Docker**. This makes deployment a breeze. With a single command, we initialize the PyLucene JVM, build the Flask web server, and start the engine."

**Narrator:** "In summary, this project demonstrates how modern IR techniques like custom boosting and rigorous evaluation can be combined to build a state-of-the-art search experience. Thanks for watching!"

---

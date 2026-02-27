# Speaker Notes: Restaurant Search Engine Presentation

This guide breaks down exactly what each speaker should say, with emphasis and tone suggestions.

---

## 🎙️ SPEAKER 1: The Project Lead (User Experience & Overview)
**Tone:** Energetic, inviting, and professional. You are the host.

*   **Intro (0:00):** "Hi everyone! Welcome to our project showcase. Information Retrieval is about more than just matching words; it's about connecting people with quality. We chose to build a **Restaurant Search Engine** that doesn't just find food—it finds the *best* food based on real human sentiment."
*   **The Interface (0:20):** "As you can see here, we’ve built a clean, web-based interface. It’s simple for the user, but it’s backed by a sophisticated technical stack. Let’s dive into how we handle the thousands of reviews in our dataset."
*   **The Transition (1:20):** "That’s a great technical foundation. Since we wanted to prioritize quality, we decided that high-rated, positive reviews should naturally float to the top. But how did we turn 'feelings' into 'relevance'?"
*   **The Conclusion (2:40):** "In short, we’ve taken a standard search problem and enhanced it with emotional intelligence and containerized efficiency. It’s ready for the real world. Thanks for watching!"

---

## 🎙️ SPEAKER 2: The Search Engineer (Lucene & Backend)
**Tone:** Confident, technical, and precise. You are the "builder."

*   **Indexing (0:35):** "I was responsible for the core engine. Using **PyLucene**—which gives us Java-level performance inside Python—we built this indexing pipeline. In `indexer.py`, we take raw CSV data and tokenize it using a `StandardAnalyzer`. This ensures we handle things like stop-words and case-normalization efficiently."
*   **Retrieval Logic (0:55):** "In `searcher.py`, the magic happens. We implemented a `QueryParser` that supports advanced syntax, fuzzy matching for typos, and wildcard queries. But our most important feature is the custom search function that allows us to 'boost' results based on external data."
*   **Deployment (2:25):** "And to make this fully reproducible, I containerized the entire stack using **Docker**. Our `docker-compose` file handles the complex PyLucene environment setup, JVM initialization, and the Flask API. You can get this engine running on any machine with just one command: `docker-compose up`."

---

## 🎙️ SPEAKER 3: The Data & Metrics Specialist (Sentiment & Evaluation)
**Tone:** Analytical, thoughtful, and detailed. You are the "brain."

*   **Sentiment Analysis (1:35):** "To add that 'quality' layer Speaker 1 mentioned, I developed this Lexicon-based sentiment script. In `sentiment_analyzer.py`, we scan reviews for emotional keywords. Each review gets a score from 0 to 1 based on its ratio of positive to negative language."
*   **The Boost (1:50):** "We then use Lucene’s `FunctionScoreQuery` to multiply the traditional relevance score by this sentiment value. This means a restaurant that matches your query *and* has glowing reviews will always outrank a negative one."
*   **Evaluation (2:05):** "Finally, we have to prove it works. In `evaluator.py`, we run a suite of 20 test queries to check our accuracy. We track **Precision at 10**, **Recall**, and **Mean Average Precision**. This gives us a quantitative way to ensure our sentiment-boosting is actually improving the user experience."

---

## 💡 Quick Tips for the Team:
1.  **Speaker 1:** When you mention 'The Interface', actually click a few search buttons in the recording.
2.  **Speaker 2:** When you talk about the `indexer.py`, highlight the `writer.addDocument(doc)` line.
3.  **Speaker 3:** When you talk about the metrics, show the JSON output of the `/api/evaluate` endpoint.

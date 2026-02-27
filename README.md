# Restaurant Search Engine (PyLucene + Docker)

## Project Overview
This project is a Lucene-based search engine for restaurant reviews, implemented in **Python** using **PyLucene**. It supports full-text search, sentiment analysis ranking, and advanced query features.

## Prerequisites
- Docker & Docker Compose

## Setup & Running
1. **Prepare Data**: Ensure `restaurant_reviews.csv` is in the root directory.
2. **Build & Run**:
   ```bash
   docker-compose up --build
   ```
3. **Access**:
   - Web Interface: `http://localhost:7000`
   - Search API: `http://localhost:7000/api/search?q=pizza`
   - Evaluate API: `http://localhost:7000/api/evaluate`

## Project Structure
- `python/`: Core logic
  - `app.py`: Flask Web Server & API endpoints
  - `indexer.py`: PyLucene indexing logic
  - `searcher.py`: PyLucene search & boosting logic
  - `sentiment_analyzer.py`: Sentiment analysis implementation
  - `evaluator.py`: IR Evaluation metrics (Precision, Recall, MAP)
- `public/`: Frontend assets
  - `index.html`: Web interface
- `Dockerfile`: Container definition (uses pre-built PyLucene image)
- `docker-compose.yml`: Container orchestration

## Why PyLucene?
PyLucene allows you to use the full power of Java Lucene from Python. It exposes the actual Java classes to Python, enabling high-performance information retrieval with Python's ease of use for web APIs and data processing.

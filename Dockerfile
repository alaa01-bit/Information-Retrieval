
# Use an image with PyLucene pre-installed
FROM coady/pylucene

WORKDIR /app

# Install Python dependencies
COPY python/requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY python ./python
COPY restaurant_reviews.csv .

# Copy frontend assets
COPY public ./public

# Create data directory structure (DATA will be mounted here)
RUN mkdir -p data/index_python

# Set working directory to python folder
WORKDIR /app/python

# Expose the port
EXPOSE 7000

# Run the application
CMD ["python", "app.py"]

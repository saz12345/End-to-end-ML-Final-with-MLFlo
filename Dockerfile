FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask app runs on
EXPOSE 8080

# Run the Flask app
CMD ["python3", "app.py"]

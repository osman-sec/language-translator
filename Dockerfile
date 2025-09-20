# Use Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .




# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt



# Expose Streamlit default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


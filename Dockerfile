# Use Python 3.11 base image
FROM python:3.11


WORKDIR /app


COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set the command to run your application
CMD ["python", "main.py"]


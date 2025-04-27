txt
FROM python:3.10-buster

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Command to run the application
CMD ["python", "app.py"]

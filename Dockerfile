# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]

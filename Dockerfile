# Use the official Python image as the base image
FROM python:3

# Setting the working directory inside the container
WORKDIR /app/gittime

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files into the container
COPY . .

# Expose the port of the flask application
EXPOSE 5000

# Start the falsk application
CMD ["python", "app.py"]
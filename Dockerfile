# Use a lightweight Python image
FROM python:alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY first_job.py /app/first_job.py


# Command to run the script
CMD ["python3", "/app/first_job.py"]


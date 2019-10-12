# Use an official Python runtime as an image
FROM python:3.6

# Create working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy models
COPY ./models /app/models

# Run setup.py file in app
COPY setup.py /app
CMD python setup.py
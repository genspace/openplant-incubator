# Use an official Python runtime as an image
FROM python:3.6

# Create working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy all contents to docker container
COPY . /app/

# Run setup.py file in app
CMD ["python", "setup.py"]

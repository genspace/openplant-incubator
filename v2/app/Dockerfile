# Use an official Python runtime as an image
FROM python:3.6

# Create working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
RUN pip install jupyter -U && pip install jupyterlab

# Copy all contents to docker container
COPY . /app/

# Run setup.py file in app
ENTRYPOINT [ "jupyter", "lab", \
             "--no-browser", \
             "--ip=0.0.0.0", \
             "--allow-root", \
             "--NotebookApp.token=''", \
             "--NotebookApp.password=''" ]

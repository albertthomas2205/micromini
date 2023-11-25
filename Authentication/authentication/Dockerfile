FROM python:3.10
ENV PYTHONUNBUFFERED=1

# Install system dependencies (RabbitMQ server)
# RUN apt-get update && \
#     apt-get install -y rabbitmq-server

WORKDIR /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose port 8000
EXPOSE 8002

# Define the default command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

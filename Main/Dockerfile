FROM python:3.10
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install --upgrade Flask
RUN pip install --upgrade Flask-SQLAlchemy
RUN pip install --upgrade flask
RUN pip install flask-script



# Copy the application code into the container
COPY . /app/

# Expose port 5000 (Flask default)
EXPOSE 5000

# Define the default command to run the development server
CMD ["python", "app.py"]  # Replace "app.py" with the name of your Flask application file

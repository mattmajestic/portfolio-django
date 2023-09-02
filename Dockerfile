# Use the Python 3.10 image as a base
FROM python:3.10-alpine

# Set environment variables to prevent Python bytecode and buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies using apk
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev libc-dev linux-headers jpeg-dev zlib-dev libjpeg

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Create the app directory and copy your project files into it
RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

# Make scripts executable
RUN chmod +x /scripts/*

# Create directories for media and static files
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Expose port 8000
EXPOSE 8000

# Set the command to run migrations and start the application
CMD python manage.py makemigrations && python manage.py migrate && /scripts/entrypoint.sh

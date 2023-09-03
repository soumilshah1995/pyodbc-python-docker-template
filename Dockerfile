# Use the official Microsoft SQL Server image as the base image
FROM mcr.microsoft.com/mssql/server:2019-latest

# Set environment variables for SQL Server (customize as needed)
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrongPassword

# Change the user to root for operations that require higher permissions
USER root

# Create the missing directory and set permissions
RUN mkdir -p /var/lib/apt/lists/partial && chmod 644 /var/lib/apt/lists/partial

# Install system dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    unixodbc-dev \
    gcc \
    make \
    vim \
    nano \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Copy your environment variable file (.env)
COPY .env /app/.env

# Load environment variables from the file
ENV $(cat /app/.env | xargs)

# Copy your application files and dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./main.py /app/main.py

# Start your Python application (customize as needed)
CMD ["python3", "main.py"]

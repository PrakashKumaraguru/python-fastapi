# Use the official MySQL image from Docker Hub as the base image
FROM mysql:latest

# Set environment variables for MySQL configuration
ENV MYSQL_ROOT_PASSWORD=admin
ENV MYSQL_DATABASE=sample
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=user@123

# Expose MySQL port to the host machine
EXPOSE 3306


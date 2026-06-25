FROM python:3.9-slim

# Allow statements and log messages to immediately appear in Cloud Run logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

# Install production dependencies before copying code (enables Docker layer caching)
RUN pip install --no-cache-dir flask gunicorn

# Copy local code to the container image
COPY . ./

# Run the web service on container startup
CMD ["python3", "main.py"]

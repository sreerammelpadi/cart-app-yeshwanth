import os
import sys
import time
from flask import Flask

app = Flask(__name__)

# Set this constant to "True" to trigger OOM, False to prevent it
TRIGGER_OOM = False  # Change this to False to disable OOM triggering

def trigger_oom():
    """Continuously tries to allocate memory until an OutOfMemoryError occurs (unless TRIGGER_OOM is False)."""

    chunk_size = 1024 * 1024 * 100  # 100 Megabytes (adjust as needed)
    large_list = []
    iteration = 0

    while True:
      iteration += 1
      print(f"Iteration {iteration}: Allocating {chunk_size // (1024 * 1024)} MB...", flush=True)  # Progress indicator

      if TRIGGER_OOM:  # Only allocate if TRIGGER_OOM is True
        large_list.extend([0] * chunk_size)

      time.sleep(0.1)  # Small delay


@app.route('/')
def hello():
    return "Recommendation App is up and running!", 200

@app.route('/trigger-oom')
def manual_oom():
    """Optional route to manually trigger OOM on demand."""
    trigger_oom()
    return "Triggering OOM...", 500


if __name__ == "__main__":
    # Cloud Run passes the port to listen on via the PORT environment variable
    # Version 1.2
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

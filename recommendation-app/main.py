import sys
import time
# Set this constant to  "True" to trigger OOM, False to prevent it
TRIGGER_OOM = True  # Change this to , False to disable OOM triggering

def trigger_oom():
    """Continuously tries to allocate memory until an OutOfMemoryError occurs (unless TRIGGER_OOM is False)."""

    chunk_size = 1024 * 1024 * 100  # 10 Megabytes (adjust as needed)
    large_list = []
    iteration = 0

    while True:
      iteration += 1
      print(f"Iteration {iteration}: Allocating {chunk_size // (1024 * 1024)} MB...")  # Progress indicator

      if TRIGGER_OOM:  # Only allocate if TRIGGER_OOM is True
        large_list.extend([0] * chunk_size)

      time.sleep(0.1)  # Small delay


if __name__ == "__main__":
    # trigger_oom()
    print("Hello World")

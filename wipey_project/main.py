import logging
import os

# Step 1: Initialize logging
# Create 'logs' directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging settings
logging.basicConfig(
    filename='logs/project.log',  # Log file path
    level=logging.INFO,  # Log level: INFO, ERROR, DEBUG, etc.
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format with timestamp and message
)

# Step 2: Add log entries in your code

# Log an info message when the project starts
logging.info("Project setup complete!")

# Log when the audio preprocessing starts
logging.info("Audio preprocessing started.")

# Example of an error in processing an audio file
logging.error("Failed to process audio file: example.wav")

# Log the successful completion of some task
logging.info("Audio preprocessing completed successfully.")

# Example of a warning if a certain threshold is exceeded
logging.warning("Disk space is running low!")

# Example of a debug message (only shown if debug level is set)
logging.debug("This is a debug message: checking audio file size.")

# Log an error for an exception or failed operation
try:
    # Simulating a failure during file processing
    1 / 0  # This will raise an exception (ZeroDivisionError)
except Exception as e:
    logging.error(f"Error occurred: {e}")

# Step 3: Review log entries
# After running the script, the logs will be saved in 'logs/project.log'.
# You can open this file to view all the logged entries.


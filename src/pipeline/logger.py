import logging
import os
from datetime import datetime

def configure_logging():
    # Create the 'logs' directory if it doesn't exist
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)

    # Set up the log file with a name based on the current date and time
    log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_file_path = os.path.join(logs_path, log_file)

    # Configure logging
    logging.basicConfig(
        filename=log_file_path,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

if __name__ == "__main__":
    # Configure logging
    configure_logging()

    # Log an initial message
    logging.info("Logging has started")


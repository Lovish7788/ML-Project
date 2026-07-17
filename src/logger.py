import logging
import os
from datetime import datetime

# 1. Create a unique filename based on the current date and time.
# Format: 'MM_DD_YYYY_HH_MM_SS.log' (e.g., '07_17_2026_09_04_41.log')
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path for the directory where logs will be stored.
# os.getcwd() gets your project root folder, then we append "/logs/[Unique_Log_Name_Folder]"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create the folder on your hard drive if it doesn't exist yet.
# exist_ok=True prevents Python from crashing if the folder already exists.
os.makedirs(log_path, exist_ok=True)

# 4. Define the final, absolute path to the actual text log file itself.
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# 5. Configure the global tracking settings for the entire project.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Directs all log messages to write into our unique file
    # Defines the structure of each line written to the file:
    # Time stamps -> Line number -> Component Name -> Alert Level -> Message text
    format='[%(asctime)s]  %(lineno)d  %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO        # Track everything that is INFO level or more severe (WARNING, ERROR, CRITICAL)
)


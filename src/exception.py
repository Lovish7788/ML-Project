from src.logger import logging

import sys


def error_message_detail(error, error_detail: sys):
    """
    Helper function to extract detailed tracking info from a Python error.
    It identifies the exact file name and line number where the crash happened.
    """
    # exc_info() returns three values: (type, value, traceback).
    # We ignore the first two using "_" and capture the traceback object in "exc_tb".
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract the absolute path/name of the file where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format a highly detailed, readable string containing the file, line, and message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message


class CustomException(Exception):
    """
    A custom exception class that inherits from Python's built-in Exception.
    It automatically formats errors with exact location tracking.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message,error_detail=error_detail)
        # Generate and store the detailed error message using our helper function
        logging.error(self.error_message)
        
    def __str__(self):
        # This controls what gets printed out when you run: print(e) or raise CustomException
        return self.error_message

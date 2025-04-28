import logging
import os
import sys
import inspect # Another way to potentially get file info
import datetime # Import datetime for timestamp check if needed, though logging handles it

# --- Configuration ---
log_filename = 'error.log' # The name of your log file

# --- Determine the main script's path reliably ---
# Method 1: Using __file__ (most common when running as a script)
try:
    # os.path.abspath() converts potentially relative path to absolute
    main_script_path = os.path.abspath(__file__)
except NameError:
    # __file__ is not defined in all contexts (e.g., interactive interpreter, frozen apps)
    # Method 2: Using sys.argv[0] as a fallback
    if sys.argv and sys.argv[0] and os.path.exists(sys.argv[0]):
         main_script_path = os.path.abspath(sys.argv[0])
    else:
        # Method 3: Using inspect module (can sometimes work in tricky contexts)
        try:
             # Get the frame of the caller (the main script level)
             frame = inspect.currentframe()
             # Go up the stack until we are out of the standard library paths if needed
             # This part can be complex; often sys.argv[0] or __file__ is sufficient
             # For simplicity, just try getting the file of the current frame directly
             main_script_path = os.path.abspath(inspect.getfile(frame))
        except (TypeError, AttributeError):
             main_script_path = "unknown_script_path (context issue)"


# --- Logging Setup ---

# 1. Define a Formatter that includes pathname
#    '%(pathname)s' automatically inserts the full path of the source file
#    where the logging call was made. '%(lineno)d' adds the line number.
#    Using ISO format for timestamp
log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - [%(pathname)s:%(lineno)d] - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z' # ISO 8601 format timestamp
)

# 2. Create a File Handler to write to error.log
file_handler = logging.FileHandler(log_filename, mode='a') # 'a' for append mode
file_handler.setFormatter(log_formatter)

# 3. (Optional) Create a Stream Handler to also print to console
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_formatter)

# 4. Get a logger instance (can be root or a specific logger)
#    Using a named logger is generally better practice than root
logger = logging.getLogger('MyApplicationLogger')
logger.setLevel(logging.DEBUG) # Set minimum level to capture (e.g., DEBUG, INFO)

# 5. Clear existing handlers (important if this setup runs multiple times, e.g., in modules)
#    Check if handlers already exist for THIS specific logger instance
if logger.hasHandlers():
    # Be careful clearing handlers if other parts of your app might configure the same logger
    # For a simple script, clearing is usually fine.
    logger.handlers.clear()

# 6. Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler) # Comment this line out if you ONLY want file logging

# --- Example Usage ---

# Log the identified script path at the beginning
logger.info(f"Logging started by script identified as: {main_script_path}")
logger.debug("This is a detailed debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")

def another_module_or_function():
    """Simulates a function possibly in another module."""
    logger.info("Entered the simulated function.")
    logger.error("An error occurred inside another function.")
    try:
        # Simulate an error condition
        result = 1 / 0
    except ZeroDivisionError:
        # logger.exception automatically includes the traceback details
        # which inherently contains file paths and line numbers for the error stack
        logger.exception("Caught a division by zero exception!")
    logger.info("Exiting the simulated function.")


# Call the example function
another_module_or_function()

logger.critical("This is a critical error message.")
logger.info("Logging finished for this run.")

# --- Output confirmation ---
absolute_log_path = os.path.abspath(log_filename)
print("-" * 60)
print(f"Log messages generated at: {datetime.datetime.now().isoformat()}")
print(f"(Includes source file paths) written to log file: {absolute_log_path}")
print(f"The main script generating these logs is located at: {main_script_path}")
print("-" * 60)


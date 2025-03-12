# Example of how to use rocklogger

# Import the Rocklogger class from the rocklogger package
from rocklogger import Rocklogger

# Initialize the logger
# level can be 'info', 'debug', 'warning', or 'error'
# use_date_in_filename determines if the date is included in the log filename
logger = Rocklogger(level='debug', use_date_in_filename=True).get_logger()

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')

# The logs will be saved in a 'logs' directory in the same location as this script
# Two log files will be created:
# 1. example_YYYYMMDD.log - Contains all log messages
# 2. example_error_YYYYMMDD.log - Contains only error level messages

# You can also use the logger in a try-except block to log exceptions
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception as e:
    logger.error(f"An error occurred: {e}", exc_info=True)

# When you're done with the logger, you can close it (optional)
# This is automatically done when the Rocklogger instance is garbage collected
# logger.close()

# Example of how the singleton pattern works across multiple files

# Import the Rocklogger class from the rocklogger package
from rocklogger import Rocklogger

# This will use the existing instance if example.py has already been run
# Otherwise, it will create a new instance
logger = Rocklogger.get_instance().get_logger()

# Log some messages from this file
logger.info('This message is from example_second_file.py')
logger.debug('The logger is using the same instance across files')

# You can see that the log files are still named after the script that
# first created the logger instance, not this script

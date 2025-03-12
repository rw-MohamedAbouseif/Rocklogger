# Example module 2 - will also use the existing logger instance

from rocklogger import Rocklogger

# This will use the existing instance if it has already been created
logger = Rocklogger.get_instance().get_logger()

# Log some messages from this module
logger.info('This message is from example_module_2.py')
logger.warning('Still using the same logger instance from the main script')

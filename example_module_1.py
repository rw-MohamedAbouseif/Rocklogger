# Example module 1 - will use the existing logger instance

from rocklogger import Rocklogger

# This will use the existing instance if it has already been created
logger = Rocklogger.get_instance().get_logger()

# Log some messages from this module
logger.info('This message is from example_module_1.py')
logger.debug('The logger is using the same instance across modules')

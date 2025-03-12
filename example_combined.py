# Example of how the singleton pattern works across multiple files
# when they are imported within the same Python process

# First, import and use the logger
from rocklogger import Rocklogger
logger = Rocklogger.get_instance(level='debug', use_date_in_filename=True).get_logger()
logger.info('This is the main script creating the first logger instance')

# Now import the other modules
# They will use the same logger instance that was created above
print("\nImporting example_module_1:")
import example_module_1

print("\nImporting example_module_2:")
import example_module_2

# Log a final message from the main script
logger.info('Back to the main script - still using the same logger instance')

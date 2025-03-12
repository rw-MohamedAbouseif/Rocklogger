# rocklogger

A simple and flexible logging utility for Python applications.

### PyPI
https://pypi.org/project/rocklogger/

## Installation

```bash
pip install rocklogger
```

## Usage

### Basic Usage

```python
from rocklogger import Rocklogger

# Initialize the logger
# level can be 'info', 'debug', 'warning', or 'error'
logger = Rocklogger(level='debug', use_date_in_filename=True).get_logger()

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
```

### Log Files

The logger creates two log files in a 'logs' directory in the same location as your script:
1. `your_script_name_YYYYMMDD.log` - Contains all log messages
2. `your_script_name_error_YYYYMMDD.log` - Contains only error level messages

If `use_date_in_filename` is set to `False`, the date will not be included in the filename.

### Logging Exceptions

```python
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception as e:
    logger.error(f"An error occurred: {e}", exc_info=True)
```

### Closing the Logger

When you're done with the logger, you can close it (optional):

```python
# This is automatically done when the Rocklogger instance is garbage collected
logger.close()
```

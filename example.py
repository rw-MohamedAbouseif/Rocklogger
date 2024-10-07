# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:07:19 2022
Updated on Fri Okt 04 12:21:20 2024

@author: Mohamed
"""

from Rocklogger import Rocklogger
# Initialize with date in filename
logger = Rocklogger(level='debug', use_date_in_filename=True).get_logger()
logger.debug('This is a debug message.')

# Initialize without date in filename
# logger = Rocklogger(level='debug', use_date_in_filename=False).get_logger()
# logger.debug('This is a debug message.')

# Example code to trigger an uncaught exception
print("This will be logged.")
raise Exception("This is an uncaught exception!")
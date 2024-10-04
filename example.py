# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:25:38 2022

@author: BOMAN
"""

from Rocklogger import Rocklogger


logger = Rocklogger().init(level='info')
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
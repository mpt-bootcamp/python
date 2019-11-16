#! /usr/bin/env python3
#
# This is a main Python template script.
#

import os
import sys
import subprocess
import argparse
import logging
import datetime

def init_logger():
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add error file handler
    error_handler = logging.FileHandler('error.log')
    # error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logger_formatter)
    logger.addHandler(error_handler)

    # Add console log handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logger_formatter)
    logger.addHandler(console_handler)


def main():
    # Enable logging
    init_logger()
    logger = logging.getLogger(__file__)
    logger.info("Started")
    
    (filename, fileext) = os.path.splitext(os.path.basename(__file__))
    filedir = (os.path.dirname(os.path.realpath(__file__)))
    logger.info("%s %s", filename, filedir)

# Main entry
#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
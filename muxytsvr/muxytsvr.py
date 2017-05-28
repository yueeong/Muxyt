#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Yueeong"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from lib.logger import setup_logger

logger = setup_logger(logfile=None)

def main(args):
    """ Main entry point of the app """

    logger.info("hello world")
    logger.info(args.joinsession)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
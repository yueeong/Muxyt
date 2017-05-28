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


    logger.info(args.joinsession)

def load_config():
    '''
    loads config yaml
    :return: 
    '''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument("-start", "--start_server", default=False, action="store_true", dest="start_server")
    mutex_group.add_argument("-stop", "--stop_server",  default=False, action="store_true", dest="stop_server")


    # Specify output of '--version'
    mutex_group.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s (version {version})'.format(version=__version__))

    args = parser.parse_args()
    """ This is executed when run from the command line """
    main(args)
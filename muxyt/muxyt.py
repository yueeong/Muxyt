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
    parser = argparse.ArgumentParser()

    # Required positional argument
    #parser.add_argument("thing", help="Required positional argument")


    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-js", "--joinsession", action="store", dest="joinsession")
    parser.add_argument("-ss", "--joinsession", action="store_true", dest="showsession")
    parser.add_argument("-ls", "--listsessions", action="store_true", dest="listsessions")


    # Specify output of '--version'
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s (version {version})'.format(version=__version__))

    args = parser.parse_args()

    main(args)
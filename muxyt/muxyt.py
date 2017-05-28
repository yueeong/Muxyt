#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Yueeong"
__version__ = "0.1.0"
__license__ = "MIT"


import argparse
import subprocess
from lib.logger import setup_logger

logger = setup_logger(logfile=None)


def main(args):
    """ Main entry point of the app """

    logger.info("hello world")
    # logger.info(args)
    if args.session_to_join is not None:
        logger.info(args)
    elif args.session_users_to_show is not None:
        logger.info(args.session_users_to_show)
        show_users_of_session()
    elif args.list_all_sessions is not None:
        logger.info(args.list_all_sessions)

def join_active_session(session_name):
    '''
    subprocess to run tmux -S /tmp/sharedsocket attach -t session_name
    :param session_name: 
    :return: 
    '''

def show_users_of_session(session_name):
    '''
    subproc tmux -S /tmp/sharedsocket list-clients -t <session_name>
    grep for pts/N etc and who -u | grep "pts/9" | awk '{print $1}'
    
    :param session_name: 
    :return: 
    '''

def list_all_sessions():
    '''
    subproc  tmux -S /tmp/sharesession ls
    :return: 
    '''

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    #parser.add_argument("thing", help="Required positional argument")


    # Optional argument which requires a parameter (eg. -d test)
    mutex_grp = parser.add_mutually_exclusive_group()
    mutex_grp.add_argument("-js", "--join_session", type=str, action="store", dest="session_to_join")
    mutex_grp.add_argument("-su", "--show_session_users", type=str, action="store", dest="session_users_to_show")
    mutex_grp.add_argument("-ls", "--list_all_sessions", action="store_true", default=False, dest="list_all_sessions")


    # Specify output of '--version'
    mutex_grp.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s (version {version})'.format(version=__version__))

    args = parser.parse_args()

    main(args)
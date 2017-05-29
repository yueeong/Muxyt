#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "yueeong"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import yaml
from utils.logger import setup_logger

import libtmux

logger = setup_logger(logfile=None)

def main(args):
    svrconfig = load_config("/etc/muxytsvr.conf")

    su = SvrUp(svrconfig)


class SvrUp():
    def __init__(self, config):
        self.tserver = libtmux.Server(socket_path=config.socket_path)




def load_config(path):
    '''
    loads config yaml
    :return: 
    '''
    with open(path,'r') as file:
        try:
            yamlconf = yaml.load(file)
            return yamlconf
        except:
            logger.error("Could not load : " + path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument("-start", "--start_server", default=False, action="store_true", dest="start_server")
    mutex_group.add_argument("-stop", "--stop_server",  default=False, action="store_true", dest="stop_server")
    mutex_group.add_argument("-rl", "--reload_server", default=False, action="store_true", dest="reload_server")


    # Specify output of '--version'
    mutex_group.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s (version {version})'.format(version=__version__))

    args = parser.parse_args()
    main(args)
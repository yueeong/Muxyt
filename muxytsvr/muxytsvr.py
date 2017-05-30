#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "yueeong"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import sys
import yaml
from pprint import pprint
import libtmux
from utils.logger import setup_logger



logger = setup_logger(logfile=None)

def main(args):

    try:
        svrconfig = load_config("/etc/muxytsvr.conf")
    except FileNotFoundError:
        logger.info("Could not load system level config. Loading local config file")
        svrconfig = load_config("muxytsvr/config/config.yaml")

    su = SvrUp(config=svrconfig)

    if args.start_server is not False:
        su.start_server()

    elif args.stop_server is not False:
        su.stop_server()

    elif args.reload_server is not False:
        su.reload_server()


class SvrUp():
    def __init__(self, config):
        self.tserver = libtmux.Server(socket_path=config["socket_path"])
        self.nodes = config['nodes']
        for each in self.nodes:
            logger.debug(each['name'])

    def start_server(self):
        '''

        :return:
        '''
        logger.info("start")
        for each in self.nodes:
            print(each)
            self.tserver.new_session(session_name=each['name'])



    def stop_server(self):
        '''

        :return:
        '''
        logger.info('Stopping all sessions and server...')
        self.tserver.kill_server()

    def reload_server(self):
        '''

        :return:
        '''
        pass




def load_config(path):
    '''
    loads config yaml
    :return: 
    '''
    try:
        with open(path,'r') as file:
            try:
                yamlconf = yaml.safe_load(file)
                return yamlconf
            except:
                logger.error("yaml Could not load : " + path)
    except FileNotFoundError as fnferr:
        logger.error("Could not find : " + path)
        raise fnferr
    except Exception as e:
        logger.error("Something went wrong loading : " + path)
        logger.error(e)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument("-start", "--start_server",  action="store_true", dest="start_server")
    mutex_group.add_argument("-stop", "--stop_server",   action="store_true", dest="stop_server")
    mutex_group.add_argument("-rl", "--reload_server",  action="store_true", dest="reload_server")


    # Specify output of '--version'
    mutex_group.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s (version {version})'.format(version=__version__))

    args = parser.parse_args()
    main(args)
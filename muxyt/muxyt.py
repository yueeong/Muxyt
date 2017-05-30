#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Yueeong"
__version__ = "0.1.0"
__license__ = "MIT"


import argparse
import yaml
import libtmux
from pprint import pprint

def main(args):
    """ Main entry point of the app """



    try:
        config = load_config("/etc/muxytsvr.conf")
    except FileNotFoundError:
        print("Could not load system level config. Loading local config file")
        config = load_config("muxytsvr/config/config.yaml")

    uu = UserUp(config=config)

    if args.session_to_join is not None:
        uu.join_active_session(args.session_to_join)

    elif args.session_users_to_show is not None:
        print(args.session_users_to_show)

    elif args.list_all_sessions is not None:
        # print(args.list_all_sessions)
        uu.list_all_sessions()

def load_config(path):
    with open(path, 'r') as conffile:
        try:
            yamlconf = yaml.load(conffile)
            return yamlconf
        except:
            print('**** Could not load ' + path)

class UserUp():
    def __init__(self, config):
        self.tserver = libtmux.Server(socket_path=config['socket_path'])

    def list_all_sessions(self):
        '''
        subproc  tmux -S /tmp/sharesession ls
        :return: 
        '''
        list_of_sessions = self.tserver.list_sessions()
        # print(list_of_sessions)
        print('Session: <Name> (no. connected)')
        for each in list_of_sessions:
            print('Session: ' + each.name + ' (' + each.attached + ')')

            # print(each._info)
            # print(self.tserver.(each))


    def show_users_of_session(self, session_name):
        '''
        subproc tmux -S /tmp/sharedsocket list-clients -t <session_name>
        grep for pts/N etc and who -u | grep "pts/9" | awk '{print $1}'

        :param session_name: 
        :return: 
        '''
        print(session_name)

    def join_active_session(self, session_name):
        '''
        subprocess to run tmux -S /tmp/sharedsocket attach -t session_name
        :param session_name: 
        :return: 
        '''
        print('Joining : ' + session_name + '.....')
        sess_to_join = self.tserver.find_where({"session_name": session_name})
        try:
            self.tserver.attach_session(sess_to_join.id)
        except AttributeError:
            print('Session: \"' + session_name + '\"  Not Found..')
        except:
            print('Some error occurred.')





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    #parser.add_argument("thing", help="Required positional argument")

    # import os
    # pprint(os.environ)
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
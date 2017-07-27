#!/bin/bash
echo $1
varthing=$1
echo $varthing
if [[ $TERM = "screen" ]] && [[ $(ps -p $PPID -o comm=) = "tmux" ]]; then
mkdir $HOME/muxitlogs 2> /dev/null
logname="${varthing}.$(date '+%Y%m%d-%H%M%S').muxit.log"
script -f $HOME/muxitlogs/${logname}
exit
fi
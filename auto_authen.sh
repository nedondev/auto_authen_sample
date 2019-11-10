#!/bin/sh
 
# -q quiet
# -c nb of pings to perform
# https://jeromejaglale.com/doc/unix/shell_scripts/ping
# How it works
# $? returns the exit status of the command previously executed.
# If ping is successful, $? will return 0. If not, it will return another number.

while true
do
    ping -q -c3 google.com > /dev/null
 
    if [ $? -eq 0 ]
    then
	    echo "ok"
    else
        python3 ./login.py
    fi
    sleep 10
done

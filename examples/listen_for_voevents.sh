#!/bin/sh

# Start an instance of Comet and connect to 4PiSky broker.
# VOEvent packets received are passed via stdin to the $HANDLER script.


# The 'local ivorn' is the string identifying this machine on the VOEvent network.
# It's not very important unless you want to *broadcast* events, but it has
# to conform to a standard format all the same, something like e.g.
# ivo://fpstoolstest/some_random_machine
LOCALIVORN=ivo://fpstoolstest/$(hostname)

# This is the script that comet will pass every VOEvent to, for processing:
HANDLER=./process_voevent_from_stdin_2.py

# The remote broker that we will subscribe to. The '--remote' flag can be
# repeated with different addresses if you want to  listen to multiple remotes.
REMOTE=localhost

# Comet maintains a local 'dbm' database directory, where it keeps track of what it's seen before.
# By default this is /tmp - which is usually fine, but if you're running multiple instances on one 
# machine then you should separate them, otherwise they'll both read from the same database and you'll
# get confusing results (e.g. 'I have seen this message before' when it really hasn't).
EVENTDB_PATH=./cometdbtemp

# Put it all together:
mkdir -p $EVENTDB_PATH
/usr/bin/env twistd -n comet \
    --verbose \
    --receive \
    --local-ivo=$LOCALIVORN \
    --remote=$REMOTE \
    --cmd=$HANDLER \
    --eventdb=$EVENTDB_PATH \





#!/bin/sh

# Start an instance of Comet and connect to 4PiSky broker.
# VOEvent packets received are passed via stdin to the $HANDLER script.

IVORN=fpstoolstest/$(hostname)
HANDLER=./process_voevent_from_stdin_1.py
REMOTE=voevent.4pisky.org

/usr/bin/env twistd -n comet \
    --verbose \
    --local-ivo=ivo://$IVORN \
    --remote=$REMOTE \
    --cmd=$HANDLER




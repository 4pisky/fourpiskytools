#!/usr/bin/env bash

TWISTD_PIDFILE=twistd.pid
if [ -f  $TWISTD_PIDFILE ]; then
    kill $(<twistd.pid)
fi

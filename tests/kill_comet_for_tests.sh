#!/usr/bin/env bash

COMET_DB_DIR=comet_test_db_dir
TWISTD_PIDFILE=twistd.pid
if [ -f  $TWISTD_PIDFILE ]; then
    kill $(<twistd.pid)
fi
rm -rf ${COMET_DB_DIR}

#!/usr/bin/env bash

COMET_DB_DIR=comet_test_db_dir
mkdir -p ${COMET_DB_DIR}
/usr/bin/env twistd comet --receive \
    --local-ivo=ivo://fpstoolstest/toxtest \
    --eventdb=${COMET_DB_DIR}
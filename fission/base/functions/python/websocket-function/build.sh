#!/bin/sh
set -e

cd ${SRC_PKG}/fission-functions-main/fission/base/functions/python/websocket-function

pip3 install -r  requirements.txt -t  ${SRC_PKG}

cp -r  ${SRC_PKG} ${DEPLOY_PKG}

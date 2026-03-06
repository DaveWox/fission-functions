#!/bin/sh
cd ${SRC_PKG}/fission/base/functions/python/websocket-function

pip3 install -r  ${SRC_PKG}/requirements.txt -t  ${SRC_PKG} &&  cp -r  ${SRC_PKG} ${DEPLOY_PKG}

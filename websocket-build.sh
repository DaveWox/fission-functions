#!/bin/sh
set -eux

# Find the actual GitHub extracted directory
ROOT=$(find . -maxdepth 1 -type d -name "fission-functions*" | head -n 1)
SRCDIR="${ROOT}/fission/base/functions/python/websocket-function"

# Install dependencies into the source directory
pip3 install -r "${SRCDIR}/requirements.txt" -t "${SRCDIR}"

# Copy final build output to deployment package
cp -r "${SRCDIR}" "${DEPLOY_PKG}"

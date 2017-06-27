#!/usr/bin/env bash
FOLDER="$(cd "$(dirname "$0")" && pwd)"
rm -rf ${FOLDER}/env
conda create --yes -p ${FOLDER}/env python=3.6.0 pymongo pandas

${FOLDER}/env/bin/pip install mongoengine



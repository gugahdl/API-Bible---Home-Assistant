#!/bin/bash

CONFIG_PATH=/data/options.json

APP_KEY=$(jq -r '.app_key' $CONFIG_PATH)
VERSION_ID=$(jq -r '.bible_version_id' $CONFIG_PATH)
UPDATE_HOUR=$(jq -r '.update_hour' $CONFIG_PATH)

export APP_KEY
export VERSION_ID

echo "Iniciando YouVersion Versículo do Dia..."
echo "Versão ID: ${VERSION_ID} | Hora: ${UPDATE_HOUR}h"

python3 /usr/bin/youversion_votd.py

while true; do
    sleep 60
    CURRENT_HOUR=$(date +%-H)
    CURRENT_MIN=$(date +%-M)
    if [ "${CURRENT_HOUR}" = "${UPDATE_HOUR}" ] && [ "${CURRENT_MIN}" = "1" ]; then
        echo "Atualizando versículo do dia..."
        python3 /usr/bin/youversion_votd.py
    fi
done
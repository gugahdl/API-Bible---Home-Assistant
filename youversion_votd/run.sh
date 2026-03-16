#!/bin/bash
set -e

APP_KEY=$(bashio::config 'app_key')
VERSION_ID=$(bashio::config 'bible_version_id')
UPDATE_HOUR=$(bashio::config 'update_hour')

export APP_KEY
export VERSION_ID

echo "Iniciando YouVersion Versículo do Dia..."
python3 /usr/bin/youversion_votd.py

while true; do
    sleep 60
    CURRENT_HOUR=$(date +%-H)
    CURRENT_MIN=$(date +%-M)
    if [ "${CURRENT_HOUR}" = "${UPDATE_HOUR}" ] && [ "${CURRENT_MIN}" = "1" ]; then
        echo "Atualizando versículo..."
        python3 /usr/bin/youversion_votd.py
    fi
done
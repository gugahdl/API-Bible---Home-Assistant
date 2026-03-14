#!/usr/bin/with-contenv bashio

bashio::log.info "Iniciando YouVersion Versículo do Dia..."

# Lê as opções configuradas pelo usuário
APP_KEY=$(bashio::config 'app_key')
VERSION_ID=$(bashio::config 'bible_version_id')
UPDATE_HOUR=$(bashio::config 'update_hour')

# Valida a app_key
if bashio::var.is_empty "${APP_KEY}"; then
    bashio::log.fatal "App Key não configurada! Acesse a configuração do addon e informe sua YouVersion App Key."
    exit 1
fi

bashio::log.info "Versão da Bíblia ID: ${VERSION_ID}"
bashio::log.info "Hora de atualização: ${UPDATE_HOUR}:00"

export APP_KEY
export VERSION_ID

# Executa imediatamente ao iniciar
bashio::log.info "Buscando versículo do dia inicial..."
python3 /usr/bin/youversion_votd.py || bashio::log.error "Falha ao buscar versículo inicial"

# Loop: verifica a cada minuto se é hora de atualizar
while true; do
    sleep 60
    CURRENT_HOUR=$(date +%-H)
    CURRENT_MIN=$(date +%-M)

    if [ "${CURRENT_HOUR}" = "${UPDATE_HOUR}" ] && [ "${CURRENT_MIN}" = "1" ]; then
        bashio::log.info "Atualizando versículo do dia..."
        python3 /usr/bin/youversion_votd.py || bashio::log.error "Falha ao atualizar versículo"
    fi
done

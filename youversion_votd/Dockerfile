ARG BUILD_FROM
FROM $BUILD_FROM

LABEL \
    io.hass.version="1.0.0" \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7|i386"

RUN apk add --no-cache python3 py3-pip && \
    pip3 install requests --break-system-packages

COPY rootfs /
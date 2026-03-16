ARG BUILD_FROM
FROM $BUILD_FROM

LABEL \
    io.hass.version="1.0.0" \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7|i386"

RUN apk add --no-cache python3 py3-pip && \
    pip3 install requests --break-system-packages

COPY rootfs /

RUN find /etc/services.d -name "run" -exec chmod 755 {} \; && \
    find /etc/cont-init.d -name "*.sh" -exec chmod 755 {} \; && \
    chmod 755 /usr/bin/youversion_votd.py
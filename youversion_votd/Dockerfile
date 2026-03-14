ARG BUILD_FROM
FROM $BUILD_FROM

# Labels obrigatórias conforme documentação oficial
LABEL \
    io.hass.version="1.0.0" \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7|i386"

# Install Python and dependencies
RUN apk add --no-cache python3 py3-pip && \
    pip3 install requests --break-system-packages

# Copy rootfs overlay (places files at correct paths inside container)
COPY rootfs /

RUN chmod a+x /usr/bin/youversion_votd.py /run.sh

CMD [ "/run.sh" ]

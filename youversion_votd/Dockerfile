ARG BUILD_FROM
FROM $BUILD_FROM

LABEL \
    io.hass.version="1.0.0" \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7|i386"

RUN apk add --no-cache python3 py3-pip bash && \
    pip3 install requests --break-system-packages

COPY run.sh /run.sh
COPY rootfs/usr/bin/youversion_votd.py /usr/bin/youversion_votd.py

RUN chmod 755 /run.sh /usr/bin/youversion_votd.py

ENTRYPOINT ["/bin/bash", "/run.sh"]
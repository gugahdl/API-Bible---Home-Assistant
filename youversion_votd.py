#!/usr/bin/env python3
"""
YouVersion Versículo do Dia - Home Assistant Addon
Busca o versículo do dia e cria/atualiza um sensor no Home Assistant via API REST.
"""

import os
import re
import sys
import json
import datetime
import requests

# ── Configurações vindas do container (run.sh via bashio) ──────────────────────
APP_KEY    = os.environ.get("APP_KEY", "")
VERSION_ID = os.environ.get("VERSION_ID", "1588")

# Acesso à API interna do Home Assistant (disponível via homeassistant_api: true)
HA_TOKEN   = os.environ.get("SUPERVISOR_TOKEN", "")
HA_URL     = "http://supervisor/core/api"

YOUVERSION_BASE = "https://api.youversion.com/v1"
YV_HEADERS = {"X-YVP-App-Key": APP_KEY}


def strip_html(text: str) -> str:
    """Remove tags HTML do texto retornado pela API."""
    return re.sub(r"<[^>]+>", "", text).strip()


def fetch_votd() -> dict:
    """Busca o versículo do dia na YouVersion API."""
    day_of_year = datetime.datetime.now().timetuple().tm_yday

    # 1) Passage ID do dia
    resp = requests.get(
        f"{YOUVERSION_BASE}/votd/{day_of_year}",
        headers=YV_HEADERS,
        timeout=15,
    )
    resp.raise_for_status()
    passage_id = resp.json()["passage_id"]  # ex: "JHN.3.16"

    # 2) Texto do versículo
    resp2 = requests.get(
        f"{YOUVERSION_BASE}/bibles/{VERSION_ID}/passages/{passage_id}",
        headers=YV_HEADERS,
        timeout=15,
    )
    resp2.raise_for_status()
    data = resp2.json()

    # 3) Copyright da versão
    resp3 = requests.get(
        f"{YOUVERSION_BASE}/bibles/{VERSION_ID}",
        headers=YV_HEADERS,
        timeout=15,
    )
    copyright_short = ""
    if resp3.ok:
        copyright_short = resp3.json().get("copyright_short", "")

    text_clean = strip_html(data.get("content", ""))
    reference  = passage_id.replace(".", " ")

    return {
        "text":            text_clean,
        "reference":       reference,
        "passage_id":      passage_id,
        "bible_version":   str(VERSION_ID),
        "copyright":       copyright_short,
        "updated_at":      datetime.datetime.now().isoformat(),
    }


def update_ha_sensor(votd: dict) -> None:
    """Cria ou atualiza o sensor no Home Assistant via API REST interna."""
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type":  "application/json",
    }

    payload = {
        "state":      votd["reference"],
        "attributes": {
            "friendly_name": "Versículo do Dia",
            "icon":          "mdi:book-open-variant",
            "text":          votd["text"],
            "reference":     votd["reference"],
            "passage_id":    votd["passage_id"],
            "bible_version": votd["bible_version"],
            "copyright":     votd["copyright"],
            "updated_at":    votd["updated_at"],
        },
    }

    resp = requests.post(
        f"{HA_URL}/states/sensor.youversion_versiculo_do_dia",
        headers=headers,
        json=payload,
        timeout=10,
    )
    resp.raise_for_status()
    print(f"[OK] Sensor atualizado: {votd['reference']}")


def main():
    if not APP_KEY:
        print("[ERRO] APP_KEY não definida.", file=sys.stderr)
        sys.exit(1)

    print(f"[INFO] Buscando versículo do dia (versão ID: {VERSION_ID})...")

    try:
        votd = fetch_votd()
        print(f"[INFO] {votd['reference']}: {votd['text'][:80]}...")
        update_ha_sensor(votd)
    except requests.HTTPError as e:
        print(f"[ERRO] HTTP {e.response.status_code}: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERRO] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

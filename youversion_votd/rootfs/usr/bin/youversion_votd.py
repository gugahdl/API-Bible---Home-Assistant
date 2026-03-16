#!/usr/bin/env python3
import os
import re
import sys
import datetime
import requests

APP_KEY    = os.environ.get("APP_KEY", "")
VERSION_ID = os.environ.get("VERSION_ID", "3254")
HA_TOKEN   = os.environ.get("SUPERVISOR_TOKEN", "")
HA_URL     = "http://supervisor/core/api"

YOUVERSION_BASE = "https://api.youversion.com/v1"
YV_HEADERS = {"X-YVP-App-Key": APP_KEY}

def strip_html(text):
    return re.sub(r"<[^>]+>", "", text).strip()

def fetch_votd():
    day_of_year = datetime.datetime.now().timetuple().tm_yday

    # 1) Busca o passage_id do dia
    resp = requests.get(
        f"{YOUVERSION_BASE}/verse_of_the_days/{day_of_year}",
        headers=YV_HEADERS,
        timeout=15,
    )
    resp.raise_for_status()
    passage_id = resp.json()["passage_id"]
    print(f"[INFO] Passage ID do dia: {passage_id}")

    # 2) Busca o texto da passagem
    resp2 = requests.get(
        f"{YOUVERSION_BASE}/bibles/{VERSION_ID}/passages/{passage_id}",
        headers=YV_HEADERS,
        timeout=15,
    )
    resp2.raise_for_status()
    data = resp2.json()

    content = data.get("data", data)
    if isinstance(content, dict):
        text_raw = content.get("content", content.get("text", str(content)))
    else:
        text_raw = str(content)

    text_clean = strip_html(str(text_raw))
    reference = passage_id.replace(".", " ")

    return {
        "text":          text_clean,
        "reference":     reference,
        "passage_id":    passage_id,
        "bible_version": str(VERSION_ID),
        "updated_at":    datetime.datetime.now().isoformat(),
    }

def update_ha_sensor(votd):
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type":  "application/json",
    }
    payload = {
        "state": votd["reference"],
        "attributes": {
            "friendly_name": "Versículo do Dia",
            "icon":          "mdi:book-open-variant",
            "text":          votd["text"],
            "reference":     votd["reference"],
            "bible_version": votd["bible_version"],
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
        print("[ERRO] APP_KEY não definida.")
        sys.exit(1)

    print(f"[INFO] Buscando versículo do dia (versão ID: {VERSION_ID})...")
    try:
        votd = fetch_votd()
        print(f"[INFO] {votd['reference']}: {votd['text'][:80]}...")
        update_ha_sensor(votd)
    except requests.HTTPError as e:
        print(f"[ERRO] HTTP {e.response.status_code}: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERRO] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
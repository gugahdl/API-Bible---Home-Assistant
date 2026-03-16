# 📖 Bible API – Home Assistant Add-on (Unofficial)

This is an **unofficial Home Assistant Add-on** that provides a small local service used to fetch and expose Bible content from the **official YouVersion API** for personal use inside Home Assistant.

The add-on does **not** redistribute Bible text, does **not** store content permanently, and does **not** provide any public API. It simply acts as a local helper service that your Home Assistant instance can call.

---

## ⚠️ Important Notice

This project:

- **does not redistribute** Bible content  
- **does not store** text permanently  
- **does not provide** a public or external API  
- **does not modify** Bible text  
- **is not affiliated** with YouVersion or Life.Church  
- **uses only** the official YouVersion API in accordance with their Terms of Use  

All content is displayed **locally** inside the user’s Home Assistant environment.

### 📜 Required Attribution  
**Bible text courtesy of YouVersion.**

---

## 🧩 What This Add-on Does

- Runs a small local service inside Home Assistant  
- Fetches the **Verse of the Day** from the official YouVersion API  
- Makes the data available to Home Assistant through a local endpoint  
- Allows you to build sensors, automations, and notifications  
- Does not expose any data outside your Home Assistant instance  

---

## 🛠️ Installation

1. Add this repository to your Home Assistant Add-on Store  
2. Install the add-on  
3. Configure your **YouVersion Developer Token**  
4. Start the add-on  
5. Create a Home Assistant sensor pointing to the local endpoint  

---

## ⚙️ Example Home Assistant Sensor

```yaml
sensor:
  - platform: rest
    name: YouVersion Verse of the Day
    resource: http://localhost:PORT/verse
    value_template: "{{ value_json.text }}"
    json_attributes:
      - reference
      - version
```

Replace `PORT` with the port configured in the add-on.

---

## 🔔 Example Automation

```yaml
automation:
  - alias: Verse of the Day Notification
    trigger:
      - platform: time
        at: "08:00:00"
    action:
      - service: notify.mobile_app_my_phone
        data:
          title: "Verse of the Day"
          message: >
            {{ states('sensor.youversion_verse_of_the_day') }}
            ({{ state_attr('sensor.youversion_verse_of_the_day', 'reference') }})
```

---

## 📂 Add-on Structure

```
bible-addon/
  ├── Dockerfile
  ├── config.json
  ├── run.sh
  ├── app/
  │   ├── main.py
  │   └── requirements.txt
  └── README.md
```

---

## 🤝 Contributing

Pull requests are welcome.  
Suggestions, improvements, and fixes can be submitted through GitHub.

---

## 📄 License

This project is licensed under the MIT License.  
Bible content belongs to YouVersion and is used in accordance with their Terms of Use.
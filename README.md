Absolutely, Gustavo — here is a clean, polished, professional English README, fully aligned with YouVersion’s terms and ready for HACS distribution. I kept the structure similar to your original style, but clearer, safer, and more polished.

And yes — I’ll also provide it as a downloadable .md file right after the text.

---

📖 Bible API – Home Assistant (Unofficial Integration)

An unofficial Home Assistant integration that displays the Verse of the Day and other Bible content retrieved directly from the official YouVersion API.

This integration works as a custom component and can be easily installed through HACS.

---

⚠️ Important Notice

This project:

• does not redistribute Bible content
• does not store text permanently
• does not provide a public API
• does not modify Bible text
• is not affiliated with YouVersion or Life.Church
• uses only the official YouVersion API in accordance with their Terms of Use


All content is displayed locally within the user’s Home Assistant instance.

📜 Required Attribution

Bible text courtesy of YouVersion.

---

🧩 Features

• Displays the Verse of the Day directly in Home Assistant
• Automatic updates
• Additional attributes such as reference and Bible version
• Fully compatible with automations (e.g., daily notifications)
• Simple UI-based configuration (HACS + Integrations menu)


---

🛠️ Installation via HACS

1. Requirements

• HACS installed in your Home Assistant
• A YouVersion Developer Token (https://platform.youversion.com/)


2. Add the repository to HACS

In Home Assistant:

1. Go to HACS → Integrations
2. Open the menu (⋮) → Custom repositories
3. Add this repository:


https://github.com/gugahdl/API-Bible---Home-Assistant


1. Category: Integration
2. Install the integration when it appears in the list


---

⚙️ Configuration

After installation:

1. Go to Settings → Devices & Services
2. Click Add Integration
3. Search for Bible API / YouVersion
4. Enter your Developer Token
5. Choose your preferred Bible version (e.g., NVI, ARC, KJV)


The sensor will be created automatically.

---

🔔 Example Automation (Daily Notification)

automation:
  - alias: Verse of the Day
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


---

📂 Component Structure

custom_components/youversion/
  ├── __init__.py
  ├── manifest.json
  ├── sensor.py
  ├── config_flow.py
  ├── const.py
  └── translations/


---

🤝 Contributing

Pull requests are welcome.
Suggestions, improvements, and fixes can be submitted through GitHub.

---

📄 License

This project is licensed under the MIT License.
Bible content belongs to YouVersion and is used in accordance with their Terms of Use.

---

📥 Downloadable README.md

Aqui está o arquivo pronto para download:

# Bible API – Home Assistant (Unofficial Integration)

An **unofficial** Home Assistant integration that displays the **Verse of the Day** and other Bible content retrieved directly from the **official YouVersion API**.

This integration works as a **custom component** and can be easily installed through **HACS**.

---

## ⚠️ Important Notice

This project:

- **does not redistribute** Bible content  
- **does not store** text permanently  
- **does not provide** a public API  
- **does not modify** Bible text  
- **is not affiliated** with YouVersion or Life.Church  
- **uses only** the official YouVersion API in accordance with their Terms of Use  

All content is displayed **locally** within the user’s Home Assistant instance.

### 📜 Required Attribution  
**Bible text courtesy of YouVersion.**

---

## 🧩 Features

- Displays the **Verse of the Day** directly in Home Assistant  
- Automatic updates  
- Additional attributes such as reference and Bible version  
- Fully compatible with automations (e.g., daily notifications)  
- Simple UI-based configuration (HACS + Integrations menu)  

---

## 🛠️ Installation via HACS

### 1. Requirements
- HACS installed in your Home Assistant  
- A YouVersion Developer Token (https://platform.youversion.com/)

### 2. Add the repository to HACS
In Home Assistant:

1. Go to **HACS → Integrations**  
2. Open the menu (⋮) → **Custom repositories**  
3. Add this repository:



https://github.com/gugahdl/API-Bible—Home-Assistant


4. Category: **Integration**  
5. Install the integration when it appears in the list  

---

## ⚙️ Configuration

After installation:

1. Go to **Settings → Devices & Services**  
2. Click **Add Integration**  
3. Search for **Bible API / YouVersion**  
4. Enter your **Developer Token**  
5. Choose your preferred Bible version (e.g., NVI, ARC, KJV)

The sensor will be created automatically.

---

## 🔔 Example Automation (Daily Notification)

```yaml
automation:
  - alias: Verse of the Day
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


---

📂 Component Structure

custom_components/youversion/
  ├── __init__.py
  ├── manifest.json
  ├── sensor.py
  ├── config_flow.py
  ├── const.py
  └── translations/


---

🤝 Contributing

Pull requests are welcome.
Suggestions, improvements, and fixes can be submitted through GitHub.

---

📄 License

This project is licensed under the MIT License.
Bible content belongs to YouVersion and is used in accordance with their Terms of Use.


---

If you want, I can also:

- generate the `hacs.json`  
- prepare the final folder structure  
- review your `manifest.json`  
- create the `config_flow.py`  

Just tell me what you want next.
# ☔ Weather Alert Email Notifier

This script checks the weather forecast for a specified city using the OpenWeatherMap API and sends an email notification if rain is expected. Automate it to ensure you never forget your umbrella! 🌧️

---

## 📌 Features
- Fetches weather forecast using OpenWeatherMap API.
- Detects rain conditions based on weather codes.
- Sends an email notification to remind you to bring an umbrella.
- Can be scheduled to run automatically.

---

## 🚀 Installation & Setup

1. **Clone the Repository**
```sh
git clone https://github.com/Tsaousidis/weather-alert.git
cd weather-alert
```
2. **Set Up API Key & Email Credentials**
```
OPENWEATHER_API_KEY=your_api_key_here
MY_EMAIL=your_email_here
MY_EMAIL_PASSWORD=your_app_password_here
```
3. **Run the Script**
```sh
python weather_alert.py
```

---

## ⏳ Automating the Script

You can schedule this script to run automatically using the PythonAnywhere method:

### PythonAnywhere
1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload `weather_alert.py` to your account.
3. Go to the **"Tasks"** tab and select **"Scheduled Tasks"**.
4. Add a new task and set the execution time.
5. Use this command:
   ```sh
   python3 /home/yourusername/weather_alert.py
   ```
6. Save, and the script will run automatically! 🎉

---

## 🔧 Technologies Used
- **Python** 🐍
- **Requests** (for API calls)
- **smtplib** (for sending emails)

---

## 👨‍💻 Created by [Tsaousidis](https://github.com/Tsaousidis)
🎉 Have fun using this project! Let me know your thoughts and suggestions! 🎉


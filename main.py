
import requests
import smtplib

# Constants
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" 
CITY = "Thessaloniki" # Change this to any city you want

# Credentials
API_KEY = "myapikey" # Change this with your API key from home.openweathermap.org
MY_EMAIL = "myemail@email.com" # Change this with your email
MY_PASSWORD = "mypassword" # Change this with your app password you've created in your email 

# Parameters for API request
parameters = {
    "q": CITY,
    "appid": API_KEY,
    "cnt": 4,
}

# Fetch weather data
response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain 
will_rain = any(200 <= hour["weather"][0]["id"] < 700 for hour in weather_data["list"])

# Send an email notification if rain is expected
if will_rain:
    try:
        # Send notification in my email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            subject = "It's going to rain today!"
            body = "Remember to bring an umbrella!"
            msg = f"Subject: {subject}\r\n\r\n{body}"

            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg)
        print(f"✅ Email sent successfully to {MY_EMAIL}")
    except smtplib.SMTPException as e:
        print(f"❌ Failed to send email: {e}")

import os
import time
import requests
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

MY_LAT = float(os.environ.get("MY_LAT"))
MY_LNG = float(os.environ.get("MY_LNG"))

client = Client(
    os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN")
)


def fetch_data(url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def is_iss_overhead():
    iss_data = fetch_data(os.environ.get("ISS_URL"))
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lon = float(iss_data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lon <= MY_LNG + 5


def is_night():
    susnset_params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    sun_data = fetch_data(os.environ.get("SUSNSET_URL"), susnset_params)
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True


def sendSMS():
    message = client.messages.create(
        to=os.environ.get("MY_NUMBER"),
        from_=os.environ.get("TWILIO_NUMBER"),
        body="look up! ISS is overhead",
    )
    print(message.sid)


while 1:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        sendSMS()

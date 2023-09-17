import requests
from datetime import datetime

sunset_url = "https://api.sunrise-sunset.org/json"
iss_url = "http://api.open-notify.org/iss-now.json"
MY_LAT = 32.0782587
MY_LNG = 34.8985302

susnset_params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}


def fetch_data(url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


sun_data = fetch_data(sunset_url, susnset_params)
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
now = datetime.now().hour
print(sunrise)
print(sunset)
print(now)

iss_data = fetch_data(iss_url)
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lon = float(iss_data["iss_position"]["longitude"])
print(iss_lat)
print(iss_lon)

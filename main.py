import requests
from datetime import datetime

sunset_url = "https://api.sunrise-sunset.org/json"
iss_irl = "http://api.open-notify.org/iss-now.json"
MY_LAT = 32.0782587
MY_LNG = 34.8985302

susnset_params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get(sunset_url, params=susnset_params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

now = datetime.now().hour
print(now)

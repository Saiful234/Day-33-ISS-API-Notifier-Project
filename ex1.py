import requests
import urllib3


LATITUDE = 13.0836939
LONGITUDE = 80.270186

parameter = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }
urllib3.disable_warnings()
response = requests.get("https://api.sunrise-sunset.org/json", params=parameter, verify=False)
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)
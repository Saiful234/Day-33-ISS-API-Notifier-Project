import requests
import datetime
import smtplib
import time

EMAIL = lenovo498@gmail.com
PASSWORD  = Fclcnu21@131

LATITUDE = 51.438173
LONGITUDE = -0.070393

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    print(iss_data)
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if LATITUDE-5 <= iss_latitude <=LATITUDE+5 and LONGITUDE-5 <= iss_longitude <= LONGITUDE:
        return True

def is_night():
    parameter = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter, verify=False)
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="sathish1234@gmail.com", msg="Subject: ISS is over head\n\n "
                                                                                   "The ISS is above you in the sky.")

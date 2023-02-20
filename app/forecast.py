import requests
from datetime import datetime
from config import config

headers = {"user-agent": "solar-assistant controller application"}


def calculate_todays_cloud_average():
    lat = config["forecast"]["lat"]
    lon = config["forecast"]["lon"]

    response = requests.get(
        f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lon}",
        headers=headers,
    )

    if response.status_code != 200:
        print("Web request for weather forecast failed")
        print(response.status_code)
        print(response.text)
        exit()

    now = datetime.utcnow()

    time_series = response.json()["properties"]["timeseries"]

    cloud_area_fractions = []
    for time_slot in time_series:
        time = datetime.fromisoformat(time_slot["time"])
        details = time_slot["data"]["instant"]["details"]
        if (
            now.date() == time.date()
            and float(details["ultraviolet_index_clear_sky"]) > 0
        ):
            cloud_area_fractions.append(float(details["cloud_area_fraction"]))

    if not cloud_area_fractions:
        return 0

    cloud_area_fraction_average = sum(cloud_area_fractions) / len(cloud_area_fractions)
    return cloud_area_fraction_average

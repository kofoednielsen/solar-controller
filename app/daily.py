import forecast
from config import config
import inverter

cloud_average = forecast.calculate_todays_cloud_average()

print(f"Today's cloud average is: {cloud_average}")

best_threshold = max(filter(lambda t: cloud_average >= t, config['cloud_thresholds']))

time_of_use_voltages = config['cloud_thresholds'][best_threshold]['time_of_use_voltages']

print("Setting time of use voltages to: ")
for slot, voltage in time_of_use_voltages.items():
    print(f"Slot {slot}: {voltage} V")
    inverter.set_time_of_use_voltage_point(slot, voltage)


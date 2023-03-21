import forecast
from config import config
import inverter

cloud_average = forecast.calculate_todays_cloud_average()

print(f"Today's cloud average is: {cloud_average}")

best_threshold = max(filter(lambda t: cloud_average >= t, config["cloud_thresholds"]))

time_of_use= config["cloud_thresholds"][best_threshold]

print("Setting time of use voltages to: ")
for slot, voltage in time_of_use['time_of_use_voltages'].items():
    print(f"Slot {slot} Voltage: {voltage} V")
    inverter.set_time_of_use(slot, "voltage", voltage)

if time_of_use.get('time_of_use_grid_charge'):
    print("Setting time of us grid charge to:")
    for slot, grid_charge in time_of_use['time_of_use_grid_charge'].items():
        print(f"Slot {slot} Grid charge: {grid_charge}")
        inverter.set_time_of_use(slot, "grid_charge", 'true' if grid_charge else 'false')

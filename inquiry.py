import bluetooth, json
from blscan import get_devices_rssi

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

print("Found {} devices".format(len(nearby_devices)))

nearby_devices = {row[0]: {"name": row[1]} for row in nearby_devices}
get_devices_rssi(nearby_devices)

with open("devices.json", "w") as f:
    f.write(json.dumps(nearby_devices))

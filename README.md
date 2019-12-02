# python-ble

python-ble is a project which goal is to display nearby bluetooth devices on a web page.

## requirements

   - python > 3.6
   - libbluetooth-dev
   - modules in requirements.txt

## how to

The code currently provides two simple scripts:

	- inquiry.py - scan devices and store them in a json file with their ids, names, and RSSI.
	- app.py - simple Flask app
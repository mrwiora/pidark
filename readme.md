Do you want to control your remote control power switches and do you want to do this with an home automation system like homeassistant?

The result is that you want to have a command-line interface without any fancy webserver or something running.
This is the project that enables you with that.

The basic idea is that I'm taking the raw-codes produced by pilight and applying them on the GPIO Pin my sender is connected to.

basic usage:
```
pidark-send.py "208 624 208 624 624 208 624 208 624 208 624 208 624 208 624 208 208 624 208 624 208 624 208 624 208 624 208 624 208 624 208 624 624 208 624 208 208 624 208 624 208 624 208 624 208 624 208 624 208 7072"
```
what in this case is the same as "pilight-send -p techlico_switch -i 16128 -u 2 -f"

In case you want the raw-code for your device already supported in pilight, just start the server in debug mode and copy/paste your raw code

Installation
---------------

In case of an empty system please install the following packages:
```
sudo apt-get install python3 python3-venv python3-pip
```

In each case (e.g. running this application on the system you are running Home Assistant):
```
pip3 install -r requirements.txt
```

Checklist
---------------
Basic:
- [x] basic control of GPIO connected RF sender
- [x] start paramter processing of program arguments
- [ ] add computed raw-codes (copy from pilight) based on parameters

Possible to implement
- [ ] Receiver processing (to learn new codes)

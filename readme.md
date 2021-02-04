# Readme
Attempting to control camera to get 2 fixed zoom positions.

## How to use
Not ready for use, currently in development.

## Background
* zoom-in-fully.py -> is working (based off below link) 
* Python examples from PTZ: https://help.ptzoptics.com/support/solutions/articles/13000077734-an-introduction-to-ip-control-scripting-for-ptzoptics-cameras)
* The user manual for the camera: https://ptzoptics.com/wp-content/uploads/2019/07/PT12X-ZCAM-User-Manual-v1_2-rev-7-19.pdf
* A Github project that has advanced features but I can't get working: https://github.com/misterhay/VISCA-IP-Controller

## How to test (Ubuntu)
* Install git on Ubuntu by `sudo apt install git`
* Clone repository by `git clone https://github.com/jbjbjb1/PTZOptics-Simple-IP.git`
* Start venv by `source env-cam/bin/activate`
* Run the python script by `python3 PTZOptics-Simple-IP/zoom-in-fully.py`
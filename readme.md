# Readme
This app controls the TPZOptics camera zoom positions to three positions: zoom in, zoom stage, zoom out.

## How to use
Run the .exe file (dist\simple_gui.exe) and click the buttons to zoom the camera as required! To change settings, copy the settings file (simple_cmds_settings.txt) in to the same folder as the .exe file and re-run the program.

## Improvements
* Add a preview to the GUI of the camera (2 sec refresh rate)
* Add a "connected status" to the GUI with advice if needing to troubleshoot

## Background
* zoom-in-fully.py -> is working (based off below link) 
* Python examples from PTZ: https://help.ptzoptics.com/support/solutions/articles/13000077734-an-introduction-to-ip-control-scripting-for-ptzoptics-cameras)
* The user manual for the camera: https://ptzoptics.com/wp-content/uploads/2019/07/PT12X-ZCAM-User-Manual-v1_2-rev-7-19.pdf
* A Github project that has advanced features but I can't get working: https://github.com/misterhay/VISCA-IP-Controller

## How to generate .exe
PyInstaller is used to bundle the script into a .exe file.

1. ensure you are in the pipenv environment (`pipenv shell`)
2. `pyinstaller --onefile --windowed simple_gui.py`
3. To debug, build without `--windowed` option and run in cmd with `simple_gui.exe`
4. To run the .exe, open the file and click the buttons

## How to test (Ubuntu)
* Install git on Ubuntu by `sudo apt install git`
* Clone repository by `git clone https://github.com/jbjbjb1/PTZOptics-Simple-IP.git` (you may need to remove the directory if it's already there and you are updating the code by `rm -rf PTZOptics-Simple-IP`)
* Start venv by `source env-cam/bin/activate` (may be superceded by pipenv shell), then move into `cd PTZOptics-Simple-IP`
* Run the python script by `python3 simple_gui.py` (or other python files)

## Issues
* Can not get pipenv working in Ubuntu, resorted back it venv
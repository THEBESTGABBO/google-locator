# google-locator
Python script to retrieve google shared location using [selenium](https://selenium-python.readthedocs.io/) and [locationsharinglib](https://github.com/costastf/locationsharinglib).

# How it works
1) Check for a valid cookies file
2) If not found retrieve the cookies using Selenium
3) Extract location from cookies file using locationsharinglib

# Requirements
Google Chrome or Chromium installed, minimum version 109

# Get-Started
1) Download or clone the repository
2) Create a new virtual environment with ```python3 -m venv locator```
3) Install the required libraries with ```pip install -r requirements.txt```
4) Insert your data into the Locator.py file
5) Run Locator.py and have fun!

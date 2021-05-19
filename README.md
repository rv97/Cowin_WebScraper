# Cowin Web Scraper

This tool allows to get info on the available slots for COVID-19 Vaccine in Cowin App India.

## Information
### Softwares required
1. Latest version of [firefox](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release)
2. Latest version of [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
### Setting this up locally

1. Create a virtual env using ```virtualenv venv```
2. Activate it using ``` source venv/bin/activate```
3. Install the requirements.txt using ``` pip install -r requirements.txt```
4. Set the path for geckodriver using ``` export PATH=$PATH:/Users/Sample/Desktop``` (For ex, my geckodriver is in Desktop)
5. Start the Flask server using ``` flask run ```
6. Go to [http://localhost:5000](http://localhost:5000)
7. You will be shown with the Swagger UI
8. Register for the notifications and the continue with the rest of the steps in order.
9. This script will be running every 5 min until stopped.

import requests
import time

# Default temperature range values
DEFAULT_MIN_TEMP = 70
DEFAULT_MAX_TEMP = 85
DEFAULT_LOCATION = "London,gb"  # Default location code for London, UK

# Get user preferences for temperature range and location
def get_user_preferences():
    try:
        min_temp = float(input("Enter your preferred minimum temperature (in Fahrenheit): "))
        max_temp = float(input("Enter your preferred maximum temperature (in Fahrenheit): "))
        location = input("Enter your preferred location (e.g., 'London,gb'): ")

        return min_temp, max_temp, location
    except ValueError:
        print("Invalid input. Please enter valid temperature values.")
        return None, None, None

# Get the current temperature from the OpenWeatherMap API.
def get_current_temperature(location):
    api_key = "63b8ab29a7c21daec9b4d104659e8d8a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        print("Unable to get the current temperature.")
        return None

# Send an alert if the current temperature is too high or too low.
def send_alert(current_temperature, min_temp, max_temp):
    if current_temperature < min_temp:
        print("Alert: The temperature is too low.")
    elif current_temperature > max_temp:
        print("Alert: The temperature is too high.")

# Check the temperature at user-defined intervals and send an alert if necessary.
def temperature_alert_agent():
    min_temp, max_temp, location = get_user_preferences()

    while min_temp is None or max_temp is None or location is None:
        min_temp, max_temp, location = get_user_preferences()

    while True:
        current_temperature = get_current_temperature(location)
        if current_temperature is not None:
            send_alert(current_temperature, min_temp, max_temp)
        time.sleep(60)  # Check the temperature every minute

if __name__ == "__main__":
    temperature_alert_agent()

# Temperature Alert App

## Description

This app provides temperature alerts to users based on their location. Users can set the temperature threshold and receive alerts when the temperature reaches that threshold.

## Instructions to Run the Project

[import requests
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
]

## Special Considerations




## SOS FIRBRIGADE 

Our Temperature Alert Agent is designed to keep you safe in case of extreme temperatures. If the temperature goes above a certain threshold that you set, the agent will automatically send an alert/notification to your phone. If the temperature continues to rise and reaches a critical level, the agent can also contact the fire brigade to ensure your safety. This feature is designed to give you peace of mind and protect you from potential harm.

import requests

def send_alert():
    # Replace with your own phone number and message
    phone_number = '+1234567890'
    message = 'SOS! Fire detected at location X.'

    # Send the message using Twilio API
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    url = 'https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json'.format(account_sid)
    data = {
        'From': '+14159694361',
        'To': phone_number,
        'Body': message,
    }
    response = requests.post(url, data=data, auth=(account_sid, auth_token))

    # Check if the message was sent successfully
    if response.status_code == 201:
        print('Message sent successfully!')
    else:
        print('Error sending message.')

def detect_fire():
    # Replace with your own fire detection code
    pass

if _name_ == '_main_':
    # Run the fire detection code
    if detect_fire():
        # Send an alert if fire is detected
        send_alert()




## VOICE ALERT 

#THIS IS JUST A DEMO FOR THE IDEA OF VOICE ALERT KEEPING IN MIND VISUALLY IMPAIRED COMMUNITY 
Our Temperature Alert Agent is designed to keep you informed about the temperature in your area. If the temperature goes above a certain threshold that you set, the agent will automatically send an alert/notification to your phone. In addition to this, the agent can also give voice alerts to notify you of the temperature change. This feature is designed to give you an additional layer of protection and ensure that you’re always aware of the temperature in your area.

import pyttsx3

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.getProperty('voices', voices[1].id)
friend.say("Alert:HIGH)     # SET ACCORDING TO THE TEMP 
friend.runandWait()
friend.stop()


## USE OF EMOJIS 

Emojis are a fun and creative way to represent hot and cold temperatures in our Temperature Alert Agent. We use the hot face emoji (🔥) to represent high temperatures and the cold face emoji (❄️) to represent low temperatures. For example, we use these emojis in your Python code or in your notifications to indicate whether the current temperature is above or below a certain threshold.

    # Define hot and cold temperature thresholds
hot_temp = 30 # degrees Celsius
cold_temp = 10 # degrees Celsius

    # Define hot and cold temperature emojis
hot_emoji = "🔥"
cold_emoji = "❄️"

//CONSIDERING WEATHER--
🌧️ Raindrops falling down,
☁️ Clouds cover the sky above,
🌞 Sun shines through at last.

    # Check if the current temperature is above the hot threshold
if current_temp > hot_temp:
    print(f"The current temperature is {current_temp}°C {hot_emoji}")
    
    # Check if the current temperature is below the cold threshold
elif current_temp < cold_temp:
    print(f"The current temperature is {current_temp}°C {cold_emoji}")
    
    # Otherwise, the temperature is within the normal range
else:
    print(f"The current temperature is {current_temp}°C")







### DISPLAY OF GRAPH AT THE END OF THE MONTH/ ANUALL REPORT
the agent can also create a graph of temperature variation in recent months. This feature is designed to help you visualize how the temperature has changed over time and identify any patterns or trends. You can use this information to make informed decisions about how to prepare for changes in the weather.



 import matplotlib.pyplot as plt

    # Define the temperature data
temperatures = [10, 12, 15, 18, 20, 22, 25, 28, 30]  // VALUES TAKEN VIA ASSUMPTION

    # Define the x-axis labels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

    # Plot the temperature data
plt.plot(months, temperatures)

    # Add labels to the graph
plt.title('Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (C)')

    # Show the graph
plt.show()
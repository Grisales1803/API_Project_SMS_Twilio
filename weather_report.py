import requests
import json

def weather(city):
  '''
  Function that obtains the weather based on the city. 
  '''
  # Error management
  try:
    # Call the API with the city
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=21ef0bb1788c87ed4b0fa9b7a851e162&units=metric')
    # Save the json content of the variable r in a variable called response_dict
    response_dict = r.json()
    # Capture the weather description
    description = response_dict["weather"][0]["description"].title()
    # Capture the temperature in Celsius
    temp = response_dict['main']['temp']
    # Send the description and temperature value to the HTML page
    return temp, description
  # In case there is an error with the API, send 'null' to both variables
  except Exception as e:
    description = "null"
    temp = "null"
    return temp, description
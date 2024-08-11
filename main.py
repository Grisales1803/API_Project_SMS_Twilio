import requests
import datetime
from people_space import whoSpace
from weather_report import weather
from database import create_database
from harry_potter import random_hp_character
from twilio_sms import send_SMS
from flask import Flask, render_template, request, jsonify 

app = Flask('app')
# Activate the App inside Flask
# / is the main page of the website, example AOL
@app.route('/')  
def home():
  return render_template('index.html')

@app.route('/send_sms_final', methods=['POST'])
def send_sms_final():
  # Obtain the number of people in space
  n_people_space = whoSpace()
  # Obtain the information from the database
  contacts = create_database()
  # Initialize confirmation message
  conf = 'Message has been sent to: '
  # Get the current date and time
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  # Create a counter to check on the last contact
  counter = 0
  for contact in contacts:
    # Extract contact name
    contact_name = contact['Name']
    # Extract the weather based on the city
    city = contact['City']
    temp, description = weather(city)
    # Obtain the data from Harry Potter API
    hp_character, he_she, his_her, wizard_text, house_text, hp_picture = random_hp_character()
    # Build the message
    message = f'''
    Hello {contact_name}! Interesting fact: There are {n_people_space} people in the space right now!.
    The temperature in {city} is {temp} Celsius with {description}. Your random Harry Potter's character is {hp_character}.
    {he_she}{wizard_text}{he_she}{house_text}{his_her} picture is the following: {hp_picture}
    Date and Time: {date_time}
    ''' 
    # Send the SMS with Twilio
    send_SMS(contact, message)
    counter += 1
    # Append the contact name to the confirmation message
    if counter < len(contacts):
      conf += f'{contact_name}, '
    else:
      conf += f'{contact_name}.'

  # Log the message in a .txt file
  with open('messages.txt', 'a') as file:
    file.write(message)
  
  # Open the confirmation page with the confirmation message
  return render_template("confirmation.html", conf=conf)


# Run the app
app.run(host='0.0.0.0', port=8080)


import requests
import json
import random

def random_hp_character():
    # Save the content of the API in a variable called 'r'
    r = requests.get('https://hp-api.herokuapp.com/api/characters')

    # Save the json content of the variable r in a variable called response_dict
    response_dict = r.json()

    # Obtain the total number of characters
    total_caracters = len(response_dict)

    # Obtain a random number from 0 to total_caracters
    random_number = random.randint(0, total_caracters-1)

    # Extract one of the characters
    character = response_dict[random_number]

    # Extract the information requiered
    name = character['name']
    gender = character['gender']
    if gender == 'male':
        he_she = 'He'
        his_her = 'His'
    elif gender == 'female':
        he_she = 'She'
        his_her = 'Her'
    else:
        he_she = 'It'
        him_her = 'Its'
    wizard = character['wizard']
    if wizard:
        wizard_text = ' is a wizard. '
    else:
        wizard_text = ' is not a wizard. '
    house = character['house']
    if house == "":
        house_text = ' does not belong to a wizard house. '
    else:
        house_text = f' belongs to {house} house. '
    picture = character['image']
    if picture == "":
        picture_text = 'Does not have a picture available right now.'
    else:
        picture_text = picture

    return name, he_she, his_her, wizard_text, house_text, picture_text
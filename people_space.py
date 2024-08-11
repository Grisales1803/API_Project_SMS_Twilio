import requests
import json

def whoSpace():
    '''
    Function that returns the number of people in space right now
    '''
    # Save the content of the API in a variable called 'r'
    r = requests.get('http://api.open-notify.org/astros.json')

    # Save the json content of the variable r in a variable called response_dict
    response_dict = r.json()

    # Extract the values (Which is a list of dictionaries) from the key 'people' and save it in a list called 
    # people
    people = response_dict['people']
    # Extract all the names that are in the key 'name' for every dictionary in the list called people
    names = [person['name'] for person in people]

    # Return the number of people in space 
    number_people_space = len(names)
    return number_people_space

    # Print the current number of people in the space:
    #print(f"The number of people in the space is: {len(names)}")
    #print('')

    # Print their names
    #print('Their names are:')
    #print('')
    # Print the list of names
    #for name in names:
    #    print(name)
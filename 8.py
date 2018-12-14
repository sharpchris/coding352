# Codebites URL: https://codechalleng.es/bites/21/
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

space = '+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+'
# 1. Get all Jeeps
def get_all_jeeps(cars=cars):
    #produces a list of jeeps
    jeeps = cars['Jeep']
    #converts list to string, ref: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
    jeeps_str = ', '.join(jeeps)
    #returns the jeeps string
    return jeeps_str
#calls the function
print(get_all_jeeps())
print(space)

# 2. Get the first car of every manufacturer
def get_first_of_type(cars=cars):
    # loops through the cars dictionary and grabs the keys
    first_cars = []
    for key in cars.keys():
        first_cars.append(cars[key][0])
    return first_cars
    
print(get_first_of_type())
print(space)

# 3. Get all vehicles containing the string 'Trail' in their names
def get_trails(cars=cars):
    # makes an empty string that we'll insert trail cars into
    trail_cars = []
    # loops through teh values in cars
    for v in cars.values():
        # loops through v, which is the list containing specific models
        for i in v:
            # Checks if "Trail" is included in name: ref: https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
            if "Trail" in i:
                trail_cars.append(i)
    return trail_cars

print(get_trails())
print(space)

# 4. Sort the models (values) alphabetically

def sort_models(cars=cars):
    # empty list to store all models
    all_cars = []
    # loop through car models and grab values
    for v in cars.values():
        # loop through list of cars and extract specific models
        for i in v:
            # push all models into single list
            all_cars.append(i)
    # sort dat list bruh
    all_cars.sort()
    # return dat shat
    return all_cars

print(sort_models())
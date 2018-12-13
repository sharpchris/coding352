cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    Jeep_models = cars['Jeep']
    models_string = ', '.join(Jeep_models)
    return models_string


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_cars = []
    for manufacturerer in cars:
        first_cars.append(cars[manufacturerer][0])
    return first_cars


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    # Make the grep string lowercase to satisfy case-insensitivity
    search_string = grep.lower()
    matching_models = []
    for models_of_manufacturerer in cars.values():
        for model in models_of_manufacturerer:
            # search_string is lowercase, and make the car model lowercase
            # in order to satisfy case-insensitivity
            if search_string in model.lower():
                matching_models.append(model)

    # Sort alphabetically
    matching_models.sort()
    return matching_models


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""

    # The "value" of each dict key is a list object
    for list_of_models in cars.values():
        list_of_models.sort()

    return cars

"""
get_all_jeeps()
first_cars = get_first_model_each_manufacturer()
print(first_cars)
matching_models = get_all_matching_models()
print(matching_models)
sorted_cars = sort_car_models()
print(sorted_cars)
"""


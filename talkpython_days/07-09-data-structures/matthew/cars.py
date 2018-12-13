cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    print((', ').join(cars['Jeep']))
    return((', ').join(cars['Jeep']))
        

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    my_list=[cars[i][0] for i in cars.keys()]
    print(my_list)
    return my_list


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    my_list= []
    for v in cars.values():
        for model in v:
            if grep in model.lower():
                my_list.append(model)
                print(my_list)
    return my_list
                

def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for v in cars.values():
        v.sort()
    print(cars)
    return cars

# get_all_jeeps()
# get_first_model_each_manufacturer()
# get_all_matching_models()
sort_car_models()
def make_car(manufacturer, model, **car_info):
    #Build a dictionary containing everything we know about the car.
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

car_profile = make_car('saburu', 'outback', color='blue', tow_package=True)

print(car_profile)
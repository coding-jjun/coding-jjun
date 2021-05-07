def make_car(manufacturer,model,**car_information):
    car_information['manufacturer']=manufacturer
    car_information['model']=model
    return car_information
o=make_car('Subaru', 'outback', color='blue', tow_package=True)
print(type(o))
print(o)
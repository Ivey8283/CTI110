#Zachary Ivey
#10/5/2024
#P2LAB2
#Tests our knowledge on how to use a dictionary to store and display data to a user

car_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26,
    }

keys = car_mpg.keys()
 
print("car_names(['Camaro', 'Prius', 'Model S', 'Silverado'])")

vehicle = input("Enter a vehicle to see it's mpg: ", )

mpg = car_mpg[vehicle]

print('The', vehicle, 'gets', mpg, 'mpg.')

miles = input('How many miles will you drive the ' + vehicle + '?')

gallons_of_gas = float(miles) / float(mpg)

print(f'{gallons_of_gas:.2f}', 'gallon(s) of gas are needed to drive the ' + vehicle + ' ' + miles + ' miles.')

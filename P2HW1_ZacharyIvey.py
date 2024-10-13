#Zachary Ivey
#10/12/2024
#P2HW1
#tests the students ability to edit and enhance old projects

print('This program calculates and displays travel expenses')

budget = float(input('Enter Budget: '))

location = input('Enter your travel destination: ')

gas = float(input('How much do you think you will spend on gas? '))

accomodation = float(input('Approximately, how much will you need for accomodation/hotel? '))

food = float(input('Last, how much do you need for food? '))

print('------------Travel Expenses------------')

print(f'{'Location:':<20} {location}')

print(f'{'Initial Budget:':<20} ${budget:.2f}')

print(f'{'Fuel:':20} ${gas:.2f}')

print(f'{'Accomodation:':<20} ${accomodation:.2f}')

print(f'{'Food:':<20} ${food:.2f}')

print('---------------------------------------')

remaining_balance = budget - gas - accomodation - food

print(f'{'Remaining Balance: ':<20} ${remaining_balance:.2f}')


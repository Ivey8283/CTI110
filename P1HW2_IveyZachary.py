#Zachary Ivey
#9/27/2024
#P1HW2
#Program that preforms basic math with entered data from a user.
#Program is written using Pseudocode logic

print('This program calculates and displays travel expenses')


budget = int(input('Enter Budget: '))
           #budget Will represent the budget for the trip

location = input('Enter your travel destination: ')
            #the location value represents the desired location

gas = int(input('How much do you think you will spend on gas? '))
           #gas represent the amount of money the user spends on gas

accomodation = int(input('Approximately, how much will you need for accomodation/hotel? '))
            #accomodation represents the money spend on accomodations

food = int(input('Last, how much do you need for food? '))
            #food represents how much is spent on food

print('------------Travel Expenses------------')

print('Location: ', location)
        #using the location variable will input the value entered by the user

print('Initial Budget: ', budget)
        #using the budget variable will input the value the user inputted for the budget prompt

print('Fuel: ', gas)
        #gas represents the value the user inputted into the gas prompt

print('Accomodation', accomodation)
        #accomodation represents the value the user inputted into the accomodation prompt

print('Food', food)
        #food is the value the user inputted into the food prompt

remaining_balance = budget - gas - accomodation - food
        #the variable "remaining_balance" is the remainder of the budget after all the expenses are taken out

print('Remaining Balance: ', remaining_balance)
        #this number is what's left in the budget

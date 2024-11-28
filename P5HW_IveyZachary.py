#Zachary Ivey
#11-23-2024
#P5HW
#Tests the students ability to use loops, functions, and module imports to complete a program

import random

def add_game():
    num1 = random.randint(1,250)
    num2 = random.randint(1,250)
    correct_ans = num1 + num2

    print(num1, '+', num2)

    guesses = 0

    while True:
        try:
            ans = int(input('Enter Answer. '))
            guesses +=1

            if ans < correct_ans:
                print('Sorry, guess is too low.')
            elif ans > correct_ans:
                print('Sorry, guess is too high.')
            else:
                print('Congratulations!!!! Your answer is correct.')
                print(f'Number of guesses: {guesses}')
                break
        except ValueError:
            print()

def sub_game():
    num1 = random.randint(1,250)
    num2 = random.randint(1,250)
    correct_ans = num1 - num2

    print(num1, '-', num2)

    guesses = 0

    while True:
        try:
            ans = int(input('Enter Answer.  '))
            guesses +=1

            if ans < correct_ans:
                print('Sorry, guess is too low.')
            elif ans > correct_ans:
                print('Sorry, guess is too high.')
            else:
                print('Congratulations!!!! Your answer is correct.')
                print(f'Number of guesses: {guesses}')
                break
        except ValueError:
            print()


def menu():
    while True:
        print('MAIN MENU')
        print('----------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        
        try:
            option = int(input('Please choose one of the menu options: '))

            if option == 1:
                add_game()
            elif option == 2:
                sub_game()
            else:
                print('Thank you for playing...')
                print('Bye!!')
                break
        except ValueError:
            print('1, 2, or 3?')

menu()

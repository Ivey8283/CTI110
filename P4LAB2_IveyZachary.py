#Zachary Ivey
#11-7-2024
#P4LAB2
#Test's the students knowledge of to write code to display information to a user using loops
while True:
        try:
            num = int(input('Enter an integer: '))
            
            if num < 0:
                print('This program does not handle negative numbers.')
                another = input('Would you like to run the program again? : ')
                if another != 'yes':
                    print('Exiting program.')
                    break
                continue
            
            for i in range(1, 13):
                print(f'{num} * {i} = {num * i}')

            another = input('Would you like to run the program again?: ')
            if another != 'yes':
                print('Exiting program...')
                break
        except ValueError:
            print('Enter an integer')

#Zachary Ivey
#10/19/2024
#P3LAB
#Tests the students ability towrite code to display information to the user

money = float(input('Enter the amount of money as a float: $',))

cents = money * 100

dollars = int(cents) // 100
cents = cents - dollars * 100

quarters = int(cents) // 25
cents = cents - quarters * 25

dimes = int(cents) // 10
cents = cents - dimes * 10

nickels = int(cents) // 5
cents = cents - nickels * 5

pennies = int(cents) // 1
cents = cents - pennies * 1

if dollars == 1:
    print('Dollar', dollars)

elif dollars >= 2:
    print("Dollars", dollars)

elif money == 0:
    print('No change')

else:
    pass

if quarters == 1:
    print('Quarter', quarters)

elif quarters >= 2:
    print("Quarters", quarters)

else:
    pass
    
if dimes == 1:
    print('Dime', dimes)

elif dimes >= 2:
    print('Dimes', dimes)

else:
    pass

if nickels == 1:
    print('Nickel', nickels)

elif nickels >= 2:
    print('Nickels', nickels)

else:
    pass

if pennies == 1:
    print('Penny', pennies)

elif pennies >= 2:
    print('Pennies', pennies)

else:
    pass

#Zachary Ivey
#10/13/2024
#P2HW2
#Helps the students ability to use lists

module1 = float(input('Enter grade for module 1: '))
module2 = float(input('Enter grade for module 2: '))
module3 = float(input('Enter grade for module 3: '))
module4 = float(input('Enter grade for module 4: '))
module5 = float(input('Enter grade for module 5: '))
module6 = float(input('Enter grade for module 6: '))

#these will be what the student puts in for their module grades

module_grades = [module1, module2, module3, module4, module5, module6]

#this makes the inputed grades into a list

print('------------Results------------')

#this is to make the program look neater

print(f'{'Lowest Grade:':<20} {min(module_grades)}')

#this will display the lowest grade in the list

print(f'{'Highest Grade:':<20} {max(module_grades)}')

#this will display the highest grade in the list

print(f'{'Sum of Grades:':<20} {sum(module_grades)}')

#this will display the sum of all the grades in the list

average_grade = sum(module_grades) / len(module_grades)

#this will calculate the average of all the grades in the list

print(f'{'Average:':<20} {average_grade:.2f}')

#this displays the averages of all the grades in the list

print('-------------------------------------')

#this is to make the program look neater

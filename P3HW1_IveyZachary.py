#Zachary Ivey
#10/19/2024
#P3HW1
#Tests pur ability to correct a code and complete it

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

print('------------Results------------')

print(f'{'Lowest Grade:':<20} {min(grades)}')

print(f'{'Highest Grade:':<20} {max(grades)}')

print(f'{'Sum of Grades:':<20} {sum(grades)}')

avg = sum(grades) / len(grades)

print(f'{'Average:':<20} {avg:.2f}')


# determine letter grade for average

print('-------------------------------------')

if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')

elif avg <= 59:
    print('Your grade is: F') # TO DO: finish this
else:
    print('')

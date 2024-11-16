#Zachary Ivey
#11-10-2024
#P4HW1
#tests the students ability to edit and enhance exiting programs

num_scores = int(input('How many scores do you want to enter? '))
#asks the user for the number of scores

scores = []
#creates a list for the scores

for i in range(num_scores):
#creates a loop for each score
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
#Gets the score from the user
        if 0 <= score <= 100:
#makes sure the score is valid
            scores.append(score)
#Stores the valid scores
            break
#Exits the loop
        else:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
#if the score isnt valid it will prompt the user to enter another
print('-----------Results-----------')
#This is to make the program neater

lowest_score = min(scores)
print(f'Lowest Score  : {lowest_score}')
#gives the lowest score a value and displays the lowest score

scores.remove(lowest_score)
print(f'Modified List : {scores}')
#Removes the lowest score and displays the scores

average_score = sum(scores) / len(scores)
print(f'Scores Average: {average_score:.2f}')
#creates a value and displays the average of all scores

if average_score >= 90:
    letter_grade = 'A'

elif average_score >= 80:
    letter_grade = 'B'

elif average_score >= 70:
    letter_grade = 'C'

elif average_score >= 60:
    letter_grade = 'D'

else:
    letter_grade = 'F'
#gives the average a letter grade

print(f'Grade         :{letter_grade}')
#Displays the letter grade

print('-----------------------------')
#to make the program look neater

#Zachary Ivey
#10/23/2024
#P3HW2
#tests the students understanding of decision structures

employee_name = input("Enter employee's name: ")
#this represents the input for the employee's name

hours_worked = float(input("Enter number of hours worked: "))
#this is the value for number of hours the employee worked

pay = float(input("Enter employee's pay rate: "))
#this represents the employee's pay

print("")
#this is to make the program neater

print("Employee name:     ", employee_name)
#this will display the employee's name

print("Hours Worked      Pay Rate      OverTime      OverTime Pay      RegHour Pay      Gross Pay")
#This will be the the order the data will be displayed in

print("------------------------------------------------------------------------------------------------")

reg_hours = hours_worked
#this will allow the true amount of hours worked to be shown later when all the data is displayed

if reg_hours > 40:
    overtime = reg_hours - 40
    reg_hours = 40
else: overtime = 0
#this if statement assigns anything  over 40 hours into a ovetime variable and also caps the regular hours worked at 40

overtime_pay = overtime * pay * 1.5
#this calculates the overtime pay

if overtime <= 0:
    overtime = 0
    overtime_pay = 0
else: overtime
#this will give overtime a value to default to if there is no overtime

reg_pay = reg_hours * pay
#this calculates the regular pay before overtime

gross_pay = reg_pay + overtime_pay
#this adds the regular pay and overtime pay

print(f"{hours_worked:<15.2f}", f"{pay:<18.2f}", f"{overtime:<15.2f}", f"{overtime_pay:<15.2f}", f"${reg_pay:<15.2f}", f"${gross_pay:<15.2f}")
#this displays all the data

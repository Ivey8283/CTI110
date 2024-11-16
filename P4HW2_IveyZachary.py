#Zachary Ivey
#11-10-2024
#P4HW2
#tests the students ability to edit and enhance excisting programs


def calculate_employee_salary():
    # creates a list to store employee data
    employee_data = []
    
    # totals for the total numbers later
    total_overtime_pay = 0
    total_reg_pay = 0
    total_gross_pay = 0
    total_employees = 0

    while True:
        employee_name = input("Enter employee's name or 'done' to terminate: ")
        
        if employee_name.lower() == "done":
            break
        
        # input for hours worked and pay rate
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay = float(input(f"What is {employee_name}'s pay rate? "))
        
        # display header row for the first employee
        if not employee_data:
            print("\nEmployee name:     Hours Worked      Pay Rate      OverTime      OverTime Pay      RegHour Pay      Gross Pay")
            print("------------------------------------------------------------------------------------------------")
        
        # calculate regular hours and overtime
        reg_hours = hours_worked
        if reg_hours > 40:
            overtime = reg_hours - 40
            reg_hours = 40
        else:
            overtime = 0
        
        overtime_pay = overtime * pay * 1.5
        
        if overtime <= 0:
            overtime = 0
            overtime_pay = 0
        
        # calculates regular pay and gross pay
        reg_pay = reg_hours * pay
        gross_pay = reg_pay + overtime_pay
        
        # store the employees data in the list
        employee_data.append({
            'name': employee_name,
            'hours_worked': hours_worked,
            'pay_rate': pay,
            'overtime': overtime,
            'overtime_pay': overtime_pay,
            'reg_pay': reg_pay,
            'gross_pay': gross_pay
        })
        
        # displays the data for the employee entered
        print(f"{hours_worked:<15.2f}", f"{pay:<18.2f}", f"{overtime:<15.2f}", f"{overtime_pay:<15.2f}", f"${reg_pay:<15.2f}", f"${gross_pay:<15.2f}")
        
        # updates the totals for the total numbers
        total_overtime_pay += overtime_pay
        total_reg_pay += reg_pay
        total_gross_pay += gross_pay
        total_employees += 1
    
    print(f"Total number of employees entered:          {total_employees:}")
    print(f"Total amount paid for overtime:            ${total_overtime_pay:,.2f}")
    print(f"Total amount paid for regular hours:       ${total_reg_pay:,.2f}")
    print(f"Total amount paid in gross:                ${total_gross_pay:,.2f}")
    #displays the total information the user entered

    print("")

# calls the function to run the program again
calculate_employee_salary()

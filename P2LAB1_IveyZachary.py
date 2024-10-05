#Zachary Ivey
#10/5/2024
#P2LAB1
#Test's our ability to wrtie code that performs mathematical calculations\
PI = 3.14159

radius = float(input('What is the radius of the circle? '))

diameter = radius * 2

circum = 2 * PI * radius

area = PI * radius * radius

print('The diameter of the circle is ', f'{diameter:.1f}')

print('The circumference of the circle is ', f'{circum:.2f}')

print('The area of the circle is ', f'{area:.3f}')

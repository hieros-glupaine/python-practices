
# Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Please, enter your name: ")
age = input("Please, enter your age: ")

print(name)
print(age)

# Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.

name = "Grace"
print(name)

name = "George"

name = "Grace"
name = "George"

print(name)

# Below you’ll find some code with a number of errors. Try to go through the program line by line and fix the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.

''' hourly_wage = input("Please enter your hourly wage: ') 

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ") '''

hourly_wage = input("Please enter your hourly wage: ")  
print(hourly_wage) # code was correct though quotations marks were different, and when printing the variable was incorrectly added as a string or variable name w/ typos.

hours_worked = input("How many hours did you work this week? ")
print(hours_worked) # code was correct, however, the order of assigning values to the variable and printing were inverted, resulting in an error.

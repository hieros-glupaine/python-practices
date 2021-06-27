
# Try to approximate the behaviour of the is operator using ==. 
# Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = list1

print(id(list1) == id(list2))

print(list1 is list2)

# Try to use the is operator or the id function to investigate the difference between this:

# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]

# And this:

# numbers = [1, 2, 3, 4]
# numbers.append(5)

# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(id(numbers))
print(id(new_numbers))

numbers = [1, 2, 3, 4]
print("numbers id before: ", id(numbers))

numbers.append(5)
print("numbers id after appending 5: ", id(numbers))

# Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

input_number = int(input("Please, enter a number here: "))

if input_number == 0:
  print("The number you entered is zero.")
elif input_number > 0:
  print("The number you entered is a positive number")
else:
  print("The number you entered is a negative number")

# Write a program to determine whether an employee is owed any overtime. 
# You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. 
# The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. 
# In effect, the employees get paid 110% of their hourly wage for any overtime.

hours_worked = float(input("Please, enter how many hours the employee has worked: "))
hourly_wage = float(input("Please, enter the employee's hourly wage: "))

if hours_worked > 40:
  overtime = (hours_worked - 40) * (hourly_wage * 1.10)
  amount_due = (40 * hourly_wage) + overtime
  print(f"The employee has worked {hours_worked} hours and is owed ${amount_due} including overtime.")
else:
  print(f"The employee has worked {hours_worked} hours and is not owed overtime, their pay is ${hours_worked*hourly_wage}.")


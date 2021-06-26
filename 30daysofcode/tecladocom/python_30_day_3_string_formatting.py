
# Using the variable below, print "Hello, world!". You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.

greeting = "Hello, world"

print(greeting+"!")

# Ask the user for their name, and then greet the user, using their name as part of the greeting.
# The name should be in title case, and shouldn't be surrounded by any excess white space.

user_name = input("Please, enter your name: ")
greeting = f"Hello, {user_name}!"

print(greeting.title())

# Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019

# Outpout should look like this: Joker (2019), directed by Todd Phillips

output1 = f"{title} ({release_year}), directed by {director}"

print(output1)

output2 = "{0} ({1}), directed by {2}"

print(output2.format("Joker",2019,"Todd Phillips"))

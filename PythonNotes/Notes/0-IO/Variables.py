# A variable is a storage container

x = 6
x = "string"
x = 7.654

#	Variables can be reassigned to different data types

#### More Professional Way To Print Variables  ####
name = input("What is your name? ")
name = name.title()
school = input(f"{name}, what school do you attend? ")
subject = input(f"Ok, {name} at {school}, what is your favorite subject? ")
grade = int(input(f"{name}, what did you get on your last test? "))
print(f"Wow, {name}, you got a {grade} in your {subject} test!")

'''
	<variable> = <something>
	<variable> == <something>  #Checks to see if they are equivalent
'''

# CONSTANTS - Python does not have a 'const' keyword
GRAVITY = 9.81
PI = 3.141593653589


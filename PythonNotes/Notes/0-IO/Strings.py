import string

'''
String Data Type:
	- Non-Primitive
	- Iterable
	- Sequence Data Type
	- Array of Characters
'''

# All Data Input Is Strings
num1 = input("Number 1: ")
num2 = input("Number 2: ")

print(num1 + num2) # Concatenates the strings
#No C-Style Casting

'''
Escape Characters:
	\n = New Line
	\t = Tab
	\\s = Space
	\" = Quote
	\' = Apostrophe
	\b = Backspace
	\\ = Backslash
'''

#### Iterables: ####
firstName = "Brett"
lastName = "Crawdaddy"
print(firstName + lastName) # Outputs "Brett Crawdaddy"
print(firstName, lastName)  # Outputs "BrettCrawdaddy"
print(firstName * 2)        # Outputs "BrettBrett"

fullName = ""
fullName += firstName
fullName += lastName
fullName *= 2

print(len(firstName)) # Outputs 5

# Strings can be indexed into with subscript operator

username = f"{firstName}.{lastName}"
email = f"{username}@stu.evsck12.com"
print(email)

# [startChar : endChar+1]
# [startChar : ] Gets to the end of the string
print(email[2:7])
print(email[len(email)-4:])
print(email[-4:])

print(email[::-1]) # Prints the string backwards
print(email[::2])  # Prints every second character

print(string.ascii_letters)
print(string.ascii_lowercase[::-1])

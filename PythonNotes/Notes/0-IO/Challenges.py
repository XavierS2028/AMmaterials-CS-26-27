import string

# Challenge 1
num = input("What is your credit card number? ")

print(f"{num[0:len(num)-4]}####")

# Challenge 2
url = input("What is the URL? ")

if url.endswith(".gov"):
	print("URL is government")
else:
	print("URL is non-government")

# Challenge 3

# Challenge 4

	# Found ".isalnum" from https://www.w3schools.com/python/python_ref_string.asp
key = input("What is your API key? ")

if not key.isalnum():
	print("Not all characters are letters or numbers.")
else:
	print("All characters are numbers or letters.")

# Challenge 5

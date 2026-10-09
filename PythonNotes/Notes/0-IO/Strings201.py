'''
Ask the user for their email
Print out their username in the format of 
	"Welcome {username}!"
'''

email = input("What is your email? ")

firstName = ""
lastName = ""
username = ""

def loopExtraction():
	for i in range(len(email)):
		if email[i] == "@":
			username = email[0:i]
			break

	for i in range(len(username)):
		if username[i] == ".":
			firstName = username[0:i]
			lastName = username[i+1:len(username)]

username = email[0:email.find("@")]
firstName = username[0:username.find(".")]
lastName = username[username.find(".")+1:]

'''
#### String Methods ####
	- Returns the string after the original chars have been replaced.
	  <string>.replace(<originalChar>, <newChar>)

	- Find
		<string>.find(<char>)
		Returns -1 if character is not found
	
	- Index
		<string>.index(<char>)
		Throws error if character is not found

	- Title
		<string>.title()
		Returns the string that has been turned to Title Case

	- Strip
		<string>.strip()  - Removes leading and trailing spaces
		<string>.lstrip() - Removes leading spaces
		<string>.rstrip() - Removes trailing spaces

	- Search
		<string>.startswith()
		<string>.endwith()
#### #### #### #### #### 
'''

# username = email[0:14]

print(f"Welcome {username}!")
print(f"Welcome, {firstName.title()} {lastName.title()}!")

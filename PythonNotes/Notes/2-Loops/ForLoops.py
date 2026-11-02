# ForLoops.py
import string
'''
for <variable> in <list>:
    doSomething

for i in range(0, <highestNumber - 1>):
    doSomething


range(<startValue>, <endValue - 1>, <stepSize>)


'''



#for i in range(0, 100):
#    print(i)


for i in range(0, 21, 2):
    print(i)

print()

for i in range(1, 20, 2):
    print(i)

print()

for i in range(0, 201, 20):
    print(i)

print()

for i in range(10, -1, -1):
    print(i)

print()

for i in string.ascii_uppercase:
    print(i)

print()


#classrooms = ["Jones", "Kebortz", "Valentine"]
#subjects = ["History", "English", "Biology"]

#for room in range(0, len(classrooms)):
#    print(f"{classrooms[room]} teaches {subjects[room]}")

#firstnames = ["jim", "john", "jo", "jon", "james", "j"]
#lastnames = ["bo", "smith", "robert", "snow", "cameron", "k"

#for i in range(len(firstnames)):
#    print(f"{firstnames[i]}.{lastnames[i]}@stu.evsck12.com")


word = "McDonald's Play Place"
wordList = []

for letter in word:
    wordList.append(letter)

for i in range(len(wordList)):
    if wordList[i] in "aeiou":
        wordList[i] = "*"

for letter in wordList:
    print(letter, end="")

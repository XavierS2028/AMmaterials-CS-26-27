# GradeCalculator.py

percentage = int(input("Percentage on test: "))

percentageArticle = "A"
letterGrade       = ""
letterArticle     = "a"

if (percentage == 8) or (percentage == 18) or ((80 <= percentage) and (percentage <= 89)):
    percentageArticle = "An"

if percentage < 60:
    letterGrade = "F"
elif percentage < 70:
    letterGrade = "D"
elif percentage < 80:
    letterGrade = "C"
elif percentage < 90:
    letterGrade = "B"
else:
    letterGrade = "A"

if (letterGrade == "A") or (letterGrade == "F"):
    letterArticle = "an"

print(f"{percentageArticle} {percentage} got you {letterArticle} {letterGrade}!")
#FutureDay.py
currentDate = int(input(
"""Enter today's day:
    Sunday    - 0
    Monday    - 1
    Tuesday   - 2
    Wednesday - 3
    Thursday  - 4
    Friday    - 5
    Saturday  - 6
> """))
currentDate = currentDate % 7

daysElapsed = int(input("""Enter the number of days elapsed since today: """))

futureDate = currentDate + daysElapsed
futureDate = futureDate % 7

dayNames = ["Sunday", 
            "Monday", 
            "Tuesday", 
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"]

currentDayName = dayNames[currentDate]
futureDayName = dayNames[futureDate]

print(f"Today is {currentDayName} and the future day is {futureDayName}")
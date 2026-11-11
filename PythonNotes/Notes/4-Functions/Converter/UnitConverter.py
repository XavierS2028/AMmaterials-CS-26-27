# UnitConverter.py

from DistanceConversions import *
from TemperatureConversions import *

#global variables/objects
menu = '''
    in to ft (if)           mph to kph (mk)
    ft to in (fi)           kph to mph (km)

    tbsp to tsp (tbts)      lbs to kg (lk)
    tsp to tbsp (tstb)      kg to lbs (kl)

    c to f (cf)             oz to cups (oc)
    f to c (fc)             cups to oz (co)

    stop (stop)

What would you like to do?
> '''

userInput = input(menu)

while userInput != "stop":
    if userInput == "if":
        print(inchesToFeet(float(input("Inches: "))))
    elif userInput == "fi":
        print(feetToInches(float(input("Feet: "))))
    elif userInput == "tbts":
        pass
    elif userInput == "tstb":
        pass
    elif userInput == "cf":
        print(celsiusToFahrenheit(float(input("Celsius: "))))
    elif userInput == "fc":
        print(fahrenheitToCelsius(float(input("Fahrenheit: "))))
    elif userInput == "mk":
        pass
    elif userInput == "km":
        pass
    elif userInput == "lk":
        pass
    elif userInput == "kl":
        pass
    elif userInput == "oc":
        pass
    elif userInput == "co":
        pass
    else:
        print("I'm sorry, I don't know what you mean.")

    userInput = input(menu)

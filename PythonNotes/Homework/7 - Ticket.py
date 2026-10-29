# Ticket.py
ticketSize = 0
ticketSizes = ["You are not getting a ticket", 
               "You are getting a small ticket", 
               "You are getting a big ticket"]

speed = int(input("Do you know how fast you were going? (mph) "))
isBirthday = input("Say, is it your birthday? (y/n) ")

if isBirthday == "y":
    isBirthday = True
else:
    isBirthday = False

if isBirthday:
    speed -= 5

if speed <= 60:
    ticketSize = 0
elif speed <= 80:
    ticketSize = 1
else:
    ticketSize = 2

print(ticketSizes[ticketSize])
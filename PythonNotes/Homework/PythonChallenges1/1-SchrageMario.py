# SchrageMario.py

for i in range(1, 5):
    spaceCount = 4 - i

    spaces = ""
    hashes = ""

    for j in range(0, spaceCount):
        spaces += " "

    for k in range(0, i):
        hashes += "#"

    print(f"{spaces}{hashes} {hashes}{spaces}")
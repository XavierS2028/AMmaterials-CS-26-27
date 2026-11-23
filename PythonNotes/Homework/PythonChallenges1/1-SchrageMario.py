# SchrageMario.py

height = int(input("Height: "))

for layer in range(1, height + 1):
    spaceCount = height - layer

    spaces = ""
    hashes = ""

    for j in range(spaceCount):
        spaces += " "

    for k in range(layer):
        hashes += "#"

    print(f"{spaces}{hashes} {hashes}{spaces}")

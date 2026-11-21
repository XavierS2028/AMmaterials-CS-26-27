# 99BottlesOfPythonJuice.py

for bottles in range(99, -1, -1):
    nextWord = "bottles"

    if bottles == 2:
        nextWord = "bottle"

    if bottles >= 2:
        print(f"{bottles} bottles of python juice on the wall, {bottles} bottles of python juice")
        print(f"Take one down and pass it around, {bottles - 1} {nextWord} of python juice on the wall")

    elif bottles == 1:
        print("One bottle of python juice on the wall, one bottle of python juice")
        print("Take one down and pass it around, no more bottles of python juice on the wall")

    elif bottles == 0:
        print("No more bottles of python juice on the wall, no more bottles of python juice")
        print("Go to the store and buy some more, 99 bottles of python juice on the wall")

    print()
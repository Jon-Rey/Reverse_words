
running = True

while running:

    string = input("Reverse: ")
    str(string)
    newString = ""

    for c in reversed(string):
        newString += c

    print(newString)

    if string == "999":
        running = False



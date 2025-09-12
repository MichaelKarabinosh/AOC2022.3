with open("InputFile", "r") as file:
    lines = file.readlines()
    num = 0
    for line in lines:
        half = int(len(line) / 2)
        firstComp = line[:half]
        secondComp = line[half:]
        for string in firstComp:
            if string in secondComp:
                if string.isupper():
                    num += ord(string.lower()) - 70
                else:
                    num += ord(string) - 96
                break

    print("Part One:", num)






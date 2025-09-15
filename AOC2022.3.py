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
    num = 0
    counter = 0
    res = []
    n = 3

    for i in range(0,len(lines),n):
       res.append(lines[i:i + n])

    for entry in res:
        firstComp = res[0]
        secondComp = res[1]
        thirdComp = res[3]
        for string in firstComp:
            if string in secondComp:
                if string in thirdComp:
                    if string != "\n":
                        if string.isupper():
                            num += ord(string.lower()) - 70
                        else:
                            num += ord(string) - 96
                        break
    print(num)
    print(res)
    hi = "jkff"







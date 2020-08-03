fileread = open("sched", "r")
filewrite = open("courses", "w")
req = open("pos", "w")
term = "F"
classes = []
while True:
    line = fileread.readline()

    if not line:
        break

    #print(line)
    Flag = False
    for i in line:
        if i.isdigit():
            Flag = True
            break
    if line[0:1] == 'X':
        term = line[1:2]
        continue
    if not ((line[len(line) - 2:len(line) - 1].isupper() or line[len(line) - 2:len(line) - 1] == "h" or line[len(
            line) - 2:len(line) - 1] == "u") and (Flag and line[len(line) - 2:len(line) - 1] != "A" and 85 > len(line) > 35)):
        continue
    #print(len(line))
    # get term

    # set discipline
    word = line[0:3] + " "

    # set class num
    counter = 0
    for i in line:
        if i.isdigit():
            break
        counter += 1
    word += line[counter:counter + 3]

    # to write in all classes if wanted

    if word not in classes:
        classes.append(word)
        req.writelines(word + "\n")
    word += " "
    # set term
    word += term + " "

    # set periods
    index = 0
    counter = 0
    seenum = False
    for i in line:  # get index start
        if i.isdigit() and not seenum:
            index = counter
            seenum = True
        elif i != ',' and i != 's' and not i.isdigit():
            seenum = False
        counter += 1

    word += "["
    for i in line[index:]:
        if i.isdigit():
            word += i
        elif i == "s":
            word += i
        elif i == ",":
            word += " "
        else:
            break
    word += "] "

    # set days
    for i in line[index:]:
        if not i.isdigit() and i != "s" and i != "," and i != " ":
            word += i
    word += ""

    #filewrite.writelines(word)

print("done")
fileread.close()
filewrite.close()

fileread = open("requirements", "r")
filewrite = open("reqs", "w")

while True:
    line = fileread.readline()
    if not line:
        break
    word = line[0:3] + " "
    counter = 0
    for i in line:
        if i.isdigit():
            break
        counter += 1
    word += line[counter:counter + 3] + " :"
    line = fileread.readline() # blank
    line = fileread.readline()
    # first find where the last : is
    # get 3 uppercase letters, then find the next num, then look for or/and right after, if none are found end it there
    counter = 0
    index = 0
    for i in line:
        if i == ":":
            index = counter
            if  line[index-1:index] == ")" and line[index-2:index-1] == "s":
                break
        counter+=1
    if index == 0 or line[index-1:index] != ")":
        filewrite.writelines(word + "\n")
        line = fileread.readline()
        continue
        # get first prereq
    if line[index+2:index+5] == "Per" or line[index+2:index+5] == "By ":
        word += " PERMISSION of instructor"
        line = fileread.readline()
        filewrite.writelines(word + "\n")
        continue
    # 3 year case
    if line[index + 2:index + 5] == "3 y":
        line = fileread.readline()
        filewrite.writelines(word + "\n")
        continue
    # off stands for offered
    if line[index + 2:index + 5] == "Off":
        line = fileread.readline()
        filewrite.writelines(word + "\n")
        continue
    # comma case
    while True:
        # add the letter
        # 'At ' case to any, should be changed
        if line[index + 2:index + 5] == "at " or line[index + 2:index + 5] == "At ":
            word += " any "
        else:
            word += line[index+1:index+5] + " "
        # print(line[index+6:index+9])
        if line[index+2:index+5] == "any":
            word += line[index+6:index+9].upper() + " "
        find = 0
        dex = index
        # if junior sophomore or senior, dont get numbers
        if not (line[index+2:index+5] == "sen" or line[index+2:index+5] == "sop" or line[index+2:index+5] == "jun" ):
            for i in line[index:]:
                if i.isdigit():
                    word+=line[dex:dex+3]
                    break
                dex += 1
            if line[dex+3:dex+4] == ",":
                word += " and "
                index = dex+4
                continue
            word += " "
        break

    # and statement
    # find next cap and look 4 then 3 before
    bigW = dex
    for i in line[dex:]:
        if i.isupper():
            break
        bigW += 1
    # print(line[bigW-2:bigW-1])
    if line[bigW-2:bigW-1] == "d":
        word += line[bigW-4:bigW-1]
        word += " "
        word += line[bigW: bigW+3]
    elif line[bigW-2:bigW-1] == "r":
        word += line[bigW - 3:bigW-1]
        word += " "
        word += line[bigW: bigW + 3]
    else:
        line = fileread.readline()
        filewrite.writelines(word + "\n")
        continue
    word += " "
    # second num
    dex = bigW
    for i in line[dex:]:
        if i.isdigit():
            word+=line[dex:dex+3]
            break
        dex += 1

    # start pre req checks
    # first get down the and or statements


    line = fileread.readline()
    filewrite.writelines(word + "\n")




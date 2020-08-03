filewrite = open("map", "w")
vizwrite = open("forViz", "w")
fileread = open("reqs", "r")
allNodes = open("pos", "r")

# first thing is to add all of the "x" -> "y"
while True:
    line = fileread.readline()
    if not line:
        break
    word = line[:7]
    # look for a word after :
    # after you find a word, go to next space and then look for next cap word
    counter = 9
    while True:
        for i in line[counter:]:
            if not (not i.isupper() or i.isdigit()) and len(line) > counter+5:
                if line[counter:counter+3] == "PER":
                    counter += 6
                    break
                # any 200 case
                if line[counter:counter+3] == "ANY" or line[counter:counter+3] == "ONE" or line[counter:counter+3] == "TWO":
                    tempSearch = open("pos", "r")

                    # get past any differences in letters
                    for p in line[counter:]:
                        if p.isdigit():
                            break
                        counter += 1
                    # print(line[counter:counter+1])
                    counter -= 4
                    while True:
                        line2 = tempSearch.readline()
                        if not line2:
                            break
                        if line2[:4] == line[:4]:
                            print("LINE: " + line2[4:5] + " MAIN: " + line[counter+4:counter+5])
                        if line2[4:5] == line[counter+4:counter+5] and line2[:4] == line[:4]:
                            filewrite.writelines(line2[:7] + " -> " + word + "\n")
                            vizwrite.writelines("\"" + line2[:7] + "\" -> \"" + word + "\"" + "\n")
                else:
                    temp = line[counter:counter+7]
                    filewrite.writelines(temp + " -> " + word + "\n")
                    vizwrite.writelines("\"" + temp + "\" -> \"" + word + "\"" + "\n")
                counter += 6
                break
            counter += 1
        # get to next space
        for i in line[counter:]:
            if i == " ":
                break
            counter += 1
        if counter >= len(line):
            break


    # vizwrite.writelines("\"" + word + "\"" + "\n")
    filewrite.writelines(word + "\n")



# I should add all the nodes after I've added the originals

while True:
    line = allNodes.readline()
    if not line:
        break

# param yours: the classes you have
# param needed is the classes you need to complete the requirement
from heuristics import *
# This is where you decide whether or not to add a certain class, trying to add as few as possible without getting rid of important classes
def addFillers(current):
    current.append("2017 ANY 111 F [1] T")
    current.append("2017 ANY 112 F [2] T")
    current.append("2017 ANY 115 F [5] T")
    current.append("2017 ANY 116 F [6] T")
    return current
def decideImportant(course, completed, req):
    available = []
    final = []
    temp = completeRemainders(completed, req)
    for i in course:
        if i[5:12] in temp:
            final.append(i)
            continue
        fileread = open("reqs(H)", "r")
        while True:
            line = fileread.readline()
            if not line:
                break
            if line[0:7] in temp:
                # if it's part of the classes needed to unlock
                if i[5:12] in line:
                    final.append(i)
                    continue
    return final
    # I also need to figure out whether this class unlocks a class thats in my requirements
def completeRemainders(yours, needed):
    satisfied = 0
    failures = 0
    temp = []
    for i in needed:
        for j in i[1:]:  # check each element and return whether it it's in yours
            if j in yours:
                satisfied += 1
        if satisfied < i[0]:
            failures += i[0]-satisfied
            for x in i[1:]:
                temp.append(x)
        satisfied = 0
    return temp

def complete(yours, needed):
    satisfied = 0
    for i in needed:
        for j in i[1:]:  # check each element and return whether it it's in yours
            if j in yours:
                satisfied += 1
        if satisfied < i[0]:
            return False
        satisfied = 0
    return True
# the lower this num the better, if you complete a course it will return 0
def completeNum(yours, needed):
    satisfied = 0
    failures = 0
    for i in needed:
        for j in i[1:]:  # check each element and return whether it it's in yours
            if j in yours:
                satisfied += 1
        if satisfied < i[0]:
            failures += i[0]-satisfied
        satisfied = 0
    return str(failures)

def completeNumSAY(yours, needed):
    print("\n")
    satisfied = 0
    failures = 0
    for i in needed:
        for j in i[1:]:  # check each element and return whether it it's in yours
            if j in yours:
                satisfied += 1
        if satisfied < i[0]:
            failures += i[0]-satisfied
            print("Failed ", i[0]-satisfied, " ", i)
        satisfied = 0
    if failures == 0:
        print("All requirements met, heuristic has graduated")
    return str(failures)

def create():
    filewrite = open("Example of mapping", "w")
    fileread = open("reqs(H)", "r")
    allNodes = open("pos", "r")
    requirements = {}
    while True:
        line = fileread.readline()
        if not line:
            break
        # what I have to do here is create a map where each key is a class, and its value is a list of requirements to complete
        diff = 0
        start = 17
        classes = [[0]]
        flag = False
        if line[10:13] == "PER":
            classes[diff][0] += 1
            tempSearch = open("pos", "r")
            change = int(line[4])
            change -= 1
            num = str(change)
            # print(num)
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                if line2[4:5] == num and line2[:4] == line[:4]:
                    classes[diff].append(line2[0:7])
            start = 100
        elif line[10:13] == "ANY":
            classes[diff][0] += 1
            start = 0
            tempSearch = open("pos", "r")
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                # print(line[14:15])
                counter = 8
                for p in line[counter:]:
                    if p.isdigit():
                        break
                    counter += 1
                if line2[4:5] == line[counter] and line2[:4] == line[:4]:
                    classes[diff].append(line2[0:7])
        elif line[10:13] == "TTH":
            classes[diff][0] += 2
            start = 0
            tempSearch = open("pos", "r")
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                # print(line[14:15])
                counter = 8
                for p in line[counter:]:
                    if p.isdigit():
                        break
                    counter += 1
                if line2[4:5] == line[counter] and line2[:4] == line[:4]:
                    classes[diff].append(line2[0:7])
        elif line[10:13] == "THR":
            classes[diff][0] = 3
            start = 0
            tempSearch = open("pos", "r")
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                if line2[:3] == line[:3]:
                    classes[diff].append(line2[0:7])
        elif line[10:13] == "TWO":
            classes[diff][0] = 2
            start = 0
            tempSearch = open("pos", "r")
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                if line2[:3] == line[:3]:
                    classes[diff].append(line2[0:7])
        elif line[10:13] == "ONE":
            classes[diff][0] = 1
            start = 0
            tempSearch = open("pos", "r")
            while True:
                line2 = tempSearch.readline()
                if not line2:
                    break
                if line2[:3] == line[:3]:
                    classes[diff].append(line2[0:7])
        elif line[10:13] == "JUN" or line[10:13] == "SOP" or line[10:13] == "SEN":
            start = 13
            classes[diff][0] += 1
            classes[diff].append(line[10:13])
        elif len(line) >= 17:
            classes[diff][0] += 1
            classes[diff].append(line[10:17])

        # first bit complete, starting from wherever repeat this, if it's and, create a array after adding to diff, and then add that class
        # if it's or, tack on that class to diff
        while(start < len(line)):
            for i in line[start:]:
                if i == "o":  # this means or
                    if line[start+3:start+6] == "JUN" or line[start+3:start+6] == "SOP" or line[start+3:start+6] == "SEN":
                        classes[diff].append(line[start+3:start+6])
                        start+=6
                    else:
                        # 3 past is where to get the 6 letters
                        classes[diff].append(line[start+3:start+10])
                        start += 9
                    break
                if i == "a": # this means and
                    # print(line[start+4:start+7])
                    diff += 1
                    classes.append([1])
                    if line[start+4:start+7] == "JUN" or line[start+4:start+7] == "SOP" or line[start+4:start+7] == "SEN":
                        classes[diff].append(line[start+4:start+7])
                        # print(classes)
                        start+=7
                    else:
                        classes[diff].append(line[start + 4:start + 11])
                        start += 10
                    break
                start += 1

        requirements[line[0:7]] = classes
        filewrite.writelines(line[0:7] + ": " + ' '.join(map(str, classes)) + "\n")
    return requirements

requirements = create()

def combinations(finished):
    test = finished
    filesched = open("courses", "r")
    term = ""
    noDup = []
    while True:
        line = filesched.readline()
        if not line:
            break
        if term == "":
            term = line[13]
        elif term != line[13]:
            size = 0
            duplic = []
            duplic2 = []
            for i in noDup:
                if not (i[5:12] in requirements and complete(test, requirements.get(i[5:12]))): #TODO change test
                    continue
                space = 0
                for x in reversed(i):
                    if x == " ":
                        break
                    space += 1
                for p in noDup:
                    if not (p[5:12] in requirements and complete(test, requirements.get(p[5:12]))): #TODO change test
                        continue
                    if p in duplic2:
                        continue
                    flag = True
                    if i[5:12] == p[5:12]:
                        continue
                    space2 = 0
                    for x in reversed(p):
                        if x == " ":
                            break
                        space2 += 1
                    for m in i[16:len(i)-space-2]:
                        if m.isdigit():
                            if m in p[16:len(p)-space2-2]:
                                for n in i[len(i)-space:]:
                                    if n in p[len(p)-space2:]:
                                        flag = False
                    if flag: # that means these two work, then look for a third class
                        for q in noDup:
                            if not (q[5:12] in requirements and complete(test, requirements.get(q[5:12]))): #TODO change test
                                continue
                            if q[5:12] == i[5:12] or q[5:12] == p[5:12]:
                                continue
                            if q in duplic2:
                                continue
                            flag2 = True
                            space3 = 0
                            for x in reversed(q):
                                if x == " ":
                                    break
                                space3 += 1
                            for x in q[16:len(q)-space3-2]:
                                if x.isdigit():
                                    if x in i[16:len(i)-space-2] or x in p[16:len(p)-space2-2]: # if either is same period
                                        for n in q[len(q)-space3:]:
                                            if n in p[len(p)-space2:] or n in i[len(i)-space:]:
                                                flag2 = False
                            num = i[5:9] + str(((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                            flag3 = False
                            if flag2 and num not in duplic:
                                duplic.append(i[5:9] + str((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                                print("[" +i[5:12] + "] + [" + p[5:12] + "] + [" + q[5:12]+"]")
                                size += 1
                    duplic2.append(i)
            print("There were ", size, " combinations")
            print("\nnext term will be Year " + line[:4] + " Term " + line[13])
            term = line[13]
            noDup = []

            print("Say anything to continue")
            temp = input()
        if line[5:12] in requirements:
            if complete(test, requirements.get(line[5:12])) and line[5:12] not in test:
                noDup.append(line)

def possible(comp):
    # THIS IS TO SEE POSSIBLE CLASSES
    filesched = open("courses", "r")
    classWrite = open("classes", "w")
    print("Enter F for fall, W for winter, S for summer: ")
    finished = comp
    test = comp
    term = ""
    term = input()
    print("Enter the year")
    year = 0
    year = input()
    noDup = []
    while True:
        line = filesched.readline()
        if not line:
            break
        # print(line[:7])
        # print(line[:4])
        if line[13] == term and line[:4] == year:
            if line[5:12] in requirements:
                if complete(test, requirements.get(line[5:12])) and line[5:12] not in test and line[5:12] not in noDup and line[5:12] not in finished:
                    noDup.append(line[5:12])
                    print("You can take " + line[5:12])
                    classWrite.writelines(line[5:12] + "\n")

def choose(heuristic, completed, req):
    # in theory this is the method that chooses the classes
    year = ""
    term = ""
    noDup = []
    counts = 0
    filesched = open("courses", "r")
    while True:
        line = filesched.readline()
        if not line:
            break
        if term == "":
            term = line[13]
            year = line[:4]
        elif term != line[13]:
            choose = []
            duplic = []
            duplic2 = []
            noDup = decideImportant(noDup, completed, req)
            noDup = addFillers(noDup)
            #print(noDup)
            #print("noDup2: ", decideImportant(noDup, completed, req))
            for i in noDup:
                if not (i[5:12] in requirements and complete(completed, requirements.get(i[5:12]))):
                    continue
                space = 0
                for x in reversed(i):
                    if x == " ":
                        break
                    space += 1
                for p in noDup:
                    if not (p[5:12] in requirements and complete(completed, requirements.get(p[5:12]))): #TODO change test
                        continue
                    if p in duplic2:
                        continue
                    flag = True
                    if i[5:12] == p[5:12]:
                        continue
                    space2 = 0
                    for x in reversed(p):
                        if x == " ":
                            break
                        space2 += 1
                    for m in i[16:len(i)-space-2]:
                        if m.isdigit():
                            if m in p[16:len(p)-space2-2]:
                                for n in i[len(i)-space:]:
                                    if n in p[len(p)-space2:]:
                                        flag = False
                    if flag: # that means these two work, then look for a third class
                        for q in noDup:
                            if not (q[5:12] in requirements and complete(completed, requirements.get(q[5:12]))): #TODO change test
                                continue
                            if q[5:12] == i[5:12] or q[5:12] == p[5:12]:
                                continue
                            if q in duplic2:
                                continue
                            flag2 = True
                            space3 = 0
                            for x in reversed(q):
                                if x == " ":
                                    break
                                space3 += 1
                            for x in q[16:len(q)-space3-2]:
                                if x.isdigit():
                                    if x in i[16:len(i)-space-2] or x in p[16:len(p)-space2-2]: # if either is same period
                                        for n in q[len(q)-space3:]:
                                            if n in p[len(p)-space2:] or n in i[len(i)-space:]:
                                                flag2 = False
                            num = i[5:9] + str(((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                            flag3 = False
                            if flag2 and num not in duplic:
                                duplic.append(i[5:9] + str((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                                choose.append([i[5:12], p[5:12], q[5:12]])
                    duplic2.append(i)
            # at this point you have every class you could take this term
            # this is where I should make heuristic methods to add the classes, you give it your completed classes and the list of possible classes, and you add in one of the 3 classes
            #TODO CHANGE HERE
            three = heuristic(completed, choose, req)
            for i in three:
                completed.append(i)
            nice = ""
            for i in three:
                nice += "[" + i + "] "
            print("\nYear " + year + " Term " + term + ": " + nice)
            term = line[13]
            counts += 1
            year = line[:4]
            # the \n is there because for some reason after ANY 100 and SOP it adds \n to SOP
            if counts == 3:
                completed.append("SOP")
                completed.append("SOP\n")
            elif counts == 6:
                completed.append("JUN")
                completed.append("JUN\n")
            elif counts == 9:
                completed.append("SEN")
                completed.append("SEN\n")
            noDup = []
            #print(completed)
            # this is where I am going to create the useless class filter
        # I think this means the class does not exist..?
        elif line[5:12] in requirements and complete(completed, requirements.get(line[5:12])) and line[5:12] not in completed:
            noDup.append(line)

    completeNumSAY(completed, req)
"""
print("\nDoes this satisfy a CS BA?")

if complete(test, BAC):
    print("YES")
else:
    print("NO")
print("\nDoes this satisfy a PHY BA?")
if complete(test, BAP):
    print("YES")
else:
    print("NO")
    print("WAS " + completeNum(test, BAP) + " OFF")
"""
# param startdate: Year, term, eg 2019F
def recommend(heuristic, completed, req, startDate):
    # in theory this is the method that chooses the classes
    year = ""
    term = ""
    noDup = []
    counts = 0
    filesched = open("courses", "r")
    work = False
    work2 = False
    while True:
        line = filesched.readline()
        if not line:
            break
        if term == "":
            term = line[13]
            year = line[:4]
            if year == startDate[0:4]:
                work = True
        elif term != line[13]:
            starter = True
            if not work or not work2:
                term = line[13]
                counts += 1
                year = line[:4]
                if year == startDate[0:4]:
                    work = True
                if work and term == startDate[4:]:
                    work2 = True
                starter = False
                noDup = []
            if starter:
                choose = []
                duplic = []
                duplic2 = []
                noDup = decideImportant(noDup, completed, req)
                noDup = addFillers(noDup)
                #print(noDup)
                #print("noDup2: ", decideImportant(noDup, completed, req))
                for i in noDup:
                    if not (i[5:12] in requirements and complete(completed, requirements.get(i[5:12]))):
                        continue
                    space = 0
                    for x in reversed(i):
                        if x == " ":
                            break
                        space += 1
                    for p in noDup:
                        if not (p[5:12] in requirements and complete(completed, requirements.get(p[5:12]))): #TODO change test
                            continue
                        if p in duplic2:
                            continue
                        flag = True
                        if i[5:12] == p[5:12]:
                            continue
                        space2 = 0
                        for x in reversed(p):
                            if x == " ":
                                break
                            space2 += 1
                        for m in i[16:len(i)-space-2]:
                            if m.isdigit():
                                if m in p[16:len(p)-space2-2]:
                                    for n in i[len(i)-space:]:
                                        if n in p[len(p)-space2:]:
                                            flag = False
                        if flag: # that means these two work, then look for a third class
                            for q in noDup:
                                if not (q[5:12] in requirements and complete(completed, requirements.get(q[5:12]))): #TODO change test
                                    continue
                                if q[5:12] == i[5:12] or q[5:12] == p[5:12]:
                                    continue
                                if q in duplic2:
                                    continue
                                flag2 = True
                                space3 = 0
                                for x in reversed(q):
                                    if x == " ":
                                        break
                                    space3 += 1
                                for x in q[16:len(q)-space3-2]:
                                    if x.isdigit():
                                        if x in i[16:len(i)-space-2] or x in p[16:len(p)-space2-2]: # if either is same period
                                            for n in q[len(q)-space3:]:
                                                if n in p[len(p)-space2:] or n in i[len(i)-space:]:
                                                    flag2 = False
                                num = i[5:9] + str(((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                                flag3 = False
                                if flag2 and num not in duplic:
                                    duplic.append(i[5:9] + str((int(i[9:12]) * int(p[9:12]) * int(q[9:12])) + int(i[9:12]) + int(p[9:12]) + int(q[9:12])))
                                    choose.append([i[5:12], p[5:12], q[5:12]])
                        duplic2.append(i)
                # at this point you have every class you could take this term
                # this is where I should make heuristic methods to add the classes, you give it your completed classes and the list of possible classes, and you add in one of the 3 classes
                #TODO CHANGE HERE
                three = heuristic(completed, choose, req)
                for i in three:
                    completed.append(i)
                nice = ""
                for i in three:
                    nice += "[" + i + "] "
                print("\nYear " + year + " Term " + term + ": " + nice)
                term = line[13]
                counts += 1
                year = line[:4]
                # the \n is there because for some reason after ANY 100 and SOP it adds \n to SOP
                if counts == 3:
                    completed.append("SOP")
                    completed.append("SOP\n")
                elif counts == 6:
                    completed.append("JUN")
                    completed.append("JUN\n")
                elif counts == 9:
                    completed.append("SEN")
                    completed.append("SEN\n")
                noDup = []
            #print(completed)
            # this is where I am going to create the useless class filter
        # I think this means the class does not exist..?
        elif line[5:12] in requirements and complete(completed, requirements.get(line[5:12])) and line[5:12] not in completed:
            noDup.append(line)
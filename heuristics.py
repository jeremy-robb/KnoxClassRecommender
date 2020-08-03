# THOUGHTS: I just realized that for unlocking, you should only worry about
# unlocking if it is NOT for the elements

from tools import *


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
            failures += i[0] - satisfied
        satisfied = 0
    return str(failures)


# --------------------------------------------------------
# comp: This is the classes you have completed
# possible: This is a list of all the possible classes you could take
# req: This is the list of all the requirements you need to graduate

def takeFirstSeen(complete, possible, req):
    return possible[0]


def takeCSClasses(complete, possible, req):
    best = possible[0]
    maxpoints = 0
    for i in possible:
        points = 0
        for x in i:
            if x == "MAT 175" or x == "MAT 151":
                points += 3
            elif x[:3] == "CS ":
                points += 1
        if points > maxpoints:
            maxpoints = points
            best = i
    return best


def doublemajorCSPHY(comp, possible, req):
    BAP = [[4, "PHY 110", "PHY 130", "PHY 205", "MAT 205"], [2, "PHY 310", "PHY 312", "PHY 313", "PHY 314"],
           [1, "PHY 241", "PHY 245"], [2, "PHY 310", "PHY 312", "PHY 313", "PHY 314"],
           [5, "PHY 310", "PHY 312", "PHY 313", "PHY 314", "PHY 241", "PHY 242", "PHY 245", "PHY 260", "PHY 308",
            "PHY 316", "PHY 317", "PHY 300", ], [1, "MAT 210", "MAT 215", "MAT 230"]]
    BAC = [[8, "CS  141", "CS  142", "MAT 175", "CS  292", "CS  205", "CS  208", "CS  214", "CS  220"],
           [3, "CS  303", "CS  305", "CS  308", "CS  309", "CS  317", "CS  320", "CS  322", "CS  330", "CS  340",
            "CS  375", "CS  395", "CS  399", "CS  400"], [1, "CS  322", "CS  399", "CS  400"]]
    phy = 3
    cs = 3
    for i in comp:
        if i[:3] == "CS ":
            phy += 1
        elif i[:3] == "PHY":
            cs += 1
    if complete(comp, BAC):
        cs = 0
    elif complete(comp, BAP):
        phy = 0
    best = possible[0]
    maxpoints = 0
    for i in possible:
        points = 0
        for x in i:
            if x == "MAT 175" or x == "MAT 151" or x == "MAT 152" or x == "MAT 230" or x == "MAT 205":
                points += 90
            elif x[:3] == "CS ":
                points += cs
            elif x[:3] == "PHY":
                points += phy
        if points > maxpoints:
            maxpoints = points
            best = i
    return best


# choose the combination that best completes your major
# adding small bonus if item is in the major for now
def mostComplete(comp, possible, req):
    best = possible[0]
    maxpoints = 0
    for i in possible:
        points = 0
        temp = comp.copy()
        added = 0
        for x in i:
            temp.append(x)
            offset = int(completeNum(comp, req)) - int(completeNum(temp, req))
            points += offset - added
            if offset > added:
                added = offset
        # print(i, " had ", points, " points")
        if points > maxpoints:
            maxpoints = points
            best = i
    return best


def bonusToUnlockers(comp, possible, req):
    best = possible[0]
    maxpoints = 0
    for i in possible:
        points = 0
        temp = comp.copy()
        added = 0
        for x in i:
            extra = 0
            temp.append(x)
            reqRead = open("Example of mapping", "r")
            extraPoints = []
            while (True):
                line = reqRead.readline()
                if not line:
                    break
                temporary = extraPoints.copy()
                temporary.append(line[0:7])
                if x in line and (completeNum(extraPoints, req) > completeNum(temporary, req)):
                    extra += .51
                    extraPoints.append(line[0:7])
            offset = int(completeNum(comp, req)) - int(completeNum(temp, req))

            # if offset == 0 and extra == 0:  # This is to speed up the process, if something is worth nothing then just don't even consider it
            # break

            points += offset - added + extra
            if offset > added:
                added = offset
        # print(i, " had ", points, " points")
        if points > maxpoints:
            maxpoints = points
            best = i
    return best


def bonusToUnlockersTieMajor(comp, possible, req):
    best = possible[0]
    maxpoints = 0
    for i in possible:
        points = 0
        temp = comp.copy()
        added = 0
        offset = 0
        for x in i:
            if x == "ANY cls":
                points += .1
            extra = 0
            temp.append(x)
            reqRead = open("Example of mapping", "r")
            extraPoints = []
            extraBonus = 0
            while (True):
                line = reqRead.readline()
                if not line:
                    break
                temporary = extraPoints.copy()
                temporary.append(line[0:7])
                on = False
                for c in takeFrom:
                    if x[0:3] in c:
                        on = True
                if x in line and (completeNum(extraPoints, req) > completeNum(temporary, req)) and on:
                    extra += .51
                    extraPoints.append(line[0:7])
                if x == "CHI 225":  # TODO : You may need to tweak this number, this is to break the SL requirement, smaller number means break it later
                    extra += 3
            prev = offset
            offset = int(completeNum(comp, req)) - int(completeNum(temp, req))
            if offset > prev:
                for c in takeFrom:
                    if x[0:3] in c:
                        extraBonus += .5
            # if offset == 0 and extra == 0:  # This is to speed up the process, if something is worth nothing then just don't even consider it
            # break
            points += offset - added + extra + extraBonus
            if offset > added:
                added = offset
        # print(i, " had ", points, " points")
        if points > maxpoints:
            maxpoints = points
            best = i
    return best

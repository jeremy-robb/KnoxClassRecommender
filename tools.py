from lists import *
takeFrom = []

def chooseMajors():
    print("")
    print("To choose a major, type the first 3 letters of the specialization, followed by the first 2 letters of the degree")
    print("Examples: CS BA (Computer Science BA) , MATBA (Math BA) , PHYMI (Physics minor)")
    print("Choose major one")

    while True:
        major1 = input()
        if isAdded(major1.upper()):
            break
        else:
            print("Choose any of the following: ", added)
    while True:
        print("Choose major two")
        major2 = input()
        if isAdded(major2.upper()) and major2.upper() != major1.upper():
            break
        else:
            print("Choose any of the following (besides the first major): ", added)
    takeFrom.append(major1.upper())
    takeFrom.append(major2.upper())
    if "PHY" in major1.upper() or "PHY" in major2.upper():
        takeFrom.append("MATBA")
    return major([major1.upper(), major2.upper()])

def getTranscript():
    print("If you already have your transcript code (as given by this program), paste it here. If not, press enter to continue. If you do not have a transcript (incoming students), type 'new'")
    start = input()
    if len(start) > 0 and start[0] == "~":
        return list(start[1:].split("-"))
    print("To start, navigate to your unofficial transcript page (https://my.knox.edu/ICS/Registrar/Student_Tools/Unofficially_Transcript.jnz), and copy paste (ctrl a, ctrl c) the entire page here (ctrl v)")
    final = "~"
    trancount = 0
    fileread = open("courses", "r")
    avail = []
    while True:
        line = fileread.readline()
        if not line:
            break
        if line[5:8] not in avail:
            avail.append(line[5:8])
    while True:
        word = input()
        trancount += 1
        if trancount == 175:
            print("It looks like something went wrong, message Jeremy Robb (jarobb@knox.edu) to recieve instructions on how to properly paste in your transcript")
        if word == "Unofficial Transcript PDF ":
            break
        counter = 0
        flag = False
        if not word[0:3] in avail:
            continue
        for x in word:
            if x.isdigit() and len(word) - counter - 3 > 0:
                flag = True
                break
            counter += 1
        if not flag:
            continue
        #  at this point we can assume it's a class I need to add
        if "N/A" in word:
            continue
        final += word[0:3] + " " + word[counter:counter+3] + "-"
    debug = input()  #  This is just to get rid of the final line
    if len(final) > 1:
        print("")
        print("Your code is: ")
        print(final)
        return list(final[1:].split("-"))
    else:
        print("It looks like something went wrong, message Jeremy Robb (jarobb@knox.edu) to recieve instructions on how to properly paste in your transcript")
        return []

def addStatus(transcript):
    if len(transcript) >= 27:
        transcript.append("SOP")
        transcript.append("JUN")
        transcript.append("SEN")
    elif len(transcript) >= 18:
        transcript.append("SOP")
        transcript.append("JUN")
    elif len(transcript) >= 9:
        transcript.append("SOP")
    return transcript
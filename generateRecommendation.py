from available import *
from heuristics import *
from lists import *
from tools import *
print("To generate your class recommendations, press enter. If you would like to run a four year simulation, type 'sim'")
choice = input()
if choice == "sim" or choice == "new":
    requirements = create()
    major = chooseMajors()
    choose(bonusToUnlockersTieMajor, subject(""), major)
else:
    requirements = create()
    finished = getTranscript()
    finished = addStatus(finished)
    major = chooseMajors()
    recommend(bonusToUnlockersTieMajor, finished, major, "2020F")

#combinations(subject(""))
#possible(subject(""))
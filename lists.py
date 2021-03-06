from heuristics import *
def subject(name):
    if name == "aaku":
        return ["SOP", "CS  141", "CS  142", "CS  220", "MAT 175", "MAT 145", "MAT 131", "PSY 100"]
    elif name == "jeremy":
        return ["SOP", "JUN", "MAT 145", "MAT 131", "CS  141", "CS  142", "CS  220", "CS  214", "CS  205", " CS 375",
         "MAT 175", "CS  208", "MAT 123", "CS  208", "CS  375", "MAT 123", "CS  320", "CS  330", "CS  399", "MAT 121"]
    elif name == "blank":
        return [""]

    return ["MAT 131", "MAT 121"]

def isAdded(major):
    if major in added:
        return True
    return False

added = ["CS BA", "BIOBA", "PHYBA", "MATBA"]
elements = [[1, "CHI 103", "FRE 103", "GER 103", "GRK 103", "JAP 103", "LAT 103", "SPA 103", "CHI 201", "CHI 202", "CHI 221", "CHI 203", "CHI 238", "CHI 225", "CHI 220", "FRE 210", "FRE 201", "FRE 230", "FRE 215", "FRE 240", "GER 201", "GER 210", "GER 235", "GRK 215", "GRK 218", "GRK 212", "LAT 215", "LAT 212", "LAT 217", "LAT 211", "LAT 270", "LAT 218", "SPA 201", "SPA 205", "SPA 206", "SPA 230", "SPA 235", "SPA 220", "SPA 221", "SPA 222", "SPA 209", "SPA 208", "SPA 233"],
[1, "ANS 102", "ANS 103", "ANS 201", "ANS 275", "ANS 276", "ASI 142", "BUS 280", "CLA 104", "CLA 110", "CLA 111", "CLA 271", "ECO 110", "ECO 120", "EDU 201", "EDU 202", "EDU 203", "ENV 110", "ENV 115", "GER 332", "GER 332", "GER 334", "GER 334", "GWS 227", "GWS 231", "GWS 267", "GWS 267", "GWS 332", "HIS 104", "HIS 106", "HIS 107", "HIS 110", "HIS 111", "HIS 115", "HIS 133", "HIS 142", "HIS 160", "HIS 161", "HIS 181", "HIS 202", "HIS 267", "HIS 271", "HIS 281", "JOU 123", "LAS 122", "LAS 227", "LAS 231", "PHI 215", "PS  101", "PS  122", "PS  125", "PS  128", "PS  135", "PS  210", "PS  220", "PS  227", "PS  231", "PS  234", "PS  236", "PS  237", "PS  240", "PS  245", "PS  268", "PSY 205", "PSY 234", "REL 101", "REL 271"],
[1, "AFS 210", "AFS 228", "AFS 254", "AMS 241", "ANS 102", "ANS 103", "ANS 201", "ANS 241", "ANS 276", "ASI 221", "ASI 320", "ASI 321", "CHI 221", "CHI 320", "CHI 321", "CLA 103", "CLA 273", "CLA 275", "EDU 201", "ENG 242", "ENG 245", "ENG 261", "ENV 228", "FIL 261", "GER 332", "GER 332", "GWS 101", "GWS 222", "GWS 227", "GWS 231", "GWS 261", "GWS 267", "GWS 267", "GWS 273", "GWS 322", "GWS 332", "GWS 333", "GWS 334", "HIS 160", "HIS 161", "HIS 181", "HIS 228", "HIS 267", "HIS 271", "HIS 280", "HIS 281", "IDI 120", "IDI 220", "LAS 122", "LAS 227", "LAS 230", "LAS 231", "LAS 326", "LAS 334", "MUS 130", "MUS 210", "MUS 254", "PJS 100", "PS  122", "PS  125", "PS  128", "PS  227", "PS  231", "PS  236", "PS  237", "PS  241", "PS  243", "PS  268", "PS  326", "PS  333", "PS  334", "REL 103", "REL 271", "SPA 230"],
[1, "ART 110", "ART 112", "ART 113", "ART 114", "ART 115", "ART 116", "ART 117", "ART 119", "ART 214", "DAN 145", "DAN 152", "ENG 104", "ENG 205", "ENG 206", "ENG 207", "ENG 208", "ENG 209", "ENV 284", "ENV 384", "JOU 119", "MUS 100", "MUS 145", "MUS 100", "THT 121", "THT 131", "THT 209", "THT 224", "THT 233", "THT 271"],
[1, "AFS 210", "ART 105", "ART 106", "ART 202", "ASI 221", "ASI 321", "ASI 225", "CHI 331", "CHI 321", "CHI 225", "CLA 104", "CLA 110", "CLA 111", "CLA 202", "CLA 203", "CLA 270", "CLA 273", "CLA 273", "DAN 260", "ENG 105", "ENG 120", "ENG 123", "ENG 124", "ENG 125", "ENG 126", "ENG 200", "ENG 204", "ENG 205", "ENG 223", "ENG 227", "ENG 231", "ENG 232", "ENG 245", "ENG 247", "ENG 251", "ENG 252", "ENG 253", "ENG 261", "ENG 351", "ENG 352", "ENG 353", "ENV 118", "ENV 126", "FIL 124", "FIL 225", "FIL 261", "FIL 337", "FRE 215", "FRE 223", "GER 235", "GER 337", "GRK 211", "GRK 311", "GRK 218", "GRK 318", "GWS 261", "GWS 273", "HIS 104", "HIS 110", "HIS 111", "LAS 235", "LAT 211", "LAT 311", "LAT 218", "LAT 318", "MUS 101", "MUS 131", "MUS 210", "MUS 244", "PHI 115", "PHI 118", "PHI 125", "PHI 130", "PHI 142", "PHI 210", "PHI 211", "PHI 212", "PHI 218", "PHI 228", "PHI 230", "PHI 244", "PHI 247", "PHI 270", "PHI 284", "REL 125", "REL 203", "REL 284", "SPA 235", "THT 151", "THT 251", "THT 281", "THT 351", "THT 352", "THT 353"],
[1, "ANS 203", "BIO 110", "BIO 120", "BIO 130", "CHE 100", "CHE 102", "CHE 205", "CHE 211", "CHE 273", "ENV 101", "ENV 125", "ENV 170", "PHY 110", "PHY 120", "PHY 130", "PHY 130", "PHY 161", "PHY 163", "PHY 165", "PHY 167", "PHY 205", "PHY 242", "PSY 100", "PSY 202"],
[1, "BIO 331", "BUS 333", "CHE 205", "CS  141", "CS  142", "CS  208", "ECO 110", "ECO 120", "ECO 333", "ENV 188", "MAT 121", "MAT 123", "MAT 131", "MAT 145", "MAT 151", "MAT 152", "MAT 175", "MAT 185", "MAT 205", "MAT 225", "MUS 245", "PHI 202", "PHY 110", "PHY 120", "PHY 130", "PHY 130", "PHY 205", "PS  200", "PSY 281", "STA 200", "STA 225"]]
#@param, a list of all majors you want, convention is first 3 letters are the spec, second 2 letters are the degree, eg ARTBA (art bachelor of arts)
#CS BS (computer science bachelor of science) PHYMI (physics minor)
def major(majors):
    soFar = elements
    for i in majors:
        if i[:3] == "CS ":
            soFar = CS(soFar, i[3:])
        elif i[:3] == "PHY":
            soFar = PHY(soFar, i[3:])
        elif i[:3] == "BIO":
            soFar = BIO(soFar, i[3:])
        elif i[:3] == "MAT":
            soFar = MAT(soFar, i[3:])
    return soFar


def addSpec(soFar, toAdd):
    for i in toAdd:
        soFar.append(i)
    return soFar
def MAT(soFar, degree):
    if degree == "BA":          # NOT PART
        return addSpec(soFar, [[1, "MAT 151"], [7, "MAT 152", "MAT 185", "MAT 205", "MAT 210", "MAT 231", "MAT 241", "CS  141"],[4, "MAT 175", "MAT 211", "MAT 215", "MAT 216", "MAT 217", "MAT 218", "MAT 225", "MAT 227", "MAT 230", "MAT 295", "MAT 311", "MAT 313", "MAT 321", "MAT 322", "MAT 325", "MAT 327", "MAT 331", "MAT 332", "MAT 333", "MAT 341", "MAT 342", "MAT 400"],[1, "MAT 311", "MAT 313", "MAT 321", "MAT 322", "MAT 325", "MAT 327", "MAT 331", "MAT 332", "MAT 333", "MAT 341", "MAT 342", "MAT 400"],[1, "MAT 361", "MAT 399", "MAT 400"],[1, "BIO 331", "CHE 321", "CS  142", "PHY 130", "PHY 205", "PHY 205", "PHY 241", "PHY 242", "PHY 245", "PHY 260"]])

def CS(soFar, degree):
    if degree == "BA":
        return addSpec(soFar, [[8, "CS  141", "CS  142", "MAT 175", "CS  292", "CS  205", "CS  208", "CS  214", "CS  220"],[3, "CS  303", "CS  305", "CS  308", "CS  309", "CS  317", "CS  320", "CS  322", "CS  330", "CS  340", "CS  375", "CS  395", "CS  399", "CS  400"],[1, "CS  322", "CS  399", "CS  400"]])

def PHY(soFar, degree):
    if degree == "BA":             #NOTE: This is not actually part of it
        return addSpec(soFar, [[3, "MAT 152", "MAT 151", "MAT 151"], [4, "PHY 110", "PHY 130", "PHY 205", "MAT 205"],[2, "PHY 310", "PHY 312", "PHY 313", "PHY 314"],[1, "PHY 241", "PHY 245"], [2, "PHY 310", "PHY 312", "PHY 313", "PHY 314"],[5, "PHY 310", "PHY 312", "PHY 313", "PHY 314", "PHY 241", "PHY 242", "PHY 245", "PHY 260", "PHY 308", "PHY 316", "PHY 317", "PHY 300"],[1, "MAT 210", "MAT 215", "MAT 230"]])

def BIO(soFar, degree):
    if degree == "BA":
        return addSpec(soFar, [[4, "BIO 110", "BIO 120", "BIO 130", "BIO 210"],[1, "BIO 311", "BIO 312", "BIO 314", "BIO 315", "BIO 316", "BIO 317", "BIO 319"],[1, "BIO 320", "BIO 321", "BIO 324", "BIO 325", "BIO 328", "BIO 329"],[1, "BIO 331", "BIO 332", "BIO 333", "BIO 335", "BIO 336", "BIO 338", "BCH 265", "BCH 334", "BCH 335", "BCH 340", "BCH 345"],[4, "BIO 311", "BIO 312", "BIO 314", "BIO 315", "BIO 316", "BIO 317", "BIO 319", "BIO 320", "BIO 321", "BIO 324", "BIO 325", "BIO 328", "BIO 329", "BIO 331", "BIO 332", "BIO 333", "BIO 335", "BIO 336", "BIO 338", "BCH 265", "BCH 334", "BCH 335", "BCH 340", "BCH 345"],[1, "BIO 380", "BIO 400"],[1, "BIO 381", "BIO 400", "BIO 382", "BIO 383", "BIO 384", "BIO 385"],[2, "CHE 100", "CHE 102"]])
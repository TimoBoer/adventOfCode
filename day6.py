def createDependencies(orbitlist, orbitFromCOM):
    if len(orbitlist) > 0:
        for orbit in orbitlist:
            if (orbit[:3] == orbitFromCOM[-1]):
                orbitFromCOM.append(orbit[-3:])
                createDependencies(orbitlist, orbitFromCOM)
                orbitFromCOM.pop()

    if len(orbitFromCOM) > 1:
        result = orbitFromCOM[:]
        allOrbits.append(result)

def countOrbits(allOrbits):
    total = 0
    for path in allOrbits:
        for orbit in path:
            total += 1
    return total

data_file = open("input06.txt", "r")
orbitFile = data_file.read().splitlines()
allOrbits = []
createDependencies(orbitFile, ["COM"])
print(countOrbits(allOrbits))
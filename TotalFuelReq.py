#calculate the total needed fuel for all modules and fuel
#ModuleMassList is an array
def TotalFuelCalc(ModuleMassList):
    totalfuel = 0
    for mass in ModuleMassList:
        mass = mass // 3 - 2
        totalfuel += mass
        while mass // 3 - 2 > 0:
            mass = mass // 3 - 2
            totalfuel += mass
    return totalfuel


#IntcodeComputer with + and * functions
#intcode is an array.
def IntcodeComputer(intcode):
    i = 0
    while i < len(intcode) and intcode[i] != 99:
        if intcode[i] == 1:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        elif intcode[i] == 2:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        else:
            print("an unexpected integer was encountered at:" , i, "namely:",intcode[i])
            return 0
        i = i + 4
    return intcode


#bruteforce find noun + verb for goal (19690720)
def SolveGravityAssist(initialMemory, goal):
    for i in range(100):
        for j in range(100):
            intcode = initialMemory[:]
            intcode[1] = i
            intcode[2] = j
            if IntcodeComputer(intcode)[0] == goal:
                return intcode


def wireIntersection(wirepath):
    wiredelta = [wireDelta(wire) for wire in wirepath]
    wireCord = [calcCord(wire) for wire in wiredelta]
    #we now have coordinates for the lines
    for index,wireOneCord in enumerate(wireCord[0][1:]):
        for index,wireTwoCord in enumerate(wireCord[1][1:]):


def wireDelta(wire):
    for index,wirestep in enumerate(wire):
        if wirestep[0] == "L":
            wire[index] = [-1 * int(wirestep[1:]), 0]
        elif wirestep[0] == "R":
            wire[index] = [int(wirestep[1:]), 0]
        elif wirestep[0] == "U":
            wire[index] = [0, int(wirestep[1:])]
        else:
            wire[index] = [0, -1 * int(wirestep[1:])]
    return wire


def calcCord(wire):
    wire.insert(0, [0, 0])
    for index, wirestep in enumerate(wire):
        if index > 0:
            wire[index][0] = wire[index - 1][0] + wire[index][0]
            wire[index][1] = wire[index - 1][1] + wire[index][1]
    wire.pop(0)
    return wire


#input handling.
text_file = open("C:/Users/T.boer/Documents/pystuff/input.txt", "r")
ModuleMassList = [int(val) for val in text_file.read().splitlines()]

text_file = open("C:/Users/T.boer/Documents/pystuff/intcode.txt", "r")
initialMemory = [int(val) for val in text_file.read().split(",")]

text_file = open("C:/Users/T.boer/Documents/pystuff/inputwires.txt", "r")
wirepathlines = text_file.read().splitlines()
wirepath = [line.split(",") for line in wirepathlines]
wireIntersection(wirepath)
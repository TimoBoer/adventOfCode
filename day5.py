def IntcodeComputer(intcode, inputs):
    i = 0
    results = []
    while intcode[i] != 99:
        opcode = int(str(intcode[i])[-2:])
        parameters = str(intcode[i])[:-2]
        if opcode == 1:
            i = calc(i, parameters, intcode, "add")
        elif opcode == 2:
            i = calc(i, parameters, intcode, "multi")
        elif opcode == 3:
            intcode[intcode[i + 1]] = inputs.pop(0)
            i = i + 2
        elif opcode == 4:
            if parameters == "1":
                results.append(intcode[i + 1])
            else:
                results.append(intcode[intcode[i + 1]])
            i = i + 2
        elif opcode == 5:
            i = jump(i, parameters, intcode, "true")
        elif opcode == 6:
            i = jump(i, parameters, intcode, "false")
        elif opcode == 7:
            i = equal(i, parameters, intcode, "less")
        elif opcode == 8:
            i = equal(i, parameters, intcode, "equal")
        else:
            print("an unexpected integer was encountered at:" , i, "namely:",intcode[i])
            return 0

    return results


#handles opcode 1 and 2 for adding and multiplication
def calc(index, parameters, intcode, version):
    one = index + 1
    two = index + 2
    three = index + 3
    while len(parameters) < 3:
        parameters = "0" + parameters

    if parameters[2] == "0":
        one = intcode[index + 1]
    if parameters[1] == "0":
        two = intcode[index + 2]
    if parameters[0] == "0":
        three = intcode[index + 3]

    if version == "add":
        intcode[three] = intcode[one] + intcode[two]
    else:
        intcode[three] = intcode[one] * intcode[two]

    return index + 4


def jump(index, parameters, intcode, version):
    one = index + 1
    two = index + 2
    while len(parameters) < 2:
        parameters = "0" + parameters

    if parameters[1] == "0":
        one = intcode[index + 1]
    if parameters[0] == "0":
        two = intcode[index + 2]
    if version == "true":
        if intcode[one] != 0:
            return int(intcode[two])
    else:
        if intcode[one] == 0:
            return int(intcode[two])

    return index + 3


def equal(index, parameters, intcode, version):
    one = index + 1
    two = index + 2
    three = index + 3
    while len(parameters) < 3:
        parameters = "0" + parameters

    if parameters[2] == "0":
        one = intcode[index + 1]
    if parameters[1] == "0":
        two = intcode[index + 2]
    if parameters[0] == "0":
        three = intcode[index + 3]
    if version == "less":
        if intcode[one] < intcode[two]:
            intcode[three] = 1
        else:
            intcode[three] = 0
    else:
        if intcode[one] == intcode[two]:
            intcode[three] = 1
        else:
            intcode[three] = 0

    return index + 4


def day5(file, inputs):
    text_file = open(file, "r")
    initialMemory = [int(val) for val in text_file.read().split(",")]
    return IntcodeComputer(initialMemory, inputs)

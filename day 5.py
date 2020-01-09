def IntcodeComputer(intcode):
    i = 0
    while i < len(intcode) and intcode[i] != 99:
        opcode = int(str(intcode[i])[-2:])
        parameters = str(intcode[i])[:-2]
        if opcode == 1:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
            i = i + 4
        elif opcode == 2:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
            i = i + 4
        elif opcode == 3: #done
            intcode[intcode[i + 1]] = int(input())
            i = i + 2
        elif opcode == 4: #done
            if parameters == "0":
                print(intcode[intcode[i + 1]])
            else:
                print(intcode[i + 1])
            i = i + 2
        else:
            print("an unexpected integer was encountered at:" , i, "namely:",intcode[i])
            return 0

    return intcode

text_file = open("input5.txt", "r")
initialMemory = [int(val) for val in text_file.read().split(",")]
IntcodeComputer(initialMemory)
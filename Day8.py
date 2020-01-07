def decoder(layerData):
    lowest = 150
    for index, layer in enumerate(layerData):
        if layer.count("0") <= lowest:
            lowest = layer.count("0")
            found = index
    one = layerData[found].count("1")
    two = layerData[found].count("2")
    return one * two


def decoder2(layerData):
    result = ["2"] * 150
    for layer in layerData:
        for index, num in enumerate(layer):
            if result[index] == "2":
                result[index] = layer[index]
    return "".join(result)


data_file = open("input08.txt" , "r")
line = data_file.read()[:-1]
layerData = [line[i:i + 150] for i in range(0, len(line), 150)]
print(decoder(layerData))
final = (decoder2(layerData))
for i in range(6):
    print(final.replace("0", " ")[i * 25:(i + 1) * 25])

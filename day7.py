from day5 import day5
import itertools


def findbest(input):
    possibilities = list(itertools.permutations([0,1,2,3,4]))
    best = input
    for attempt in possibilities:
        last = 0
        for amp in attempt:
            last = day5("input07.txt", [amp, last])[0]
        if last > best:
            best = last
    return best


print(findbest(0))

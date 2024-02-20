# Advent of Code 2016
# Day 03: Squares With Three Sides
# https://adventofcode.com/2016/day/3

def isValidTriangle(sides):
    return sides[2] < sum(sides[0:2])

def a(data):
    counter = 0
    for line in data:
        fields = list(map(lambda x: int(x), line.split()))
        fields.sort()
        if isValidTriangle(fields):
            counter += 1
    return counter
                
def b(data):
    counter = 0
    for idx in range(0, len(data), 3):
        f1 = list(map(lambda x: int(x), data[idx].split()))
        f2 = list(map(lambda x: int(x), data[idx+1].split()))
        f3 = list(map(lambda x: int(x), data[idx+2].split()))
        t1 = [f1[0], f2[0], f3[0]]
        t2 = [f1[1], f2[1], f3[1]]
        t3 = [f1[2], f2[2], f3[2]]
        t1.sort()
        t2.sort()
        t3.sort()
        if isValidTriangle(t1):
            counter += 1
        if isValidTriangle(t2):
            counter += 1
        if isValidTriangle(t3):
            counter += 1
    return counter    

def test():
    print()
    print("Test 1:", "Passed" if isValidTriangle([5, 10, 25]) == False else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 03: Squares With Three Sides")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day03/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
# Advent of Code 2016
# Day 01: No Time for a Taxicab
# https://adventofcode.com/2016/day/1
    
def a(data):
    instructions = data[0].split(", ")
    x = y = 0
    theta = 90
    for i in instructions:
        theta += 90 if i[0] == "L" else -90
        theta %= 360
        steps = int(i[1:])
        match (theta):
            case 0: x += steps
            case 90: y += steps
            case 180: x -= steps
            case 270: y -= steps
    return abs(x) + abs(y)
                
def b(data):
    instructions = data[0].split(", ")
    x = y = 0
    theta = 90
    visited = set()
    visited.add((x,y))
    for i in instructions:
        theta += 90 if i[0] == "L" else -90
        theta %= 360
        steps = int(i[1:])
        while (steps > 0):
            match (theta):
                case 0: x += 1
                case 90: y += 1
                case 180: x -= 1
                case 270: y -= 1
            if (x,y) not in visited:
                visited.add((x,y))
            else:
                return abs(x) + abs(y)
            steps -= 1
    return

def test():
    print()
    print("Test 1:", "Passed" if a(["R2, L3"]) == 5 else "Failed")
    print("Test 2:", "Passed" if a(["R2, R2, R2"]) == 2 else "Failed")
    print("Test 3:", "Passed" if a(["R5, L5, R5, R3"]) == 12 else "Failed")
    print("Test 4:", "Passed" if b(["R8, R4, R4, R8"]) == 4 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 01: No Time for a Taxicab")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day01/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
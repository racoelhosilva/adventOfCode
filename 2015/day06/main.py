# Advent of Code 2015
# Day 06: Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

def turnOnA(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] = True
    return grid

def turnOffA(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] = False
    return grid

def toggleA(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] = not grid[y][x]
    return grid

def a(data):
    line = [False for _ in range(1000)]
    grid = [line.copy() for _ in range(1000)]
    for command in data:
        fields = command.split(" ")
        coords1 = fields[-3].split(",")
        coords2 = fields[-1].split(",")
        if (fields[0] == "toggle"):
            grid = toggleA(grid, coords1, coords2)
        elif (fields[1] == "on"):
            grid = turnOnA(grid, coords1, coords2)
        elif (fields[1] == "off"):
            grid = turnOffA(grid, coords1, coords2)
    total = 0
    for y in range(1000):
        for x in range(1000):
            if grid[y][x]:
                total+=1
    return total
    
def turnOnB(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] += 1
    return grid

def turnOffB(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] = max(0, grid[y][x]-1)
    return grid

def toggleB(grid, coords1, coords2):
    for y in range(int(coords1[1]), int(coords2[1])+1):
        for x in range(int(coords1[0]), int(coords2[0])+1):
            grid[y][x] += 2
    return grid
                
def b(data):    
    line = [0 for _ in range(1000)]
    grid = [line.copy() for _ in range(1000)]
    for command in data:
        fields = command.split(" ")
        coords1 = fields[-3].split(",")
        coords2 = fields[-1].split(",")
        if (fields[0] == "toggle"):
            grid = toggleB(grid, coords1, coords2)
        elif (fields[1] == "on"):
            grid = turnOnB(grid, coords1, coords2)
        elif (fields[1] == "off"):
            grid = turnOffB(grid, coords1, coords2)
    total = 0
    for y in range(1000):
        for x in range(1000):
            total += grid[y][x]
    return total

def test():
    print()
    print("Test 1:", "Passed" if a(["turn on 0,0 through 999,999"]) == 1000000 else "Failed")
    print("Test 2:", "Passed" if a(["toggle 0,0 through 999,0"]) == 1000 else "Failed")
    print("Test 3:", "Passed" if a(["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"]) == 999996 else "Failed")
    print("Test 4:", "Passed" if b(["turn on 0,0 through 0,0"]) == 1 else "Failed")
    print("Test 5:", "Passed" if b(["toggle 0,0 through 999,999"]) == 2000000 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 06: Probably a Fire Hazard")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day06/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
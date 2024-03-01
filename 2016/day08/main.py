# Advent of Code 2016
# Day 08: Two-Factor Authentication
# https://adventofcode.com/2016/day/8
    
def a(data):
    maxWidth, maxHeight = 50, 6
    display = [[0 for _ in range(maxWidth)] for _ in range(maxHeight)]
    for instruction in data:
        fields = instruction.split(" ")
        if (fields[0] == "rect"):
            width, height = fields[1].split("x")
            width = int(width)
            height = int(height)
            for y in range(height):
                for x in range(width):
                    display[y][x] = 1
        elif (fields[1] == "row"):
            row = int(fields[2].split("=")[1])
            shift = int(fields[-1])
            display[row] = display[row][maxWidth-shift:] + display[row][:maxWidth - shift]
        elif (fields[1] == "column"):
            col = int(fields[2].split("=")[1])
            shift = int(fields[-1])
            while (shift > 0):
                extra = display[5][col]
                display[5][col] = display[4][col]
                display[4][col] = display[3][col]
                display[3][col] = display[2][col]
                display[2][col] = display[1][col]
                display[1][col] = display[0][col]
                display[0][col] = extra
                shift -= 1
    return sum(list(map(lambda x: sum(x), display)))
                
def b(data): 
    maxWidth, maxHeight = 50, 6
    display = [[0 for _ in range(maxWidth)] for _ in range(maxHeight)]
    for instruction in data:
        fields = instruction.split(" ")
        if (fields[0] == "rect"):
            width, height = fields[1].split("x")
            width = int(width)
            height = int(height)
            for y in range(height):
                for x in range(width):
                    display[y][x] = 1
        elif (fields[1] == "row"):
            row = int(fields[2].split("=")[1])
            shift = int(fields[-1])
            display[row] = display[row][maxWidth-shift:] + display[row][:maxWidth - shift]
        elif (fields[1] == "column"):
            col = int(fields[2].split("=")[1])
            shift = int(fields[-1])
            while (shift > 0):
                extra = display[5][col]
                display[5][col] = display[4][col]
                display[4][col] = display[3][col]
                display[3][col] = display[2][col]
                display[2][col] = display[1][col]
                display[1][col] = display[0][col]
                display[0][col] = extra
                shift -= 1
    for y in display:
        for x in y:
            if (x == 1):
                print("#", end="")
            else:
                print(" ", end="")
        print()

def test():
    print()
    print("Test 1:", "Passed" if a(["rect 3x2"]) == 6 else "Failed")
    print("Test 2:", "Passed" if a(["rect 3x2", "rotate row y=0 by 1", "rect 1x1"]) == 7 else "Failed")
    print("Test 3:", "Passed" if a(["rect 3x2", "rotate column x=0 by 1", "rect 1x1"]) == 7 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 08: Two-Factor Authentication")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day08/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:")
    b(data)
# Advent of Code 2015
# Day 02: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2
    
def a(data):
    result = 0
    for dimensions in data:
        dimensions = dimensions.split("x")
        length, width, height = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
        lw = length * width
        wh = width * height
        hl = height * length
        result += 2 * lw + 2 * wh + 2 * hl + min(lw, min(wh, hl))
    return result
                
def b(data):    
    result = 0
    for dimensions in data:
        dimensions = dimensions.split("x")
        length, width, height = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
        lw = 2 * length + 2 * width
        wh = 2 * width + 2 * height
        hl = 2 * height + 2 * length
        result += length * width * height + min(lw, min(wh, hl))
    return result

def test():
    print()
    print("Test 1:", "Passed" if a(["2x2x2"]) == 28 else "Failed")
    print("Test 2:", "Passed" if a(["2x3x4"]) == 58 else "Failed")
    print("Test 3:", "Passed" if a(["1x1x10"]) == 43 else "Failed")
    print("Test 4:", "Passed" if a(["2x3x5", "3x5x7"]) == 225 else "Failed")
    print("Test 5:", "Passed" if b(["2x2x2"]) == 16 else "Failed")
    print("Test 6:", "Passed" if b(["2x3x4"]) == 34 else "Failed")
    print("Test 7:", "Passed" if b(["1x1x10"]) == 14 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 02: I Was Told There Would Be No Math")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day02/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
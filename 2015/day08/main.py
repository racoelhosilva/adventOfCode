# Advent of Code 2015
# Day 08: Matchsticks
# https://adventofcode.com/2015/day/8

import re

def a(data):
    text = total = 0
    for line in data:
        total += len(line)
        cleanLine = re.sub(r"\\x..", "+", line[1:-1].replace("\\\\", "_").replace("\\\"", "-"))
        text += len(cleanLine)
    return total - text
                
def b(data):
    total = text = 0
    for line in data:
        text += len(line)
        memLine = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
        total += len(memLine)
    return total - text

def test():
    print()
    print("Test 1:", "Passed" if a(["\"\""]) == 2 else "Failed")
    print("Test 2:", "Passed" if a(["\"abc\""]) == 2 else "Failed")
    print("Test 3:", "Passed" if a(["\"aaa\\\"aaa\""]) == 3 else "Failed")
    print("Test 4:", "Passed" if a(["\"\\x27\""]) == 5 else "Failed")
    print("Test 5:", "Passed" if a(["\"\"", "\"abc\"", "\"aaa\\\"aaa\"", "\"\\x27\""]) == 12 else "Failed")
    print("Test 6:", "Passed" if b(["\"\""]) == 4 else "Failed")
    print("Test 7:", "Passed" if b(["\"abc\""]) == 4 else "Failed")
    print("Test 8:", "Passed" if b(["\"aaa\\\"aaa\""]) == 6 else "Failed")
    print("Test 9:", "Passed" if b(["\"\\x27\""]) == 5 else "Failed")
    print("Test 10:", "Passed" if b(["\"\"", "\"abc\"", "\"aaa\\\"aaa\"", "\"\\x27\""]) == 19 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 08: Matchsticks")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day08/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
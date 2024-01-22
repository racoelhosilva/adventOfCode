# Advent of Code 2015
# Day 01: Not Quite Lisp
# https://adventofcode.com/2015/day/1
  
def a(data):
    result = 0
    for c in data[0]:
        if c == '(':
            result += 1
        elif c == ')':
            result -= 1
    return result
                
def b(data):    
    floor = 0
    for i, c in enumerate(data[0]):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0:
            return i+1
    return 0

def test():
    print()
    print("Test 1:", "Passed" if a(["((("]) == 3 else "Failed")
    print("Test 2:", "Passed" if a([")))"]) == -3 else "Failed")
    print("Test 3:", "Passed" if a(["()()()"]) == 0 else "Failed")
    print("Test 4:", "Passed" if b([")))"]) == 1 else "Failed")
    print("Test 5:", "Passed" if b(["(()))"]) == 5 else "Failed")
    print()
    
if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 01: Not Quite Lisp")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day01/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
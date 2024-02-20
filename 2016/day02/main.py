# Advent of Code 2016
# Day 02: Bathroom Security
# https://adventofcode.com/2016/day/2
    
def a(data):
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    x = y = 1
    solution = 0
    for line in data:
        solution *= 10
        for instruction in line:
            match instruction:
                case "U": y = max(0, y - 1) 
                case "D": y = min(2, y + 1)
                case "L": x = max(0, x - 1)
                case "R": x = min(2, x + 1)
        solution += keypad[y][x]
    return solution
                
def b(data):    
    keypad = [[0,0,1,0,0],
              [0,2,3,4,0],
              [5,6,7,8,9],
              [0,"A","B","C",0],
              [0,0,"D",0,0]]
    x,y = 0,2
    solution = ""
    for line in data:
        for instruction in line:
            nx,ny = x,y
            match instruction:
                case "U": ny = max(0, ny - 1) 
                case "D": ny = min(4, ny + 1)
                case "L": nx = max(0, nx - 1)
                case "R": nx = min(4, nx + 1)
            if (keypad[ny][nx] != 0):
                x,y = nx,ny
        solution += str(keypad[y][x])
    return solution

def test():
    print()
    print("Test 1:", "Passed" if a(["ULL", "RRDDD", "LURDL", "UUUUD"]) == 1985 else "Failed")
    print("Test 2:", "Passed" if b(["ULL", "RRDDD", "LURDL", "UUUUD"]) == "5DB3" else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 02: Bathroom Security")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day02/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
# Advent of Code 2015
# Day 03: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3
    
def a(data):
    x,y = 0,0
    visited = set()
    visited.add((x,y))
    for c in data[0]:
        match c:
            case '^': y+=1
            case 'v': y-=1
            case '>': x+=1
            case '<': x-=1
        visited.add((x,y))
    return len(visited)
                
def b(data):    
    sx,sy = 0,0
    rx,ry = 0,0
    visited = set()
    visited.add((sx,sy))
    for i,c in enumerate(data[0]):
        if i % 2 == 0:
            match c:
                case '^': sy+=1
                case 'v': sy-=1
                case '>': sx+=1
                case '<': sx-=1
            visited.add((sx,sy))
        else:
            match c:
                case '^': ry+=1
                case 'v': ry-=1
                case '>': rx+=1
                case '<': rx-=1
            visited.add((rx,ry))
    return len(visited)

def test():
    print()
    print("Test 1:", "Passed" if a([""]) == 1 else "Failed")
    print("Test 2:", "Passed" if a([">"]) == 2 else "Failed")
    print("Test 3:", "Passed" if a(["><"]) == 2 else "Failed")
    print("Test 4:", "Passed" if a(["^>v<"]) == 4 else "Failed")
    print("Test 5:", "Passed" if a(["^v^v^v^v^v"]) == 2 else "Failed")
    print("Test 6:", "Passed" if b(["><"]) == 3 else "Failed")
    print("Test 7:", "Passed" if b(["^>v<"]) == 3 else "Failed")
    print("Test 8:", "Passed" if b(["^v^v^v^v^v"]) == 11 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 03: Perfectly Spherical Houses in a Vacuum")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day03/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
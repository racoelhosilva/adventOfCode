# Advent of Code 2015
# Day 25: Let It Snow
# https://adventofcode.com/2015/day/25
    
def a(data):
    fields = "".join(data[0][:-1].split(",")).split(" ")
    row, col = int(fields[-3]), int(fields[-1])
    value = 1 + sum([x for x in range(1, row)])
    f = value + sum([row + idx for idx in range(1, col)])
    
    val = 20151125
    for _ in range(1,f):
        val *= 252533
        val %= 33554393

    return val
                
def b(data):    
    return

def test():
    print()
    print("Test 1:", "Passed" if a(["To continue, please consult the code grid in the manual.  Enter the code at row 1, column 1."]) == 20151125 else "Failed")
    print("Test 2:", "Passed" if a(["To continue, please consult the code grid in the manual.  Enter the code at row 2, column 1."]) == 31916031 else "Failed")
    print("Test 3:", "Passed" if a(["To continue, please consult the code grid in the manual.  Enter the code at row 3, column 2."]) == 8057251 else "Failed")
    print("Test 4:", "Passed" if a(["To continue, please consult the code grid in the manual.  Enter the code at row 6, column 6."]) == 27995004 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 25: Let It Snow")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day25/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
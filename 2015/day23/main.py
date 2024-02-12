# Advent of Code 2015
# Day 23: Opening the Turing Lock
# https://adventofcode.com/2015/day/23
    
def a(data):
    a = b = 0
    i = 0
    while (i < len(data)):
        fields = "".join(data[i].split(",")).split(" ")
        match (fields[0]):
            case "hlf":
                if fields[1] == "a":
                    a = a/2
                else:
                    b = b/2
                i += 1
            case "tpl":
                if fields[1] == "a":
                    a = 3 * a
                else:
                    b = 3 * b
                i += 1
            case "inc":
                if fields[1] == "a":
                    a = a + 1
                else:
                    b = b + 1
                i += 1
            case "jmp":
                i += int(fields[1])
            case "jie":
                if fields[1] == "a":
                    condition = a % 2 == 0
                else:
                    condition = b % 2 == 0
                if condition:
                    i += int(fields[2])
                else:
                    i += 1
            case "jio":
                if fields[1] == "a":
                    condition = a == 1
                else:
                    condition = b == 1
                if condition:
                    i += int(fields[2])
                else:
                    i += 1
    return b
                
def b(data):
    a = 1
    b = 0
    i = 0
    while (i < len(data)):
        fields = "".join(data[i].split(",")).split(" ")
        match (fields[0]):
            case "hlf":
                if fields[1] == "a":
                    a = a/2
                else:
                    b = b/2
                i += 1
            case "tpl":
                if fields[1] == "a":
                    a = 3 * a
                else:
                    b = 3 * b
                i += 1
            case "inc":
                if fields[1] == "a":
                    a = a + 1
                else:
                    b = b + 1
                i += 1
            case "jmp":
                i += int(fields[1])
            case "jie":
                if fields[1] == "a":
                    condition = a % 2 == 0
                else:
                    condition = b % 2 == 0
                if condition:
                    i += int(fields[2])
                else:
                    i += 1
            case "jio":
                if fields[1] == "a":
                    condition = a == 1
                else:
                    condition = b == 1
                if condition:
                    i += int(fields[2])
                else:
                    i += 1
    return b

def test():
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 23: Opening the Turing Lock")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day23/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
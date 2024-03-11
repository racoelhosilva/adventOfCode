# Advent of Code 2016
# Day 09: Explosives in Cyberspace
# https://adventofcode.com/2016/day/9
    
def a(data):
    data = data[0]
    idx = 0
    while (idx < len(data)):
        if (data[idx] == "("):
            second_idx = idx
            while (data[second_idx] != ")"):
                second_idx += 1
                transform = data[idx:second_idx+1]
            first, second = transform[1:-1].split("x")
            first, second = int(first), int(second)

            data = data[:idx] + data[second_idx+1:min(second_idx+first+1, len(data))] * second + data[second_idx + first + 1:]
            idx = idx + first * second
        else:
            idx += 1
    return len(data)

def decompress(s):
    if "(" not in s:
        return len(s)
    ret = 0
    while "(" in s:
        idx = s.find("(")
        ret += idx
        s = s[idx:]
        idx = s.find(")")
        n1, n2 = s[1:idx].split("x")
        s = s[idx+1:]
        ret += decompress(s[:int(n1)]) * int(n2)
        s = s[int(n1):]
    ret += len(s)
    return ret

def b(data):    
    data = data[0]
    return decompress(data)

def test():
    print()
    print("Test 1:", "Passed" if a(["ADVENT"]) == 6 else "Failed")
    print("Test 2:", "Passed" if a(["A(1x5)BC"]) == 7 else "Failed")
    print("Test 3:", "Passed" if a(["(3x3)XYZ"]) == 9 else "Failed")
    print("Test 4:", "Passed" if a(["A(2x2)BCD(2x2)EFG"]) == 11 else "Failed")
    print("Test 5:", "Passed" if a(["(6x1)(1x3)A"]) == 6 else "Failed")
    print("Test 6:", "Passed" if a(["X(8x2)(3x3)ABCY"]) == 18 else "Failed")
    print("Test 7:", "Passed" if b(["(3x3)XYZ"]) == 9 else "Failed")
    print("Test 8:", "Passed" if b(["X(8x2)(3x3)ABCY"]) == 20 else "Failed")
    print("Test 9:", "Passed" if b(["(27x12)(20x12)(13x14)(7x10)(1x12)A"]) == 241920 else "Failed")
    print("Test 10:", "Passed" if b(["(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]) == 445 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 09: Explosives in Cyberspace")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day09/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
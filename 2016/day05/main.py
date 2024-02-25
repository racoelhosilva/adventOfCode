# Advent of Code 2016
# Day 05: How About a Nice Game of Chess?
# https://adventofcode.com/2016/day/5

import hashlib

def a(data, n):
    password = ""
    index = 0
    while (len(password) < n):
        string = data[0] + str(index)
        h = str(hashlib.md5(string.encode()).hexdigest())
        if h[0:5] == "00000":
            password += h[5]
        index += 1
    return password
                
def b(data, n):    
    password = ["" for _ in range(n)]
    index = 0
    counter = 0
    while (counter < n):
        string = data[0] + str(index)
        h = str(hashlib.md5(string.encode()).hexdigest())
        if h[0:5] == "00000":
            if h[5] in list(map(lambda x: str(x), range(n))):
                if password[int(h[5])] == "":
                    password[int(h[5])] = h[6]
                    counter += 1
        index += 1
    return "".join(password)

def test():
    print()
    print("Test 1:", "Passed" if a(["abc"], 1) == "1" else "Failed")
    print("Test 2:", "Passed" if a(["abc"], 8) == "18f47a30" else "Failed")
    print("Test 3:", "Passed" if b(["abc"], 8) == "05ace8e3" else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 05: How About a Nice Game of Chess?")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day05/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data, 8))
    print("Part b:", b(data, 8))
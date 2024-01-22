# Advent of Code 2015
# Day 04: The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4

import hashlib

def a(data):
    result = 0
    while hashlib.md5((data[0] + str(result)).encode()).hexdigest()[0:5] != "00000":
        result += 1
    return result
                
def b(data):
    result = 0
    while hashlib.md5((data[0] + str(result)).encode()).hexdigest()[0:6] != "000000":
        result += 1
    return result

def test():
    print()
    print("Test 1:", "Passed" if a(["abcdef"]) == 609043 else "Failed")
    print("Test 2:", "Passed" if a(["pqrstuv"]) == 1048970 else "Failed")
    print("Test 3:", "Passed" if b(["abcdef"]) == 6742839 else "Failed")
    print("Test 4:", "Passed" if b(["pqrstuv"]) == 5714438 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 04: The Ideal Stocking Stuffer")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day04/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
# Advent of Code 2016
# Day 07: Internet Protocol Version 7
# https://adventofcode.com/2016/day/7

import re

def hasABBA(string):
    for i in range(len(string) - 3):
        s = string[i:i+4]
        if (s[0] == s[-1] and s[1] == s[2] and s[0] != s[1]):
            return True
    return False

def a(data):
    counter = 0
    for line in data:
        splits = re.split(r'\[([^\]]+)\]', line)
        bracket = False
        normal = False
        for idx, s in enumerate(splits):
            if idx % 2 == 0 and hasABBA(s):
                normal = True
            if idx % 2 == 1 and hasABBA(s):
                bracket = True
                break
        if normal and not bracket:
            counter += 1
    return counter
                
def extractTriplets(strings):
    result = []
    for string in strings:
        for i in range(len(string) - 2):
            s = string[i:i+3]
            if (s[0] == s[-1] and s[0] != s[1]):
                result += [s]
    return result

def b(data):
    counter = 0
    for line in data:
        splits = re.split(r'\[([^\]]+)\]', line)
        normal = extractTriplets([split for idx, split in enumerate(splits) if idx % 2 == 0])
        bracket = extractTriplets([split for idx, split in enumerate(splits) if idx % 2 == 1])
        for t in normal:
            op = t[1] + t[0] + t[1]
            found = False
            for b in bracket:
                if b == op:
                    counter += 1
                    found = True
                    break
            if (found):
                break
    return counter

def test():
    print()
    print("Test 1:", "Passed" if a(["abba[mnop]qrst"]) == 1 else "Failed")
    print("Test 2:", "Passed" if a(["abcd[bddb]xyyx"]) == 0 else "Failed")
    print("Test 3:", "Passed" if a(["aaaa[qwer]tyui"]) == 0 else "Failed")
    print("Test 4:", "Passed" if a(["ioxxoj[asdfgh]zxcvbn"]) == 1 else "Failed")
    print("Test 5:", "Passed" if b(["aba[bab]xyz"]) == 1 else "Failed")
    print("Test 6:", "Passed" if b(["xyx[xyx]xyx"]) == 0 else "Failed")
    print("Test 7:", "Passed" if b(["aaa[kek]eke"]) == 1 else "Failed")
    print("Test 8:", "Passed" if b(["zazbz[bzb]cdb"]) == 1 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 07: Internet Protocol Version 7")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day07/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
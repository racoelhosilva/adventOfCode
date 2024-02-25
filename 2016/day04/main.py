# Advent of Code 2016
# Day 04: Security Through Obscurity
# https://adventofcode.com/2016/day/4
    
import re, collections

def a(data):
    total = 0
    for line in data:
        name, number, checksum = re.match(r"([\D]+)([\d]+?)\[(\w+)\]", line).groups()
        name = name.replace("-","")
        number = int(number)
        frequencies = collections.Counter(name)
        top5Freq = list(frequencies.values())
        top5Freq.sort(reverse=True)
        top5Freq = top5Freq[4] 
        valid = True
        for c in checksum:
            if frequencies[c] < top5Freq:
                valid = False
                break
        if valid:
            total += number
    return total
                
def b(data):    
    for line in data:
        name, number, checksum = re.match(r"([\D]+)([\d]+?)\[(\w+)\]", line).groups()
        name = name.replace("-","")
        number = int(number)
        frequencies = collections.Counter(name)
        top5Freq = list(frequencies.values())
        top5Freq.sort(reverse=True)
        top5Freq = top5Freq[4] 
        valid = True
        for c in checksum:
            if frequencies[c] < top5Freq:
                valid = False
                break
        if valid:
            new_string = ""
            for c in name:
                new_string += chr(((ord(c) - ord('a')) + number) % 26 + ord('a'))
            if "north" in new_string:
                return number
    return -1
        

def test():
    print()
    print("Test 1:", "Passed" if a(["aaaaa-bbb-z-y-x-123[abxyz]"]) == 123 else "Failed")
    print("Test 2:", "Passed" if a(["a-b-c-d-e-f-g-h-987[abcde]"]) == 987 else "Failed")
    print("Test 3:", "Passed" if a(["not-a-real-room-404[oarel]"]) == 404 else "Failed")
    print("Test 4:", "Passed" if a(["totally-real-room-200[decoy]"]) == 0 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 04: Security Through Obscurity")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day04/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
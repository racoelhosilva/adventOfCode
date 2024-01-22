# Advent of Code 2015
# Day 05: Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

def vowelCount(string):
    counter = 0
    for c in string:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            counter += 1
    return counter 

def doubleLetter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def hasInvalidPair(string):
    return len(string.split("ab")) > 1 or len(string.split("cd")) > 1 or len(string.split("pq")) > 1 or len(string.split("xy")) > 1

def a(data):
    result = 0
    for string in data:
        if not hasInvalidPair(string) and doubleLetter(string) and vowelCount(string) >= 3:
            result += 1
    return result

def repeatedPair(string):
    for i in range(len(string)-3):
        for j in range(i+2, len(string)-1):
            if string[i:i+2] == string[j:j+2]:
                return True
    return False

def spacedRepeat(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def b(data):    
    result = 0
    for string in data:
        if repeatedPair(string) and spacedRepeat(string):
            result += 1
    return result

def test():
    print()
    print("Test 1:", "Passed" if vowelCount("ugknbfddgicrmopn") == 3 else "Failed")
    print("Test 2:", "Passed" if doubleLetter("ugknbfddgicrmopn") == True else "Failed")
    print("Test 3:", "Passed" if hasInvalidPair("ugknbfddgicrmopn") == False else "Failed")
    print("Test 4:", "Passed" if a(["ugknbfddgicrmopn"]) == 1 else "Failed")
    print("Test 5:", "Passed" if a(["aaa"]) == 1 else "Failed")
    print("Test 6:", "Passed" if doubleLetter("jchzalrnumimnmhp") == False else "Failed")
    print("Test 7:", "Passed" if hasInvalidPair("haegwjzuvuyypxyu") == True else "Failed")
    print("Test 8:", "Passed" if vowelCount("dvszwmarrgswjxmb") == 1 else "Failed")
    print("Test 9:", "Passed" if a(["jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]) == 0 else "Failed")
    
    print("Test 10:", "Passed" if repeatedPair("qjhvhtzxzqqjkmpb") == True else "Failed")
    print("Test 11:", "Passed" if spacedRepeat("qjhvhtzxzqqjkmpb") == True else "Failed")
    print("Test 12:", "Passed" if b(["qjhvhtzxzqqjkmpb"]) == 1 else "Failed")
    print("Test 13:", "Passed" if b(["xxyxx"]) == 1 else "Failed")
    print("Test 14:", "Passed" if spacedRepeat("uurcxstgmygtbstg") == False else "Failed")
    print("Test 15:", "Passed" if repeatedPair("ieodomkazucvgmuy") == False else "Failed")
    print("Test 16:", "Passed" if b(["uurcxstgmygtbstg", "ieodomkazucvgmuy"]) == 0 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 05: Doesn't He Have Intern-Elves For This?")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day05/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
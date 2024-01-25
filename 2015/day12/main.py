# Advent of Code 2015
# Day 12: JSAbacusFramework.io
# https://adventofcode.com/2015/day/12
    
import re, json

def a(data):
    numbers = list(map(lambda x: int(x), re.findall(r"([-]*[0-9]+)", data[0])))
    return sum(numbers)

def helper(jsonData):
    if type(jsonData) == int:
        return jsonData
    if type(jsonData) == list:
        return sum([helper(jData) for jData in jsonData])
    if type(jsonData) != dict:
        return 0
    if 'red' in jsonData.values():
        return 0
    return helper(list(jsonData.values()))
     
def b(data):    
    return helper(json.loads(data[0]))

def test():
    print()
    print("Test 1:", "Passed" if a(["[1,2,3]"]) == 6 else "Failed")
    print("Test 2:", "Passed" if a(['{"a":2,"b":4}']) == 6 else "Failed")
    print("Test 3:", "Passed" if a(["[[[3]]]"]) == 3 else "Failed")
    print("Test 4:", "Passed" if a(['{"a":{"b":4},"c":-1}']) == 3 else "Failed")
    print("Test 5:", "Passed" if a(['{"a":[-1,1]}']) == 0 else "Failed")
    print("Test 6:", "Passed" if a(['[-1,{"a":1}]']) == 0 else "Failed")
    print("Test 7:", "Passed" if a(['[]']) == 0 else "Failed")
    print("Test 8:", "Passed" if a(['{}']) == 0 else "Failed")
    print("Test 9:", "Passed" if b(["[1,2,3]"]) == 6 else "Failed")
    print("Test 10:", "Passed" if b(['[1,{"c":"red","b":2},3]']) == 4 else "Failed")
    print("Test 11:", "Passed" if b(['{"d":"red","e":[1,2,3,4],"f":5}']) == 0 else "Failed")
    print("Test 12:", "Passed" if b(['[1,"red",5]']) == 6 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 12: JSAbacusFramework.io")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day12/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
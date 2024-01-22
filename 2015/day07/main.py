# Advent of Code 2015
# Day 07: Some Assembly Required
# https://adventofcode.com/2015/day/7
    
def transformData(data):
    for idx, line in enumerate(data):
        data[idx] = line.split(" -> ")
    return data
    
def a(data):
    helper = dict()
    while not ("a" in helper.keys()):
        for connection in data:
            if connection[1] in helper.keys():
                continue
            if (connection[0].isnumeric()):
                helper[connection[1]] = int(connection[0])
            else:
                operation = connection[0].split(" ")
                if len(operation) == 1:
                    if operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]]
                elif len(operation) == 2:
                    if operation[0] == "NOT" and operation[1] in helper.keys():
                        helper[connection[1]] = 2**16 - helper[operation[1]] - 1
                elif len(operation) == 3:
                    if operation[1] == "AND" and (operation[0] in helper.keys() or operation[0].isnumeric()) and (operation[2] in helper.keys() or operation[2].isnumeric()):
                        operator1 = int(operation[0]) if operation[0].isnumeric() else helper[operation[0]]
                        operator2 = int(operation[2]) if operation[2].isnumeric() else helper[operation[2]]
                        helper[connection[1]] = operator1 & operator2
                    elif operation[1] == "OR" and operation[0] in helper.keys() and operation[2] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] | helper[operation[2]]
                    elif operation[1] == "LSHIFT" and operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] << int(operation[2])
                    elif operation[1] == "RSHIFT" and operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] >> int(operation[2])
    return helper["a"]
                
def b(data):    
    helper = dict()
    helper["b"] = a(data)
    while not ("a" in helper.keys()):
        for connection in data:
            if connection[1] in helper.keys():
                continue
            if (connection[0].isnumeric()):
                helper[connection[1]] = int(connection[0])
            else:
                operation = connection[0].split(" ")
                if len(operation) == 1:
                    if operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]]
                elif len(operation) == 2:
                    if operation[0] == "NOT" and operation[1] in helper.keys():
                        helper[connection[1]] = 2**16 - helper[operation[1]] - 1
                elif len(operation) == 3:
                    if operation[1] == "AND" and (operation[0] in helper.keys() or operation[0].isnumeric()) and (operation[2] in helper.keys() or operation[2].isnumeric()):
                        operator1 = int(operation[0]) if operation[0].isnumeric() else helper[operation[0]]
                        operator2 = int(operation[2]) if operation[2].isnumeric() else helper[operation[2]]
                        helper[connection[1]] = operator1 & operator2
                    elif operation[1] == "OR" and operation[0] in helper.keys() and operation[2] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] | helper[operation[2]]
                    elif operation[1] == "LSHIFT" and operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] << int(operation[2])
                    elif operation[1] == "RSHIFT" and operation[0] in helper.keys():
                        helper[connection[1]] = helper[operation[0]] >> int(operation[2])
    return helper["a"]

def test():
    print()
    print("Test 1:", "Passed" if a(transformData(["NOT b -> a","0 -> b"])) == 2**16-1 else "Failed")
    print("Test 2:", "Passed" if a(transformData(["b AND c -> a","1 -> b","5 -> c"])) == 1 else "Failed")
    print("Test 3:", "Passed" if a(transformData(["b OR c -> a","1 -> b","5 -> c"])) == 5 else "Failed")
    print("Test 4:", "Passed" if a(transformData(["b LSHIFT 2 -> a","1 -> b"])) == 4 else "Failed")
    print("Test 5:", "Passed" if a(transformData(["b RSHIFT 2 -> a","5 -> b"])) == 1 else "Failed")
    print("Test 7:", "Passed" if a(transformData(["123 -> x","456 -> y","x AND y -> d","x OR y -> e","x LSHIFT 2 -> f","y RSHIFT 2 -> g","NOT x -> h","NOT y -> a"])) == 65079 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 07: Some Assembly Required")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day07/input.txt", "r").read().splitlines()
    data = transformData(data)
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
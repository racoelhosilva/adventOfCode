# Advent of Code 2016
# Day 06: Signals and Noise
# https://adventofcode.com/2016/day/6
    
import collections

def a(data):
    result = ""
    for idx in range(len(data[0])):
        frequencies = collections.Counter([word[idx] for word in data])
        result += frequencies.most_common(1)[0][0]
    return result
                
def b(data):    
    result = ""
    for idx in range(len(data[0])):
        frequencies = collections.Counter([word[idx] for word in data])
        result += frequencies.most_common()[-1][0]
    return result

def test():
    print()
    example = ["eedadn","drvtee","eandsr","raavrd","atevrs","tsrnev","sdttsa","rasrtv","nssdts","ntnada","svetve","tesnvt","vntsnd","vrdear","dvrsen","enarar"]
    print("Test 1:", "Passed" if a(example) == "easter" else "Failed")
    print("Test 2:", "Passed" if b(example) == "advent" else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2016\nDay 06: Signals and Noise")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2016/day06/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
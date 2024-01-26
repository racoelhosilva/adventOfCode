# Advent of Code 2015
# Day 16: Aunt Sue
# https://adventofcode.com/2015/day/16
    
def a(data):
    info = dict()
    results = {"children": 3, "cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
    for line in data:
        auntInfo = dict()
        fields = line.split(" ")
        auntInfo[fields[2][:-1]] = int(fields[3][:-1])
        auntInfo[fields[4][:-1]] = int(fields[5][:-1])
        auntInfo[fields[6][:-1]] = int(fields[7])
        info[int(fields[1][:-1])] = auntInfo
        
    for aunt in range(1,501):
        for field, value in info[aunt].items():
            if results[field] != value:
                info.pop(aunt)
                break
    return list(info.keys())[0]
                
def b(data):    
    info = dict()
    results = {"children": 3, "cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
    for line in data:
        auntInfo = dict()
        fields = line.split(" ")
        auntInfo[fields[2][:-1]] = int(fields[3][:-1])
        auntInfo[fields[4][:-1]] = int(fields[5][:-1])
        auntInfo[fields[6][:-1]] = int(fields[7])
        info[int(fields[1][:-1])] = auntInfo
        
    for aunt in range(1,501):
        for field, value in info[aunt].items():
            if field in ["cats", "trees"]:
                if value <= results[field]:
                    info.pop(aunt)
                    break
            elif field in ["pomeranians", "goldfish"]:
                if value >= results[field]:
                    info.pop(aunt)
                    break
            elif results[field] != value:
                info.pop(aunt)
                break
    
    return list(info.keys())[0]

def test():
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 16: Aunt Sue")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day16/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
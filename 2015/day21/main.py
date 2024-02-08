# Advent of Code 2015
# Day 21: RPG Simulator 20XX
# https://adventofcode.com/2015/day/21
    
import itertools

def play(boss, player):
    pDamage = max(1, player[1] - boss[2])
    bDamage = max(1, boss[1] - player[2])
    while(boss[0] > 0 and player[0] > 0):
        boss[0] -= pDamage
        player[0] -= bDamage

    return boss[0] <= 0

def a(data):
    boss = []
    for line in data:
        boss.append(int(line.split(" ")[-1]))

    weapons = [[8,4,0],[10,5,0], [25,6,0], [40,7,0],[74,8,0]]
    armor = [[0,0,0],[13,0,1],[31,0,2], [53,0,3], [75,0,4],[102,0,5]]
    rings = [[0,0,0],[20,0,1],[25,1,0],[40,0,2],[50,2,0],[80,0,3],[100,3,0]]
    ringCombinations = [[[0,0,0],[0,0,0]]] + (list(itertools.combinations(rings, 2)))
    minCost = float("inf")
    for w in weapons:
        for a in armor:
            for r in ringCombinations:
                player = [100,0,0]
                player[1] += w[1] + r[0][1] + r[1][1]
                player[2] += a[2] + r[0][2] + r[1][2]
                if (play(boss.copy(), player)):
                    cost = w[0] + a[0] + r[0][0] + r[1][0]
                    minCost = min(cost, minCost)
                    
    return minCost
                
def b(data):
    boss = []
    for line in data:
        boss.append(int(line.split(" ")[-1]))

    weapons = [[8,4,0],[10,5,0], [25,6,0], [40,7,0],[74,8,0]]
    armor = [[0,0,0],[13,0,1],[31,0,2], [53,0,3], [75,0,4],[102,0,5]]
    rings = [[0,0,0],[20,0,1],[25,1,0],[40,0,2],[50,2,0],[80,0,3],[100,3,0]]
    ringCombinations = [[[0,0,0],[0,0,0]]] + (list(itertools.combinations(rings, 2)))
    maxCost = 0
    for w in weapons:
        for a in armor:
            for r in ringCombinations:
                player = [100,0,0]
                player[1] += w[1] + r[0][1] + r[1][1]
                player[2] += a[2] + r[0][2] + r[1][2]
                if (not play(boss.copy(), player)):
                    cost = w[0] + a[0] + r[0][0] + r[1][0]
                    maxCost = max(cost, maxCost)
                    
    return maxCost

def test():
    print()
    print("Test 1:", "Passed" if play([12,7,2], [8,5,5]) == True else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 21: RPG Simulator 20XX")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day21/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
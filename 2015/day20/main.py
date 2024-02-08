# Advent of Code 2015
# Day 20: Infinite Elves and Infinite Houses
# https://adventofcode.com/2015/day/20

import math

def a(data):
    total = 0
    num = 0
    while total < int(data[0]):
        num += 1
        small_divisors = [n for n in range(1,int(math.sqrt(num)) + 1) if num % n == 0]
        large_divisors = [num / d for d in small_divisors if num != d * d]
        total = (sum(small_divisors) + sum(large_divisors)) * 10
    return num

def a2(data):
    target = int(data[0]) // 10
    houses = [0 for _ in range(1,target+1)]
    for i in range(1,target):
        for j in range(i, target, i):
            houses[j] += i
        if houses[i] >= target:
            return i
                
def b(data):    
    total = 0
    num = 0
    while total < int(data[0]):
        num += 1
        small_divisors = [n for n in range(1,int(math.sqrt(num)) + 1) if num % n == 0]
        large_divisors = [num / d for d in small_divisors if num != d * d]
        total = (sum(d for d in small_divisors if num / d <= 50) + sum(d for d in large_divisors if num / d <= 50)) * 11
    return num

def b2(data):
    target = int(data[0]) // 11
    houses = [0 for _ in range(1,target+1)]
    for i in range(1,target):
        for c in range(1,51):
            idx = i * c
            if idx < target:
                houses[idx] += i
        if houses[i] >= target:
            return i

def test():
    print()
    print("Test 1:", "Passed" if a(["140"]) == 8 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 20: Infinite Elves and Infinite Houses")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day20/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a2(data))
    print("Part b:", b2(data))
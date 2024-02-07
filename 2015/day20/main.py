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
                
def b(data):    
    total = 0
    num = 0
    while total < int(data[0]):
        num += 1
        small_divisors = [n for n in range(1,int(math.sqrt(num)) + 1) if num % n == 0]
        large_divisors = [num / d for d in small_divisors if num != d * d]
        total = (sum(d for d in small_divisors if num / d <= 50) + sum(d for d in large_divisors if num / d <= 50)) * 11
    return num

def test():
    print()
    print("Test 1:", "Passed" if a(["140"]) == 8 else "Failed")
    print("Test 2:", "Passed" if b(["140"]) == None else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 20: Infinite Elves and Infinite Houses")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day20/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(data))
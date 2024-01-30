# Advent of Code 2015
# Day 18: Like a GIF For Your Yard
# https://adventofcode.com/2015/day/18
    
def a(data, iterations):
    grid = []
    for r in range(len(data)):
        row = []
        for c in range(len(data[0])):
            row.append(1 if data[r][c] == "#" else 0)
        grid.append(row)
    
    for i in range(iterations):
        new_grid = []
        for r in range(len(grid)):
            new_row = []
            for c in range(len(grid[r])):
                neighbors = []
                if r != 0:
                    neighbors.append(grid[r-1][c])
                    if c != 0:
                        neighbors.append(grid[r-1][c-1])
                    if c != len(grid[r]) - 1:
                        neighbors.append(grid[r-1][c+1])
                if r != len(grid) - 1:
                    neighbors.append(grid[r+1][c])
                    if c != 0:
                        neighbors.append(grid[r+1][c-1])
                    if c != len(grid[r]) - 1:
                        neighbors.append(grid[r+1][c+1])
                if c != 0:
                        neighbors.append(grid[r][c-1])
                if c != len(grid[r]) - 1:
                        neighbors.append(grid[r][c+1])
                
                if (grid[r][c] == 1):
                    if (sum(neighbors) == 2 or sum(neighbors) == 3):
                        new_row.append(1)
                    else:
                        new_row.append(0)
                    
                elif (grid[r][c] == 0):
                    if (sum(neighbors) == 3):
                        new_row.append(1)
                    else:
                        new_row.append(0)    
            
            new_grid.append(new_row)
            
        grid = new_grid
        
    return sum([sum(x) for x in grid])
                
def b(data, iterations):
    grid = []
    for r in range(len(data)):
        row = []
        for c in range(len(data[0])):
            row.append(1 if data[r][c] == "#" else 0)
        grid.append(row)
    
    grid[0][0] = 1
    grid[0][len(grid[0])-1] = 1    
    grid[len(grid)-1][0] = 1    
    grid[len(grid)-1][len(grid[0])-1] = 1 
    
    for i in range(iterations):
        new_grid = []
        for r in range(len(grid)):
            new_row = []
            for c in range(len(grid[r])):
                neighbors = []
                if r != 0:
                    neighbors.append(grid[r-1][c])
                    if c != 0:
                        neighbors.append(grid[r-1][c-1])
                    if c != len(grid[r]) - 1:
                        neighbors.append(grid[r-1][c+1])
                if r != len(grid) - 1:
                    neighbors.append(grid[r+1][c])
                    if c != 0:
                        neighbors.append(grid[r+1][c-1])
                    if c != len(grid[r]) - 1:
                        neighbors.append(grid[r+1][c+1])
                if c != 0:
                        neighbors.append(grid[r][c-1])
                if c != len(grid[r]) - 1:
                        neighbors.append(grid[r][c+1])
                
                if (grid[r][c] == 1):
                    if (sum(neighbors) == 2 or sum(neighbors) == 3):
                        new_row.append(1)
                    else:
                        new_row.append(0)
                    
                elif (grid[r][c] == 0):
                    if (sum(neighbors) == 3):
                        new_row.append(1)
                    else:
                        new_row.append(0)    
            
            new_grid.append(new_row)
        new_grid[0][0] = 1
        new_grid[0][len(new_grid[0])-1] = 1    
        new_grid[len(new_grid)-1][0] = 1    
        new_grid[len(new_grid)-1][len(new_grid[0])-1] = 1 
        grid = new_grid
        
    return sum([sum(x) for x in grid])

def test():
    print()
    example = [".#.#.#","...##.","#....#","..#...","#.#..#","####.."]
    print("Test 1:", "Passed" if a(example,0) == 15 else "Failed")
    print("Test 2:", "Passed" if a(example,1) == 11 else "Failed")
    print("Test 3:", "Passed" if a(example,2) == 8 else "Failed")
    print("Test 4:", "Passed" if a(example,3) == 4 else "Failed")
    print("Test 5:", "Passed" if a(example,4) == 4 else "Failed")
    print("Test 6:", "Passed" if b(example,0) == 17 else "Failed")
    print("Test 7:", "Passed" if b(example,1) == 18 else "Failed")
    print("Test 8:", "Passed" if b(example,2) == 18 else "Failed")
    print("Test 9:", "Passed" if b(example,3) == 18 else "Failed")
    print("Test 10:", "Passed" if b(example,4) == 14 else "Failed")
    print("Test 11:", "Passed" if b(example,5) == 17 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 18: Like a GIF For Your Yard")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day18/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data,100))
    print("Part b:", b(data,100))
# Advent of Code 2015
# Day 14: Reindeer Olympics
# https://adventofcode.com/2015/day/14
    
def a(data, time):
    maxDistance = 0
    for line in data:
        fields = line.split(" ")
        speed, duration, rest = int(fields[3]), int(fields[6]), int(fields[-2])
        distance = timeSpent = 0
        while timeSpent < time:
            if timeSpent + duration <= time:
                distance += duration * speed
                timeSpent += duration
            else:
                distance += (time - timeSpent) * speed
                timeSpent += (time - timeSpent)
            
            timeSpent += rest
        maxDistance = max(maxDistance, distance)
    return maxDistance
                
def b(data, time):
    reindeers = []
    scores = []
    positions = []
    for line in data:
        fields = line.split(" ")
        speed, duration, rest = int(fields[3]), int(fields[6]), int(fields[-2])
        reindeers.append([speed, duration, rest])
        scores.append(0)
        positions.append(0)

    for second in range(time):
        for idx, reindeer in enumerate(reindeers):
            if (second % (reindeer[1] + reindeer[2])) < reindeer[1]:
                positions[idx] += reindeer[0]
        for idx, reindeer in enumerate(reindeers):
            if positions[idx] == max(positions):
                scores[idx] += 1

    return max(scores)

def test():
    print()
    example = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.","Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]
    print("Test 1:", "Passed" if a(example, 1000) == 1120 else "Failed")
    print("Test 2:", "Passed" if b(example, 1000) == 689 else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 14: Reindeer Olympics")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day14/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data, 2503))
    print("Part b:", b(data, 2503))
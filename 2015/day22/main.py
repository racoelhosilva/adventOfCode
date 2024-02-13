# Advent of Code 2015
# Day 22: Wizard Simulator 20XX
# https://adventofcode.com/2015/day/22
    
import heapq

def a(data, pHp, pM):
    bhp = int(data[0].split(" ")[-1])
    dmg = int(data[1].split(" ")[-1])
    shield_dmg = max(1, dmg - 7)

    # manaSpent, myHP, myMana, bossHP, shieldDuration, poisonDuration, rechargeDuration
    remaining = [(0, 50, 500, bhp, 0, 0, 0)]
    visited = set(remaining)

    while len(remaining) > 0:
        ms, hp, m, bhp, sd, pd, rd = heapq.heappop(remaining)
        
        # Starting effects
        if pd > 0:
            bhp -= 3
            pd -= 1
        if rd > 0:
            m += 101
            rd -= 1
        
        if m < 53:
            continue

        # Calculate player's turn
        player = []
        if m > 53:
            player.append((ms + 53, hp, m - 53, bhp - 4, sd, pd, rd))
        if m > 73:
            player.append((ms + 73, hp + 2, m - 73, bhp - 2, sd, pd, rd))
        if m > 113 and sd <= 1:
            player.append((ms + 113, hp, m - 113, bhp, 3, pd, rd))
        if m > 173 and pd == 0:
            player.append((ms + 173, hp, m - 173, bhp, sd, 6, rd))
        if m > 229 and sd <= 1:
            player.append((ms + 229, hp, m - 229, bhp, sd, pd, 5))

        # Calculate boss's response
        for ms, hp, m, bhp, sd, pd, rd in player:
            if pd > 0:
                bhp -= 3
                pd -= 1
            if bhp < 0:
                return ms
            
            if sd > 0:
                hp -= shield_dmg
                sd -= 1
            else:
                hp -= dmg
            
            if rd > 0:
                m += 101
                rd -= 1

            if hp < 0 or m < 53:
                continue
        
            if (ms, hp, m, bhp, sd, pd, rd) not in visited:
                heapq.heappush(remaining, (ms, hp, m, bhp, sd, pd, rd))
                visited.add((ms, hp, m, bhp, sd, pd, rd))

def b(data, pHp, pM):
    bhp = int(data[0].split(" ")[-1])
    dmg = int(data[1].split(" ")[-1])
    shield_dmg = max(1, dmg - 7)

    # manaSpent, myHP, myMana, bossHP, shieldDuration, poisonDuration, rechargeDuration
    remaining = [(0, 50, 500, bhp, 0, 0, 0)]
    visited = set(remaining)

    while len(remaining) > 0:
        ms, hp, m, bhp, sd, pd, rd = heapq.heappop(remaining)
        
        hp -= 1
        if hp < 0:
            continue

        # Starting effects
        if pd > 0:
            bhp -= 3
            pd -= 1
        if rd > 0:
            m += 101
            rd -= 1
        
        if m < 53:
            continue

        # Calculate player's turn
        player = []
        if m > 53:
            player.append((ms + 53, hp, m - 53, bhp - 4, sd, pd, rd))
        if m > 73:
            player.append((ms + 73, hp + 2, m - 73, bhp - 2, sd, pd, rd))
        if m > 113 and sd <= 1:
            player.append((ms + 113, hp, m - 113, bhp, 3, pd, rd))
        if m > 173 and pd == 0:
            player.append((ms + 173, hp, m - 173, bhp, sd, 6, rd))
        if m > 229 and sd <= 1:
            player.append((ms + 229, hp, m - 229, bhp, sd, pd, 5))

        # Calculate boss's response
        for ms, hp, m, bhp, sd, pd, rd in player:
            if pd > 0:
                bhp -= 3
                pd -= 1
            if bhp < 0:
                return ms
            
            if sd > 0:
                hp -= shield_dmg
                sd -= 1
            else:
                hp -= dmg
            
            if rd > 0:
                m += 101
                rd -= 1

            if hp < 0 or m < 53:
                continue
        
            if (ms, hp, m, bhp, sd, pd, rd) not in visited:
                heapq.heappush(remaining, (ms, hp, m, bhp, sd, pd, rd))
                visited.add((ms, hp, m, bhp, sd, pd, rd))

def test():
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 22: Wizard Simulator 20XX")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day22/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data, 50, 500))
    print("Part b:", b(data, 50, 500))
# Advent of Code 2015
# Day 11: Corporate Policy
# https://adventofcode.com/2015/day/11

def incrementPassword(password):
    newPassword = list(password)
    cur = len(password)-1
    newPassword[cur] = chr((ord(password[cur]) - ord('a') + 1) % 26 + ord('a'))
    while (newPassword[cur] == 'a'):
        if (cur == 0):
            break
        cur -= 1
        newPassword[cur] = chr((ord(password[cur]) - ord('a') + 1) % 26 + ord('a'))
    return "".join(newPassword)

def threeIncreasingLetters(password):
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2:
            return True
    return False

def forbiddenLetters(password):
    if "i" in password or "o" in password or "l" in password:
        return True
    return False

def twoPairs(password):
    flag = None
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if flag is None:
                flag = password[i]
            elif flag != password[i]:
                return True
    return False

def a(data):
    password = data[0]
    while forbiddenLetters(password) or not threeIncreasingLetters(password) or not twoPairs(password):
        password = incrementPassword(password)
    return password

def b(data):
    password = incrementPassword(data)
    while forbiddenLetters(password) or not threeIncreasingLetters(password) or not twoPairs(password):
        password = incrementPassword(password)
    return password

def test():
    print()
    print("Test 1:", "Passed" if incrementPassword("aaaaaaaa") == "aaaaaaab" else "Failed")
    print("Test 2:", "Passed" if incrementPassword("aaaazzzz") == "aaabaaaa" else "Failed")
    print("Test 3:", "Passed" if incrementPassword("zzzzzzzz") == "aaaaaaaa" else "Failed")
    print("Test 4:", "Passed" if threeIncreasingLetters("hijklmmn") == True else "Failed")
    print("Test 5:", "Passed" if twoPairs("abbceffg") == True else "Failed")
    print("Test 6:", "Passed" if twoPairs("abbcegjk") == False else "Failed")
    print()

if __name__ == "__main__":
    print("\tAdvent of Code 2015\nDay 11: Corporate Policy")
    data = open("/home/rodrigo/Documents/projects/adventOfCode/2015/day11/input.txt", "r").read().splitlines()
    test()
    print("Part a:", a(data))
    print("Part b:", b(a(data)))
data = [line.split(" ") for line in open("input.txt", "r").read().splitlines()]

s = 0
for line in data:
    if line[0] == "A":
        if line[1] == "X":
            s += 1
            s += 3
        elif line[1] == "Y":
            s += 2
            s += 6
        elif line[1] == "Z":
            s += 3
            s += 0
    elif line[0] == "B":
        if line[1] == "X":
            s += 1
            s += 0
        elif line[1] == "Y":
            s += 2
            s += 3
        elif line[1] == "Z":
            s += 3
            s += 6
    elif line[0] == "C":
        if line[1] == "X":
            s += 1
            s += 6
        elif line[1] == "Y":
            s += 2
            s += 0
        elif line[1] == "Z":
            s += 3
            s += 3

print(s)

s = 0
for line in data:
    if line[0] == "A": #
        if line[1] == "X":
            s += 0 # you lose
            s += 3 # you had to pick scissors to lose from a rock
        elif line[1] == "Y":
            s += 3 # you draw
            s += 1 # you had to pick rock to draw from a rock
        elif line[1] == "Z":
            s += 6 # you win
            s += 2 # you had to pick paper to win from a rock

    elif line[0] == "B":
        if line[1] == "X":
            s += 0 # you lose
            s += 1 # you had to pick rock to lose from a paper
        elif line[1] == "Y":
            s += 3 # you draw
            s += 2 # you had to pick paper to draw from a paper
        elif line[1] == "Z":
            s += 6 # you win
            s += 3 # you had to pick scissors to win from a paper

    elif line[0] == "C":
        if line[1] == "X":
            s += 0 # you lose
            s += 2 # you had to pick paper to lose from a scissors
        elif line[1] == "Y":
            s += 3 # you draw
            s += 3 # you had to pick scissors to draw from a scissors
        elif line[1] == "Z":
            s += 6 # you win
            s += 1 # you had to pick rock to win from a scissors

print(s)
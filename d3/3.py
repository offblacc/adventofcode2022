import sys

data = open('test.txt').read().splitlines()

sum = 0
for line in data:
    for letter in line[0:len(line)//2]:
        if letter in line[len(line)//2:]:
            if letter.isupper():
                sum += ord(letter) - 64 + 26
                break
            else:
                sum += ord(letter) - 96
                break
print(sum)

sum = 0
for i in range(0, len(data), 3):
    for letter in data[i]:
        if letter in data[i+1] and letter in data[i+2]:
            if letter.isupper():
                sum += ord(letter) - 64 + 26
                break
            else:
                sum += ord(letter) - 96
                break
print(sum)
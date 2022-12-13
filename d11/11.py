from math import prod
data = open('input.txt').read()
monkeys = []
monkey_inspection_count = []
dividers = []

for line in data.split('\n'):
    if "divisible by" in line:
        dividers.append(int(line.split()[-1]))

for monkey in [x.split('\n') for x in data.split('\n\n')]:
    monkey_inspection_count.append(0)
    monkey_line_iter = iter(monkey)
    if not next(monkey_line_iter).startswith('Monkey'):
        raise ValueError('Invalid monkey data')
    monkeys.append([])
    monkeys[-1].append([])
    for worry_value in map(int, next(monkey_line_iter).split(': ')[1].split(', ')):
        monkeys[-1][-1].append(dict())
        for divider in dividers:
            monkeys[-1][-1][-1].update({divider: worry_value % divider})

    monkeys[-1].append([int(x) if x.isdigit()
                       else x for x in next(monkey_line_iter).split("= ")[1].split()][-2:])
    for _ in range(3):
        monkeys[-1].append(int(next(monkey_line_iter).split()[-1]))

for _ in range(10000):    
    i = -1
    for monkey in monkeys:
        i += 1
        for dividers_of_num in monkey[0]:
            monkey_inspection_count[i] += 1
            new_dividers_dict = dict()
            if monkey[1][0] == '*':
                if monkey[1][1] == 'old':
                    for divider_modulo_pair in dividers_of_num.items():
                        new_dividers_dict.update({divider_modulo_pair[0]: (divider_modulo_pair[1] * divider_modulo_pair[1]) % divider_modulo_pair[0]})
                else:
                    for divider_modulo_pair in dividers_of_num.items():
                        new_dividers_dict.update({divider_modulo_pair[0]: (divider_modulo_pair[1] * monkey[1][1]) % divider_modulo_pair[0]})
            elif monkey[1][0] == '+':
                if monkey[1][1] == 'old':
                    for divider_modulo_pair in dividers_of_num.items():
                        new_dividers_dict.update({divider_modulo_pair[0]: (divider_modulo_pair[1] + divider_modulo_pair[1]) % divider_modulo_pair[0]})
                else:
                    for divider_modulo_pair in dividers_of_num.items():
                        new_dividers_dict.update({divider_modulo_pair[0]: (divider_modulo_pair[1] + monkey[1][1]) % divider_modulo_pair[0]})

            if new_dividers_dict[monkey[2]] == 0:
                monkeys[monkey[3]][0].append(new_dividers_dict)
            else:
                monkeys[monkey[4]][0].append(new_dividers_dict)
        monkey[0] = []

print(prod(sorted(monkey_inspection_count, reverse=True)[0:2]))
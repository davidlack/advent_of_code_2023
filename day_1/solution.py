
def sum_list_of_first_and_last_digits(lines):
    numbers = [[char for char in line if char.isnumeric() == True] for line in lines]
    total = sum([int(lst[0]+lst[-1]) for lst in numbers])
    return total, numbers

lines = [line for line in open('input.txt').read().splitlines()]
print(f'Part 1 solutions: {sum_list_of_first_and_last_digits(lines)}')
total = 0
for line in lines:
    lst = []
    for i in range(len(line)):
        if line[i].isnumeric():
            lst.append(line[i])
        elif line[i: i+len('one')] == 'one':
            lst.append('1')
        elif line[i: i+len('two')] == 'two':
            lst.append('2')
        elif line[i: i+len('three')] == 'three':
            lst.append('3')
        elif line[i: i+len('four')] == 'four':
            lst.append('4')
        elif line[i: i+len('five')] == 'five':
            lst.append('5')
        elif line[i: i+len('six')] == 'six':
            lst.append('6')
        elif line[i: i+len('seven')] == 'seven':
            lst.append('7')
        elif line[i: i+len('eight')] == 'eight':
            lst.append('8')
        elif line[i: i+len('nine')] == 'nine':
            lst.append('9')
    total += int(lst[0]+lst[-1])
print(f'Part 2 solutions: {total}')
print('Done!')
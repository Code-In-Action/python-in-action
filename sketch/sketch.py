#!/usr/bin/env python3
# -*- coding: utf-8 -*-
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Main':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            # print(role, end='')
            # print('said:',end='')
            # print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('the data file is missing')
try:
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        print(other, file=other_file)

except IOError as err:
    print('FileError:' + str(err))

print(man)
print(other)
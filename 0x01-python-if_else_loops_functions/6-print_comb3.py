#!/usr/bin/python3
for firstnum in range(0, 10):
    for secondnum in range(firstnum + 1, 10):
        if firstnum == 8 and secondnum == 9:
            print("{}{}".format(firstnum, secondnum))
        else:
            print("{}{}, ".format(firstnum, secondnum), end='')

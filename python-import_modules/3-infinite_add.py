#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = (sys.argv)
    lenght = len(args)
    if lenght < 2:
        print(0)
    else:
        sum = 0
        for i in range(1, lenght):
            sum = sum + int(args[i])
        print(sum)

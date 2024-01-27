#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = (sys.argv)
    lenght = len(args)
    if lenght < 2:
        print("0 arguments.")
    else:
        print(f"{lenght - 1} arguments:")
        for i in range(1, lenght):
            print(f"{i}: {args[i]}")

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvLen = (len(sys.argv)) - 1
    result = 0

    for i in range(1, argvLen + 1):
        result += int(sys.argv[i])
    print(result)

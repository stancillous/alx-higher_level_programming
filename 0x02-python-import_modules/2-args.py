#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvLen = (len(sys.argv)) - 1
    print("{} argument".format(argvLen)) if argvLen == 1 else print("{} arguments".format(argvLen) )

    for i in range(1, argvLen + 1):
        print("{}: {}".format(i, sys.argv[i]))

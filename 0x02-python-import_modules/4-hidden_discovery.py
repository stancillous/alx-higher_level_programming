#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":

    for file in dir(hidden_4):
        if file[0] != '_' and file[1] != '_':
            print(file)

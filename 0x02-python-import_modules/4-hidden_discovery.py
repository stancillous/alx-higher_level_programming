#!/usr/bin/python3
import glob
files = glob.glob("*.pyc")

for file in files:
    filtered_names = [name for name in dir(file) if not name.startswith('_')]
    print(filtered_names)

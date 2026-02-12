#!/usr/bin/env python3
 
import sys

nombre = sys.argv[0]

print("=== Command Quest ===")

if len(sys.argv) == 1:
    print("No arguments provided!")
    print(f"Program name: {nombre}")
elif len(sys.argv) > 1:
    print(f"Program name: {nombre}")
    print(f"Arguments received: {len(sys.argv) - 1}")

    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

print(f"Total arguments: {len(sys.argv)}\n")

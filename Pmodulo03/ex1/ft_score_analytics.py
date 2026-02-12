#!/usr/bin/env python3

#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")

scores = []

try:
    i = 1
    while i < len(sys.argv):
        scores.append(int(sys.argv[i]))
        i += 1

    print("Scores processed:")
    for s in scores:
        print(s)

except ValueError as error:
    print(f"Error: {error}")

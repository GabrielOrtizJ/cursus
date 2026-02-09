#!/usr/bin/env python3

"""Using the main function to display the values ​​of a plant

    We use `main` to indicate that if we compile this file,
    'main' will be compiled, but if this file is imported
    from elsewhere, `main` will not be compiled.
"""
if __name__ == "__main__":
    name = "Rose"
    height = "25cm"
    age = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("\n=== End of Program ===")

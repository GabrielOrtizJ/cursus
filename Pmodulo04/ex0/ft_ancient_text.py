#!/usr/bin/env python3

def ft_ancient_text():

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        return
    print("RECOVERED DATA:")
    data = file.read()
    print(data)
    print("\nData recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    ft_ancient_text()

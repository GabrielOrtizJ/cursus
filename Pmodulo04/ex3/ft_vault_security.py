#!/usr/bin/env python3

def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("ERROR: Vault data not found. Extraction failed.\n")
        return

    print("\nSECURE PRESERVATION:")
    new_protocols = ("\n{[}CLASSIFIED{]} New security protocols archived")
    with open("classified_data.txt", "a") as file:
        file.write(new_protocols)
        print(new_protocols)

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()

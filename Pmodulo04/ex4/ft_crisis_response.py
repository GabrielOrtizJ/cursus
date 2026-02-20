#!/usr/bin/env python3

def ft_crisis_response():
    """
    Cyber Archives Crisis Response System

    Handles multiple archive access scenarios safely:
    - Missing archives (FileNotFoundError)
    - Security-restricted files (PermissionError)
    - Normal archive access
    Logs crisis alerts, responses, and status confirmations.
    """
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_data.txt", "r") as file:
            data = file.read()
            print(f"{data}\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - {data}")
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Archive not found or denied access")
    finally:
        print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()

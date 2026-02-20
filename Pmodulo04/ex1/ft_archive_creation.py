#!/usr/bin/env python3

def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
    except Exception as e:
        print(f"ERROR: Unable to initialize storage unit. Reason: {e}")
        return

    try:
        print("Inscribing preservation data...")
        entry = (
            "{[}ENTRY 001{]} New quantum algorithm discovered\n"
            "{[}ENTRY 002{]} Efficiency increased by 347 %\n"
            "{[}ENTRY 003{]} Archived by Data Archivist trainee"
        )
        file.write(entry)
        print(f"{entry}\n")
        print("Data inscription complete. Storage unit sealed.")
    except Exception as e:
        print(f"ERROR: Failed to inscribe data. Reason: {e}")
    finally:
        file.close()

    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()

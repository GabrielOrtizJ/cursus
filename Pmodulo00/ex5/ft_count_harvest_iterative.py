def ft_count_harvest_iterative():
    """function to iterate according to the number of days that pass
        through the entry"""
    day = int(input("Days until harvest: "))
    for i in range(day):
        print(f"Day {i}")
    print("Harvest time!")

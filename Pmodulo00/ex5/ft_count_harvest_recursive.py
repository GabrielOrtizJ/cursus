def ft_count_harvest_recursive():
    """function to iterate according to the number of days that pass
    through the entry"""
    days = int(input("Days until harvest: "))

    def count(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)

    count(1)

def ft_water_reminder():
    """ function to calculate if plants are fine """
    day = int(input("Days since last watering:"))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

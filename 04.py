for max_step in [1079, 10079, 100079, 1000079, 10000079, 100000079]:
    x = 0
    y = 0
    while max_step > 0:
        while True:
            y += 1
            max_step -= 1
            if max_step == 0 or (y%3==0 and y%5!=0):
                break

        if max_step == 0:
            break

        while True:
            x += 1
            max_step -= 1
            if max_step == 0 or (x%5==0 and x%3!=0):
                break

    print(x, y)
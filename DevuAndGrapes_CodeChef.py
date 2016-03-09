t = int(input())
counter = 0

while counter <t:
    settings =[int(x) for x in input().split()]
    grapes = [int(x) for x in input().split()]
    grapes_sorted = sorted(grapes, key=lambda grape: grape % settings[1])
    remainder=0
    smm = 0
    count = 0
    for x in grapes_sorted:
        if x <= settings[1]:
            count += settings[1]-x
        else:
            if x%settings[1] > settings[1]/2:
                count += settings[1]-(x % settings[1])
            else:
                count += x % settings[1]
    print(count)
    counter += 1
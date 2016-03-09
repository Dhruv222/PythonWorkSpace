t = int(input())
counter = 0

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

while counter < t:
    settings = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    last_tracked=0
    count=0
    for x in a:
        if binarySearch(b,x):
            count+=1
    print(count)
    print(settings[0]-(settings[1]+settings[2]-count))
    counter += 1
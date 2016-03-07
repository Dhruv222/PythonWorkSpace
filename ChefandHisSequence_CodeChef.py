t = input()
counter=0
output=[]

while counter < int(t):
    lenN = int(input())
    n = [int(x) for x in input().split()]
    lenF = int(input())
    f = [int(x) for x in input().split()]
    j = 0
    while j < lenF:
        if f[j] not in n:
            break
        j += 1
    if j == lenF:
        print("Yes")
    else:
        print("No")
    counter += 1

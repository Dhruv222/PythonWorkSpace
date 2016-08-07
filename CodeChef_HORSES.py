t = int(input())
for i in range(t):
    n = int(input())
    s = [int(x) for x in input().split(" ")]
    s.sort()
    min = s[1]-s[0]
    for j in range(n-1):
        curr_min = s[j+1]-s[j]
        if(curr_min<min):
            min = curr_min
    print(min)
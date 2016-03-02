t=input()
counter=0
output=[]

while counter < int(t):
    product = 1
    add = 0
    n = input()
    n=int(n)
    output.append(n)
    array = [int(x) for x in input().split()]

    for x in range(0, n-1):
        product = array[x]
        add = array[x]
        for num in range(1,n-x):
            add += array[x+num]
            product *= array[x+num]
            if add == product:
                output[counter] += 1
    counter += 1

counter=0
for x in range(0,int(t)):
    print(output[x])

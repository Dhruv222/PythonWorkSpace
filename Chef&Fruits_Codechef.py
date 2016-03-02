t=input()
counter=0
output=[]

while(counter<int(t)):
    array=[int(x) for x in input().split()]
    output.append(abs(array[0]-array[1]))
    if abs(array[0]-array[1])<array[2]:
        print(0)
    else:
        print(abs(array[0]-array[1])-array[2])
    counter +=1

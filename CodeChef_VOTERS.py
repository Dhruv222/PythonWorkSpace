num = [int(x) for x in input().split()]
arr = [[],[],[]]
output = []
for i in range(3):
    for j in range(num[i]):
        arr[i].append(int(input()))
i, j, k = 0,0,0
while(1):
    if(arr[0][i]==arr[1][j]):
        output.append(arr[0][i])
        i+=1
        j+=1
        if(arr[2][k]==arr[0][i]):
            k+=1
        elif(arr[2][k]<arr[0][i]):
            while(1):
                k+=1
                if(arr[2][k]>=arr[0][i]):
                    break
    if(arr[2][k]==arr[1][j]):
        output.append(arr[2][k])
        k+=1
        j+=1
        if(arr[2][k-1]==arr[0][i]):
            i+=1
        elif(arr[2][k]>arr[0][i]):
            while(1):
                i+=1
                if(arr[2][k]<=arr[0][i]):
                    break
    if(arr[0][i]==arr[2][k]):
        output.append(arr[0][i])
        i+=1
        k+=1
        if(arr[1][j]==arr[0][i-1]):
            j+=1
        elif(arr[1][j]<arr[0][i]):
            while(1):
                j+=1
                if(arr[1][j]>=arr[0][i]):
                    break
print(output)
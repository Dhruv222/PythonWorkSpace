for i in range(int(input())):
    test=[int(x) for x in input().split(" ")]
    wallet=[]
    for j in range(test[0]):
        wallet.append(int(input()))
    test_case=pow(2,test[0])
    for l in range(test_case):
        bin_str='{0:b}'.format(l)
        sum=0
        for k in range(len(bin_str)):
            if(bin_str[-1-k]=='1'):
                sum+=wallet[-1-k]
        if(sum==test[1]):
            print("Yes")
            break
        elif(l==(test_case-1)):
            print("No")
def sel_sort(array):
    for x in range(len(array)):
        print("X=",x)
        min=x
        print("ARRAY:",array)
        for j in range(x+1, len(array)):
            print("J=",j)
            if(array[j]<array[min]):
                print("MIN Changed:",j)
                min=j
        print("min element:",array[min])
        temp=array[x]
        array[x]=array[min]
        array[min]=temp
    print(array)
    
input_array=[int(x) for x in input().split(" ")]
sel_sort(input_array)
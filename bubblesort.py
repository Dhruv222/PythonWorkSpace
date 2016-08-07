def bsort(array):
    for x in range(len(array)-1):
        for y in range(len(array)-x-1):
            if(array[y]>array[y+1]):
                temp=array[y]
                array[y]=array[y+1]
                array[y+1]=temp
    print(array)
    
input_array=[int(x) for x in input().split(" ")]
bsort(input_array)
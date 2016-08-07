def isort(array):
    for x in range(len(array)):
        item=array[x]
        j=x-1
        while (j>=0 and array[j]>item):
            array[j+1]=array[j]
            j-=1
        array[j+1]=item
    print(array)
    
input_array=[int(x) for x in input().split(" ")]
isort(input_array)
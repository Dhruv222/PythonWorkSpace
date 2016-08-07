def recur(s):
    if(len(s)==1):
        return s
    else:
        print("Part1: ",s[:int(len(s)/2)])
        part1=recur(s[:int(len(s)/2)])
        print("Part1:Sorted: ",part1)
        print("Part2: ",s[int(len(s)/2):])
        part2=recur(s[int(len(s)/2):])
        print("part2:sorted: ",part2)
        return merge(part1, part2)
        
def merge(part1, part2):
    arr=[]
    i=0
    print("i=",i)
    j=0
    print("j=",j)
    while(i<len(part1) and j<len(part2)):
        if(part1[i]>part2[j]):
            arr.append(part1[i])
            i+=1
            print("INSIDE IF ",i)
        else:
            arr.append(part2[j])
            j+=1
            print("INSIDE ELSE ",j)
    if(i==len(part1)):
        print("IF =0")
        arr=arr+part2[j:]
    else:
        print("ELSE j=0")
        arr=arr+part1[i:]
    return arr
    
input_array=[int(x) for x in input().split(" ")]
print(recur(input_array))
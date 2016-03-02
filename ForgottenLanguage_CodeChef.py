t=input()
counter=0
output=[]
word_truth=False
while(counter<int(t)):
    output.append("")
    TCdesc=[int(x) for x in input().split()]
    n=[x for x in input().split()]
    modern_array=[]
    for num in range(0, TCdesc[1]):
        k=[]
        k=[x for x in input().split()]
        modern_array=modern_array+k[1:]
    for word in n:
        word_truth=False
        for string in modern_array:
            if word==string:
                output[counter] = output[counter] + " YES"
                word_truth=True
                break
        if not(word_truth):
            output[counter]=output[counter]+" NO"
    print(output[counter])
    counter +=1

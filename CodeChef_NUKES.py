vars = [int(x) for x in input().split(" ")]
output = ""
test=vars[0]
for i in range(vars[2]):
    
    output+=str(test%(vars[1]+1))+" "
    test=test//(vars[1]+1)
print(output)
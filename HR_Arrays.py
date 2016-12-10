t = input()
arr = [ int(x) for x in input().strip().split(' ') ]
arr.reverse()
output = ''
for i in arr:
    output += str(i)+" "
print(output.strip())

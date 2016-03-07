t = int(input())

def f( s ):
    balance = 0
    max_balance = 0
    for index in range(0, len(s)):
        if s[index] == '(':
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance, balance)
    return max_balance
counter = 0
while counter < t:
    output = ""
    st = input()
    st_balance = f(st)
    for index in range(0, 2*st_balance):
        if index < st_balance:
            output += "("
        else:
            output += ")"
    print(output)
    counter += 1

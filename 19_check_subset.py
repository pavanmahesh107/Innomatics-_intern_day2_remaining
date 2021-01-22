def Subset(a,b):
    result = 0
    for j in a:
        if j in b:
            result = 1
        else:
            result = 0
            break
    return True if result == 1 else False

test_case = int(input(""))
for j in range(test_case):
    a= int(input(""))
    seta = set(int(x) for x in input().split(" "))
    b =int(input(""))
    setb = set(int(x) for x in input().split(" "))
    print(Subset(seta , setb))

p = int(input(""))
na = set(map(int , input("").split(" ")))
m1 = int(input(""))
na1 = set(map(int , input("").split(" ")))
Final_Set = na.difference(na1)
output = 0
for i in Final_Set:
    output+=1
print(output)

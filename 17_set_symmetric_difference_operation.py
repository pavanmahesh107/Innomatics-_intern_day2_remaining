p0 = int(input(""))
p = set(filter(int , input("").split(' ')))
p1 = int(input(""))
Final_Set = set(filter(int , input("").split(' ')))
SetA = p.symmetric_difference(Final_Set)
output = 0
for i in SetA:
    output+=1
print(output)

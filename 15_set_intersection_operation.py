p1 = int(input(""))
li1=set(map(int , input("").split(" ")))
p2 = int(input(""))
li2=set(map(int , input("").split(" ")))
na = set(li1.intersection(li2))
output=0
for i in na:
  output+=1
print(output)

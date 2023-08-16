#fibonacci
nt=int(input("Enter Limit: "))
n1=0
n2=1
print(0)
while n2<nt:
    nth=n2+n1
    n1=n2
    n2=nth
    if n2>nt:
        break
    print(n2)
#pyramid
a=int(input("Enter Limit: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

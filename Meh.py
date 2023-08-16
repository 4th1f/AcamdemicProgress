import time
n=int(input("Enter Starting Limit: "))
m=int(input("Enter Limit: "))
for i in range (n,m+1):
    i=i**i
    print(i)
    time.sleep(0.1)

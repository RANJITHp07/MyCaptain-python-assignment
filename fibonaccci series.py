#to print a fibonacci series
m=0
n=1
num=int(input("enter the number till fibonacci numbers has to be found"))
print(m,n,sep=",",end=",")
for i in range(0,num):
    fab=m+n
    m=n
    n=fab
    print(fab,end=",")


   

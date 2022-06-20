#to print the frequency of a string
s=input("enter the string:")
str="" #empty string
d={}
for i in s:
    c=0
    if(i not in str):
      str=str+i
      for j in s:
        if(i==j):
            c=c+1
      d[i]=c
l=list(d.values())
l.sort(reverse=True)
for i in l:
    for j in d:
        if(i==d[j]):
            print(j,":",d[j])

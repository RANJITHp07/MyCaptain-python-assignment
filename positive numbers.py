#to print the positive numbers in a list
list1=eval(input("enter the list:"))
list2=[]
for i in list1:
    if(i>0):
        list2.append(i)# adding elements to the second list
print("the list of positive numbers are:",list2)
        

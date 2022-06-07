#to find the extension of the file
s=input("Input the Filename is: ")
f=s.split(".")
if(f[-1]=="py"):
    print("The extension of the file is :'python'")
else:
    print("not python extension")

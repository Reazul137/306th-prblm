filename = input ("Input the FIlename : ")
f_extns = filename.split(" . ")
print("The extension of the file is : " + repr(f_extns[-1]))
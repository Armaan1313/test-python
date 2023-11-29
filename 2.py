a=str(input("Enter color 1: "))
b=str(input("Enter color 2: "))

if a=="red" or a=="blue" or a=="yellow":

   print("Color 1: ",a)
else:
    print(" Invalid")
    

if a=="red" or a=="blue" or a=="yellow":
    print("Color 2: ",b)
else:
    print(" Invalid ")
    
    
if(a=="red" and b=="yellow"):
    print("orange")
    
elif(a=="red" and b=="blue"):
    print("purple")
    
elif(a=="blue" and b=="yellow"):
    print("green") 
    
elif(a=="blue" and b=="red"):
    print("purple")      
    
elif(a=="yellow" and b=="red"):
    print("orange") 
    
elif(a=="yellow" and b=="blue"):
    print("green")
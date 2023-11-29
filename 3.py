a=int(input( "enter your salary in Germany in euros"))
b=input(" Enter the country you want to migrate to")

if(b=="canada"):
    salary=a*0.86
    if(salary>56000):
        print("you will be rich")
    else:
        print("you will be poor")
elif (b=="USA"):
    salary=a*1.10
    if(a>45000):
     print("you will be rich")
    else:
      print("you will be poor")
        
elif (b=="cambodia"):
    salary=a*4000
    if(a>7649856):
     print("you will be rich")
    else:
      print("you will be poor")
        
elif (b=="uk"):
    salary=a*0.86
    if(a>45423):
     print("you will be rich")
    else:
       print("you will be poor")
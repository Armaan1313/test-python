month = int(input("Enter the month in the numeric form. "))
day=int(input("enter the day in the numeric form"))
year= int(input("Enter the year in the numeric form. "))

if  (month > 12) or month==0 or month<0:
    print("Error: Invalid Month Input")
if(day > 31) or day==0 or day<0:
     print("Error: Invalid Month Input")
if(year > 99) or year<0:
     print("Error: Invalid Month Input")
     
     if month==2:
         if year%4==0 and month>29:
             print("invalid date")
         elif month>28:
             print("invalid date")
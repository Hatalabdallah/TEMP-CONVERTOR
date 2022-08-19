temp=float(input("Enter temperature: "))
value=input(" 'C' OR 'F' ")
if value=='F' :
    c=(temp-32)/1.8
    print("Your temperature in celsius is: ",c)
else:
    f=temp*1.8 + 32
    print("Your temperature in fahrenheit is: ",f)
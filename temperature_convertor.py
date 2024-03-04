print("TEMPERATURE CONVERTER")
try:
    temp= input("Enter the temperature to convert into celsius or fahrenheit:(in the format,54F,100C):")
#to extract the numerical vaule
    number=int(temp[:-1])
#extract the convwntion part(eitherr 'C' or 'F')
    convention= temp[-1]
#check input convention is in 'C' or 'F'
    if convention.upper()== "C":
        result = int(round((9*number)/5 +32))
        output = "Fahrenheit"
    elif convention.upper() =="F":
        result = int(round((number-32)*5 / 9))
        output = "Celsius"
except:
    print("Invalid Input")
#display the convection
print("The temperature in",output,"is",result,"degrees.")

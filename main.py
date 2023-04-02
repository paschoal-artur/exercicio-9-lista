#Receiving temperature from user
temp = float(input("What's the fahrenheit temperature at your location? \n"))

#Transforming into celsius
celsius = ((temp - 32) / 9) * 5
celsius = int(celsius)

#Printing to the user
print(f"The temperature in Celsius where you are is {celsius}°C")

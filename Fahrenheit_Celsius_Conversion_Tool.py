temperature = float(input("What is the temperature today?: "))
unit = input("(C)elsius or (F)arenheit: ")
if unit.upper() == "C":
    convert = (9 / 5 * (temperature) + 32)
    print("The temperature in Fahrenheit is " + str(convert))
else:
    convert = (5 / 9 * (temperature - 32) )
    print("The temperature in Celsius is " +str(convert))


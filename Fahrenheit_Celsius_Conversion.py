weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    convert = weight / 0.45
    print("Your weight in lbs is " + str(convert))
else:
    convert = weight * 0.45
    print("Your weight in Kg is " + str(convert))

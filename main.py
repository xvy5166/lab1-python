Temperature = float(input("Enter temperature: "))
Unit = input("Enter unit in F/f or C/c: ")
if (Unit == "F" or Unit == "f"):
  print(f"{Temperature}° in Fahrenheit is equivalent to {float((Temperature-32)*5/9)}° Celsius.")
elif(Unit == "C" or Unit == "c"):
  print(f"{Temperature}° in Celsius is equivalent to {Temperature*1.8+32}° in Fahrenheit.")
else:
  print(f"Invalid unit({Unit}).")

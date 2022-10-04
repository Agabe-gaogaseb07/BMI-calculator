
#Prompts the needed details with the float and the input function.
#The float rounds all decimals to a whole number.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg?: "))

#Calculates the Body Mass Index using the weight and height entered to the power of 2.
BMI = float(int(weight) / int(height**2))

#Using the f-string it will print out what is your Body Mass Index(BMI).
print(f"Your BMI is, {BMI}")

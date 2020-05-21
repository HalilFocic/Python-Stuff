

def BMI(weight, height):
	
	return weight / (height * height) 

state = True
while state:
	weight = float(input("Please enter your weight(kg):\n"))
	height = float(input("Please enter your height(meters):\n"))

	bmi = BMI(weight,height)
	if bmi<18.5:
		print("You are underweight!\n")
	elif bmi<25:
		print("You are in normal range\n")
	else:
		print("You are overweight\n")
	print(f"Your BMi is {bmi}\n")

	answer = input("Do you want to calculate again?").lower()

	if answer =="no":
		state=False




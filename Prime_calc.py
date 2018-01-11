"""Prime Number Detector"""

while True:
	sample = int(input("Is this a Prime Number? : "))
	x = 1
	denom_list = []
	
	while x <= sample: 
		remain = sample%x
		if remain == 0:
			denom_list.append(x)
		x = x +1
		
	if len(denom_list) == 2:
		print(str(sample) + " is Prime")
	else:
		print(str(sample) + " is not Prime.")
		print("These are the denominators of " + str(sample) + ":")
		print(str(denom_list))
	
	response = input("Would you like to do that again? y/n: \n")
	if response == "n":
		break
	else:
		print("Let's start from the top then.")

def legalAges():
#	lifevent  = (
#	16, #Driving,
#	18, #Voting,
#	21, #Drinking,
#	65 #Retirement
#	)
#
#	print("The legal driving age is " + str(lifevent[0]) + ".")
#	print("The legal voting age is " + str(lifevent[1]) + ".")
##	print("The legal drinking age is " + str(lifevent[2]) + ".")
#	print("The legal retirement age is " + str(lifevent[3]) + ".")

	lifevent = {
		"DrivingAge": 16,
		"VotingAge": 18,
		"DrinkingAge": 21,
		"RetirementAge": 65
		}

	print("The legal driving age is " + str(lifevent["DrivingAge"]) + ".")
	print("The legal voting age is " + str(lifevent["VotingAge"]) + ".")
	print("The legal drinking age is " + str(lifevent["DrinkingAge"]) + ".")
	print("The legal retirement age is " + str(lifevent["RetirementAge"]) + ".")


legalAges()

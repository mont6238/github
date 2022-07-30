def addnumbers(num1,num2):
	num1 = int(num1)
	num2 = int(num2)

#	sum = num1 + num2
	return(num1 + num2)


x, y = input("Enter two values: ").split()


print ("The sum of the two values are: ", addnumbers(x,y))

#boolean my
#boolean 2
hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60
calculation_to_units = hours
name_of_unit = "hours"  # global scope


# function can return print formula like print statement without parentesis
def day_to_units(num_days):
	'''
	condition_check = num_days > 0
	#nested function below type() inside print statement
	print(type(condition_check))
	'''
	if num_days > 0:
		return f"{num_days} days are {num_days * calculation_to_units} {name_of_unit}"
	elif num_days == 0:
		return "entered 0"
	elif num_days < 0:
		return "negative number"
	else:
		return "error here"

user_input = input("how many days for calculation?\n")

if user_input.isnumeric()
	print("number")
		#user_input.isdecimal():
		#print("integer")
else:
	print("your input is not a number")

'''
try:
    x = float(a)
except ValueError:
    print("You must enter a number")
'''
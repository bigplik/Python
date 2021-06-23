# boolean my
# boolean 2
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
    #python can works without else statement at the end


def validate_and_execute():
	#isdigit() function fillter float and negative numbers to not be used
	if user_input.isdigit():
	    user_input_number = int(user_input)
	    calculated_value = day_to_units(user_input_number)
	    print(calculated_value)
	else:
	    print("your input is not a valid number")

user_input = input("how many days for calculation?\n")
validate_and_execute()


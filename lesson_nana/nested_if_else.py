hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60
calculation_to_units = hours
name_of_unit = "hours"  # global scope


# function can return print formula like print statement without parentesis
def day_to_units(num_days):
    return f"{num_days} days are {num_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
	if user_input.isdigit():
		user_input_number = int(user_input)
		if user_input_number > 0:
			calculated_value = day_to_units(user_input_number)
			print(calculated_value)
		elif user_input_number == 0:
			print("enter zero")
	else:
	    print("your input is not a valid number")

user_input = input("how many days for calculation?\n")
validate_and_execute()

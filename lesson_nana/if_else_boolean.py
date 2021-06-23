#if else boolean
hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60
calculation_to_units = hours
name_of_unit = "hours"  # global scope


# function can return print formula like print statement without parentesis
def day_to_units(num_days):
	if num_days > 0:
		return f"{num_days} days are {num_days * calculation_to_units} {name_of_unit}"
	else:
		return "errr"

user_input = input("how many days are for calculation?\n")
# need to change user input value to int by int(user_input) function as input
# always sign values as string, this method is called 'casting'
my_var = day_to_units(int(user_input))
print(my_var)

'''to check if value is integer use isinstance(variable, type of variable you want to check) function
    if isinstance(num_days, int) == False:
    	return "wrong variable, only int are accepted"
'''
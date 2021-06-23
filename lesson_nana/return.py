#function with return values with input

hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60
calculation_to_units = seconds
name_of_unit = "seconds" #global scope


#function can return print formula like print statement without parentesis
def day_to_units(num_days):
	return f"{num_days} days are {num_days * calculation_to_units} {name_of_unit}"

user_input = input("how many days are for calculation?")
# need to change user input value to int by int(user_input) function as input
# always sign values as string, this method is called 'casting'
my_var = day_to_units(int(user_input))
print(my_var)


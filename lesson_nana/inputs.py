#user input
hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60
calculation_to_units = seconds
name_of_unit = "seconds" #global scope


def scope_check(num_days):
	my_var = "variable inside a function"
	print(name_of_unit)
	print(num_days)
	print(my_var)

scope_check(input("how many days want to calculate?"))
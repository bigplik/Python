#functions

hours = 24
minutes = 24 * 60
seconds = 24 * 60 * 60

#calculation to units eg. to seconds, or hours
calculation_to_units = seconds
name_of_unit = "seconds"

'''
def day_to_units(days):
	num_of_days = days
	print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

day_to_units(176900)
'''

#2nd eg. for function with parameters without defining extra variable like above
def day_to_units(num_days, custom_message):
	print(f"{num_days} days are {num_days * calculation_to_units} {name_of_unit}")
	print(custom_message)

day_to_units(104343, "custom_message")

# common practice!!!! not to make too many parameters eg.10, better is use about two
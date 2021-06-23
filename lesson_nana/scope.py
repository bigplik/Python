'''
scope - zakres
variable scopes in functions
global scope - variables available from any scope
local scope - internal variables created inside function, can't be acessed from 
			outside function those variable can only be used inside function where they are 
			created
local scope2nd - internal variable that is defined inside a function block, and not
		    as function paramter inside the brackets, like local scope variable described
		    above
'''
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

scope_check(12)
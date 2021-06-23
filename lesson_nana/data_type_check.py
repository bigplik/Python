#check data type

def data_check(data):
	data_type_int = isinstance(data,int)
	data_type_str =  isinstance(data,str)
	data_type_float = isinstance(data,float)
	if data_type_int == True:
		return "integer"
	elif data_type_str == True:
		return "string"
	elif data_type_float == True:
		return "float"
	else:
		return "not integer and string"
'''	if isinstance(data, int) == False:
    	return "your data isn't int!"
    else:
    	return "it's int!"'''

my_var = data_check(222)
print(my_var)
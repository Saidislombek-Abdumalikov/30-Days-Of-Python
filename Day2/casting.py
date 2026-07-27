#int to float

num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)

#flot to int
gravity = 9.81
print('gravity_float', gravity)
gravity_int = int(gravity)
print('gravity_int',gravity_int)


#int to str
num_int = 10
print('num_int', num_int)
num_str = str(num_int)
print('num_str', num_str)

num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_float', float(num_str))  # 10.6
print('num_int', int(num_int))      # 10


# str to list
first_name = 'Saidislom'
last_name = 'Abdumalikov'
print(first_name)       
print(last_name)       
first_name_to_list = list(first_name)
last_name_to_list = list(last_name)

print(first_name_to_list)            # ['S', 'a', 'i', 'd', 'i', 's', 'l', 'o', 'm']
print(last_name_to_list)             # ['A', 'b', 'd', 'u', 'm', 'a', 'l', 'i', 'k', 'o', 'v']
# Corrected code snippet to handle ValueError
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Corrected code snippet to handle TypeError
def concatenate_string_int(string, integer):
    return string + str(integer)

# Corrected code snippet to handle IndexError
def access_list_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return None

# Example Usage
# ValueError
num = convert_to_int("abc")
if num is None:
    print("Invalid input for integer conversion")

# TypeError
result = concatenate_string_int("The number is: ", 123)
print(result)

# IndexError
my_list = [1, 2, 3]
element = access_list_element(my_list, 5)
if element is None:
    print("Index out of bounds")


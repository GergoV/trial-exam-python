
# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_list_items(list_in, *args): # Foolproof only if accepts multiple
    list_out = []
    if type(list_in) != list:
        raise TypeError('Input paramter is not a list.')
    else:
        for i in list_in:
            list_out.append(i*2)
        return list_out

print(double_list_items([1, 2, 4]))

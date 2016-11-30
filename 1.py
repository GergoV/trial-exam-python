# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_list_items(list_in, *args): # Foolproof only if accepts multiple paramters too.
    list_out = []
    try:
        for i in list_in:
            list_out.append(i*2)
        return list_out
    except TypeError:
        print('Error: Input parameter is not a list. Please input list.')

print(double_list_items(1, 2))

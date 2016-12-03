# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def count_a(input_filename):
    try:
        if type(input_filename) != str:
            raise TypeError('Please input filename as string.')
        else:
            with open(input_filename) as f:
                a_quant = 0
                for i in input_filename:
                    if i == 'a':
                        a_quant += 1
                return a_quant
    except FileNotFoundError:
        print('File not found.')


out = count_a('gotcha.txt')
print(out)

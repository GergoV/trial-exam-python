pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

pirates_faux_1 = [
  ['Olaf', 12, False]
]

pirates_faux_2 = [
  {'has_wooden_leg': False, 'gold': 12}
]

pirates_faux_3 = [
  {'Called': 'Jason', 'has_wood_leg': False, 'money': 12}
]

pirates_faux_4 = [
  {'Name': 'Olaf', 'has_wooden_leg': 'Has not', 'gold': 'many'}
 ]

def get_veteran_pirates(pirate_list):
    if type(pirate_list) != list:
        raise TypeError('Please input list.')
    out_list = []
    for i in range(len(pirate_list)):
        if type(pirate_list[i]) != dict:
            raise TypeError('List must contain dictionaries.')
        elif len(pirate_list[i]) <3:
            raise AttributeError('Not enough parameters.')
        else:
            try:
                if pirate_list[i]['has_wooden_leg'] == True and pirate_list[i]['gold'] > 15:
                    out_list.append(pirate_list[i]['Name'])
            except KeyError:
                raise KeyError('Wrong database format.')
    return out_list


out = get_veteran_pirates(pirates_faux_4)
print(out)



"""
Dicionários aninhados e formas de chamar
"""

nested_dict = {
    'mother': {
        'child_1st': 'child_1st_value',
        'child_2nd': 'child_2nd_value'
    },

    'father': {
        'child_1st': 'child_1st_value',
        'child_2nd': 'child_2nd_value'
    }
}

print(nested_dict)
print(len(nested_dict))

for key in nested_dict.keys():
    print('[A]', key)

for key in nested_dict.values():
    print('[B]', key)

for key in nested_dict.items():
    print('[C]', key)

print(nested_dict['mother']['child_1st'])
print(nested_dict['father']['child_2nd'])

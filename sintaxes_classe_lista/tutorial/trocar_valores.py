

"""
Substituir valores de lista por outros dentro dela
"""

bool_list = [False, None, True]
generic_list = [[]]

print([1], bool_list)
bool_list[0], bool_list[2] = bool_list[1], bool_list[1]
print([2], bool_list)
bool_list[1] = generic_list[0]
print([3], bool_list)

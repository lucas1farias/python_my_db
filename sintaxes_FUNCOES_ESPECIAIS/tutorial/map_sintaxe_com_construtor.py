

"""
Objetivo:
    mostrar método map como forma alternativa de comprehension
"""

print(tuple(map(float, '2892458')))          # map
print(tuple(int(obj) for obj in '2892458'))  # comprehension

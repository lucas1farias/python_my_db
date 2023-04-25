

from random import choice


def c_plus_plus_data_types():
    """
    C++ is a strongly-typed programming language, which means that every variable must have a data type associated with
    it. C++ supports a wide range of data types, including the following:

    Boolean: This data type can only have two values: true or false. It is useful for representing conditions in a
             program.

    Character: This data type represents a single character, such as a letter, digit, or symbol. In C++, characters are
               enclosed in single quotes, such as 'a' or '5'.

    Integer: This data type represents a whole number. C++ supports several types of integers, such as int, short, long,
             and long long.

    Floating-point: This data type represents a number with a fractional part. C++ supports two types of floating-point
                    numbers: float and double.

    Void: This data type represents the absence of a value. It is often used to indicate that a function does not return
          a value.

    Arrays: This data type represents a collection of elements of the same data type. Arrays can be one-dimensional,
            two-dimensional, or multi-dimensional.

    Structures: This data type allows you to define a new data type by grouping together variables of different data
                types. Each variable in a structure is called a member.

    Pointers: This data type represents a memory address. Pointers are useful for manipulating data directly in memory.

    Enumerations: This data type allows you to define a new data type by specifying a set of named values. Each value in
                  an enumeration is assigned an integer value starting from zero.

    User-defined data types: C++ also allows you to define your own data types using classes and templates.
    """


engines = (1, 2, 3, 4)
directions = ('frente', 'trás')
commands = set({})

counter = 0
while counter < 100:
    one_engine = choice(engines)
    other_engine = choice(engines)
    one_direction = choice(directions)
    commands.add(f'{str(one_engine)}{str(other_engine)} {one_direction}')
    counter += 1

for code in commands:
    if code[0:2] == '12':
        print(code)
    elif code[0:2] == '13':
        print(code)
    elif code[0:2] == '14':
        print(code)
    elif code[0:2] == '23':
        print(code)
    elif code[0:2] == '24':
        print(code)
    elif code[0:2] == '34':
        print(code)

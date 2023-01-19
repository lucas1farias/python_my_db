

"""
    def func(arg)     -> func(value)                   [Parâmetro comum]
    def func(arg)     -> func(arg=value)               [Parâmetro nomeado]
    def func(*args)   -> func(v1, v2, v3)              [*args recebe uma tupla implícita (sem parânteses)]
    def func(**kargs) -> func(k1=x, k2=y, k3=z)        [**kwargs recebe um dicionário implícita (chaves não podem começar com números)]
    def func(arg, *args, arg2, **kwargs)               [Ordem correta dos elementos de uma função completa (sintaxe na linha abaixo)]
        func(0, 1, 2, arg2='a', key1='b', key2='c')    [arg = 0, *args = 1, 2, arg2 = 'a', **kwargs = {'key1': 'a', 'key2': 'b'}]
"""

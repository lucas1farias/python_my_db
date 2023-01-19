

def logica():
    """
    Errada: if var == something and     == something else
    Certa:  if var == something and var == something else
    Conslusão: O alvo das condições deve ser repetido a cada nova comparação
    """


# Condição de uma linha
op = 'b'
if op == 'a' and op == 'e' and op == 'i' and op == 'o':
    print('Sim')
else:
    print('Não')

# Condição em linhas múltiplas
op2 = 'b'
if op2 == 'b' and op2 == 'c' and op2 == 'd' and op2 == 'f' and op2 == 'g' and op2 == 'h' and op2 == 'j' and op2 == 'k' \
 and op2 == 'l' and op2 == 'm' and op2 == 'n' and op2 == 'p' and op2 == 'q' and op2 == 'r' and op2 == 's' and op2 == 't' \
 and op2 == 'v' and op2 == 'w' and op2 == 'x' and op2 == 'y' and op2 == 'z':
    print('Sim')
else:
    print('Não')

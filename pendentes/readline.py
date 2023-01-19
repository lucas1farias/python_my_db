

from os import chdir

chdir('../sintaxes_p_SO/csv')

# -------------------------------------------------- Leitura (tipo 1) --------------------------------------------------
with open('withOpenRead.txt', 'r') as doc:  # Um módulo já deve existir
    # print(doc.readline())           # A cada chamada, uma linha é exibida
    # print(doc.readline())
    # print(doc.readline(3))          # Passando um índice como argumento, o dado pode ser exibido de forma filtrada
    # print(doc.readline(), end='')   # Forma de exibir impedindo o salto de linha
    pass

# -------------------------------------------------- Leitura (tipo 2) --------------------------------------------------
with open('withOpenRead.txt', 'r') as doc2:
    leitura = doc2.read().split('\n')
    print(leitura)
    print(leitura[0])
    print(leitura[1])
    print(leitura[2])
    print(leitura[2][0:3])  # Leitura filtrada de linha

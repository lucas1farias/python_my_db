

def send_msg(msg: str) -> str:
    return msg


# Há um erro aqui, que não é considerado nas restrições do interpretador normal
print(send_msg(["I don't like mornings"]))

# Terminal: entrar na pasta do arquivo e executar: (mypy 'nome_arquivo.formato')



"""
Instalação:
    pip install passlib

Objetivo:
    criptografar dados, mudando seus dados visuais originais

Observação:
    1. a importação do método é complexa, portanto recomenda-se um apelido
"""

from passlib.hash import pbkdf2_sha256 as codify

languages = ('C', 'Javascript', 'Python')

languages_encrypted = [codify.hash(lang) for lang in languages]
print(languages_encrypted)

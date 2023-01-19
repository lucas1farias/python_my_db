

from passlib.hash import pbkdf2_sha256 as codify

languages = ('C', 'Javascript', 'Python')

languages_encrypted = [codify.hash(lang) for lang in languages]

print(languages_encrypted)

print(f'{languages[0]} é igual a {languages_encrypted[0]}? {codify.verify(languages[0], languages_encrypted[0])}')

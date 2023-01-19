

def word_counter(the_text: str, keyword: str, not_allowed_characters: tuple, plural: str = 's'):

    # Reformatando texto, pois Python diferencia letras maiúsculas e minúsculas
    the_text = the_text.lower()

    # Removendo caracteres de pontuação, pois podem afetar a palavra procurada (ex: palavra. != palavra)
    for character in not_allowed_characters:
        the_text = the_text.replace(character, '')

    # Inserção de todas as palavras num array, p/ que a contagem seja possível
    text_to_list = the_text.split()

    # Contagem é feita pelo método string "count", nas ordens: singular, plural, ambas
    countage_singular = text_to_list.count(keyword)
    countage_plural = text_to_list.count(keyword + plural)
    countage_both = countage_singular + countage_plural

    return f"""
    Palavra procurada              || {keyword} / {keyword + plural}
    Núm. de ocorrências (singular) || {keyword} [{countage_singular}] vez(es)
    Núm. de ocorrências (plural)   || {keyword + plural} [{countage_plural}] vez(es)
    Núm. de ocorrências (ambas)    || {keyword}/{keyword + plural} [{countage_both}] vez(es)"""


if __name__ == '__main__':

    text = """
    Operadores de String
    Python oferece operadores para processar texto (ou seja, valores de string). Assim como os números, as strings podem
    ser comparadas usando operadores de comparação: ==, !=, <, > e assim por diante. O operador ==, por exemplo, retorna
    True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
    """

    print(word_counter(
        the_text=text,
        keyword='string',
        not_allowed_characters=(',', '.', '(', ')', '\n'),
        plural='s'))

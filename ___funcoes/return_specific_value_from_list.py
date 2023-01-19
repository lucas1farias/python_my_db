

def query_from_list(source_, wanted_data, multiple):

    try:

        # Recomendação: O texto precisa ser formatado p/ remover caracteres separadores, pois geram problemas
        # Em "sentence", após a palavra "forte", há um [.], se não fosse removido via "replace", haveria problemas
        text_cleaned = source_.replace('.', '').replace(',', '').replace(':', '')
        text_as_array = text_cleaned.split()

        if multiple:
            storage = []
            for data in wanted_data:
                storage.append(text_as_array.pop(text_as_array.index(data)))
            return " ".join(storage)
        else:
            data_acquired = text_as_array.pop(text_as_array.index(wanted_data))
            return data_acquired

    except ValueError:
        return f'O dado procurado: "{wanted_data}" não está no texto analisado.'


if __name__ == '__main__':

    text = """
    Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, 
    funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991"""

    name = query_from_list(source_=text, wanted_data='Guido', multiple=False)
    last_name = query_from_list(source_=text, wanted_data=['van', 'Rossum'], multiple=True)
    sentence = query_from_list(source_=text, wanted_data='tipagem dinâmica e forte'.split(), multiple=True)
    not_found = query_from_list(source_=text, wanted_data='tipagem dinâmica e forte.'.split(), multiple=True)

    print([1], name)
    print([2], last_name)
    print([3], sentence)
    print([4], not_found)

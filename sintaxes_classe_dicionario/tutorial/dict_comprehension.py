

from random import randint

tracks = [
    {'soundtrack': 'Chop Suey', 'times_played': randint(1, 1001)},
    {'soundtrack': 'Spiders', 'times_played': randint(1, 1001)},
    {'soundtrack': 'Toxicity', 'times_played': randint(1, 1001)},
    {'soundtrack': 'Vermilion pt2', 'times_played': randint(1, 1001)}
]


# Dict comprehension
def find_top_song_played(json):
    # Dict comprehension [key_int:value_str] com dados em ordem manipulada (+ prático ordenar por chaves numéricas)
    rank_most_played_unordered = {key['times_played']: key['soundtrack'] for key in json}

    # Pegando a chave com o maior valor numérico
    most_played_song = max(rank_most_played_unordered)

    # Usando a chave de maior valor como par na função "get" p/ coletar seu valor
    most_played_song_name = rank_most_played_unordered.get(most_played_song)

    top_song = f"""
    ---------- MÚSICA MAIS TOCADA ----------
    {most_played_song_name} foi tocada {most_played_song} vezes"""

    print(rank_most_played_unordered)
    print(most_played_song)
    print(most_played_song_name)
    print(top_song)


# List comprehension
def find_top_song_played_(json):
    tracks_played_unordered_int = [key['times_played'] for key in json]
    most_played_track_int = max(tracks_played_unordered_int)

    # A lista matriz é percorrida p/ achar o int que coincida com [ most_played_track_int ], e retornando o seu valor
    most_played_track_str = ''.join([key['soundtrack'] for key in json if key['times_played'] == most_played_track_int])

    top_song = f"""
    ---------- MÚSICA MAIS TOCADA ----------
    {most_played_track_str} foi tocada {most_played_track_int} vezes
    """

    print(tracks_played_unordered_int)
    print(most_played_track_int)
    print(most_played_track_str)
    print(top_song)


# Sorted
def find_top_song_played__(json):
    tracks_and_played_frequency = [(key['soundtrack'], key['times_played']) for key in json]

    #                                            tupla((str[0], int[1]))      ordenar pelo índice:    1   último índice
    tracks_and_played_frequency_ordered = sorted(tracks_and_played_frequency, key=lambda index: index[1])[-1]

    top_song = f"""
    ---------- MAIS TOCADA ----------
    {tracks_and_played_frequency_ordered[0]} foi tocada {tracks_and_played_frequency_ordered[1]} vezes"""

    print(tracks_and_played_frequency)
    print(tracks_and_played_frequency_ordered)
    print(top_song)


if __name__ == '__main__':
    from random import randint
    # find_top_song_played(json=tracks)
    # find_top_song_played_(json=tracks)
    # find_top_song_played__(json=tracks)

    sample = {1: True, 2: False, 3: None}

    # Dict comprehension genérico
    dict_sample_1st = {key: key for key in sample}
    print(dict_sample_1st)

    # Dict comprehension invertendo lugares das chaves com os valores
    dict_sample_2nd = {item[1]: item[0] for item in sample.items()}
    print(dict_sample_2nd)

    # Dict comprehension: números dos índices e strings como chave e valor
    letters = 'abcdefg'
    dict_sample_3rd = {letters[i]: i for i in range(len(letters))}
    print(dict_sample_3rd)

    # Dict comprehension: uso do if (números aleatórios como chave, e seu valor é a análise se é ímpar)
    types = ('odd', 'even')
    random_numbers = [randint(1, 99) for n in range(25)]
    scan = {n: types[0] for n in random_numbers if n % 2}
    print(scan)

    # Dict comprehension: uso do if e else (números aleatórios como chave, e seu valor é a análise se é par ou ímpar)
    random_numbers = [randint(1, 99) for n in range(25)]
    scan = {n :(types[0] if n % 2 else types[1]) for n in random_numbers}
    print(scan)

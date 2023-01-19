

from random import shuffle


def deck() -> list:
    suits = ['♥', '♦', '♣', '♠']
    integers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck_box = [(number + cell) for cell in suits for number in integers]  # exemplo aqui
    shuffle(deck_box)
    return deck_box


deck_obj = deck()
print(len(deck_obj))
clubs = sorted(tuple(filter(lambda card: '♣' in card, deck_obj)), reverse=True)
diamonds = sorted(tuple(filter(lambda card: '♦' in card, deck_obj)), reverse=True)
hearts = sorted(tuple(filter(lambda card: '♥' in card, deck_obj)), reverse=True)
spades = sorted(tuple(filter(lambda card: '♠' in card, deck_obj)), reverse=True)
print(clubs)
print(diamonds)
print(hearts)
print(spades)

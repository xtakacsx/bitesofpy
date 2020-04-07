from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    main_deck = []
    cards = [x for x in range(10)] + ["Draw Two", "Skip", "Reverse"]
    for suit in SUITS:
        for i in cards:
            count = 1 if i == 0 else 2
            for _ in range(count):
                main_deck.append(UnoCard(suit=suit, name=str(i)))
    for _ in range(4):
        main_deck.append(UnoCard(suit=None, name="Wild"))
        main_deck.append(UnoCard(suit=None, name="Draw Four"))
    return main_deck

# CARD
# SUIT, RANK, VALUE


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str(self):
        return self.rank + " of" + self.suit


two_hearts = Card("Hearts", "Two")
print(two_hearts)

two_hearts.suit

two_hearts.rank

two_hearts.value

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

from random import sample
import collections

Card = collections.namedtuple("Card", ["suit", "rank"])


class Dek():
    RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
    SUITS = "spade heart diamond club".split()

    @property
    def cards(self):
        return self._cards

    def __init__(self) -> None:
        self._cards = [Card(s, r) for s in self.SUITS for r in self.RANKS]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def get_hand(dek, size: int) -> list[Card]:
    return sample(dek.cards, size)

# probabilidad que salgan pares en las manos


def main(hand_size: int, n_tries: int):
    dek = Dek()
    hands = [get_hand(dek, hand_size) for _ in range(n_tries)]

    statistics = []
    pairs = 0
    pure_pairs = 0
    for hand in hands:
        print(f"hand: {sorted(hand)}")
        card_val = []
        for c in hand:
            card_val.append(c[1])
        cards_count = collections.Counter(card_val).most_common()
        for card_count in cards_count:
            # if card_count[1] > 1:
            #     pairs += card_count[1] // 2
            #     break
            if card_count[1] == 2:
                pure_pairs += 1
                break
        statistics.append(pairs / len(hand))
        # print(cards_count)
    statistic = pure_pairs / n_tries
    print(statistic)
    return statistic


if __name__ == "__main__":
    hand_size = int(input("De cuántas barajas será la mano?: "))
    n_tries = int(input("Cuántas veces quiere ejecutar la simulación?: "))

    main(hand_size, n_tries)

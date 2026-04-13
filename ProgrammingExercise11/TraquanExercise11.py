import random


class Deck:
    # Creates a deck of 52 cards and shuffles it
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    # Deals one card from the deck
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("\nReshuffling the discard pile...\n")

        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    # Moves cards in play to the discard pile for a new hand
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Converts a card number into a rank and suit
def card_to_string(card_number):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank = ranks[card_number % 13]
    suit = suits[card_number // 13]

    return rank + " of " + suit


# Displays the current hand
def display_hand(hand):
    print("\nYour current hand:")
    for i in range(len(hand)):
        print(str(i + 1) + ". " + card_to_string(hand[i]))


# Gets the card positions the user wants to replace
def get_replacement_choices():
    print("\nEnter the card numbers you want to replace.")
    print("Example: 1 3 5")
    print("Press Enter if you do not want to replace any cards.")

    user_input = input("Cards to replace: ").strip()

    if user_input == "":
        return []

    parts = user_input.split()
    choices = []

    for item in parts:
        if item.isdigit():
            number = int(item)
            if 1 <= number <= 5 and number not in choices:
                choices.append(number)

    return choices


# Main game function
def play_poker_hand():
    deck = Deck(52)
    hand = []

    # Deal the first five cards
    for _ in range(5):
        hand.append(deck.deal())

    print("=== Poker Hand Game ===")
    display_hand(hand)

    # Ask which cards to replace
    choices = get_replacement_choices()

    # Replace selected cards
    for choice in choices:
        hand[choice - 1] = deck.deal()

    # Show final hand
    print("\n=== Final Hand ===")
    display_hand(hand)


# Main function
def main():
    play_poker_hand()


main()
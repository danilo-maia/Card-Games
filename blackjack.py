import random
import os


suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
numbers = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
           'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


def check_num(text):
    while True:
        try:
            value = int(input(text))
        except ValueError:
            clear_terminal()
            print('A number, please!')
        else:
            return value

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = numbers[rank]

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.all_deck_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_deck_cards.append(Card(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.all_deck_cards)

    def remove_card(self):
        return self.all_deck_cards.pop()


class Dealer:
    def __init__(self):
        self.all_cards = []
        self.pontuation = 0

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_card(self, card):
        self.all_cards.append(card)

    def ace_check(self):
        self.pontuation = 0

        valid_ace = False
        check_aces = 0

        for card in self.all_cards:
            if card.rank == 'Ás':
                check_aces += 1
                continue

            self.pontuation += card.value

        if check_aces > 0:
            for i in range(check_aces):
                if self.pontuation + 11 <= 21:
                    self.pontuation += 11
                    valid_ace = True
                else:
                    self.pontuation += 1

            for card in self.all_cards:
                if card.rank == 'Ás':
                    if valid_ace:
                        card.value = 11
                        valid_ace = False
                    else:
                        card.value = 1

    def bust_check(self):
        if self.pontuation > 21:
            return True
        return False


class Player(Dealer):
    def __init__(self, name, money):
        super().__init__()
        self.name = name
        self.money = money

    def bet_check(self):
        while True:
            values = [100, 250, 500]
            options = [1, 2, 3]
            answer = check_num(f'Bet Value? You have ${self.money}\n1: 100\n2: 250\n3: 500\nAnswer: ')
            if answer in options:
                if values[answer-1] <= self.money:
                    return values[answer-1]
                else:
                    clear_terminal()
                    print(f'Not enough money.')
            else:
                clear_terminal()
                print('Not valid number')

    def __str__(self):
        return f'{self.name} has ${self.money}'


deck = Deck()
deck.shuffle_cards()

player = Player(input('What is your name? '), 250)

print(f'\nHey {player.name}!\n')

bet_value = player.bet_check()

dealer = Dealer()


class Blackjack:
    def __init__(self):
        self.hidden_card = True

    def distribuir_cartas(self):
        for i in range(2):
            player.add_card(deck.remove_card())
        for i in range(2):
            dealer.add_card(deck.remove_card())

    def show_cards(self):
        print("DEALER'S HAND")
        for card in dealer.all_cards:
            if card == dealer.all_cards[-1]:
                if self.hidden_card:
                    print(f'------\n')
                else:
                    print(f'{card} / {card.value}\n')
            else:
                print(f'{card} / {card.value}')

        print(f"{player.name.upper()}'S HAND:")
        for card in player.all_cards:
            if card == player.all_cards[-1]:
                print(f'{card} / {card.value}\n')
            else:
                print(f'{card} / {card.value}')

    def ask_player(self):
        clear_terminal()

        has_valid_ace = False

        while True:
            print(f'CURRENT BET: ${bet_value}\n')

            has_valid_ace = player.ace_check()

            self.show_cards()

            if has_valid_ace:
                print(
                    f'Your score is {player.pontuation - 10} / {player.pontuation}\n')
            else:
                print(f'Your score is {player.pontuation}\n')

            if player.pontuation > 21:
                print(f'{player.name} busted! score: {player.pontuation}')
                return

            answer = input('1: Hit\n2: Stand\nAnswer: ')
            if answer == '1':
                player.all_cards.append(deck.remove_card())
            elif answer == '2':
                print(f'\n{player.name} Stands. Score: {player.pontuation}')
                return
            else:
                clear_terminal()

            clear_terminal()

    def ask_dealer(self):
        clear_terminal()

        self.hidden_card = False

        while True:
            print(f'CURRENT BET: ${bet_value}\n')

            dealer.ace_check()

            self.show_cards()

            print(f'{player.name} score: {player.pontuation} points')

            if dealer.pontuation > 21:
                print(f'Dealer busted! score: {dealer.pontuation} points')
                return
            if dealer.pontuation >= 17:
                print(f'Dealer Stands! score: {dealer.pontuation} points')
                return

            dealer.all_cards.append(deck.remove_card())

            clear_terminal()

    def check_win(self):
        if player.bust_check():
            player.money -= bet_value
            print(f'\nYou lost ${bet_value}. Current value: ${player.money}.')
        elif dealer.bust_check():
            player.money += bet_value
            print(
                f'\nYOU WIN! ${bet_value} goes to your account. Current value: ${player.money}.')
        elif len(dealer.all_cards) == 2 and dealer.pontuation == 21:
            if len(player.all_cards) == 2 and player.pontuation == 21:
                print("He made a BLACKJACK, but it's a draw anyway")
            else:
                print(
                    f'He made a BLACKJACK. You lost ${bet_value}. Current value: ${player.money}.')
        elif len(player.all_cards) == 2 and player.pontuation == 21:
            player.money += bet_value
            print(
                f'You made a BLACKJACK and WIN. ${bet_value} goes to your account. Current value: ${player.money}.')
        elif dealer.pontuation > player.pontuation:
            player.money -= bet_value
            print(f'\nYou lost ${bet_value}. Current value: ${player.money}.')
        elif dealer.pontuation < player.pontuation:
            player.money += bet_value
            print(
                f'\nYOU WIN! ${bet_value} goes to your account. Current value: ${player.money}.')
        else:
            print('\nThere was a draw!')

    def play_again(self):
        global bet_value
        while True:
            decision = input('\nPlay again?\n1: Yes\n2: No\nAnswer:  ')
            if decision == '1':
                clear_terminal()
                print(player)
                if player.money < 100:
                    print("Not enough cash, stranger!")
                    return False
                else:
                    bet_value = player.bet_check()
                    return True
            elif decision == '2':
                clear_terminal()
                print(player)
                return False
            else:
                clear_terminal()
                print('Not valid character\n')
                print(player)

    def play(self):

        game_on = True
        while game_on:
            self.distribuir_cartas()
            self.ask_player()
            if not player.bust_check():
                self.ask_dealer()
            self.check_win()
            game_on = self.play_again()

            deck = Deck()
            deck.shuffle_cards()
            self.hidden_card = True
            player.all_cards = []
            dealer.all_cards = []

        print(f'Thanks for Playing, {player.name}!')


game = Blackjack()
game.play()

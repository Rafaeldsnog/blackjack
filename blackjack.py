import sys
import os
import random
import time

############################################################

# DECLARATION OF GLOBAL VARIABLES
global full_deck


# Creation of the deck and list tuples with values for each card
def full_deck_generation():
    suits = ['h', 'd', 'c', 's']
    cards_faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    full_deck = []
    for face in cards_faces:
        for suit in suits:
            card = f"{face}{suit}"
            full_deck.append(card)

    full_deck_values = []
    for card in full_deck:
        if card[0] == 'A':
            value = 11
            full_deck_values.append(tuple([card, value]))
        elif card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0] == '1':
            value = 10
            full_deck_values.append(tuple([card, value]))
        else:
            value = int(card[0])
            full_deck_values.append(tuple([card, value]))
    return full_deck_values


full_deck_values = full_deck_generation()
#########################################

user_name = input("What is your name?\n-> ")

###################################################################
# VERIFICATION AND INPUT OF THE NUMBER OF DECKS TO BE PLAYED

n_of_decks = 0
while n_of_decks < 1 or n_of_decks > 8:
    try:
        n_of_decks = int(input("\nChoose number of decks(1~8): "))
    except ValueError:
        print("Not Valid input ")

####################################################################
# Creating all the cards to be played dict in list of tuples
all_cards = []
if n_of_decks == 1:
    for jj in full_deck_values:
        all_cards.append(jj)
    initial_deck = all_cards
    initial_len = len(all_cards)

else:
    for ii in range(n_of_decks):
        for jj in full_deck_values:
            all_cards.append(jj)
    initial_deck = all_cards
    initial_len = len(all_cards)

print(all_cards)
#####################################################################

# USER INITIAL BANKROLL
user_bank = 1000


#### FUNCTIONS DEFINITION #########################################
def place_bets(user_name, user_bank):
    bet = -1
    count = 1
    while bet > user_bank or bet < 0:
        if count > 1:
            print("Not valid Input\n")
        count += 1
        bet = input(
            f"Place the amount to bet this round (press a/A to go All-in or k/K to cash out).\n{user_name}: ${user_bank}\n-> $")

        if bet.lower() == 'a':
            bet = user_bank
            return bet, user_bank
        elif bet.lower() == 'k':
            return bet, user_bank

        try:
            bet = float(bet)
            if bet == 0:
                return bet, user_bank
        except:
            print("Not valid input!")
            bet = -1

    return bet, user_bank


# Definition of the random cards picker

def random_card():
    global all_cards
    if len(all_cards) < 0.5 * initial_len:
        all_cards = initial_deck
        print("SHUFFLING! ")
        time.sleep(2)
        # INSERT HERE THE CARD COUNTING RESET

    selected_card = random.choice(all_cards)
    all_cards.remove(selected_card)

    return selected_card


def hit(user_cards, user_score):
    new_card = random_card()
    user_cards.append(new_card)
    user_score += new_card[1]
    return user_cards, user_score


def dealer_game(dealer_cards, dealer_score):
    end_dealer = False
    count_d = 0
    print("\nDEALER GAME")
    time.sleep(1.5)
    while not end_dealer:
        if dealer_score < 17:
            new_card = random_card()
            dealer_cards.append(new_card)
            dealer_score += new_card[1]
            print(f"DEALER CARDS: {dealer_cards}. DEALER SCORE: {dealer_score}")
            time.sleep(1.5)
            count_d += 1

        elif dealer_score >= 17 and dealer_score <= 21:
            end_dealer = True
            if count_d == 0:
                print(f"DEALER CARDS: {dealer_cards}. DEALER SCORE: {dealer_score}")
            time.sleep(1)

            return dealer_cards, dealer_score
        else:
            print(f"DEALER CARDS: {dealer_cards}. DEALER SCORE: {dealer_score}")
            time.sleep(1)
            end_dealer = True
            return dealer_cards, dealer_score


def user_game(user_cards, user_score):
    end_round = False
    while not end_round:
        option = input("H/h -> hit; D/d -> double; any -> stand\n->")
        if option.lower() == 'h':
            user_cards, user_score = hit(user_cards, user_score)
            if user_score > 21:
                for index, card in enumerate(user_cards):
                    if ("A" in card[0]) and card[1] == 11:
                        user_cards[index] = (card[0], 1)
                        user_score -= 10
                        print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")
                        user_game(user_cards, user_score)
                    else:
                        print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")
                        return user_cards, user_score
            elif user_score == 21:
                print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")
                return user_cards, user_score

            else:
                print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")


        elif option.lower() == 'd':
            user_cards, user_score = hit(user_cards, user_score)
            print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")
            end_round = True
        else:
            print(f"USER CARDS: {user_cards}. USER SCORE: {user_score}")
            end_round = True
    return user_cards, user_score


# TODO: insert cards counting in code
###########################################
# GAME DEVELOPMENT
end_game = False
while not end_game:
    time.sleep(2)
    os.system('cls')
    bet, user_bank = place_bets(user_name, user_bank)

    if isinstance(bet, str):
        if bet.lower() == 'k':
            print(f"Cash Out: {user_bank}. Thanks for Playing!")
            time.sleep(2)
            quit()

    print(f"USER BANK: {user_bank}\n BET: {bet}")

    # INITIAL CARDS DELT
    dealer_1 = random_card()
    dealer_2 = random_card()

    user_1 = random_card()
    user_2 = random_card()

    print(f"\nCARDS TO BE DELT: {len(all_cards)}\n")
    print(f"DEALER CARDS: {dealer_1[0]} *\n")
    print(f"USER CARDS: {user_1[0]}  {user_2[0]}\n")
    user_score = user_1[1] + user_2[1]
    dealer_score = dealer_1[1] + dealer_2[1]
    print(f"SCORE: {user_score}")

    user_cards = [user_1, user_2]
    dealer_cards = [dealer_1, dealer_2]

    user_cards, user_score = user_game(user_cards, user_score)

    if user_score > 21:
        print("BUSTED!")
        print(f"DEALER CARDS: {dealer_cards} DEALER SCORE: {dealer_score}")
        user_bank -= bet
        time.sleep(1.5)

    else:
        dealer_cards, dealer_score = dealer_game(dealer_cards, dealer_score)
        if dealer_score > 21:
            print("YOU WON!")
            user_bank += bet
            time.sleep(1.5)

        elif user_score > dealer_score:
            print("YOU WON!")
            user_bank += bet
            time.sleep(1.5)

        elif user_score == dealer_score:
            print("PUSH!")
            time.sleep(1.5)

        else:
            print("YOU LOOSE!")
            user_bank -= bet
            time.sleep(1.5)

    if user_bank == 0:
        print("BUSTED!")
        end_game = True

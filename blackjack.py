import sys
import random
import time
############################################################
#Creation of the deck and list tuples with values for each card

global full_deck
global all_cards

def full_deck_generator():
    suits = ['h','d','c','s']
    cards_faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    full_deck = []
    for face in cards_faces:
        for suit in suits:
            card = f"{face}{suit}"
            full_deck.append(card)

    full_deck_values = []
    for card in full_deck:
        if card[0]=='A':
            value = 11
            full_deck_values.append(tuple([card,value]))
        elif card[0] =='J' or card[0] =='Q' or card[0] =='K' or card[0] == '1':
            value = 10
            full_deck_values.append(tuple([card,value]))
        else:
            value = int(card[0])
            full_deck_values.append(tuple([card,value]))
    return full_deck_values
full_deck_values = full_deck_generator()
#########################################

user_name = input("What is your name?\n-> ")

###################################################################
# VERIFICATION AND INPUT OF THE NUMBER OF DECKS TO BE PLAYED

n_of_decks = 0
while n_of_decks <6 or n_of_decks >8:
    try:
        n_of_decks = int(input("Choose number of decks(6~8): "))
    except ValueError:
        print("Not Valid input ")

####################################################################
# Creating all the cards to be played dict in list of tuples
all_cards = []
for ii in range(n_of_decks-1):
    for jj in full_deck_values:
        all_cards.append(jj)

initial_deck = all_cards
initial_len = len(all_cards)
#print(all_cards)
#####################################################################

# USER INITIAL BANKROLL
user_bank = 1000

#### FUNCTIONS DEFINITION #########################################
def place_bets(user_name,user_bank):
    bet = -1
    count = 1
    while bet>user_bank or bet<0:
        if count>1:
            print("Not valid Input\n")

        bet = input(f"Place the amount to bet this round. Press a/A to go All-in.\n{user_name}: ${user_bank}\n->" )

        if isinstance(bet,str):
            if bet.lower() == 'a':
                bet = user_bank
                return bet,user_bank
        try:
            bet = float(bet)
        except:
            bet = -1
        count+=1

    return bet,user_bank

place_bets(user_name,user_bank)


# Definition of the random cards picker

def random_card(all_cards):

    if len(all_cards) < 0.5*initial_len:
        all_cards = initial_deck
        print("SHUFFLING! ")
        time.sleep(2)
        # INSERT HERE THE CARD COUNTING RESET

    selected_card = random.choice(all_cards)
    all_cards.remove(selected_card)

    return selected_card


card = random_card(all_cards)
print(card)
time.sleep(2)
print('acabou a espera')


# ###########################################
#
# end_game = False
# while not end_game:
#
#     bet = place_bets(user_name,user_bank)
#
#     key1 ,value1 ,all_cards, count = random_card(all_cards, n_of_decks,count)
#
#     key2 ,value2 ,all_cards, count = random_card(all_cards, n_of_decks,count)
#
#     if key1 == None or key2 == None:
#         print("SHUFFLING")
#         all_cards = full_deck_generator()
#         key1, value1, all_cards = random_card(all_cards, n_of_decks, count)
#         key2, value2, all_cards = random_card(all_cards, n_of_decks, count)
#
#     print(f"your cards are {key1} {key2} and you have {value1+value2}")
#
#
#
#
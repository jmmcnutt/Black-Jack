import random
import art

print(art.logo)
keep_playing = True

while keep_playing is True:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealers_hand = [cards[random.randint(0, len(cards) - 1)], ]
    deal = input("Type 'deal' to start the hand:\n")
    players_hand = []
    players_hand.append(cards[random.randint(0, len(cards) - 1)])
    players_hand.append(cards[random.randint(0, len(cards) - 1)])


    def deal_the_cards():
        print(f'Dealers Hand: {dealers_hand}')
        print(f'Your Hand: {players_hand}, current score: {sum(players_hand)}')

        hit = input("Type 'y' to get another card, type 'n' to pass:\n")

        while hit == 'y':

            if hit == 'y':
                players_hand.append(cards[random.randint(0, len(cards) - 1)])
                if sum(players_hand) < 20:
                    print(f'Your Hand: {players_hand}, current score: {sum(players_hand)}')
                    hit = input("Type 'y' to get another card, type 'n' to pass:\n")
                elif sum(players_hand) > 21:
                    if 11 in players_hand:
                        for item in players_hand:
                            if item == 11:
                                x = players_hand.index(item)
                                players_hand[x] = 1
                                print(f'Your Hand: {players_hand}, current score: {sum(players_hand)}')
                                hit = input("Type 'y' to get another card, type 'n' to pass:\n")
                    else:
                        print(f'Your Hand: {players_hand}, current score: {sum(players_hand)}')
                        print(f'Bust! Your total is over 21: {players_hand}')
                        hit = 'n'
                else:
                    print(f'Your Hand: {players_hand}, current score: {sum(players_hand)}')
                    hit = 'n'


    def npc_cards():
        dealers_hand.append(cards[random.randint(0, len(cards) - 1)])
        under_21 = True

        while under_21 is True:
            if sum(dealers_hand) > 21:
                if 11 in dealers_hand:
                    for item in dealers_hand:
                        if item == 11:
                            x = dealers_hand.index(item)
                            dealers_hand[x] = 1

            if sum(dealers_hand) < 17:
                dealers_hand.append(cards[random.randint(0, len(cards) - 1)])

            else:
                under_21 = False





    deal_the_cards()
    npc_cards()

    if sum(players_hand) > 21:
        print(f"Your hand: {players_hand}\nDealer's Hand: {dealers_hand}\nBust! Your total is: {sum(players_hand)}")
    elif sum(dealers_hand) > 21:
        print(f"Your hand: {players_hand}\nDealer's Hand: {dealers_hand}\nYou Win! Your total is: {sum(players_hand)} \nThe Dealer Bust! The dealer's total: {sum(dealers_hand)}")
    elif sum(players_hand) > sum(dealers_hand):
        print(f"Your hand: {players_hand}\nDealer's Hand: {dealers_hand}\nYou Win! Your total is: {sum(players_hand)} \nThe dealer's total is: {sum(dealers_hand)}")
    elif sum(players_hand) < sum(dealers_hand):
        print(f"Your hand: {players_hand}\nDealer's Hand: {dealers_hand}\nYou Lose! Your total is: {sum(players_hand)} \nThe dealer's total is: {sum(dealers_hand)}")
    else:
        print(f"Your hand: {players_hand}\nDealer's Hand: {dealers_hand}\nYou Tie! Your total is: {sum(players_hand)} \nThe dealer's total is: {sum(dealers_hand)}")

    y = input("Type 'y' to play again, 'no' to stop playing:\n")
    if y == 'n':
        keep_playing = False
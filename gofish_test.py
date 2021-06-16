from gofish import *
from pokercards import *

if __name__ == "__main__":
	deck = CardDeck()

	print("deal cards from deck to player_hand")
	cards = [deck.deal_card() for _ in range(7)]
	player_hand = GoFishHand(cards=cards)

	player_hand.print()
	print(player_hand.get_num_cards())

	print("manually add 3 cards with rank value 1 to player_hand")
	print("Notice: rank value 1 cards are automatically collected")
	print("as four of a kind!")
	# add 3 cards with rank 2
	player_hand.add_cards([Card(14), Card(27), Card(40)])

	player_hand.print()

	print("Should have rank value of 1 in this four of a kind list")
	print(player_hand.get_four_ofa_kind())

	print("Score:")
	print(player_hand.get_score())



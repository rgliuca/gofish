from blackjack import *

class GoFishHand:
    CARD_RANK = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, player_name="", cards=[]):
        # You need to keep track of two things in this class:
        #   1. the cards in this hand
        #   2. the rank of (4 of a kind, cards with the same values)  You can 
        #     compute the score from this.
        pass
    
    def remove_rank_cards(self, rank):
        # removes cards with the given rank from this "hand" and returns
        # the cards as a list to the caller
        # If there aren't any cards with the given rank, then return an
        # empty list
        pass
    
    def add_cards(self, cards):
        # cards is a list
        # Just like in BJHand, add cards to this "hand" but with an additional
        # function of checking if you have the full suit of a given rank
        pass

    def get_score(self):
        # returns the number of four a kind this hand has
        pass
    
    def get_four_ofa_kind(self):
        # returns a list of the 4 of a kind in this "hand", you can just return
        # a list of the ranks of these four a kind
        # you can use Card.get_value() for the rank value 
        pass
    
    def print(self, col_size=5, show_all_cards=True):
        # prints the cards in hand
        pass
               
if __name__ == "__main__":
  cards = CardDeck()
  cards.shuffle()
  cards.deal_card().print()

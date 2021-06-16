from blackjack import *

class GoFishHand:
    CARD_RANK = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, cards=[]):
        # You need to keep track of two things in this class:
        #   1. the cards in this hand
        #   2. the rank of (4 of a kind, cards with the same values)  You can 
        #     compute the score from this.  Use a list to keep track of the ranks
        #     You can use this member variable: self._four_ofa_kinds = []
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
        # function of checking if you have the full suit of a given rank.  If 
        # four of a kind is found, remove these 4 cards from this “hand” and 
        # add the rank value to the self._four_ofa_kinds list
        pass

    def get_score(self):
        # returns the number of four a kind in this "hand".  Can get this info 
        # from self._four_ofa_kinds list
        pass
    
    def get_four_ofa_kind(self):
        # Returns a list of four of a kind in this “hand”.  You can just return 
        # the list self._four_ofa_kinds
        pass
    
    def print(self, col_size=5, show_all_cards=True):
        # prints the cards in hand
        pass
    
    def get_num_cards(self):
        # return the number of cards in "hand"
        pass
    
class GoFishHumanPlayer():
    def __init__(self, name, cards):
        pass
    
    def fish_from_players(self, other_players):
        # get input from the user to pick its rank card and a computer player id
        pass

class GoFishComputerPlayer():
    next_computer_player_id = 1
    
    def __init__(self, cards):
        # This init method has the following functionalities: 
        # 1. Create a “name” for the computer player.  This will require a class 
        #    variable which is a player_id (valid id: 1, 2, 3 depending on the 
        #    number of computer players).  Use the variable self._name  
        #   Examples of a valid computer player name:
        #   “Computer Player #1”, “Computer Player #2”, etc.
        # 2. Create a “GoFishHand” object for the computer player and add the cards 
        #  (list of poker Card types) to this hand.  Use self._hand
        pass
    
    @property
    def name(self):
        return self._name

    def fish_from_players(self, other_players):
        # randomly pick a player from other_players and randomly pick a rank value from 
        # this computer player's hand and return the result as a tuple: 
        # (player, rank value)
        pass
        
if __name__ == "__main__":
  cards = CardDeck()
  cards.shuffle()
  cards.deal_card().print()


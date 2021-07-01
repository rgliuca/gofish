from pokercards import *

class GoFishHand:
    CARD_RANK = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, cards=[]):
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

    def get_num_cards(Self):
        # return the number of cards in "hand"
        pass
               
class GoFishHumanPlayer:
    def __init__(self, name, cards):
        self._name = name
        self._hand = GoFishHand(name, cards)

    def fish_from_player(self, other_players):
        # other_player is a list of GoFishComputerPlayer type
        # This method will print the name of the computer players
        # and then ask the human player to "input" which computer
        # to fish the rank card from
        #
        # This method will also ask the user to "input" which of his rank 
        # cards (rank value) to fish from the selected GoFishComputer player
        # return a tuple of (GoFishComputerPlayer, rank value)
        pass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def fish(self, rank):
        # This method is called by another player (GoFishComputer or GoFishHumanPlayer)
        # to extract a list of cards (with the given "rank" value)
        # Notice, this method simply calls self._hand.remove_rank_cards()
        return self._hand.remove_rank_cards(rank) 

    def print(self):
        self._hand.print(show_all_cards=True)

    def play(self, other_players, deck):
        # other players is a list of players 
        # cards is a CardDeck, passed in by the main program

        # returns True if this player has made a play, False if the hand is
        # empty and the deck is empty

        print("********************")
        print(f"{self._name} playing...")
        print("********************")

        while True:
            pass

class GoFishComputerPlayer:
    next_computer_player_id = 1

    def __init__(self, cards):
        self._id = __class__.next_computer_player_id
        __class__.next_computer_id += 1

        self._name = f"Computer Player #{self._id}"
        self._hand = GoFishHand(self._name, cards)

    def fish_from_player(self, other_players):
        # other_player is a list of GoFishComputerPlayer or GoFishHumanPlayer
        # types.  This method will randomly pick a player from other_players 
        # list and randomly pick a rank from this computer player's 
        # hand (GoFishHand class) and return the result as a tuple:
        # (GoFishHumanPlayer/GoFishComputerPlayer, rank value)
        pass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def fish(self, rank):
        # This method is called by another player (GoFishComputer or GoFishHumanPlayer)
        # to extract a list of cards (with the given "rank" value)
        # Notice, this method simply calls self._hand.remove_rank_cards()
        return self._hand.remove_rank_cards(rank) 

    def print(self):
        self._hand.print(show_all_cards=False)

    def play(self, other_players, deck):
        # other players is a list of players 
        # cards is a CardDeck, passed in by the main program

        # returns True if this player has made a play, False if the hand is
        # empty and the deck is empty

        print("********************")
        print(f"{self._name} playing...")
        print("********************")

        while True:
            pass


if __name__ == "__main__":
  cards = CardDeck()
  cards.shuffle()
  cards.deal_card().print()



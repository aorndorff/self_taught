
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"] #Class Variable

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] #Class Variable.  None and none are there so the string list correlates with the numbers

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v # Instance Variable
        self.suit = s # Instance Variable
        # Instance variables represent the kind of card the Card object is.
        # Create and object, pass it parameters - Card(2, 1) = 2 of Hearts
    
    def __lt__(self, c2): # __lt__ magic method that allows you to compare 2 card objects in an expression using <, >, and ==
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < cs.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True 
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self): # __repr__ magic method cuased value and suit instance variables to look up the value and suit of the card in the lists and returns them so you can print a card
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]

        return v
card1 = Card(2, 2)
card2 = Card(11, 3)

print(card1 < card2)
print(card1 > card2)
print(card1 == card2)

card3 = Card(8, 3)
print(card3)

print(card1)
print(card2)

#-----------------------------------------------------------------------------------------------------------
# Define a calss to represent a deck of cards

from random import shuffle

class Deck: #Object
    def __init__(self):
        self.cards = []
        for i in range (2, 15): # 2 to Ace, with 2 "none" at the beginning
            for j in range(4): # Each Suit
                self.cards\
                    .append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self): # rm_card a method that removes and returns a card from teh cards list, or returns NONE if its empty.  You can use the Deck class to create a new deck of cards and print each one
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck1 = Deck()
for card in deck1.cards:
    print(card)
deck2 = Deck()
print("-----------------------------------------------------------")
for card in deck2.cards:
    print(card)

#-----------------------------------------------------------------------------------------------------------
# Define a class to represent a Player

class Player:
    def __init__(self, name):
        self.wins = 0 # Instance variable keeps track of how many rouns a player has won
        self.card = None # Instance variable representing the card a player is currently holing
        self.name = name # Instance variable to keep track of player's name

#-----------------------------------------------------------------------------------------------------------
# Define a class to represent The Game
class Game:
    def __init__(self): # Init is a method
        name1 = input("Player 1 name:")
        name2 = input("Player 2 name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!!!")
        while len(cards) >= 2:
            m = "q to quit. Any " +\
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over.  {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie."

game = Game()
game.play_game()




        
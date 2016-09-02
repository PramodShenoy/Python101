import random

class Card(object):

    """docstring for Card"""
    def __init__(self, suit, rank):         # can set default value here
        super(Card, self).__init__()
        self.suit = suit
        self.rank = rank

    card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_ranks = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    """printing string instead of returning
    def __str__(self):
    	print 'dealing with a %s of %s' % (Card.card_ranks[self.rank], Card.card_suits[self.suit])
    """

    def __str__(self):
    	return '%s of %s' % (Card.card_ranks[self.rank], Card.card_suits[self.suit])

    def __cmp__(self, other):
        if self.suit < other.suit:
        	return -1
        if self.suit > other.suit:
        	return 1
        if self.rank < other.rank:
        	return -1
        if self.rank > other.rank:
        	return 1
        return 0
    
    """comparison using tuples
    def __cmp__(self, other):
    	c1 = self.suit, self.rank
    	c2 = other.suit, other.rank
    	return cmp(c1, c2)
    """


class Deck(object):

	"""docstring for Deck, create deck of initial 52 cards"""
	def __init__(self):
		super(Deck, self).__init__()
		self.cards = []
		for suit in range(4):
			for rank in range(14):
				card = Card(suit, rank)
				self.cards.append(card)
	
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		return self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

    # move cards from the deck into the hand
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())


class Hand(Deck):

	"""docstring for Hand"""
	def __init__(self, label = ''):      # init wiith default label of ''
		super(Hand, self).__init__()
		self.cards = []
		self.label = label

queen_of_diamonds = Card(1, 12)
queen_of_diamonds.__str__()

# card_assigned = queen_of_diamonds.__str__()
# print card_assigned

ace_of_hearts = Card(2, 2)
ace_of_hearts.__str__()

x = ace_of_hearts.__cmp__(queen_of_diamonds)
print 'returned value %d' % x

deck = Deck()
#print deck

hand = Hand('new hand')
print hand.cards
print 'label ' + hand.label

# remove one card from deck, which one will be removed
card = deck.pop_card()

#re-insert same card to deck
hand.add_card(card)
print hand

deck.move_cards(hand, 5)
#print deck

#print hand
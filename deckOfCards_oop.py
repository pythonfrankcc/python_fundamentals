#oop and debugging
import pdb
import random
#inheriting from object
#establishing the starting point of the debugger but cannot be used in situations with classe only runs after 
#classes are called
#pdb.set_trace()
class Card(object):
	def __init__(self,suit,val):
	#creating methods of the Card class
		self.suit=suit
		self.value=val
	#everything takes self thus we can take it for the next method
	def show(self):
		print ('{} of {}'.format(self.value,self.suit))


class Deck(object):
	def __init__(self):
		self.card=[]
		self.build()
	#build a deck now lets call the method below
	def build(self):
		for s in ['Spades','Clubs','Diamonds','Hearts']:
			#exclusive of 14 in the range
			for v in range(1,14):
				#lets now append the cards in the deck to the cards
				#we add each of these cards to the cards list but we want to add an instance of Card class
				self.card.append(Card(s,v))
				print ('{} of {}'.format(v,s))
	#creating a method to test this
	def show(self):
		for c in self.card:
			c.show()
	#we should be able to shuffle our deck
	def shuffle(self):
#trying to implement the fisher yates algorithm
#all the cards and in a decreementing order to zero 
#when accessing elements in an array we subtract one for the elements start at an index 0
		for i in range(len(self.card)-1 , 0, -1):
#you only want to pick up a random interger that is to the left of the item
			r = random.randint(0, i)
			#you want to shuffle two cards and that is the one in  i and the one in r
			self.card[i],self.card[r] = self.card[r],self.card[i]
#next is to be able to draw a card from the guy
#return whatever card that the method draw calls
	def draw(self):
		return self.card.pop()
#without specifying the index the last which is our first card is popped


class Player(object):
	def __init__(self,hand):
		self.name=[]
		self.hand=[]
	def draw(self,deck):
		self.hand.append(deck.DrawCard())
	def showhand(self):
		for card in self.hand:


#creating an instance to do the testing'''
deck = Deck()
deck.shuffle()
card = deck.draw()
card.show()

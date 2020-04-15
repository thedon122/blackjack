import random
class card:
    def __init__(self, color, rank, value):
        self.color = color
        self.rank = rank
        self.value = value

class deck:
    def __init__(self, cardDeck):
        self.cardDeck = cardDeck
    # create a deck of 51 cards
    def createDeck(self):
        i = 1
        c = 'Red Diamonds'
        r = '1'
        for index in range(51):
            if index < 8:
                i = index + 2
                c = 'Red Diamonds'
                r = str(i)
            elif index >= 8 and index < 17:
                i = index - 6
                c = 'Red Hearts'
                r = str(i)
            elif index >= 17 and index < 26:
                i = index - 15
                c = 'Black Clubs'
                r = str(i)
            elif index >= 26 and index < 35:
                i = index - 24
                c = 'Black Spades'
                r = str(i)
            elif index >= 35 and index < 39:
                i = 10
                r = 'Jack'
            elif index >= 39 and index < 43:
                i = 10
                r = 'Queen'
            elif index >= 43 and index < 47:
                i = 10
                r = 'King'
            elif index >= 47 and index <= 51:
                i = 'ask user'
                r = 'Ace'
            if index in range(34, 51, 3):
                c = 'Black Clubs'
            if index in range(34, 51, 4):
                c = 'Black Spades'
            if index in range(34, 51, 2) and index not in range(34, 51, 4):
                c = 'Red Hearts'
            if index in range(34, 51, 1) and index not in range(34, 51, 3) and index not in range(34, 51, 2):
                c = 'Red Diamonds'
            self.cardDeck.append(card(c, r, i))
        return self.cardDeck
    def randomizeDeck(self):
        return random.shuffle(self.cardDeck)
    def showDeck(self):
        for index in range(51):
            print(self.cardDeck[index].color, self.cardDeck[index].rank, self.cardDeck[index].value)
class hand():
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
    def startHand(self, cardDeck):
        for index in range(2):
            self.cardsInHand.append(cardDeck[index])
            cardDeck.remove(cardDeck[index])
        
    def hit(self, cardDeck):
        self.cardsInHand.append(cardDeck[0])
        cardDeck.remove(cardDeck[0])
        
    def showCards(self):
        for index in range(len(self.cardsInHand)):
            print(self.cardsInHand[index].color, self.cardsInHand[index].rank)
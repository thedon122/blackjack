import random
class card():
    # create a card object
    def __init__(self, color, rank, value):
        self.color = color
        self.rank = rank
        self.value = value

class deck():
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
    # creates a hand object
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
    def startHand(self, cardDeck):
    # creats a hand of 2 cards
        for index in range(2):
            self.cardsInHand.append(cardDeck[index])
            cardDeck.remove(cardDeck[index])
        
    def hit(self, cardDeck):
        self.cardsInHand.append(cardDeck[0])
        cardDeck.remove(cardDeck[0])
        
    def showCards(self):
    # show cards in hand
        for index in range(len(self.cardsInHand)):
            print(self.cardsInHand[index].color, self.cardsInHand[index].rank)
pM = [0]
pS = [0,0,0]
while True:
    try:
        pM = int(input("How much money does the player have: "))
    except ValueError:
        print('Invalid entery try again')
        continue
    else:
        break
def startNewGame():
    # creates and randomize deck also creates player and computer hand
    d = deck([])
    d.createDeck()
    d.randomizeDeck()
    pH = hand([])
    cH = hand([])
    pH.startHand(d.cardDeck)
    cH.startHand(d.cardDeck)
    game = ''
    return [d,pH,cH,game]

def playerTurn(pH,d,game):
    print('Player turn')
    pH.showCards()
    # loop for hits breaks if stay or game over
    while True:
        for idx in range(len(pH.cardsInHand)):
            if pH.cardsInHand[idx].value == 'ask user':
                pH.cardsInHand[idx].value = int(input("plase enter 1 or 11 for this ace \n"))
        value = sum([pH.cardsInHand[idx].value for idx in range(len(pH.cardsInHand))])
        if value > 21:
            game = 'lose'
            print('You lose')
            break
        elif value == 21:
            game = 'win'
            print('You win')
        while True:
            pI = (input("Do you want to hit or stay \n")).lower()
            if pI == 'hit' or pI == 'stay':
                break
            else:
                print('Invalid entry try again')
                continue
        if pI == 'hit' and d.cardDeck:
            pH.hit(d.cardDeck)
            pH.showCards()
            continue
        elif pI == 'stay':
            break
    return [pH,d,value,game]

def computerTurn(pValue,cH,d,game):
    print('computer turn')
    cH.showCards()
    # loop for hits breaks if stay or game over
    while True:
        for idx in range(len(cH.cardsInHand)):
            if cH.cardsInHand[idx].value == 'ask user':
                cH.cardsInHand[idx].value = int(input("plase enter 1 or 11 for this ace \n"))
        value = sum([cH.cardsInHand[index].value for index in range(len(cH.cardsInHand))])
        if value < 16:
            cH.hit(d.cardDeck)
            if value > 21:
                cH.showCards()
                game = 'win'
                print('You win')
                break
            elif value == 21:
                cH.showCards()
                game = 'lose'
                print('You lose')
                break
            continue
        if pValue > value:
            cH.hit(d.cardDeck)
            if value > 21:
                cH.showCards()
                game = 'win'
                print('You win')
                break
            elif value == 21:
                cH.showCards()
                game = 'lose'
                print('You lose')
                break
            continue
        if pValue < value:
            cH.showCards()
            break
    return [cH,d,value,game]

def blackJackGame(pS):
    while True:
        [d,pH,cH,game]= startNewGame()
        while game == '':
            [pH,d,pValue,game] = playerTurn(pH,d,game)
            if game != '':
                break
            [cH,d,value,game] = computerTurn(pValue,cH,d,game)
            if game != '':
                break
        if game == 'win':
            pS[0] += 1
            pS[2] += pM[0]
        elif game == 'lose':
            pS[1] += 1
            pS[2] -= pM[0]
        while True:
            pI = (input("Do you want to hit or stay \n")).lower()
            if pI == 'yes' or pI == 'no' or pI == 'y' or pI == 'n':
                break
            else:
                print('Invalid entry try again')
                continue 
        if pI == 'yes' or 'y':
            continue
        elif pI == 'no' or 'n':
            break

blackJackGame(pS)
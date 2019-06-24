import random
##
##def get_players():
##    players = int(input('Podaj liczbe graczy(1-7): '))
##    list_of_players = ['Rozdajacy']
##    for i in range(players):
##        player = input('Podaj nazwe gracza: ')
##        list_of_players.append(player)
##    return list_of_players
##
##class Talia:
##    cards = ['2s', '2d', '2h', '2c', '3s', '3d', '3h', '3c', '4s', '4d', '4h', '4c', '5s', '5d', '5h', '5c',
##             '6s', '6d', '6h', '6c', '7s', '7d', '7h', '7c', '8s', '8d', '8h', '8c', '9s', '9d', '9h', '9c',
##             '10s', '10d', '10h', '10c', 'Js', 'Jd', 'Jh', 'Jc', 'Qs', 'Qd', 'Qh', 'Qc',
##             'Ks', 'Kd', 'Kh', 'Kc', 'As', 'Ad', 'Ah', 'Ac']
##
##
##player = get_players()
##
##def print_game():
##    counter = len(player)
##    i = 1
##    while i < counter:
##        print(player[i], ':\t', random.choice(cards), '\t', random.choice(cards))
##        i +=1
##    print(player[0], ':\t', random.choice(cards), '\t', random.choice(cards))
##print_game()

###################################################################################################################################

class Card(object):
  """ Karta do gry. """
  RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  SUITS = ["c", "d", "h", "s"]

  def __init__(self, rank, suit):
      self.rank = rank
      self.suit = suit

  def __str__(self):
      rep = self.rank + self.suit
      return rep

class Hand(object):
  """ Ręka - karty do gry w ręku gracza. """
  def __init__(self):
      self.cards = []

  def __str__(self):
      if self.cards:
          rep = ""
          for card in self.cards:
              rep += str(card) + " "
      else:
          rep = "<pusta>"
      return rep

  def clear(self):
      self.cards = []

  def add(self, card):
      self.cards.append(card)

  def give(self, card, other_hand):
      self.cards.remove(card)
      other_hand.add(card)


class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")


class Unprintable_Card(Card):
  """ Karta, której ranga i kolor nie są ujawniane przy jej wyświetleniu. """
  def __str__(self):
        return "<utajniona>"

class Positionable_Card(Card):
  """ Karta, która może być odkryta lub zakryta. """
  def __init__(self, rank, suit, face_up = True):
    super(Positionable_Card, self).__init__(rank, suit)
    self.is_face_up = face_up
  def __str__(self):
    if self.is_face_up:
      rep = super(Positionable_Card, self).__str__()
    else:
      rep = "XX"
    return rep
  def flip(self):
    self.is_face_up = not self.is_face_up

  
def random_card():
    card = Card(rank = random.choice(Card.RANKS), suit = random.choice(Card.SUITS))
    return card



def get_players():
    players = int(input('Podaj liczbe graczy(1-7): '))
    list_of_players = []
    for i in range(players):
        player = input('Podaj nazwe gracza: ')
        list_of_players.append(player)
        #player = Hand()
    list_of_players.append('Rozdajacy')    
    return list_of_players



players = get_players()

def make_player():
    hands = []
    for i in players:
        i = Hand()
        hands.append(i)
    return hands
        
hands = make_player()


deck1 = Deck()
deck1.populate()
deck1.shuffle()
deck1.deal(hands, per_hand = 2)




def ask_to_card(i):
    dec = input(str(players[i]) + ', masz ' + str(count(i)) + ' pkt, chcesz dobrac karte?(T/N): ')
    if dec.upper() == 'T':
        card = random_card()
        hands[i].add(card)
        #counter
        print_card(i)
        #ask_to_card(i)
    else:
        return False
    

def print_card(i):
    x = count(i)
    print('{:15s} {:15} < {:2d} >'.format(players[i], str(hands[i]), x))



def count(i):
    x = str(hands[i])
    xx = len(x)
    suma = 0
    liczby = []
    counter = 3
    for i in range(xx):
      if x[i] == 'A':
          liczby.append(11)
      elif x[i] == 'K':
          liczby.append(10)
      elif x[i] == 'Q':
          liczby.append(10)
      elif x[i] == 'J':
          liczby.append(10)
      elif x[i] == '1':
          liczby.append(10)
      elif x[i] in Card.RANKS:
          liczby.append(int(x[i]))
          
      #liczby.append(int(x[len(players)]))
    for i in liczby:
      suma = suma + i
    return suma

def show_dealer():    
  y = str(hands[2])
  for i in range(2):
    l1 = y[i]
    y = y.replace(l1, 'X')
  #print(players[2],  ':\t', y, '\t< XX >')
  print('{:15s} {:15} < {:2s} >'.format(players[2], y , 'XX'))
    


def main():          
  for i in range(len(players) - 1):
      print_card(i)
  dealer = show_dealer()


  for i in range(len(players) - 1):
      #ask_to_card(i)
      x = count(i)
      while x <= 21:
        var = ask_to_card(i)
        if var == False:
          break
        else:
          x = count(i)
      else:
        print('FURA')

  x = count(-1)
  while x < 17:
    new = random_card()
    hands[-1].add(new)
    x = count(-1)

  if x <= 21:
    print_card(-1)
  else:
    print_card(-1)
    print('FURA')


##  for i in range(len(players)):
##    print_card(i)
  score = 0
  winner = ''
  for i in range(len(players)):
    x = count(i)
    if 21 >= x > score:
      score = x
      winner = players[i]
  if count(-1) > 21:
    print('Wszyscy wygrywaja')
  else:
    print('Wygrywa', winner, 'z wynikiem ', score)
main()



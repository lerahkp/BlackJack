############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

def calculate_score(card_list):
  cs=sum(card_list)
  if cs==21 and len(card_list)==2:
    return 0
  elif 11 in card_list and cs > 21:
    ind=card_list.index(11)
    card_list.pop(ind)
    card_list.append(1)
  else:
    return cs

def play():
  
  print(logo)

  user_cards=[]
  computer_cards=[]
  continue_game=True

  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while continue_game:
    user_cards_sum=calculate_score(user_cards)
    computer_cards_sum=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, score: {user_cards_sum}\n Computer's first card: {computer_cards[0]}")

    if user_cards_sum==0 or computer_cards_sum==0 or user_cards_sum > 21:
      continue_game=False
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card=='y':
        dc=deal_card()
        user_cards.append(dc)
      else:
        continue_game=False
  while computer_cards_sum < 17:
    cv = deal_card()
    computer_cards.append(cv)
    calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
  print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
  print(compare(user_sum=calculate_score(user_cards),computer_sum=calculate_score(computer_cards)))


def compare(user_sum,computer_sum):
  if user_sum == computer_sum:
    return("Draw, both have same score")
  elif computer_sum==0:
    return("Computer has BlackJack, Winner Winner Chicken Dinner")
  elif user_sum==0:
    return("You have BlackJack, Winner Winner Chicken Dinner")
  elif user_sum>21:
    return("You lose, you went over 21; Computer wins")
  elif computer_sum>21:
    return("You win, Computer's score is over 21; Computer loses")
  else:
    d={'User': user_sum, 'Computer': computer_sum}
    high_value = max(d, key=d.get)
    return(f"{high_value} wins")


while input("\nDo you want to play blackjack? Type 'y' or 'n':  ") == 'y':
  clear()
  play()

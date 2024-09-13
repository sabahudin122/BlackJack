import random

def deal_card():
    """RETURN RANDOM CARD FROM THE DECK"""
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(card)
    return card

def calculate_score(cards):
    """TAKE A LIST OF CARDS AND RETURN THE SCORE CALCULATED FROM CARDS"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 😑"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack 😰 "
    elif user_score == 0:
        return "You have WON 😀"
    elif user_score > 21:
        return "You went over, You LOST 😰"
    elif computer_score > 21:
        return "Opponent went over; BOOHOO you get money 😋"
    elif user_score > computer_score:
        return "You have won 😀"
    elif computer_score > user_score:
        return "Opponent won 😰 "
    else:
        return "You lose 😭 "
def play_game():
    user_cards = []  
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    """KOMPJUTERSKI DIO PROGRAMA"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your fintal hand: {user_cards}, final score: {user_score}")
    print(f"Computers final hand is:{computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == "y" :
    print("\n" * 20)
    play_game()
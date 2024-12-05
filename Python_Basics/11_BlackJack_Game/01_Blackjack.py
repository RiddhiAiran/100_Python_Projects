from logo import first
import random 

print(first)

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

def calculate_score(hand):
    # Handle Ace (11) special case
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_scores(user_score, dealer_score):
    if user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win 😄"
    elif user_score == dealer_score:
        return "Draw 🙃"
    elif user_score == 21:
        return "Blackjack! You win 🎉"
    elif dealer_score == 21:
        return "Dealer has Blackjack. You lose 😭"
    elif user_score > dealer_score:
        return "You win 😄"
    else:
        return "You lose 😭"

def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    while play == 'y':
        # Initialize game
        user_cards = []
        dealer_cards = []
        game_over = False

        # Deal initial cards
        for _ in range(2):
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))

        # User's turn
        while not game_over:
            # Calculate current scores
            user_score = calculate_score(user_cards)
            dealer_score = calculate_score(dealer_cards)

            # Display current game state
            print(f"\nYour cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {dealer_cards[0]}")

            # Check if user should stop
            if user_score == 21 or user_score > 21:
                game_over = True
            else:
                # Ask user to hit or stand
                hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                
                if hit == 'y':
                    user_cards.append(random.choice(cards))
                else:
                    # Dealer's turn
                    while dealer_score < 17:
                        dealer_cards.append(random.choice(cards))
                        dealer_score = calculate_score(dealer_cards)
                    game_over = True

        # Final results
        print(f"\nYour final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
        
        # Determine winner
        result = compare_scores(calculate_score(user_cards), calculate_score(dealer_cards))
        print(result)

        # Ask to play again
        play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()

# Run the game
blackjack()
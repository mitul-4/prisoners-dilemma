import random

def prisoners_dilemma_game(rounds):
    # Initialize scores
    john_score = 0
    jane_score = 0

    # Define possible choices
    choices = ['C', 'D']

    print(f"Playing {rounds} rounds of Prisoner's Dilemma!\n")
    
    for round_number in range(1, rounds + 1):
        # Randomly choose actions for each player
        john_choice = random.choice(choices)
        jane_choice = random.choice(choices)

        # Calculate scores based on the rules
        if john_choice == 'C' and jane_choice == 'C':
            john_score += 3
            jane_score += 3
        elif john_choice == 'C' and jane_choice == 'D':
            jane_score += 5
        elif john_choice == 'D' and jane_choice == 'C':
            john_score += 5
        elif john_choice == 'D' and jane_choice == 'D':
            john_score += 1
            jane_score += 1

        # Display round results
        # print(f"Round {round_number}:")
        # print(f"  John chose {john_choice}, Jane chose {jane_choice}")
        # print(f"  Current Scores -> John: {john_score}, Jane: {jane_score}\n")

    # Determine the winner
    print("Game Over!")
    print(f"Final Scores -> John: {john_score}, Jane: {jane_score}")
    if john_score > jane_score:
        print("John wins!")
    elif jane_score > john_score:
        print("Jane wins!")
    else:
        print("It's a tie!")

rounds_to_play = int(input("Enter the number of rounds to play: "))
prisoners_dilemma_game(rounds_to_play)
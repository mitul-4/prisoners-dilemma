import random

# Define the bots' strategies
def tit_for_tat(history):
    return 'C' if not history or history[-1] == 'C' else 'D'

def always_cooperate(history):
    return 'C'

def always_defect(history):
    return 'D'

def random_choice(history):
    return random.choice(['C', 'D'])

def generous_tit_for_tat(history):
    if not history or history[-1] == 'C':
        return 'C'
    return 'C' if random.random() < 0.1 else 'D'

def grim_trigger(history):
    return 'C' if 'D' not in history else 'D'

def win_stay_lose_shift(history):
    if not history or (len(history) > 1 and history[-2] == history[-1]):
        return 'C'
    return 'D'

def tit_for_two_tats(history):
    if len(history) < 2 or history[-2:] == ['C', 'C']:
        return 'C'
    return 'D'

# Define bot configurations
bots = {
    "Tit-for-Tat": tit_for_tat,
    "Always Cooperate": always_cooperate,
    "Always Defect": always_defect,
    "Random": random_choice,
    "Generous Tit-for-Tat": generous_tit_for_tat,
    "Grim Trigger": grim_trigger,
    "Win-Stay, Lose-Shift": win_stay_lose_shift,
    "Tit-for-Two-Tats": tit_for_two_tats
}


#------------------------------------------------------------------------------------


# Define the scoring rules
def calculate_scores(move1, move2):
    if move1 == 'C' and move2 == 'C':
        return (3, 3)
    elif move1 == 'C' and move2 == 'D':
        return (0, 5)
    elif move1 == 'D' and move2 == 'C':
        return (5, 0)
    elif move1 == 'D' and move2 == 'D':
        return (1, 1)

# Simulate a match between two bots
def simulate_match(bot1, bot2, rounds):
    history1, history2 = [], []
    score1, score2 = 0, 0

    for _ in range(rounds):
        move1 = bot1(history2)  # Bot1 decides based on Bot2's history
        move2 = bot2(history1)  # Bot2 decides based on Bot1's history
        
        # Update scores
        round_score1, round_score2 = calculate_scores(move1, move2)
        score1 += round_score1
        score2 += round_score2

        # Update histories
        history1.append(move2)
        history2.append(move1)

    return score1, score2

# Run the round-robin tournament
def axelrod_tournament(rounds_per_match):
    results = {bot: 0 for bot in bots}

    # Iterate through each pair of bots
    for bot1_name, bot1_func in bots.items():
        for bot2_name, bot2_func in bots.items():
            if bot1_name != bot2_name:
                # print(f"Match: {bot1_name} vs {bot2_name}")
                score1, score2 = simulate_match(bot1_func, bot2_func, rounds_per_match)
                # print(f"  {bot1_name} Score: {score1}, {bot2_name} Score: {score2}\n")
                results[bot1_name] += score1
                results[bot2_name] += score2

    # Display tournament results
    print("Tournament Results:")
    for bot, score in results.items():
        print(f"  {bot}: {score} points")
    print("\nWinner:", max(results, key=results.get))

# Run the tournament
rounds_per_match = int(input("Enter the number of rounds per match: "))
axelrod_tournament(rounds_per_match)
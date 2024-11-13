# Axelrod's Tournament Simulation

This is a Python implementation of an Axelrod-style tournament, where bots compete in a simulation of Prisoner's Dilemma! Each bot follows a predefined strategy to decide whether to cooperate (C) or defect (D) in each round, earning points based on the outcome of the interaction.

The game demonstrates how different strategies perform against each other, highlighting concepts like cooperation, retaliation, and forgiveness in game theory.

Might make this into a website game in the future 😅


## How to Play

1. **Install Python**  
   Ensure Python 3.x is installed on your computer.

2. **Run the Program**  
   Save the game code in a file named `game.py`, and run it using the following command in your terminal:
   ```bash
   python game.py
   ```

3. **Choose the Number of Rounds**
   When prompted, enter the number of rounds for each match. For example, to simulate a tournament where each pair of bots plays 100 rounds:
   ```sql
   Enter the number of rounds per match: 100
   ```

4. **View Results**
   After all matches are played, the program displays:
    * The total scores of each bot across all matches.
    * The overall winner of the tournament.


## Scoring System

* If both bots cooperate, they each get 3 points.
* If one cooperates while the other defects, the defector gets 5 points & the cooperator gets 0 points.
* If both bots defect, they each get 1 point.

## Bots and Their Strategies
Here’s a breakdown of the characteristics of the bots included:

### Tit-for-Tat
* Behavior: Starts by cooperating. Mirrors the opponent's last move.
* Strengths: Encourages mutual cooperation, retaliates against defection, and forgives immediately.
* Weaknesses: Struggles against Always Defect and exploitative strategies.

### Always Cooperate
* Behavior: Always cooperates, no matter what the opponent does.
* Strengths: Builds mutual cooperation if paired with cooperative bots.
* Weaknesses: Easily exploited by defectors, scoring very poorly against them.

### Always Defect
* Behavior: Always defects, no matter what the opponent does.
* Strengths: Exploits cooperative bots like Always Cooperate and Random.
* Weaknesses: Performs poorly against retaliatory strategies like Tit-for-Tat and Grim Trigger.

### Random
* Behavior: Randomly chooses `C` or `D` with equal probability.
* Strengths: Unpredictable, making it harder for deterministic strategies to exploit.
* Weaknesses: Lacks consistency, struggles to build long-term cooperation.

### Generous Tit-for-Tat
* Behavior: Similar to Tit-for-Tat but occasionally forgives defection (10% chance).
* Strengths: Performs well in noisy environments or against strategies that occasionally defect by mistake.
* Weaknesses: Slightly exploitable by Always Defect due to its forgiving nature.

### Grim Trigger
* Behavior: Starts with cooperation. Defects permanently after the opponent defects even once.
* Strengths: Strong deterrent against defection, encourages cooperation from the opponent.
* Weaknesses: Highly unforgiving, leading to mutual defection if mistakes occur.

### Win-Stay, Lose-Shift
* Behavior: Cooperates if the last round’s outcome was good (e.g., mutual cooperation or exploitation). Switches to defecting if the outcome was bad.
* Strengths: Adaptive, performs well in noisy environments.
* Weaknesses: Can fall into defection cycles against aggressive opponents.

### Tit-for-Two-Tats
* Behavior: Cooperates unless the opponent defects twice in a row.
* Strengths: More forgiving than Tit-for-Tat, making it robust in noisy environments.
* Weaknesses: Vulnerable to extended exploitation by defectors.

## Example Output

Input:
```sql
Enter the number of rounds per match: 100
```

Output:
```yaml
Tournament Results:
  Tit-for-Tat: 1203 points
  Always Cooperate: 900 points
  Always Defect: 1301 points
  Grim Trigger: 1050 points
  Random: 950 points
  Generous Tit-for-Tat: 1100 points
  Win-Stay, Lose-Shift: 1150 points
  Tit-for-Two-Tats: 1170 points

Winner: Always Defect
```

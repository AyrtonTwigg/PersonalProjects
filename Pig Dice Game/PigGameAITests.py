import random
import PigAI1 as AI1
import PigAI2 as AI2

NUM_GAMES = 100000
WIN_SCORE = 100
player1_wins = 0
player2_wins = 0


for _ in range(NUM_GAMES):
    player1_total = 0
    player2_total = 0
    turn = random.choice([1,-1])

    while player1_total < WIN_SCORE and player2_total < WIN_SCORE:
        if turn > 0:
            player1_total += AI1.Move(player1_total, player2_total, WIN_SCORE)
            turn *= -1
        else:
            player2_total += AI2.Move(player2_total, player1_total, WIN_SCORE)
            turn *= -1

    if player1_total >= WIN_SCORE:
        player1_wins += 1
    elif player2_total >= WIN_SCORE:
        player2_wins += 1

print("AI1 win precentage: %.3f%%" %(player1_wins/NUM_GAMES*100))
print("AI2 win precentage: %.3f%%" %(player2_wins/NUM_GAMES*100))

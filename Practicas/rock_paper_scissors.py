'''
Let's play! You have to return which player won! In case of a draw return Draw!.

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

def rps(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    
    if p1 == p2:
        return "Draw!"
    
    elif ((p1.startswith("r") and p2.startswith("s")) or
        (p1.startswith("s") and p2.startswith("p")) or
        (p1.startswith("p") and p2.startswith("r"))):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
 
    
print(rps('rock', 'scissors'))
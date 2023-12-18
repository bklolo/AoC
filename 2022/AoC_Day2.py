""" Part I
A, X : Rock       :   1
B, Y : Paper      :   2
C, Z : Scissors   :   3
"""


def CalcTotalScore(file):
    points = {
        'AX': 4,
        'AY': 8,
        'AZ': 3,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 7,
        'CY': 2,
        'CZ': 6
    }
    score = 0
    x = file.read().split("\n")
    for item in x:
        case = item.replace(' ', "")
        score += points[case]
    return score


""" Part II
A : R(1)
B : P(2)
C : S(3)   
X : Lose    :   0 + pts_of_losing_play
Y : Draw    :   3pts
Z : Win     :   6 + pts_of_winning_play
"""
Moves = {
    'A':
        {'name': 'rock',
         'win': 2,  # paper
         'lose': 3,  # scissors
         'draw': 1
         },
    'B':
        {'name': 'paper',
         'win': 3,  # scissors
         'lose': 1,  # rock
         'draw': 2
         },
    'C':
        {'name': 'scissors',
         'win': 1,  # rock
         'lose': 2,  # paper
         'draw': 3
         }
}


def determineMove(file):
    points = 0
    x = file.read().split("\n")
    for item in x:
        case = item.split()
        opMove = case[0]
        myMove = case[1]
        # if lose
        if myMove == 'X':
            points += Moves[opMove]['lose']
        # if draw
        if myMove == 'Y':
            points += Moves[opMove]['draw'] + 3
        # if win
        if myMove == 'Z':
            points += Moves[opMove]['win'] + 6
    return points


f = open("AoC2.txt")
# ans1 = CalcTotalScore(f)
# print(ans1)

ans2 = determineMove(f)
print(ans2)

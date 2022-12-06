from typing import Tuple
from collections import namedtuple

INPUT_FILE = 'input.txt'

Round = namedtuple('Round', ('opponent', 'mine'))

SCORE_DATA = {
    'ROCK': {
        'points': 1,
        'aliases': Round('A', 'X')
    },
    'PAPER': {
        'points': 2,
        'aliases': Round('B', 'Y')
    },
    'SCISSORS': {
        'points': 3,
        'aliases': Round('C', 'Z')
    },
}


def get_round_results(choices: Round) -> Round:
    opponent_points = 0
    my_points = 0

    for _, value in SCORE_DATA.items():
        if choices.opponent == value['aliases'].opponent:
            opponent_points = value['points']
        
        if choices.mine == value['aliases'].mine:
            my_points = value['points']

    battle_score = opponent_points - my_points

    if battle_score == 0:
        return Round(opponent_points + 3, my_points + 3)

    elif battle_score == 1 or battle_score == -2:
        return Round(opponent_points + 6, my_points) 

    elif battle_score == -1 or battle_score == 2:
        return Round(opponent_points, my_points + 6)


def main():
    my_score = 0

    with open(INPUT_FILE, 'r', encoding='utf-8') as input:
        for round_choices in input:
            choices = round_choices.strip().split(' ')

            my_score += get_round_results(Round(choices[0], choices[1])).mine

    return my_score


if __name__ == '__main__':
    print(f'My Score: {main()}')

from collections import namedtuple

EncryptionKeys = namedtuple('EncryptionKeys', ('pt1', 'pt2'))

Round = namedtuple('Round', ('opponent', 'mine', 'result'))

RoundResults = namedtuple('RoundResults', ('defeat', 'draw', 'victory'))

INPUT_FILE = 'input.txt'

ENCRYPTION_KEYS = EncryptionKeys(pt1='my_choice', pt2='round_result')

ROUND_RESULTS = RoundResults(defeat='X', draw='Y', victory='Z')

SCORE_DATA = {
    'ROCK': {
        'points': 1,
        'pt1_aliases': {
            'opponent': 'A',
            'mine': 'X'
        },
        'pt2_aliases': {
            'opponent': 'A',
            'result': RoundResults(
                defeat='Z',
                draw='X',
                victory='Y',
            )
        },
    },
    'PAPER': {
        'points': 2,
        'pt1_aliases': {
            'opponent': 'B',
            'mine': 'Y'
        },
        'pt2_aliases': {
            'opponent': 'B',
            'result': RoundResults(
                defeat='X',
                draw='Y',
                victory='Z',
            )
        },
    },
    'SCISSORS': {
        'points': 3,
        'pt1_aliases': {
            'opponent': 'C',
            'mine': 'Z'
        },
        'pt2_aliases': {
            'opponent': 'C',
            'result': RoundResults(
                defeat='Y',
                draw='Z',
                victory='X',
            )
        },
    },
}


def main(encryption_key: EncryptionKeys):
    my_score = 0

    with open(INPUT_FILE, 'r', encoding='utf-8') as input:
        for round_choices in input:
            choices = round_choices.strip().split(' ')

            if encryption_key == ENCRYPTION_KEYS.pt1:
                my_score += get_round_results(
                    Round(opponent=choices[0], mine=choices[1], result=None),
                    encryption_key
                ).mine
            else:
                my_score += get_round_results(
                    Round(opponent=choices[0], mine=None, result=choices[1]),
                    encryption_key
                ).mine

    return my_score


def get_round_results(game_round: Round, encryption_key: EncryptionKeys) -> Round:
    opponent_points = 0
    my_points = 0
    my_choice = game_round.mine

    if encryption_key == ENCRYPTION_KEYS.pt2:
        my_choice = make_my_move(game_round)

    for _, value in SCORE_DATA.items():
        if game_round.opponent == value['pt1_aliases']['opponent']:
            opponent_points = value['points']

        if my_choice == value['pt1_aliases']['mine']:
            my_points = value['points']

    return calculate_round_score(opponent_points, my_points)


def make_my_move(game_round: Round) -> str:
    my_move = None

    for _, value in SCORE_DATA.items():
        if game_round.opponent == value['pt2_aliases']['opponent']:
            if game_round.result == ROUND_RESULTS.defeat:
                my_move = value['pt2_aliases']['result'].defeat

            elif game_round.result == ROUND_RESULTS.draw:
                my_move = value['pt2_aliases']['result'].draw

            elif game_round.result == ROUND_RESULTS.victory:
                my_move = value['pt2_aliases']['result'].victory
            
            break

    return my_move

def calculate_round_score(opponent_points: int, my_points: int) -> Round:
    battle_score = opponent_points - my_points

    round_score = 0

    if battle_score == 0:
        round_score = Round(
            opponent=opponent_points + 3,
            mine=my_points + 3,
            result=ROUND_RESULTS.draw
        )

    elif battle_score == 1 or battle_score == -2:
        round_score = Round(
            opponent=opponent_points + 6,
            mine=my_points,
            result=ROUND_RESULTS.defeat
        ) 

    elif battle_score == -1 or battle_score == 2:
        round_score = Round(
            opponent=opponent_points,
            mine=my_points + 6,
            result=ROUND_RESULTS.victory
        )

    return round_score


if __name__ == '__main__':
    print(f'My Score For Part 1: {main(ENCRYPTION_KEYS.pt1)}')
    print(f'My Score For Part 2: {main(ENCRYPTION_KEYS.pt2)}')

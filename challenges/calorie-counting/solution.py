from typing import Tuple

INPUT_FILE = 'input.txt'

def get_lower_calories_info(top_three: list) -> Tuple[int, int]:
    if top_three[0] < top_three[1]:
        if top_three[0] < top_three [2]:
            return 0, top_three[0]
        else:
            return 2, top_three[0]
    elif top_three[0] < top_three[2]:
        return 1, top_three[1]
    elif top_three[1] < top_three[2]:
        return 1, top_three[1]
    
    return 2, top_three[2]


def update_top_three(top_three: list, current_elf_calories: int) -> list:
    index, lower_calorie = get_lower_calories_info(top_three)

    if lower_calorie < current_elf_calories:
        top_three[index] = current_elf_calories
    
    return top_three


def main():
    current_elf_calories = 0
    top_three = [0, 0, 0]

    with open(INPUT_FILE, mode='r', encoding='utf-8') as input:
        for row in input:
            if not row.strip():
                top_three = update_top_three(top_three, current_elf_calories)

                current_elf_calories = 0
                continue

            current_elf_calories += int(row)

    return top_three


if __name__ == '__main__':
    result = main()

    print(f'Most Calories Elf: {max(result)}')
    print(f'Top Three Most Calories Elves: {sum(result)}')

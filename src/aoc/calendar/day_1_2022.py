"""Day 1: Calorie Counting.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

from pathlib import Path

import typer

from aoc.calendar.registry import day

data_path = Path("C:/Users/Raphael/Programmation/python_projects/advent_of_code/data")


def calorie_counting(calorie_file: str) -> list[int]:
    """Returns the sum of the calorie carried for each elf.

    :param calorie_file: name of the file containing the calorie count.
    :return: greatest amount of calories in the file.
    """
    with open(data_path / f"{calorie_file}.txt", mode="r", encoding="utf-8") as data:
        split_calorie: list[str] = data.read().split("\n\n")
        clean_calorie: list[list[str]] = [calories.split("\n") for calories in split_calorie]
        int_clean_calorie: list[list[int]] = [
            [int(cal) for cal in calorie_list] for calorie_list in clean_calorie
        ]
        return [sum(calories) for calories in int_clean_calorie]


@day(name="01-12-2022")
def day_1_2022(
    calorie_file: str = typer.Argument(..., help="Name of the file containing the data.")
) -> None:
    """Day one of 2022: Find the Elf carrying the most Calories.

    :param calorie_file: name of the file containing the data.
    """
    sorted_calorie_sum: list[int] = sorted(calorie_counting(calorie_file))
    top_1: int = sorted_calorie_sum[-1]
    print(top_1)

    total_top_3: int = sum(sorted_calorie_sum[-3:])
    print(total_top_3)


if __name__ == "__main__":
    typer.run(day_1_2022)

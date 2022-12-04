"""Day 2: Rock Paper Scissors.

What would your total score be if everything goes exactly according to your strategy guide?
"""

from pathlib import Path
from typing import Mapping

import typer

from aoc.calendar.registry import day

data_path = Path("C:/Users/Raphael/Programmation/python_projects/advent_of_code/data")

outcomes_1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
outcomes_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def score(strategy_guide: str, outcomes: Mapping[str, int]) -> int:
    """Returns the greatest amount of calories carried by an elf.

    :param strategy_guide: name of the file containing the encrypted strategy.
    :param outcomes: all possible outcomes.
    :return: greatest amount of calories in the file.
    """
    with open(data_path / f"{strategy_guide}.txt", mode="r", encoding="utf-8") as data:
        guide = list(data.read().strip().split("\n"))

        total_score: int = 0
        for strategy in guide:
            total_score += outcomes[strategy]

        return total_score


@day(name="02-12-2022")
def day_2_2022(
    strategy_guide: str = typer.Argument(..., help="Name of the file containing the data.")
) -> None:
    """Day two of 2022: Total score be if everything goes exactly according to the given
    strategy guide.

    :param strategy_guide: name of the file containing the data.
    """
    result_part_1: int = score(strategy_guide, outcomes_1)
    print(result_part_1)

    result_part_2: int = score(strategy_guide, outcomes_2)
    print(result_part_2)


if __name__ == "__main__":
    typer.run(day_2_2022)

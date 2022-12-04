"""Day 3: Rucksack Reorganization.

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?
"""
import string
from pathlib import Path

import typer

from aoc.calendar.registry import day

DATA_PATH = Path("C:/Users/Raphael/Programmation/python_projects/advent_of_code/data")


def priorities(rucksacks_file: str):
    """Returns the greatest amount of calories carried by an elf.

    :param rucksacks_file: name of the file containing the rucksacks.
    :return: greatest amount of calories in the file.
    """
    with open(DATA_PATH / f"{rucksacks_file}.txt", mode="r", encoding="utf-8") as data:
        rucksacks: list[str] = list(data.read().strip().split("\n"))

        alphabet: list[str] = list(string.ascii_letters)
        sum_of_priorities: int = 0
        for rucksack in rucksacks:
            first_compartment: set[str] = set(rucksack[: len(rucksack) // 2])
            second_compartment: set[str] = set(rucksack[len(rucksack) // 2 :])

            intersection = next(iter(first_compartment.intersection(second_compartment)))
            sum_of_priorities += alphabet.index(intersection) + 1

        return sum_of_priorities


@day(name="03-12-2022")
def day_3_2022(
    rucksacks_file: str = typer.Argument(..., help="Name of the file containing the data.")
) -> None:
    """Day three of 2022: Sum of the priorities of every item types.

    :param rucksacks_file: name of the file containing the data.
    """
    result_part_1: int = priorities(rucksacks_file)
    print(result_part_1)


if __name__ == "__main__":
    typer.run(day_3_2022)

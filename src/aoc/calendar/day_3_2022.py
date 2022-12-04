"""Day 3: Rucksack Reorganization.

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?
"""

import string
from pathlib import Path

import typer

from aoc.calendar.registry import day

DATA_PATH = Path("C:/Users/Raphael/Programmation/python_projects/advent_of_code/data")


def _create_groups(rucksacks: list[str], nb_elves: int):
    """Yields successive n-sized chunks from lst."""
    for i in range(0, len(rucksacks), nb_elves):
        yield rucksacks[i : i + nb_elves]


def _common_item(items: list[set[str]]) -> str:
    """Finds the common item in a list of sets.

    :param items: list of items.
    :return: common item.
    """
    intersection: str = next(iter(set.intersection(*items)))
    return intersection


def priorities(rucksacks_file: str, nb_elves: int):
    """Returns the greatest amount of calories carried by an elf.

    :param rucksacks_file: name of the file containing the rucksacks.
    :param nb_elves: number of elves in each group.
    :return: greatest amount of calories in the file.
    """
    alphabet: list[str] = list(string.ascii_letters)

    with open(DATA_PATH / f"{rucksacks_file}.txt", mode="r", encoding="utf-8") as data:
        rucksacks: list[str] = list(data.read().strip().split("\n"))
        groups = list(_create_groups(rucksacks, nb_elves))

        sum_of_priorities: int = 0
        for group in groups:
            if nb_elves == 1:
                first_compartment: set[str] = set(group[0][: len(group[0]) // 2])
                second_compartment: set[str] = set(group[0][len(group[0]) // 2 :])
                items: list[set[str]] = [first_compartment, second_compartment]
            else:
                items = [set(grp) for grp in group]

            intersection = _common_item(items)
            sum_of_priorities += alphabet.index(intersection) + 1

        return sum_of_priorities


@day(name="03-12-2022")
def day_3_2022(
    rucksacks_file: str = typer.Argument(..., help="Name of the file containing the data."),
    nb_elves: int = typer.Option(1, help="Number of elves in each group."),
) -> None:
    """Day three of 2022: Sum of the priorities of every item types.

    :param rucksacks_file: name of the file containing the data.
    :param nb_elves: number of elves in each group.
    """
    result: int = priorities(rucksacks_file, nb_elves)
    print(result)


if __name__ == "__main__":
    typer.run(day_3_2022)

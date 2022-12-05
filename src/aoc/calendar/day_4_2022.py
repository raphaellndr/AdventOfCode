"""Day 4: Camp Cleanup.

In how many assignment pairs does one range fully contain the other?
"""

from pathlib import Path

import typer

from aoc.calendar.registry import day

DATA_PATH = Path("C:/Users/Raphael/Programmation/python_projects/advent_of_code/data")


def overlapping(assignments_file: str) -> tuple[int, int]:
    """Returns the greatest amount of calories carried by an elf.

    :param assignments_file: name of the file containing the rucksacks.
    :return: greatest amount of calories in the file.
    """
    with open(DATA_PATH / f"{assignments_file}.txt", mode="r", encoding="utf-8") as data:
        assignments: list[str] = list(data.read().strip().split("\n"))

        total_overlapping: int = 0
        total_containing: int = 0
        for assignment in assignments:
            split_assignment: list[str] = assignment.split(",")

            first_assignment: list[str] = split_assignment[0].split("-")
            second_assignment: list[str] = split_assignment[1].split("-")

            first_assignment_int: list[int] = [int(a) for a in first_assignment]
            second_assignment_int: list[int] = [int(a) for a in second_assignment]

            first_assignment_set = set(range(first_assignment_int[0], first_assignment_int[1] + 1))
            second_assignment_set = set(
                range(second_assignment_int[0], second_assignment_int[1] + 1)
            )

            if len(first_assignment_set - second_assignment_set) < len(first_assignment_set) or len(
                second_assignment_set - first_assignment_set
            ) < len(second_assignment):
                total_overlapping += 1

                if first_assignment_set.issubset(
                    second_assignment_set
                ) or first_assignment_set.issuperset(second_assignment_set):
                    total_containing += 1

    return total_containing, total_overlapping


@day(name="04-12-2022")
def day_3_2022(
    assignments_file: str = typer.Argument(..., help="Name of the file containing the data."),
) -> None:
    """Day four of 2022: Number of assignments where one fully contains the other.

    :param assignments_file: name of the file containing the data.
    """
    result_part_1, result_part_2 = overlapping(assignments_file)
    print(result_part_1, result_part_2)


if __name__ == "__main__":
    typer.run(day_3_2022)

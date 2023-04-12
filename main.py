#!/usr/bin/env python
from datetime import datetime
from subprocess import Popen

BRANCH = "contributions"
FILENAME = "contributions.txt"
HI_DICT = {
    2: {1, 2, 3, 4, 5},
    3: {3},
    4: {3},
    5: {1, 2, 3, 4, 5},
    7: {1, 5},
    8: {1, 2, 3, 4, 5},
    9: {1, 5},
    11: {1, 2, 3, 5}
}


def main():
    curr_date = datetime.now()
    _, week, weekday = curr_date.isocalendar()
    week %= 13
    if weekday in HI_DICT.get(week, set()):
        contribute(curr_date.strftime("%Y-%m-%d %H:%M"))


def contribute(date):
    run(["git", "checkout", "-B", BRANCH])
    with open(FILENAME, "a") as file:
        file.write(date + "\n")
    run(["git", "add", FILENAME])
    run(["git", "commit", "-a", "-m", date])
    run(["git", "push", "-u", "origin", BRANCH])


def run(commands):
    Popen(commands).wait()


if __name__ == "__main__":
    main()

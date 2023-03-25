#!/usr/bin/env python
from datetime import datetime
from subprocess import Popen

hi_dict = {
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
    run(["git", "checkout", "-B", "contributions"])

    curr_date = datetime.now()
    _, week, weekday = curr_date.isocalendar()
    week %= 13
    if weekday in hi_dict.get(week, set()):
        contribute(curr_date.strftime("%Y-%m-%d %H:%M"))


def contribute(date):
    with open("contributions.txt", "a") as file:
        file.write(date)
    run(["git", "commit", "-a", "-m", date])


def run(commands):
    Popen(commands).wait()


if __name__ == "__main__":
    main()

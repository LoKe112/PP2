import csv
import time
import os

from datetime import *


def CSV_split_by_week(path: str) -> None:
    """Split dstaset.csv in n files ( 1 file = 1 week)

    Args:
        path (str): path to file to cut
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            d = datetime.strptime(row[0], "%Y-%m-%d")
            with open(os.path.join("3", f"{d.year}-{d.isocalendar().week}.csv"), "a", encoding="utf-8", newline="") as file_N:
                writer = csv.writer(file_N)
                writer.writerow(row)
    print("end")


def main():
    CSV_split_by_week(os.path.join("dataset.csv"))


if __name__ == '__main__':
    main()

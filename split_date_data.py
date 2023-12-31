import csv
import time
import os


def split_date_and_data(path: str) -> None:
    """Split original dataset.csv to date(X) and data(Y) files in ladder 1

    Args:
        path (str): path to file to cut
    """
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[1]])
    with open(os.path.join("1", "X.csv"), "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open(os.path.join("1", "Y.csv"), "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end")


def main() -> None:
    split_date_and_data(os.path.join("dataset.csv"))


if __name__ == '__main__':
    main()

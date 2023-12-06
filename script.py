import csv
import os

from datetime import datetime


def find_1(path: str, date: datetime) -> list[str] | None:
    """find in full dataset

    Args:
        path (str): path to file to cut x
        date (datetime): date we want

    Returns:
        list[str] : rows 
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            d = datetime.strptime(row[0], "%Y-%m-%d")
            if d == date:
                return row
        return None


def find_2(path1: str, path2: str, date: datetime) -> list[str] | None:
    """find in split X and Y datasets

    Args:
        path1 (str): path to file to cut x
        path2 (str): path to file to cut y
        date (datetime): date we want

    Returns:
        list[str] : date row and data row
    """
    col1 = None
    col2 = None
    rowIndex = -1

    with open(path1, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            d = datetime.strptime(row[0], "%Y-%m-%d")
            if d == date:
                col1 = row[0]
                rowIndex = i
                break
    if col1 is None:
        return None

    with open(path2, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == rowIndex:
                col2 = row[0]
                break

    if col2 is None:
        return None

    return [col1, col2]


def find_3(path: str, date: datetime) -> list[str] | None:
    """find in years

    Args:
        path (str): path to file to cut
        date (datetime): date we want

    Returns:
        list[str] : rows 
    """
    for file in os.listdir(path):
        d1, d2 = map(lambda x: datetime.strptime(
            x, "%Y%m%d"), file.split(".")[0].split("_"))
        if (d1 <= date <= d2):
            with open(path + file, "r", encoding="utf-8", newline="") as fileData:
                reader = csv.reader(fileData)
                for row in reader:
                    d = datetime.strptime(row[0], "%Y-%m-%d")
                    if d == date:
                        return row
                return None
    return None


def find_4(path: str, date: datetime) -> list[str] | None:
    """find in weeks

    Args:
        path (str): path to file to cut
        date (datetime): date we want

    Returns:
        rows 
    """
    week = date.isocalendar().week
    for file in os.listdir(path):
        s = file.split(".")[0].split("-")
        y, w = int(s[0]), int(s[1])
        if (date.year == int(y) and week == w):
            with open(path + file, "r", encoding="utf-8", newline="") as fileData:
                reader = csv.reader(fileData)
                for row in reader:
                    d = datetime.strptime(row[0], "%Y-%m-%d")
                    if d == date:
                        return row
                return None
    return None


def main() -> None:
    dt = datetime.strptime(input(), "%Y-%m-%d")
    print(find_1("dataset.csv", dt))
    print(find_2("1\\X.csv", "1\\Y.csv", dt))
    print(find_3("2\\", dt))
    print(find_4("3\\", dt))


if __name__ == '__main__':
    main()

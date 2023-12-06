import csv
import time
import os
from Iterator import Iterator

def next_iteration(path: str) -> tuple:
    """get next date in file

    Args:
        path (str): path to dataset.csv 

    Returns:
        tuple: ((date, we find), (data, we found))

    Yields:
        Iterator[tuple]: ((date, we find), (data, we found))
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data = row[0]
            mass = []
            for i in range(1, len(row)):
                mass.append(row[i])
            yield (data, mass)
            

iter = next_iteration("dataset.csv")
first = next(iter)
print(first)
second = next(iter)
print(second)

iter = Iterator("dataset.csv")

for i in range(1,10):
    print(next(iter))
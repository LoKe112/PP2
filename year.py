import csv
import time

from datetime import *
from typing import Iterable

def N_cut_by_year(path: str) -> None:
    """open dataset, split dataset to /2 in year files

    Args:
        path (str): _description_
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        data: dict[int,list[Iterable]]
        data = {}
        for row in reader:
            d=datetime.strptime(row[0],"%Y-%m-%d")
            if d.year not in data:
                data[d.year]=[]
            data[d.year].append(row)
        for year in data.keys():
            start_date=data[year][0][0].replace("-","")
            end_date=data[year][-1][0].replace("-","")
            with open(f"2\\{start_date}_{end_date}.csv" , "w", encoding="utf-8", newline="") as file_N:
                writer = csv.writer(file_N)
                writer.writerows(data[year])


def main() -> None:
    N_cut_by_year("dataset.csv")


if __name__ == '__main__':
    main()
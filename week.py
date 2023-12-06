import csv
import time

from datetime import *


def CSV_split_by_week(path: str) -> None:
    """Open .csv file from path and fill "3/" folder with n files : 1 file = 1 weak

    Args:
        path (str): path to file to cut
    """    
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)        
        for row in reader:
            d=datetime.strptime(row[0],"%Y-%m-%d")
            with open(f"3\\{d.year}-{d.isocalendar().week}.csv" , "a", encoding="utf-8", newline="") as file_N:
                writer = csv.writer(file_N)
                writer.writerow(row)              
    print("end")


def main():
    CSV_split_by_week("dataset.csv")


if __name__ == '__main__':
    main()
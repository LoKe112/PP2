import csv
import time


def N_cut_by_weak(path: str) -> None:
    """Open .csv file from path and fill "3/" folder with n files : 1 file = 1 weak

    Args:
        path (str): path to file to cut
    """
    day_x = ""
    for year in range(2008, 2024):
        for month in range(1, 12):
            for i in range(0, 5):
                with open(path, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    data = []
                    for row in reader:
                        for day in range(1+7*i, 8+7*i):
                            if str(year).zfill(4) == row[0][0]+row[0][1]+row[0][2]+row[0][3] and str(month).zfill(2) == row[0][5]+row[0][6] and str(day).zfill(2) == row[0][7]+row[0][8] :
                                data.append(row)
                                day_x = row[0]
                
                if len(data):
                    with open(f"3\\{year}.{month}.{1+7*i}-{year}.{month}.{day_x}.csv", "w", encoding="utf-8", newline="") as file_N:
                        writer = csv.writer(file_N)
                        writer.writerows(data)
                
    print("end")


def main():
    N_cut_by_weak("dataset.csv")


if __name__ == '__main__':
    main()
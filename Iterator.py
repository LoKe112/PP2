import os
import csv


class Iterator:
    def __init__(self, name_of_file: str) -> None:
        """Initialization

        Args:
            name_of_file (str): path to file to iterate
        """
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding='utf-8')
        for row in file:
            self.list.append(row)
        file.close

    def __iter__(self):
        return self

    def __next__(self) -> int:
        """next



        Returns:
            int: _description_
        """
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration


def main() -> None:
    iter = Iterator("dataset.csv")

    for i in range(1, 10):
        print(next(iter))


if __name__ == '__main__':
    main()

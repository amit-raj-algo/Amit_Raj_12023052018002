import csv
import os


class CSVReader:

    @staticmethod
    def read_test_data():
        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        csv_path = os.path.join(
            base_dir,
            "data",
            "test_data.csv"
        )

        with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
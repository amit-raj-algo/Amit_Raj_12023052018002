import csv


def calculate_sum(first_number, second_number):
    return float(first_number) + float(second_number)


def read_login_data(file_path):
    data = []

    with open(file_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data.append([
                row["username"],
                row["password"],
                row["expected"]
            ])

    return data
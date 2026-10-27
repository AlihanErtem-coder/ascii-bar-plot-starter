import csv
import os


def load_rows(points):
    if not os.path.isfile(points):
        raise FileNotFoundError(points)

    rows = []

    with open(points, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(
                (
                    row["type"],
                    float(row["value1"]),
                    float(row["value2"]),
                )
            )

    return rows


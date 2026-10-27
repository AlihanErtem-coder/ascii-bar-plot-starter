from my_io import load_rows

def average_value1_by_type(rows):
    sums = {}
    counts = {}

    for point_type, value1, _value2 in rows:
        sums[point_type] = sums.get(point_type, 0.0) + value1
        counts[point_type] = counts.get(point_type, 0) + 1

    result = []
    for point_type in sorted(sums):
        average = sums[point_type] / counts[point_type]
        result.append((point_type, average))

    return result

rows = load_rows("data/points.csv")

averages = average_value1_by_type(rows)
print(averages)


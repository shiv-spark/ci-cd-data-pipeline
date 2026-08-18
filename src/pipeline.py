import csv
from pathlib import Path


def process_customers(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        row["amount"] = float(row["amount"])

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["customer_id", "name", "city", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return rows


if __name__ == "__main__":
    process_customers(
        "data/customers.csv",
        "output/customers_processed.csv"
    )
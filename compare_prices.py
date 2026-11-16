import csv
from pathlib import Path

csv_path = Path(__file__).with_name("supplier_quotes.csv")
prices_per_kg = {}

with csv_path.open(encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        supplier = row["supplier"]
        weight = float(row["weight_kg"])
        total_price = float(row["total_price"])

        price_per_kg = total_price / weight
        prices_per_kg[supplier] = price_per_kg
        print(f"{supplier}: ${price_per_kg:.2f} per kg")

lowest_price = min(prices_per_kg.values())
cheapest = [name for name, price in prices_per_kg.items() if price == lowest_price]

if len(cheapest) == 1:
    print(f"{cheapest[0]} is cheapest per kg.")
else:
    print(f"Tie: {', '.join(cheapest)}")
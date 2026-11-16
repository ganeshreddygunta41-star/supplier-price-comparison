# Supplier Price Comparison

This Python script reads sample supplier quotes from `supplier_quotes.csv`. It divides each pack's price by its weight in kilograms, then reports the cheapest supplier or lists the suppliers tied for the lowest price.

## How to run

Keep `compare_prices.py` and `supplier_quotes.csv` in the same folder. Open a terminal in that folder and run:

```text
python compare_prices.py
```

## Example output

```text
Supplier A: $12.00 per kg
Supplier B: $10.00 per kg
Supplier C: $9.00 per kg
Supplier C is cheapest per kg.
```

To compare more suppliers, add rows to `supplier_quotes.csv` using the columns `supplier`, `weight_kg`, and `total_price`.

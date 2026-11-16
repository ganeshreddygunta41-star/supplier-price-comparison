supplier_a_per_kg = 12 / 1
supplier_b_per_kg = 20 / 2

print(f"Supplier A: ${supplier_a_per_kg:.2f} per kg")
print(f"Supplier B: ${supplier_b_per_kg:.2f} per kg")
if supplier_a_per_kg < supplier_b_per_kg:
    print("Supplier A is cheaper per kg.")
elif supplier_b_per_kg < supplier_a_per_kg:
    print("Supplier B is cheaper per kg.")
else:
    print("Both suppliers charge the same price per kg.")
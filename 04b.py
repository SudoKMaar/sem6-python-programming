furniture_rates = {"table": 2000, "chair": 500, "sofa": 5000, "bed": 8000}

order = input("Enter your order as 'furniture quantity' pairs (e.g., 'table 2 chair 3'): ").split()

bill = 0

for i in range(0, len(order), 2):
    furniture = order[i]
    quantity = int(order[i+1])
    if furniture in furniture_rates:
        bill += furniture_rates[furniture] * quantity
    else:
        bill = -1
        break

if bill > 10000:
    bill *= 0.95

if bill != -1:
    bill *= 1.08

print(f"The bill amount is {bill}.")

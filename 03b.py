fruits = ["apple", "banana", "cherry", "dates", "elderberry"]
rates = [100, 50, 200, 150, 300]

order = input("Enter your order as 'fruit quantity' pairs (e.g., 'apple 2 banana 3'): ").split()
bill = 0

for i in range(0, len(order), 2):
    fruit = order[i]
    quantity = int(order[i+1])
    if fruit in fruits:
        index = fruits.index(fruit)
        bill += rates[index] * quantity
    else:
        bill = -1
        break

if bill > 500:
    bill *= 0.9

print(f"The bill amount is {bill}.")

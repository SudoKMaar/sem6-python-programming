num_terms = int(input("Enter the number of terms: "))
term1, term2 = 0, 1
count = 0

while count < num_terms:
    print(term1)
    next_term = term1 + term2
    term1 = term2
    term2 = next_term
    count += 1

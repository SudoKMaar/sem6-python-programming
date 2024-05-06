with open('emails.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract company names and write them to a new file
with open('companies.txt', 'w') as f:
    for line in lines:
        email = line.strip()
        company_name = email.split('@')[-1].split('.')[0]
        f.write(company_name + '\n')

# Read the new file and print the company names
with open('companies.txt', 'r') as f:
    company_names = f.readlines()

print("Company names:")
for company_name in company_names:
    print(company_name.strip())

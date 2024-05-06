s = input("Enter a string: ")

char_dict = {}
for char in s:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

chars = sorted(char_dict.keys(), key=lambda x: char_dict[x])
freqs = [char_dict[char] for char in chars]

print(f"Characters: {chars}")
print(f"Frequencies: {freqs}")

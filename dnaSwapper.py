raw = input("DNA sequence: ")

swap = {
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"}

output = ''

for x in range(len(raw)):
    if raw[x] in swap:
        output = output + (swap[raw[x]])
    else:
        output = output + (raw[x])

print(output)
input()

with open("input2.txt", "r") as f:
    lines = f.read()

ids = lines.split('\n')
ids.pop()
doubles = 0
triples = 0

for id in ids:
    chars = list(id)
    counts = {}
    for char in chars:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    all_counts = set(counts.values())
    if 2 in all_counts:
        doubles += 1
    if 3 in all_counts:
        triples += 1

print(doubles * triples)

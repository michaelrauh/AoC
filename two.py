with open("input2.txt", "r") as f:
    lines = f.read()

ids = lines.split('\n')
ids.pop()
doubles = 0
triples = 0

for id in ids:
    chars = list(id)
    counts = {}
    for second_id in ids:
        in_common = 0
        second_chars = list(second_id)
        for i in range(len(chars)):
            if chars[i] == second_chars[i]:
                in_common += 1
        if in_common == len(chars) -1:
            print(id)
            print(second_id)
            exit()

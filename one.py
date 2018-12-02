with open("input1.txt", "r") as f:
    lines = f.read()

seen = set()
acc = 0
split = lines.split('\n')
split.pop()
numbers = [int(i) for i in split]
runs = 0
while True:
    runs += 1
    print(runs)
    for number in numbers:
        acc += number
        if acc in seen:
            print(acc)
            exit()
        seen.add(acc)

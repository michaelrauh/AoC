with open("input1.txt", "r") as f:
    lines = f.read()

acc = 0
split = lines.split('\n')
split.pop()
numbers = [int(i) for i in split]
print(sum(numbers))

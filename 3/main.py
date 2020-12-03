with open("input.txt", "rt") as handle:
    input_text = handle.read()

data = [line for line in input_text.split("\n") if line]
width = len(data[0])

def count_trees(x_step, y_step):
    trees = 0
    for n, y in enumerate(range(0, len(data), y_step)):
        x = (n * x_step) % width
        trees += 1 if data[y][x] == "#" else 0
    return trees

product = 1

for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    product *= count_trees(x, y)

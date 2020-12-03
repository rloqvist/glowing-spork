with open("input.txt", "rt") as handle:
    input_text = handle.read()

lines = [int(line) for line in input_text.split() if line]

def product(lines):
    for i in lines:
        for j in lines:
            if i + j > 2020:
                continue
            for k in lines:
                if i + j + k == 2020:
                    return i * j * k

print(product(lines))

from functools import reduce

with open("input.txt", "rt") as handle:
    input_text = handle.read()

def parse_id(num):
    def decode_segment(chars, base):
        def reducer(acc, cur):
            index, letter = cur
            return int(acc + (chars.index(cur[1]) and base / (2 ** cur[0])))
        return reduce(reducer, (0, *enumerate(l for l in num if l in chars)))
    return decode_segment("FB", 64) * 8 + decode_segment("LR", 4)

ids = [parse_id(line) for line in input_text.split("\n") if line]
checked = min(ids)

for current in sorted(ids):
    diff = current - checked
    if diff > 1:
        print(f"Jumped {diff} seats. ({checked} to {current})")
    checked = current

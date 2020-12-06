print(sum([len("".join(set("".join(group.split())))) for group in open("input.txt", "rt").read().split("\n\n") if group]))
print(sum([len([c for c in "".join(set("".join(group.split()))) if "".join(group.split()).count(c) is len(group.split())]) for group in open("input.txt", "rt").read().split("\n\n") if group]))

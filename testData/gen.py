import sys
from random import choice

files = sys.argv[1:]

colors = ["rot", "grün", "blau"]
for file in files:
    selection = []
    previous = None
    for _ in range(20):
        previous = choice([c for c in colors if c != previous])
        selection.append(previous)

    with open(file, "w", encoding="utf-8") as file:
        file.write(" ".join(selection))

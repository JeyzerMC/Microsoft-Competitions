from itertools import groupby
with open("input.txt") as f:
    for line in f:
        groups = [list(g) for k, g in groupby(line)]
        length = ["{}{}".format(("", len(g))[len(g) > 1], g[0])
                  for g in groups]
        with open("output.txt", 'a') as o:
            o.write("".join(length))

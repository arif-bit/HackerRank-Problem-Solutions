from itertools import groupby

for i in [list(g) for k, g in groupby(input())]:
    print((len(i),int(i[0])),end=" ")
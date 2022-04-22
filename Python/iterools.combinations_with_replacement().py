from itertools import combinations_with_replacement

io = input().split()
S = io[0]
k = int(io[1])

for j in combinations_with_replacement(sorted(S),k):
    print("".join(j))
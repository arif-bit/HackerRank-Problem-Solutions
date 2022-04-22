from itertools import permutations
string=input().split()
value=string[0]
howManyCharater=int(string[1])
formattingValue=sorted(["".join(i) for i in permutations(value,howManyCharater)])
print("\n".join(formattingValue))
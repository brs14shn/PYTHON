
##Convert Single İnteger-10

"""Convert a list of multiple integers into a single integer"""

liste=[11,22,33] #except output:112233

single_int=int("".join(map(str,liste)))
print(single_int)
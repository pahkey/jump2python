import itertools

a = "abcd"
result = itertools.permutations(a, 4)
for r in result:
    print(''.join(r))

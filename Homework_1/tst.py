s = 5

i = int(input())


if i == -1:
	l = list(range(1, s*s))
	l.append(0)
else:
	l = list(range(1, i + 1))
	l.append(0)
	for i in range(i + 1, s*s +1):
		l.append(i)
	# l.append(i for i in list(range(i + 1, s*s + 1)))
# print(l)
ot = [[i for i in l[0 + s*j:s + s*j]] for j in range(0,s)]
print(ot)
# return 0
# l = [list(range(1 + s*i, s + s*i  + 1)) for i in range(0, s)]
# l[s - 1][s - 1] = 0
# l[s - 1]
# print(l)

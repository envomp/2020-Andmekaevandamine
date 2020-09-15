data = """1 0 0 0 0 1 1 0 0
1 0 0 0 0 1 1 1 0
1 0 0 1 0 0 1 0 1
0 1 0 0 1 0 1 0 1
0 0 1 0 1 0 0 0 1
0 0 1 0 1 0 0 1 0
0 0 1 1 0 0 0 1 1
0 1 0 0 0 1 1 0 0
0 0 1 0 0 1 0 0 1
0 1 0 0 1 0 0 0 1
0 1 0 0 0 1 0 1 1
0 1 0 1 0 0 1 1 1
1 0 0 1 0 0 0 0 1
0 1 0 0 1 0 1 1 0"""

matrix = [x.split() for x in data.split("\n")]
print(matrix)
rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(rez)

for row in rez:
    for i, elem in enumerate(row):
        if elem == "1":
            print(1 + i, end=" ")
    print()

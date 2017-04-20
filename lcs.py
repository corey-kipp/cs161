x = "skullandbones"
y = "lullabybabies"
nx = len(x)
ny = len(y)
T = [[None]*(ny+1) for k in range(nx+1)]

def LCS(i,j):
    if T[i][j] is None:
        if i == 0 or j == 0:
            T[i][j] = 0
        elif x[i-1] == y[j-1]:
            T[i][j] = 1 + LCS(i-1,j-1)
        else:
            T[i][j] = max(LCS(i-1,j), LCS(i, j-1))
    return T[i][j]

print(LCS(nx,ny))
print()

for row in T:
    for elem in row:
        print(elem, end='\t')
    print()
print()

S = []

def find_lcs(i,j):
    if i == 0 or j == 0:
        return
    elif x[i-1] == y[j-1]:
        S.append(x[i-1])
        find_lcs(i-1, j-1)
    else:
        shortenX = T[i-1][j]
        shortenY = T[i][j-1]
        if shortenX > shortenY:
            find_lcs(i-1,j)
        else:
            find_lcs(i,j-1)

find_lcs(nx,ny)

for char in S[::-1]:
    print(char,end='')
print()

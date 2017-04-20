L = [9,1,7,3,2,8,9,3]
n = len(L)

T = [[None]*n for k in range(n)]

def value(i,j):
    if T[i][j] is not None:
        return T[i][j]

    if i == j:
        T[i][j] = L[i]
    else:
        takeLeft = L[i] - value(i+1,j)
        takeRight = L[j] - value(i, j-1)
        T[i][j] = max(takeLeft, takeRight)

    return T[i][j]

print(value(0,n-1))

for row in T:
    for elem in row:
        print(elem, end='\t')
    print()
print()

def find_moves(i,j):
    if i == j:
        print(i)
        return

    takeLeft = L[i] - T[i+1][j]
    takeRight = L[j] - T[i][j-1]
    if takeLeft > takeRight:
        print(i)
        find_moves(i+1,j)
    else:
        print(j)
        find_moves(i,j-1)

find_moves(0,n-1)

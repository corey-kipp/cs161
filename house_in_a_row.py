L = [-3, 10, 2, -5, 7, -1, -2, -1, -3]
n = len(L)
T = [[None]*n for k in range(n)]

def houses(i, j, s):

    if T[i][j] is not None and (s==1):
        return T[i][j]
    if i==j and s==1:
        T[i][j] = L[i]
        return L[i]
    if i==j and s==0:
        take = L[i]
        dont = -L[i]
        return max(take,dont)
    else:
        takeLeft = L[i] + houses(i+1, j, 0)
        takeRight = L[j] + houses(i, j-1, 0)
        takeNone = None
        if (s == 0):
            takeNone = 0 - houses(i, j, 1)
        if (takeNone != None):
            if ((takeNone >= takeRight) and (takeNone >= takeLeft)):
                T[i][j] = takeNone
                return T[i][j]
            elif ((takeLeft >= takeRight) and (takeLeft >= takeNone)):
                T[i][j] = takeLeft
                return T[i][j]
            elif ((takeRight >= takeLeft) and (takeRight >= takeNone)):
                T[i][j] = takeRight
                return T[i][j]
        elif (takeNone == None):
            if (takeLeft >= takeRight):
                T[i][j] = takeLeft
                return T[i][j]
            else:
                T[i][j] = takeRight
                return T[i][j]
        
                
        return T[i][j]

houses(0,n-1,1)

for row in T:
    for elem in row:
        print(elem,end='\t')
    print()
print()

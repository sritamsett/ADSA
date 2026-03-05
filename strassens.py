def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11,A22), add(B11,B22))
    M2 = strassen(add(A21,A22), B11)
    M3 = strassen(A11, sub(B12,B22))
    M4 = strassen(A22, sub(B21,B11))
    M5 = strassen(add(A11,A12), B22)
    M6 = strassen(sub(A21,A11), add(B11,B12))
    M7 = strassen(sub(A12,A22), add(B21,B22))

    C11 = add(sub(add(M1,M4),M5),M7)
    C12 = add(M3,M5)
    C21 = add(M2,M4)
    C22 = add(sub(add(M1,M3),M2),M6)

    C=[]
    for i in range(mid):
        C.append(C11[i]+C12[i])
    for i in range(mid):
        C.append(C21[i]+C22[i])

    return C


def strassen_menu():

    n = int(input("Enter matrix size (power of 2): "))

    print("Enter Matrix A:")
    A=[list(map(int,input().split())) for _ in range(n)]

    print("Enter Matrix B:")
    B=[list(map(int,input().split())) for _ in range(n)]

    C=strassen(A,B)

    print("\nResult Matrix:")
    for row in C:
        print(row)


strassen_menu()
import sys

def print_parenthesis(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_parenthesis(s, i, s[i][j])
        print_parenthesis(s, s[i][j] + 1, j)
        print(")", end="")

def matrix_chain():

    n = int(input("Enter number of matrices: "))

    p = []
    print("Enter dimensions:")
    for i in range(n + 1):
        p.append(int(input(f"p[{i}] = ")))

    m = [[0 for _ in range(n)] for _ in range(n)]

    s = [[0 for _ in range(n)] for _ in range(n)]


    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    print("\nMCM Cost Matrix (m[][]):")
    for row in m:
        print(row)


    print("\nSplit Matrix (s[][]):")
    for row in s:
        print(row)

    print("\nMinimum number of multiplications =", m[0][n - 1])

    print("Optimal Parenthesization:", end=" ")
    print_parenthesis(s, 0, n - 1)
    print()


matrix_chain()
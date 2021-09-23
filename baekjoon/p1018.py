import sys

def read_chessboard(M, N):
    chessboard = []
    for _ in range(M):
        row = []
        line = input()
        for c in line:
            if c == 'W':
                row.append(1)
            else: # c == 'B'
                row.append(0)
        chessboard.append(row)
    return chessboard

def p1018(M, N, chessboard):
    best = sys.maxsize
    for i in range(M - 7):
        for j in range(N - 7):
            count = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if chessboard[k][l] == 0:
                            count += 1
                    else:
                        if chessboard[k][l] == 1:
                            count += 1
            best = min(best, count)

            count = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if chessboard[k][l] == 1:
                            count += 1
                    else:
                        if chessboard[k][l] == 0:
                            count += 1
            best = min(best, count)
    return best

M, N = map(int, input().split(' '))
chessboard = read_chessboard(M, N)
print(p1018(M, N, chessboard))
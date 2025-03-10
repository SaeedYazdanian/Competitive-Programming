def f(i, j):
    if i == r and j == c:
        return 1
    if i > r or j > c or (i, j) in cats:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = f(i+1, j) + f(i, j+1)
    return dp[i][j]

r, c = [int(x) for x in input().split()]
dp = [[-1 for j in range(c+1)] for i in range(r+1)]
cats = set([tuple([int(x) for x in input().split()]) for i in range(int(input()))])
print(f(1, 1))

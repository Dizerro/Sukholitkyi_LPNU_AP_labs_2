def solve_ijones(W, H, grid):
    MOD = 10**9 + 7
    dp = [[0]*W for _ in range(H)]
    for h in range(H):
        dp[h][0] = 1
    from collections import defaultdict
    prev_col_sums = [defaultdict(int) for _ in range(W)]
    for w in range(W):
        for h in range(H):
            ch = grid[h][w]
            if w > 0:
                dp[h][w] += dp[h][w - 1]
                dp[h][w] %= MOD
                dp[h][w] += prev_col_sums[w - 1][ch]
                dp[h][w] %= MOD
        for h in range(H):
            ch = grid[h][w]
            prev_col_sums[w][ch] += dp[h][w]
            prev_col_sums[w][ch] %= MOD
    return (dp[0][W - 1] + dp[H - 1][W - 1]) % MOD

def main():
    with open("ijones.in") as f:
        W, H = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for _ in range(H)]
    result = solve_ijones(W, H, grid)
    with open("ijones.out", "w") as f:
        f.write(str(result) + "\n")

main()

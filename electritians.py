from math import sqrt

def max_wire_length(w, heights):
    n = len(heights)
    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        dist_00 = w
        dist_01 = sqrt(w**2 + (heights[i] - 1)**2)
        dist_10 = sqrt(w**2 + (1 - heights[i-1])**2)
        dist_11 = sqrt(w**2 + (heights[i] - heights[i-1])**2)

        dp[i][0] = max(
            dp[i-1][0] + dist_00,
            dp[i-1][1] + dist_10
        )

        dp[i][1] = max(
            dp[i-1][0] + dist_01,
            dp[i-1][1] + dist_11
        )

    return round(max(dp[n-1][0], dp[n-1][1]), 2)

w = 4
heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 
           66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 
           3, 93, 34, 57, 51, 11, 39, 72]

print(max_wire_length(w,heights))
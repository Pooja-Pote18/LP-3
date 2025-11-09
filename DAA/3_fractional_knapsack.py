def knapsack(W, weights, values, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
print("Maximum value in Knapsack =", knapsack(W, weights, values, n))

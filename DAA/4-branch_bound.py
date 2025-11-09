def solve_knapsack():
    val = [50, 100, 150, 200]  # Value array
    wt = [8, 16, 32, 40]       # Weight array
    W = 64                     # Knapsack capacity
    n = len(val) - 1

    def knapsack(W, n): 
        # Base case
        if n < 0 or W <= 0:
            return 0

        # If current item weight is more than capacity, skip it
        if wt[n] > W:
            return knapsack(W, n - 1)
        
        # Either include or exclude the item
        else:
            return max(
                val[n] + knapsack(W - wt[n], n - 1),
                knapsack(W, n - 1)
            )

    result = knapsack(W, n)
    print("Maximum value for 0/1 Knapsack is:", result)


if __name__ == "__main__":           
    solve_knapsack()

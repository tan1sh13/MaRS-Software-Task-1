def min_cost(L, W, targets, D):
    prev=(0, 0, 0)   # starting position
    total_cost=0
    for target in targets:
        best_config=None
        min_cost_val=float('inf')
        # Trying all the combinations
        for i in range(L[0] + 1):          # Inner
            for j in range(L[1] + 1):      # Middle
                k=target-i-j         # Outer 
                # Check validity
                if 0 <= k <= L[2] and abs(i - k) <= D:
                    # Computing the cost
                    cost=abs(prev[0]-i)*W[0]+abs(prev[1]-j)*W[1]+abs(prev[2]-k)*W[2]
                    # Choosing minimum value
                    if cost < min_cost_val:
                        min_cost_val=cost
                        best_config=(i, j, k)

        total_cost+=min_cost_val
        prev=best_config

    return total_cost
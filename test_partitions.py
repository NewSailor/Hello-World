def find_partitions(n):
    """
    Find all positive-integer partitions of n.
    Returns a list of partitions, where each partition is a list of integers
    in non-increasing order.
    """
    def partition_helper(target, max_value, current_partition):
        if target == 0:
            return [current_partition[:]]  # Found a valid partition
        
        partitions = []
        # Try all values from min(target, max_value) down to 1
        for i in range(min(target, max_value), 0, -1):
            current_partition.append(i)
            partitions.extend(partition_helper(target - i, i, current_partition))
            current_partition.pop()
        
        return partitions
    
    return partition_helper(n, n, [])

def count_partitions(n):
    """
    Count the number of partitions of n using dynamic programming.
    This is more efficient for just counting.
    """
    # dp[i][j] = number of partitions of i using numbers <= j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: there's one way to partition 0 (empty partition)
    for j in range(n + 1):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Don't use j
            dp[i][j] = dp[i][j-1] if j > 1 else 0
            
            # Use j (if possible)
            if i >= j:
                dp[i][j] += dp[i-j][j]
    
    return dp[n][n]

# Test with small numbers first
print("Testing with small numbers:")
for n in [4, 5, 6, 7]:
    count = count_partitions(n)
    partitions = find_partitions(n)
    print(f"\nPartitions of {n} (count: {count}):")
    for i, partition in enumerate(partitions, 1):
        print(f"  {i}: {' + '.join(map(str, partition))}")
    print(f"Verification: found {len(partitions)} partitions")

# Test counting for larger numbers
print(f"\nCounting partitions for larger numbers:")
for n in [10, 20, 30, 50, 100]:
    count = count_partitions(n)
    print(f"Partitions of {n}: {count:,}")
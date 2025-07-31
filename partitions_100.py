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

def main():
    n = 100
    print(f"Finding all positive-integer partitions of {n}...")
    print("Note: This may take a while as there are many partitions of 100.")
    print()
    
    # First, let's count how many partitions there are
    count = count_partitions(n)
    print(f"Total number of partitions of {n}: {count:,}")
    print()
    
    # Ask user if they want to see all partitions (since there are many)
    print("Warning: There are a very large number of partitions.")
    print("Would you like to see:")
    print("1. All partitions (this will be a lot of output)")
    print("2. Just a few examples")
    print("3. Only the count (already shown above)")
    
    choice = input("Enter choice (1/2/3): ").strip()
    
    if choice == "1":
        print(f"\nAll partitions of {n}:")
        partitions = find_partitions(n)
        for i, partition in enumerate(partitions, 1):
            print(f"{i:6d}: {' + '.join(map(str, partition))}")
            
    elif choice == "2":
        print(f"\nFirst 20 partitions of {n}:")
        partitions = find_partitions(n)
        for i, partition in enumerate(partitions[:20], 1):
            print(f"{i:2d}: {' + '.join(map(str, partition))}")
        
        if len(partitions) > 20:
            print(f"... and {len(partitions) - 20:,} more partitions")
    
    print(f"\nVerification: Total count = {count:,}")

if __name__ == "__main__":
    main()
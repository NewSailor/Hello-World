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

def generate_partitions(n, max_num=None):
    """
    Generate partitions of n one at a time using a generator.
    This is memory efficient for large numbers.
    """
    if max_num is None:
        max_num = n
    
    def partition_generator(target, max_value):
        if target == 0:
            yield []
            return
        
        for i in range(min(target, max_value), 0, -1):
            for rest in partition_generator(target - i, i):
                yield [i] + rest
    
    yield from partition_generator(n, max_num)

def find_partitions_limited(n, limit=1000):
    """
    Find up to 'limit' partitions of n.
    Returns early if limit is reached.
    """
    partitions = []
    count = 0
    
    for partition in generate_partitions(n):
        partitions.append(partition)
        count += 1
        if count >= limit:
            break
    
    return partitions, count

def main():
    n = 100
    print(f"Finding positive-integer partitions of {n}")
    print("=" * 50)
    
    # First, let's count how many partitions there are
    print("Counting total partitions...")
    count = count_partitions(n)
    print(f"Total number of partitions of {n}: {count:,}")
    print()
    
    print("WARNING: There are over 190 million partitions of 100!")
    print("Finding all partitions would take an extremely long time and use massive amounts of memory.")
    print()
    
    print("Available options:")
    print("1. Show first few partitions (recommended)")
    print("2. Show partitions with specific constraints")
    print("3. Just show the count (already displayed)")
    print("4. Generate partitions to a file (limited number)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                break
            print("Please enter 1, 2, 3, or 4")
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
    if choice == "1":
        print("\nFirst 20 partitions of 100:")
        partitions, _ = find_partitions_limited(100, 20)
        for i, partition in enumerate(partitions, 1):
            print(f"{i:2d}: {' + '.join(map(str, partition))}")
        print(f"\n... and {count - 20:,} more partitions")
        
    elif choice == "2":
        print("\nPartition constraints:")
        print("a. Partitions using only 2's and 3's")
        print("b. Partitions with exactly 5 parts")
        print("c. Partitions with largest part = 10")
        
        sub_choice = input("Enter sub-choice (a/b/c): ").strip().lower()
        
        if sub_choice == "a":
            print("\nPartitions of 100 using only 2's and 3's:")
            partitions_23 = []
            # Only use 2's and 3's: 100 = 2*a + 3*b where a,b >= 0
            for threes in range(100//3 + 1):
                remainder = 100 - 3*threes
                if remainder % 2 == 0:
                    twos = remainder // 2
                    partition = [3] * threes + [2] * twos
                    if partition:  # non-empty
                        partitions_23.append(partition)
            
            print(f"Found {len(partitions_23)} partitions:")
            for i, partition in enumerate(partitions_23, 1):
                print(f"{i:2d}: {' + '.join(map(str, partition))}")
                
        elif sub_choice == "b":
            print("\nFirst 20 partitions of 100 with exactly 5 parts:")
            count = 0
            for partition in generate_partitions(100):
                if len(partition) == 5:
                    count += 1
                    print(f"{count:2d}: {' + '.join(map(str, partition))}")
                    if count >= 20:
                        break
            print(f"\n(Showing first {min(count, 20)} partitions with exactly 5 parts)")
            
        elif sub_choice == "c":
            print("\nFirst 20 partitions of 100 with largest part = 10:")
            count = 0
            for partition in generate_partitions(100, max_num=10):
                if partition and max(partition) == 10:
                    count += 1
                    print(f"{count:2d}: {' + '.join(map(str, partition))}")
                    if count >= 20:
                        break
            print(f"\n(Showing first {min(count, 20)} partitions with largest part = 10)")
    
    elif choice == "3":
        print(f"\nTotal partitions of {n}: {count:,}")
        
    elif choice == "4":
        try:
            limit = int(input("How many partitions to save to file? (recommended: 1000-10000): "))
            limit = min(limit, 100000)  # Cap at 100k for safety
            
            filename = f"partitions_100_first_{limit}.txt"
            print(f"\nGenerating first {limit} partitions to {filename}...")
            
            partitions, actual_count = find_partitions_limited(100, limit)
            
            with open(filename, 'w') as f:
                f.write(f"First {actual_count} partitions of 100\n")
                f.write(f"Total partitions of 100: {count:,}\n")
                f.write("=" * 50 + "\n\n")
                
                for i, partition in enumerate(partitions, 1):
                    f.write(f"{i:6d}: {' + '.join(map(str, partition))}\n")
            
            print(f"Saved {actual_count} partitions to {filename}")
            
        except ValueError:
            print("Invalid number entered.")
        except Exception as e:
            print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
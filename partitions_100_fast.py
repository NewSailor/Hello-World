def count_partitions(n):
    """
    Count the number of partitions of n using dynamic programming.
    This is more efficient for just counting.
    """
    # Use a 1D array instead of 2D for better memory efficiency
    dp = [0] * (n + 1)
    dp[0] = 1  # one way to partition 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    
    return dp[n]

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
    print(f"Integer Partitions of {n}")
    print("=" * 50)
    print()
    print("NOTE: There are 190,569,292 partitions of 100!")
    print("This program provides several ways to explore them:")
    print()
    
    print("Available options:")
    print("1. Show first few partitions (fast)")
    print("2. Show partitions with specific constraints")
    print("3. Count all partitions (may take a moment)")
    print("4. Generate partitions to a file (limited number)")
    print("5. Show some example partitions")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                break
            print("Please enter 1, 2, 3, 4, or 5")
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
    if choice == "1":
        print("\nFirst 20 partitions of 100:")
        partitions, _ = find_partitions_limited(100, 20)
        for i, partition in enumerate(partitions, 1):
            print(f"{i:2d}: {' + '.join(map(str, partition))}")
        print(f"\n... and many more partitions")
        
    elif choice == "2":
        print("\nPartition constraints:")
        print("a. Partitions using only 2's and 3's")
        print("b. Partitions with exactly 5 parts")
        print("c. Partitions with largest part = 10")
        print("d. Partitions into distinct parts")
        
        sub_choice = input("Enter sub-choice (a/b/c/d): ").strip().lower()
        
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
            
        elif sub_choice == "d":
            print("\nFirst 20 partitions of 100 into distinct parts:")
            count = 0
            for partition in generate_partitions(100):
                if len(partition) == len(set(partition)):  # all parts distinct
                    count += 1
                    print(f"{count:2d}: {' + '.join(map(str, partition))}")
                    if count >= 20:
                        break
            print(f"\n(Showing first {min(count, 20)} partitions into distinct parts)")
    
    elif choice == "3":
        print("\nCounting all partitions... (this may take a moment)")
        count = count_partitions(100)
        print(f"Total partitions of {n}: {count:,}")
        
    elif choice == "4":
        try:
            limit = int(input("How many partitions to save to file? (recommended: 1000-10000): "))
            limit = min(limit, 100000)  # Cap at 100k for safety
            
            filename = f"partitions_100_first_{limit}.txt"
            print(f"\nGenerating first {limit} partitions to {filename}...")
            
            partitions, actual_count = find_partitions_limited(100, limit)
            
            with open(filename, 'w') as f:
                f.write(f"First {actual_count} partitions of 100\n")
                f.write(f"(Total partitions of 100: 190,569,292)\n")
                f.write("=" * 50 + "\n\n")
                
                for i, partition in enumerate(partitions, 1):
                    f.write(f"{i:6d}: {' + '.join(map(str, partition))}\n")
            
            print(f"Saved {actual_count} partitions to {filename}")
            
        except ValueError:
            print("Invalid number entered.")
        except Exception as e:
            print(f"Error writing file: {e}")
            
    elif choice == "5":
        print("\nSome interesting partitions of 100:")
        print("\nSpecial partitions:")
        examples = [
            ([100], "Single part"),
            ([50, 50], "Two equal parts"),
            ([1] * 100, "All 1's"),
            ([99, 1], "99 + 1"),
            ([25, 25, 25, 25], "Four equal parts"),
            ([10] * 10, "Ten 10's"),
            ([20, 20, 20, 20, 20], "Five 20's"),
        ]
        
        for i, (partition, description) in enumerate(examples, 1):
            print(f"{i}: {' + '.join(map(str, partition))} ({description})")
        
        print(f"\nFirst 10 general partitions:")
        partitions, _ = find_partitions_limited(100, 10)
        for i, partition in enumerate(partitions, 1):
            print(f"{i:2d}: {' + '.join(map(str, partition))}")

if __name__ == "__main__":
    main()
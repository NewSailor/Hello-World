#!/usr/bin/env python3
"""
Integer Partitions of 100

This program finds positive-integer partitions of 100.
A partition is a way of writing 100 as a sum of positive integers
where order doesn't matter (e.g., 2+98 and 98+2 are the same partition).
"""

def count_partitions(n):
    """Count the number of partitions of n using dynamic programming."""
    dp = [0] * (n + 1)
    dp[0] = 1  # one way to partition 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    
    return dp[n]

def generate_partitions(n, max_num=None, limit=None):
    """Generate partitions of n, optionally limited by max_num and count."""
    if max_num is None:
        max_num = n
    
    def partition_generator(target, max_value):
        if target == 0:
            yield []
            return
        
        for i in range(min(target, max_value), 0, -1):
            for rest in partition_generator(target - i, i):
                yield [i] + rest
    
    count = 0
    for partition in partition_generator(n, max_num):
        yield partition
        count += 1
        if limit and count >= limit:
            break

def main():
    n = 100
    print(f"Integer Partitions of {n}")
    print("=" * 50)
    print()
    
    # Show some basic information
    print("What is a partition?")
    print("A partition of 100 is a way to write 100 as a sum of positive integers")
    print("where order doesn't matter. For example:")
    print("  100 = 2 + 98 (same as 98 + 2)")
    print("  100 = 1 + 1 + ... + 1 (100 ones)")
    print("  100 = 50 + 50")
    print()
    
    # Count total partitions (this is fast)
    print("Counting total partitions...")
    total_count = count_partitions(n)
    print(f"Total number of partitions of {n}: {total_count:,}")
    print()
    
    # Show first few partitions
    print("First 20 partitions of 100:")
    print("-" * 30)
    for i, partition in enumerate(generate_partitions(100, limit=20), 1):
        partition_str = " + ".join(map(str, partition))
        print(f"{i:2d}: {partition_str}")
    print(f"... and {total_count - 20:,} more partitions")
    print()
    
    # Show some special cases
    print("Some interesting special partitions:")
    print("-" * 40)
    
    special_partitions = [
        ([100], "Single part"),
        ([50, 50], "Two equal parts"),
        ([99, 1], "Nearly all in one part"),
        ([25, 25, 25, 25], "Four equal parts"),
        ([20, 20, 20, 20, 20], "Five equal parts"),
        ([10] * 10, "Ten parts of 10 each"),
        ([5] * 20, "Twenty parts of 5 each"),
        ([1] * 100, "One hundred parts of 1 each"),
    ]
    
    for i, (partition, description) in enumerate(special_partitions, 1):
        partition_str = " + ".join(map(str, partition))
        print(f"{i}: {partition_str}")
        print(f"   ({description})")
    print()
    
    # Show partitions with constraints
    print("Partitions with specific constraints:")
    print("-" * 40)
    
    # Partitions using only 2's and 3's
    print("\n1. Partitions using only 2's and 3's:")
    partitions_23 = []
    for threes in range(100//3 + 1):
        remainder = 100 - 3*threes
        if remainder % 2 == 0:
            twos = remainder // 2
            if threes > 0 or twos > 0:  # non-empty
                partition = [3] * threes + [2] * twos
                partitions_23.append(partition)
    
    print(f"Found {len(partitions_23)} partitions using only 2's and 3's:")
    for i, partition in enumerate(partitions_23, 1):
        partition_str = " + ".join(map(str, partition))
        print(f"  {i:2d}: {partition_str}")
    print()
    
    # Partitions with exactly 5 parts
    print("2. First 10 partitions with exactly 5 parts:")
    count = 0
    for partition in generate_partitions(100):
        if len(partition) == 5:
            count += 1
            partition_str = " + ".join(map(str, partition))
            print(f"  {count:2d}: {partition_str}")
            if count >= 10:
                break
    print()
    
    # Partitions into distinct parts
    print("3. First 10 partitions into distinct parts:")
    count = 0
    for partition in generate_partitions(100):
        if len(partition) == len(set(partition)):  # all parts distinct
            count += 1
            partition_str = " + ".join(map(str, partition))
            print(f"  {count:2d}: {partition_str}")
            if count >= 10:
                break
    print()
    
    print(f"Summary: There are {total_count:,} ways to partition 100!")
    print("Each partition represents a different way to break 100 into positive integer parts.")

if __name__ == "__main__":
    main()
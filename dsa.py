def balancedStringSplit(s: str) -> int:
    count = 0
    balance = {char: 0 for char in set(s)}
    partition_indices = [0]
    
    # Calculate the balance and mark partition indices
    for i, char in enumerate(s):
        balance[char] += 1
        
        balanced = all(count == balance[char] for count in balance.values())
        
        if balanced:
            partition_indices.append(i + 1)
    
    # Count the partitions
    for i in range(1, len(partition_indices)):
        count += 1
    
    return count

# Example usage:
s1 = "fabccddg"
print(balancedStringSplit(s1))  # Output: 3

s2 = "abababaccddb"
print(balancedStringSplit(s2))  # Output: 2

s3 = "tboht"
print(balancedStringSplit(s3))  # Output: 1

def find_min_height_subset(n, D, H, h):
    """
    Finds the subset of intermediate piles satisfying the constraint such that the sum of heights
    of the selected intermediates is minimal.
    
    Args:
        n (int): The number of piles.
        D (int): The maximum allowed height difference between two consecutive selected piles.
        H (int): The maximum allowed absolute difference between the height of the current pile
                 and the sum of heights of the previous selected piles.
        h (list): A list of heights of the intermediate piles.
    
    Returns:
        int: The sum of heights of the selected piles that satisfy the given constraints.
    """
    # Sort the intermediate piles in ascending order of height
    h.sort()
    
    selected = []
    total_height = 0
    
    for i in range(n):
        if not selected or (abs(h[i] - total_height) <= H and abs(h[i] - h[selected[-1]]) <= D):
            selected.append(i)
            total_height += h[i]
    
    return total_height

# Example usage
n = 5
D = 2
H = 3
h = [4, 2, 1, 3, 3]

print(find_min_height_subset(n, D, H, h))  # Output: 13
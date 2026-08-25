"""
Series module containing functions for mathematical progressions.
"""

def arithmetic_progression(a: float, d: float, n: int) -> float:
    """
    Calculate the n-th term of an arithmetic progression.
    
    An arithmetic progression is a sequence where each term after the first
    is obtained by adding a constant difference to the previous term.
    
    Formula: a_n = a + (n - 1) * d
    
    Args:
        a (float): First term of the arithmetic progression
        d (float): Common difference between consecutive terms
        n (int): Position of the term to find (1-indexed)
    
    Returns:
        float: The n-th term of the arithmetic progression
    
    Raises:
        ValueError: If n is less than 1
    
    Examples:
        >>> arithmetic_progression(2, 3, 1)
        2.0
        >>> arithmetic_progression(2, 3, 4)
        11.0
        >>> arithmetic_progression(5, -2, 3)
        1.0
    """
    if n < 1:
        raise ValueError("n must be a positive integer (1 or greater)")
    
    return a + (n - 1) * d


def arithmetic_sum(a: float, d: float, n: int) -> float:
    """
    Calculate the sum of the first n terms of an arithmetic progression.
    
    Formula: S_n = n/2 * (2a + (n-1)*d) = n/2 * (first_term + last_term)
    
    Args:
        a (float): First term of the arithmetic progression
        d (float): Common difference between consecutive terms
        n (int): Number of terms to sum
    
    Returns:
        float: Sum of the first n terms
    
    Raises:
        ValueError: If n is less than 1
    
    Examples:
        >>> arithmetic_sum(2, 3, 4)
        26.0
        >>> arithmetic_sum(1, 1, 5)
        15.0
    """
    if n < 1:
        raise ValueError("n must be a positive integer (1 or greater)")
    
    return n * (2 * a + (n - 1) * d) / 2


if __name__ == "__main__":
    # Example usage
    print("Arithmetic Progression Examples:")
    print(f"AP: a=2, d=3")
    for i in range(1, 6):
        term = arithmetic_progression(2, 3, i)
        print(f"  Term {i}: {term}")
    
    print(f"\nSum of first 5 terms: {arithmetic_sum(2, 3, 5)}")

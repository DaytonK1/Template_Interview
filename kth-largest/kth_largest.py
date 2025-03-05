def kth_largest_number(A, k):
    ''' Returns K large elements in decreasing order '''
    # Sort the array in ascending order
    A.sort()
    
    # Select the last K elements (which are the largest)
    k_largest = A[-k:]
    
    # Reverse the list to get the elements in decreasing order
    k_largest.reverse()
    
    return k_largest

def get_user_input():
    try:
        # Input for the number of elements in the array
        N = int(input("Enter the number of elements in the array (N): "))
        if N < 1 or N > 10**5:
            raise ValueError("N must be between 1 and 10^5.")
        
        # Input for the array elements
        Arr = []
        print(f"Enter the {N} elements of the array:")
        for i in range(N):
            element = int(input(f"Element {i + 1}: "))
            if element < 1 or element > 10**6:
                raise ValueError("Array elements must be between 1 and 10^6.")
            Arr.append(element)
        
        # Input for the number of largest elements to find
        K = int(input("Enter the number of largest elements to find (K): "))
        if K < 1 or K > N:
            raise ValueError(f"K must be between 1 and {N}.")
        
        return Arr, K
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None

# Main program
if __name__ == "__main__":
    Arr, K = get_user_input()
    if Arr is not None and K is not None:
        result = kth_largest_number(Arr, K)
        print(f"The {K} largest elements in decreasing order are: {result}")
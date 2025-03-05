def reverse_string(str):
    '''Reverse string in-place using O(1) extra memory'''
    left, right = 0, len(str) - 1
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return str

# Simple test cases
if __name__ == "__main__":
    test_cases = ["hello", "world",]
    
    for test in test_cases:
        chars = list(test)
        print(f"Original: {test}")
        print(f"Reversed: {''.join(reverse_string(chars))}\n")
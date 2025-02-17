"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x - 1) + foo(x - 2)

def longest_run(mylist, key):
    max_run = 0
    current_run = 0
    for num in myarray:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    """
    Recursively computes the longest continuous sequence of `key` in `myarray`
    using a divide and conquer strategy with the provided `Result` class and `to_value`.
    """
    def helper(arr):
        n = len(arr)
        # Base case: empty array – by convention, empty range is considered "entire"
        if n == 0:
            return Result(0, 0, 0, True)
        # Base case: single element array
        if n == 1:
            if arr[0] == key:
                return Result(1, 1, 1, True)
            else:
                return Result(0, 0, 0, False)
        
        # Divide the array into two halves
        mid = n // 2
        left_result = helper(arr[:mid])
        right_result = helper(arr[mid:])
        
        # Combine left_size:
        # If the entire left segment is the key, extend its left run with the right segment's left run.
        if left_result.is_entire_range:
            combined_left_size = left_result.left_size + right_result.left_size
        else:
            combined_left_size = left_result.left_size
        
        # Combine right_size:
        # If the entire right segment is the key, extend its right run with the left segment's right run.
        if right_result.is_entire_range:
            combined_right_size = right_result.right_size + left_result.right_size
        else:
            combined_right_size = right_result.right_size
        
        # The longest run in the combined segment may be:
        # - entirely in the left segment,
        # - entirely in the right segment,
        # - or crossing the boundary (left's right run + right's left run).
        combined_longest_size = max(left_result.longest_size,
                                    right_result.longest_size,
                                    left_result.right_size + right_result.left_size)
        
        # The combined segment is entirely the key if both halves are entirely the key.
        combined_is_entire_range = left_result.is_entire_range and right_result.is_entire_range
        
        return Result(combined_left_size, combined_right_size, combined_longest_size, combined_is_entire_range)
    
    # Use to_value to return the longest run from the Result object.
    return to_value(helper(myarray))




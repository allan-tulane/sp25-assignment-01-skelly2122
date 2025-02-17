

# CMPS 2200 Assignment 1

Name: Samuel Kelly

In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in main.py. You are welcome to edit this assignment-01.md file directly, or print and fill in by hand. If you do the latter, please scan to a file assignment-01.pdf and push to your github repository.

(2 pts ea) Asymptotic notation (12 pts)
1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

Yes, if we choose c=2, we see that for every n, f(n) = 2 * g(n) holds true. So, even though 2^n+1 is exactly twice 2^n, that constant factor does not change the overall growth rate as n increases. The mutiplicative constant is ignored in big-O notation. Therefore, 2^(n+1) is in O(2^n).

1b. Is $2^{2^n} \in O(2^n)$? Why or why not?

No, 2^(2^n) is not in O(2^n) because 2^(2^n) grows double-exponentially while 2^n grows only exponentially. This means that for any constant c, there exists some n such that 2^(2^n) > c · 2^n, so 2^(2^n) cannot be bounded above by a constant multiple of 2^n for large n.

1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?

No, n^(1.01) is not in O(log² n) because polynomial growth (even with a small exponent like 1.01) will eventually dominate the squared logarithmic growth. Formally, there is no constant c such that for all sufficiently large n, n^(1.01) ≤ c·(log n)².

1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?

Yes, because a polynomial with exponent 1.01 outpaces the squared logarithmic function, n^(1.01) ∈ Ω((log n)²).

1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?

No it is not, When multiplying logn^3 by a constant, it eventually will be less than n^1/2 with a large enough range. We know this because the lim as n goes to infinity of f(n)/g(n) the reuslt is infinity, indicating f(n) is not in O(g(n)). Therefore, n^1/2 is not in O((logn)^3).

1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?

Yes, as n approaches infinity, sqrt(n) increases without bound much faster than (logn)^3 does. Therefore sqrt(n) eventually dominates (logn)^3. No matter the constant factor applied to (logn)^3.

# ============================================================
# 2. SPARC to Python
# ============================================================

# 2a. Python Translation

# 2b. Explanation:
# This function computes the Fibonacci number at position `x`.
# For x = 0 or x = 1, it simply returns x (since F(0)=0 and F(1)=1).
# For x > 1, it recursively computes the sum of the two preceding Fibonacci numbers.
# In effect, it generates the Fibonacci sequence where each number is the sum of the two previous ones.


# ============================================================
# 3. Parallelism and Recursion
# ============================================================

# 3a. Iterative, Sequential Implementation of longest_run
def longest_run(myarray, key):
    max_run = 0
    current_run = 0
    for num in myarray:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run

# 3b. Work and Span of the Iterative Implementation:
# Work: O(n) - We process each element of the array once.
# Span: O(n) - The loop processes elements sequentially.

# 3c. Recursive, Divide and Conquer Implementation

# Helper class to store intermediate results
class Result:
    def __init__(self, total, prefix, suffix, best):
        self.total = total    # Total length of the segment
        self.prefix = prefix  # Length of the contiguous run of key from the beginning
        self.suffix = suffix  # Length of the contiguous run of key from the end
        self.best = best      # Longest run of key found anywhere in the segment

def longest_run_recursive(myarray, key):
    """
    Recursively computes the longest continuous sequence of `key` in `myarray`
    using a divide and conquer strategy.
    """
    def helper(arr):
        n = len(arr)
        # Base case: empty array
        if n == 0:
            return Result(0, 0, 0, 0)
        # Base case: single element array
        if n == 1:
            if arr[0] == key:
                return Result(1, 1, 1, 1)
            else:
                return Result(1, 0, 0, 0)
        # Divide the array into two halves
        mid = n // 2
        left_result = helper(arr[:mid])
        right_result = helper(arr[mid:])
        # Combine the results from the two halves
        total = left_result.total + right_result.total
        # Compute the prefix: if the left segment is entirely key, then extend with right.prefix.
        if left_result.prefix == left_result.total:
            prefix = left_result.total + right_result.prefix
        else:
            prefix = left_result.prefix
        # Compute the suffix: if the right segment is entirely key, then extend with left.suffix.
        if right_result.suffix == right_result.total:
            suffix = right_result.total + left_result.suffix
        else:
            suffix = right_result.suffix
        # The best run may be in the left, in the right, or crossing the boundary.
        best = max(left_result.best, right_result.best, left_result.suffix + right_result.prefix)
        return Result(total, prefix, suffix, best)
    return helper(myarray).best

# 3d. Work and Span of the Sequential Recursive Algorithm:
# Work: O(n) - Every element is examined exactly once in the recursive merge process.
# Span: O(n) - Because the recursive calls are made sequentially (one after the other in the worst-case), 
# the span is proportional to the number of elements.

# 3e. Work and Span with Parallelization:
# If we parallelize the two recursive calls (each executed on a separate thread):
# Work: O(n) - The total work remains unchanged.
# Span: O(log n) - The recursion tree height becomes O(log n) since the two halves are processed concurrently.

# ============================================================
# Optional: Test Code
# ============================================================
if __name__ == '__main__':
    # Testing the Fibonacci function (foo)
    print("Fibonacci of 10:", foo(10))  # Expected: 55
    # Testing the iterative longest_run function
    test_array = [2, 12, 12, 8, 12, 12, 12, 0, 12, 1]
    print("Longest run of 12 (iterative):", longest_run(test_array, 12))  # Expected: 3
    # Testing the recursive longest_run_recursive function
    print("Longest run of 12 (recursive):", longest_run_recursive(test_array, 12))  # Expected: 3


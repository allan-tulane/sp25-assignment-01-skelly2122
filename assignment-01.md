

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

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

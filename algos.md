# Algorithms  

## Dynamic Programming  

(Cormen, 3rd Ed.)

1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.  
   - *optimal substructure*: optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently  
   - [數學歸納法 mathematical induction](https://youtu.be/hyvTl036PmA?t=86): 1. 起始步驟; *2. 歸納步驟*  
3. Compute the value of an optimal solution: bottom-up or top-down with memo.
4. Construct an optimal solution from computed information.  

### Rod-cutting

1. We can cut up a rod of length $n$ in $2^{n-1}$ different ways:  
  if cut into $n$ pieces, there'd be $n-1$ cuts, for each cut either cut or no cut therefore $2^{n-1}$.  

2. optimal revenue $r_n = max_{1⩽i⩽n}(p_i+r_{n-i})$, with $r_0 = 0$  

### Matrix-chain Multiplication

- If $A_{i...k}$ and $A_{k+1...j}$ are both optimal, then $A_{i...k}\cdot A_{k+1...j}$ is optimal  

- $m_{i...j} = min_{i⩽k<j} (m_{i...k}+m_{k+1...j}+p_{i-1}{p_k}p_j)$

## Complexity

- [Is log a polynomial?](https://www.quora.com/Is-log-a-polynomial)  
  no, but it's polynomial bound.  

## Solutions

### LIS

LeetCode [300](https://leetcode.com/problems/longest-increasing-subsequence/), [673](https://leetcode.com/problems/number-of-longest-increasing-subsequence/), [1713](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/)  

#### BF: O ($2^n$)

#### [DP: O ($n^2$)](https://youtu.be/7DKFpWnaxLI?t=630)  

```Python
lis [k] = 0
for i in range (k):
    if a [k] > a [i]:
        lis [k] = max (lis [k], lis [i] + 1)
```

#### [DP + Greedy + Bin Srch: O ($n$log$n$)](https://youtu.be/l2rCz7skAlk?t=369)  

```Python
def idx (dp, p):
    # return where in dp the element is least but larger than p

dp = [a [0]]
for i in range (1, len (a)):
    j = idx (dp, i)
    if j < len (dp):
        dp [j] = a [i]
    else:
        dp.append (a [i])
```

- binary (92ms) and sequental (comment, 248ms) search implementations of ```idx()```

```Python
def idx (dp, p):
    # for j in range (len (dp)):
    #     if dp [j] >= p:
    #         return j
    # return len (dp)
    lb = 0
    ub = len (dp) - 1
    while (lb <= ub):
        md = (lb + ub)//2
        if dp [md] == p:
            return md
        elif dp [md] > p:
            ub = md - 1
        else:
            lb = md + 1
    return lb
```

## 教學

- [Sort Scale](http://163.22.72.196/html5/html5_sort_scale/sort_scale.html)  

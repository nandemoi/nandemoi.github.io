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

(Cormen, 3rd Ed.)

1. We can cut up a rod of length $n$ in $2^{n-1}$ different ways:  
  if cut into $n$ pieces, there'd be $n-1$ cuts, for each cut either cut or no cut therefore $2^{n-1}$.  

2. optimal revenue $r_n = max_{1⩽i⩽n}(p_i+r_{n-i})$, with $r_0 = 0$  

3. 

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

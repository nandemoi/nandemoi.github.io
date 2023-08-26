# Algorithms  

## Dynamic Programming  

### [Subset Sum Problem](https://www.youtube.com/watch?v=s6FhG--P7z0)

Exhaustive: O ($2^n$) vs. DP: O ($n \times sum$)

$S_{sum,j} = S_{sum,j-1} \lor S_{sum - {\color{red}A_j},j-1}$ (from a lost link)

<img src="https://nandemoi.github.io/slides/subset_sum.png" alt="subset_sum" width="600">

```C++
    for (unsigned k = 1; k < w + 1; k++) {

        abSubsetS [k][0] = false;
        vuit vitS = viS.begin ();
        bool bS = false;
        for (unsigned l = 1; l < viS.size (); l++, vitS++) {
            if (k >= *vitS)
                abSubsetS [k][l] = abSubsets [k][l - 1] ||
                                    abSubsetS [k - *vitS][l - 1];
            else
                abSubsetS [k][l] = abSubsetS [k][l - 1];
            if (abSubsets [k][l])
                bS = true;
        }

        // repeat the code paragraph above replaceing ending S's with D's
        
        if (bS && bD)
            uMaxAns = k;
    }
```

### Problems
Fibonacci
[棋盤格城市](https://zerojudge.tw/ShowProblem?problemid=l581)
knapsack
[台中女中程式解題](https://web.archive.org/web/20210923030209/http://www.tcgs.tc.edu.tw:1218/Problems?tab=tab01&page=2)

[LCS video by Abdul Bari](https://www.youtube.com/watch?v=sSno9rV8Rhg)
[Kattis: Alphabet/a solution](https://open.kattis.com/problems/alphabet)

Cormen:
rod cutting (2009)
matrix-chain multiplication
LCS
binsearch tree (2009)
polygon triangulation (1990)
+6 (1990) +12 (2009)

### Notes

* [CMU Dynamic Programming Lecture notes](https://www.cs.cmu.edu/~avrim/451f09/lectures/lect1001.pdf)

* (Cormen)
  1. Characterize the structure of an optimal solution.
  2. Recursively define the value of an optimal solution.  
     - *optimal substructure*: optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently  
     - [數學歸納法 mathematical induction](https://youtu.be/hyvTl036PmA?t=86): 1. 起始步驟; *2. 歸納步驟*  
  3. Compute the value of an optimal solution: bottom-up or top-down with memo.
  4. Construct an optimal solution from computed information.  

#### [Shortest path algorithms](https://cgi.luddy.indiana.edu/~yye/c343-2019/shortest.php)
[Difference Between BFS and Dijkstra’s Algorithms](https://www.baeldung.com/cs/graph-algorithms-bfs-dijkstra)
[Difference between BFS and Dijkstra’s algorithms when looking for shortest path? - GeekforGeeks](https://www.geeksforgeeks.org/difference-between-bfs-and-dijkstras-algorithms-when-looking-for-shortest-path/)
[What is difference between BFS and Dijkstra's algorithms when looking for shortest path? - Stack Overflow](https://stackoverflow.com/questions/25449781/what-is-difference-between-bfs-and-dijkstras-algorithms-when-looking-for-shorte)

### Rod-cutting

1. We can cut up a rod of length $n$ in $2^{n-1}$ different ways:  
  if cut into $n$ pieces, there'd be $n-1$ cuts, for each cut either cut or no cut therefore $2^{n-1}$.  

2. optimal revenue $r_n = max_{1⩽i⩽n}(p_i+r_{n-i})$, with $r_0 = 0$  

### Matrix-chain Multiplication

- If $A_{i...k}$ and $A_{k+1...j}$ are both optimal, then $A_{i...k}\cdot A_{k+1...j}$ is optimal  

- $m_{i...j} = min_{i⩽k<j} (m_{i...k}+m_{k+1...j}+p_{i-1}{p_k}p_j)$

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

## [Genetic Algorithm](https://www.geeksforgeeks.org/genetic-algorithms/)

## Complexity

- [Is log a polynomial?](https://www.quora.com/Is-log-a-polynomial)  
  no, but it's polynomial bound.  

<!--## 教學

- [Sort Scale](http://163.22.72.196/html5/html5_sort_scale/sort_scale.html)-->  


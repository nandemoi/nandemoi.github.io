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

# [CNOT Gate](https://qiskit.org/textbook/ch-gates/multiple-qubits-entangled-states.html#cnot)  

If $q_0 = \ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $q_1 = \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, ($q_1$ being the controlling qubit),  

$q_1q_0 = \ket{10} =$ <span style="color:red">$\ket{1} \otimes \ket{0} =
\begin{pmatrix} 0 \times \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\ 
                1 \times \begin{pmatrix} 1 \\ 0 \end{pmatrix} \end{pmatrix} $</span> $=
\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$  

$a_{00} = 0, a_{01} = 0, a_{10} = 1, a_{11} = 0,$ so

$CNOT|1$<span style="color:red">$0$</span>$\rangle =
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
\begin{pmatrix} a_{00} \\ a_{01} \\ a_{10} \\ a_{11} \end{pmatrix} =
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} = 
\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix},
i.e. |1$<span style="color:red">$1$</span>$\rangle$ by below

likewise,

$\ket{00} =\ket{0} \otimes \ket{0} =
\begin{pmatrix} 1 \times \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\
                0 \times \begin{pmatrix} 1 \\ 0 \end{pmatrix} \end{pmatrix} =
\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$

$CNOT|0$<span style="color:red">$0$</span>$\rangle =
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} = 
\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} =
|0$<span style="color:red">$0$</span>$\rangle$

$\ket{01} =\ket{0} \otimes \ket{1} =
\begin{pmatrix} 1 \times \begin{pmatrix} 0 \\1 \end{pmatrix} \\
                0 \times \begin{pmatrix} 0 \\ 1 \end{pmatrix} \end{pmatrix} =
\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$

$CNOT|0$<span style="color:red">$1$</span>$\rangle =
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} = 
\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} =
|0$<span style="color:red">$1$</span>$\rangle$

$\ket{11} =\ket{1} \otimes \ket{1} =
\begin{pmatrix} 0 \times \begin{pmatrix} 0 \\1 \end{pmatrix} \\
                1 \times \begin{pmatrix} 0 \\ 1 \end{pmatrix} \end{pmatrix} =
\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$

$CNOT|1$<span style="color:red">$1$</span>$\rangle =
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = 
\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} =
|1$<span style="color:red">$0$</span>$\rangle$

但是請注意：$a_{00}, a_{01}, a_{10}, a_{11}$ 可能是滿足 $a_{00}^2 + a_{01}^2 + a_{10}^2 + a_{11}^2 = 1$ 的任何實數組合 (各 qubit 可能有不同的疊加態)

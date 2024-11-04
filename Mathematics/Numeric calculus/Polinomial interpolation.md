
![[polinomial_interp.png]]

There are a couple of proofs for polinomial interpolation. We are going to use the one with the *Vandermonde* matrix:
``
$$
p(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{2}x^{2} + a_{1}x + a_{0}. \tag{1}
$$
Substituting this into the interpolation equations
$$
p(x_{j}) = y_{j},
$$
we get a system of linear equations in the coefficients $a_{j}$, which reads in matrix-vector form as the following multiplication:

$$
\begin{bmatrix}
x_{0}^{n} & x_{0}^{n-1} & x_{0}^{n-2} & \ldots & x_{0} & 1 \\
x_{1}^{n} & x_{1}^{n-1} & x_{1}^{n-2} & \ldots & x_{1} & 1 \\
\vdots & \vdots & \vdots & & \vdots & \vdots \\
x_{n}^{n} & x_{n}^{n-1} & x_{n}^{n-2} & \ldots & x_{n} & 1 
\end{bmatrix}
\begin{bmatrix}
a_{n} \\
a_{n-1} \\
\vdots \\
a_{0}
\end{bmatrix}
=
\begin{bmatrix}
y_{0} \\
y_{1} \\
\vdots \\
y_{n}
\end{bmatrix}.
$$

An interpolant $p(x)$ corresponds to a solution $A = (a_{n}, \ldots, a_{0})$ of the above matrix equation 
$$
X \cdot A = Y.
$$
The matrix $X$ on the left is a Vandermonde matrix, whose determinant is known to be 
$$
\textstyle \det(X) = \prod_{1 \leq i < j \leq n} (x_{j} - x_{i}),
$$
which is non-zero since the nodes $x_{j}$ are all distinct. This ensures that the matrix is invertible and the equation has the unique solution 
$$
A = X^{-1} \cdot Y; \text{ that is, } p(x) \text{ exists and is unique.}$$

Example:
Given $f(x) = \sqrt(5 x^2 + 4)$

Find the polinomial with the minimal order of the function with 5 restrictions. => $gr(p)$ <= $4$

We propose that:

$p(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4$

We look that it satisfies the conditions:

- $p(-1) = f(-1)$
- $p(0) = f(0)$
- $p(1) = f(1)$
- $p'(0) = f'(0)$
- $p'(1) = f'(1)$

this defines de vandermonde matrix, which we have to invert.

To calculate the error:[[Error in Polinomial interpolation]]

$f(x) - p(x) = \frac{f^{5}(\theta)}{5!} (x+1) x^2 (x-1)^2$ $\forall x \in [-1,1]$ 

Example 2: 


$$
S(x) =
\begin{cases}
S_a = a_0 + a_1 (x+1 )+ a_2 (x+1)^2+ a_3 (x+1)^3& \text{if } x \in [-1,0)  \\
S_b = b_0 + b_1 x + b_2 x^2 + b_3 x^3 & \text{if } x \in [-0,1) \\
S_c = c_0 + c_1 (x-1) + c_2 (x-1)^2 + c_3 (x-1)^3 & \text{if } x \in [1,2] 
\end{cases}
$$

Then, we get the equation set:

$$
\begin{cases}
S_a (-1) = -6\\
S_a (0) = -5\\
S_a (1) = -5\\
S_a (2) = -6\\
 
\end{cases}
$$

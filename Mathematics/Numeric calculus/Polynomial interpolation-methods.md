
## Undetermined coefficients:

Uses the Vandermonde matrix for a polynomial:
$$p(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{2}x^{2} + a_{1}x + a_{0}. \tag{1}$$
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

Consider the following set:

| x   | -1  | 0   | 1   |     |
| --- | --- | --- | --- | --- |
| y   | 12  | 5   | 4   |     |

$n=2$ so $P_2(x) = a_0 + a_1 x + a_2 x^2$ 

Evaluating the polynomial we get the matrix and the system:
$$
\begin{bmatrix}
 1& -1& 1 \\
 1& 0&  0\\
1& 1& 1
\end{bmatrix}
\begin{bmatrix}
a_{0} \\
a_{1} \\
a_{2}
\end{bmatrix}
=
\begin{bmatrix}
12 \\
5 \\
4
\end{bmatrix}.
$$
Solving the system we find $a_0 = 5$ , $a_1 = -4$ and $a_2 = 3$ :

$\rightarrow P_2(x) = 5 -4x +3x^2$ 

## Lagrange's form:

The Lagrange polynomial $L(x)$ of degree $n$ is given by:

$$L(x) = \sum_{i=0}^{n} y_i \cdot l_i(x)$$

where each **Lagrange basis polynomial** $l_i(x)$ is defined as:

$$l_i(x) = \prod_{\substack{0 \le j \le n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}$$

But a more friendly way of seeing it is:
$$
l_j(x) =
\begin{cases}
1& i = j \\
0& i \neq j
\end{cases}
$$

In expanded form, this becomes:

$$L(x) = y_0 \cdot \frac{(x - x_1)(x - x_2) \cdots (x - x_n)}{(x_0 - x_1)(x_0 - x_2) \cdots (x_0 - x_n)} + 
       y_1 \cdot \frac{(x - x_0)(x - x_2) \cdots (x - x_n)}{(x_1 - x_0)(x_1 - x_2) \cdots (x_1 - x_n)} + \cdots +
       y_n \cdot \frac{(x - x_0)(x - x_1) \cdots (x - x_{n-1})}{(x_n - x_0)(x_n - x_1) \cdots (x_n - x_{n-1})}$$

IE:  

| x   | -1  | 0   | 1   |
| --- | --- | --- | --- |
| y   | 12  | 5   | 4   |

$n = 2$ $\rightarrow P_2(x) = y_0 l_0(x) + y_1 l_1(x) + y_2 l_2(x)$
$P_2(x) = 5 l_0 (x) + 4 l_1(x) + 9 l_2(x)$

The polynomial $l_0$ is calculated with the explicit equation above:

$$l_0(x) = \frac{(x-0) (x-1)}{(-1-0)(-1-1)} = \frac{x (x-1)}{2} $$

The rest of the $l$ polynomials are calculated accordingly. In the end one gets:

$$P_2(x)= \frac{12}{2} x(x-1) - 5 (x+1)(x-1) + 2 x(x+1) $$

|     |
| --- |
## Newton's form:

![[newt_int.png]]
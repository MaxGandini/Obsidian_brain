# Newton Interpolation

## Theorem

For a polynomial $p_n$ of degree less than or equal to $n$, that interpolates $f$ at the nodes $x_i$ where $i=0,1,2,3,\cdots,n$. Let $p_{n+1}$ be the polynomial of degree less than or equal to $n+1$ that interpolates $f$ at the nodes $x_i$ where $i=0,1,2,3,\cdots,n,n+1$. Then $p_{n+1}$ is given by:

$$
p_{n+1}(x) = p_n(x) + a_{n+1}w_n(x)
$$

where 

$$
w_n(x) := \prod_{i=0}^{n}(x-x_i)
$$ 

also known as Newton basis and 

$$
a_{n+1} := \frac{f(x_{n+1}) - p_n(x_{n+1})}{w_n(x_{n+1})}.
$$

## Proof:

This can be shown for the case where $i=0,1,2,3,\cdots,n$:

$$
p_{n+1}(x_{i}) = p_n(x_{i}) + a_{n+1}\prod_{j=0}^{n}(x_{i}-x_{j}) = p_n(x_{i})
$$

and when $i=n+1$:

$$
p_{n+1}(x_{n+1}) = p_n(x_{n+1}) + \frac{f(x_{n+1}) - p_n(x_{n+1})}{w_n(x_{n+1})}w_n(x_{n+1}) = f(x_{n+1}).
$$ 

By the uniqueness of interpolated polynomials of degree less than $n+1$, 

$$
p_{n+1}(x) = p_n(x) + a_{n+1}w_n(x)
$$ 

is the required polynomial interpolation. The function can thus be expressed as:

$$
p_n(x) = a_{0} + a_{1}(x-x_{0}) + a_{2}(x-x_{0})(x-x_{1}) + \cdots + a_{n}(x-x_{0})\cdots (x-x_{n-1}).
$$

## Polynomial coefficients

To find $a_i$, we have to solve the lower triangular matrix formed by arranging 

$$
p_n(x_{i}) = f(x_{i}) = y_{i}
$$ 

from above equation in matrix form:

$$
\begin{bmatrix} 1 & \ldots & 0 \\ 1 & x_{1}-x_{0} & \\ 1 & x_{2}-x_{0} & (x_{2}-x_{0})(x_{2}-x_{1}) & \vdots \\ \vdots & \vdots & \ddots & \\ 1 & x_{k}-x_{0} & \ldots & \prod_{j=0}^{n-1}(x_{n}-x_{j}) \end{bmatrix}
\begin{bmatrix} a_{0} \\ \vdots \\ a_{n} \end{bmatrix} = \begin{bmatrix} y_{0} \\ \vdots \\ y_{n} \end{bmatrix}.
$$

The coefficients are derived as

$$
a_j := [y_{0}, \ldots, y_{j}]
$$

where 

$$
[y_{0}, \ldots, y_{j}]
$$ 

is the notation for divided differences. Thus, Newton polynomials are used to provide a polynomial interpolation formula of $n$ points.
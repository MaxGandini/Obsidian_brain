# Error in Polynomial Interpolation

To calculate the difference between a polynomial interpolation $p(x)$ and the actual function $f(x)$, you can use the **remainder term** in the interpolation error formula. 

The general formula for the error in polynomial interpolation is given by:

$$
E(x) = f(x) - p(x) = \frac{f^{(n+1)}(\theta)}{(n+1)!} \prod_{i=0}^{n} (x - x_i),
$$

where:
- $E(x)$ is the interpolation error at the point $x$.
- $f^{(n+1)}(\theta)$ is the $(n+1)$-th derivative of the function $f$ evaluated at some point $\theta$ in the interval containing $x$ and the interpolation nodes $x_0, x_1, \ldots, x_n$.
- $(n+1)!$ is the factorial of $n+1$.
- The product $\prod_{i=0}^{n} (x - x_i)$ represents the product of the differences between $x$ and each of the interpolation nodes $x_i$.

## Example

If you specifically know the polynomial $p(x)$ is obtained using a degree 4 polynomial (meaning $n = 4$), you can rewrite the error formula as:

$$
E(x) = f(x) - p(x) = \frac{f^{(5)}(\theta)}{5!} \prod_{i=0}^{4} (x - x_i),
$$

where $\prod_{i=0}^{4} (x - x_i) = (x - x_0)(x - x_1)(x - x_2)(x - x_3)(x - x_4)$.

## Conclusion

This error term indicates that the difference between the actual function and the polynomial interpolation depends not only on the behavior of the function (as reflected in its higher-order derivatives) but also on how far the interpolation point $x$ is from the nodes. The closer $x$ is to the interpolation nodes, the smaller the error is likely to be, especially if $f(x)$ is smooth.

![[newton_raphson.png]]

The method consists in approximating the value of a function starting from an initial guess.

1. **Initial Guess**: Start with an initial guess \( x_0 \) close to the root.

2. **Linear Approximation**: At the point \( (x_0, f(x_0)) \), the equation of the tangent line can be given by:
   $$
   y = f(x_0) + f'(x_0)(x - x_0)
   $$
   where \( f'(x_0) \) is the derivative of \( f \) at \( x_0 \).

3. **Finding the X-Intercept**: To find where this tangent line intersects the x-axis (i.e., where \( y = 0 \)):
   $$
   0 = f(x_0) + f'(x_0)(x - x_0)
   $$
   Rearranging gives:
   $$
   x = x_0 - \frac{f(x_0)}{f'(x_0)}
   $$
   This gives the next approximation \( x_1 \).

4. **Iteration**: Repeat this process using the new approximation:
   $$
   x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
   $$
## Convergence Considerations

- The Newton-Raphson method converges quickly when the initial guess is close to the actual root, typically exhibiting quadratic convergence.
- However, it can fail to converge or converge to the wrong root if the initial guess is poor or if \( f'(x) = 0 \) at any point during the iterations.


Gaussian Quadrature is a method of approximating definite integrals by choosing optimal points (nodes) and weights for the function. It is especially useful for polynomial functions, as it gives exact results for polynomials up to degree $2n-1$ with $n$ points.

The integral $\int_a^b f(x) \, dx$ can be approximated as:

$$\int_a^b f(x) \, dx \approx \sum_{i=1}^n w_i f(x_i)$$

where $x_i$ are the nodes and $w_i$ are the weights determined based on the interval and the degree of precision desired.

For the interval $[-1, 1]$, the nodes $x_i$ and weights $w_i$ can be derived from **Legendre polynomials**.

### Example for 2-point Gaussian Quadrature

Using 2 points for the interval $[-1, 1]$, we have:

$$\int_{-1}^1 f(x) \, dx \approx w_1 f(x_1) + w_2 f(x_2)$$

with nodes $x_1 = -\frac{1}{\sqrt{3}}$ and $x_2 = \frac{1}{\sqrt{3}}$, and weights $w_1 = w_2 = 1$.

For an arbitrary interval $[a, b]$, a change of variable can be applied:

$$\int_a^b f(x) \, dx = \frac{b - a}{2} \sum_{i=1}^n w_i f\left( \frac{b - a}{2} x_i + \frac{b + a}{2} \right)$$

---
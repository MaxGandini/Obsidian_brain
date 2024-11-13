
The Trapezoidal Rule is a simpler numerical integration technique that approximates the area under the curve by dividing the interval $[a, b]$ into $n$ subintervals and approximating each subinterval with a trapezoid.

For an integral $\int_a^b f(x) \, dx$, the approximation with $n$ intervals is:

$$\int_a^b f(x) \, dx \approx \frac{b - a}{2n} \left( f(a) + 2 \sum_{i=1}^{n-1} f(x_i) + f(b) \right)$$

where $x_i = a + i \cdot h$ and $h = \frac{b - a}{n}$ is the width of each subinterval.


For a single interval $[a, b]$, the Trapezoidal Rule simplifies to:

$$\int_a^b f(x) \, dx \approx \frac{b - a}{2} \left( f(a) + f(b) \right)$$

---

# Comparison

- **Gaussian Quadrature** is generally more accurate for polynomial functions, as it chooses optimal points and weights.
- **Trapezoidal Rule** is simpler and effective for functions that are approximately linear over small intervals, but may require many intervals for complex functions.
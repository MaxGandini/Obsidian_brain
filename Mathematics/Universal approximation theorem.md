There is not a single Universal approximation theorem, but a family of them. These theorems in general take a family of neural networks $\phi$, and state that there exists a sequence of neural nets : $\phi_1, \phi_2,...$ 
such that $\phi_n$ tends to $f$ a function.
Here, we are going to state the paradigmatic case, but bear in mind, there are many:

Arbitrary width:

Let $C(X, \mathbb{R}^m)$ denote the set of continuous functions from a subset $X$ of a Euclidean space $\mathbb{R}^n$ to a Euclidean space $\mathbb{R}^m$. Let $\sigma \in C(\mathbb{R}, \mathbb{R})$, where $(\sigma \circ x)_i = \sigma(x_i)$ denotes $\sigma$ applied to each component of $x$.

Then $\sigma$ is not a polynomial function if and only if, for every $n \in \mathbb{N}$, $m \in \mathbb{N}$, compact $K \subseteq \mathbb{R}^n$, $f \in C(K, \mathbb{R}^m)$, and $\varepsilon > 0$, there exist $k \in \mathbb{N}$, $A \in \mathbb{R}^{k \times n}$, $b \in \mathbb{R}^k$, and $C \in \mathbb{R}^{m \times k}$ such that:

$$ \sup_{x \in K} \|f(x) - g(x)\| < \varepsilon $$ where $$ g(x) = C \cdot (\sigma \circ (A \cdot x + b)). $$
This example is particularly important because it is the foundational theory for a [[Perceptron]] . These, generally use sigmoid(step) functions or functions such as the [[logistic function]] .

Also a very important example is the [[ReLU]] or rectified linear unit activation function.

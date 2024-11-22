[[polinomial_interpolation]]
powerlaw: A Python Package for Analysis of Heavy-Tailed Distributions

powerlaw is a toolbox using the statistical methods developed in Clauset et al. 2007 <http://arxiv.org/abs/0706.1062>_ and Klaus et al. 2011 <http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0019779>_ to determine if a probability distribution fits a power law. Academics, please cite as:

Jeff Alstott, Ed Bullmore, Dietmar Plenz. (2014). powerlaw: a Python package for analysis of heavy-tailed distributions. PLoS ONE 9(1): e85777 <http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0085777>_

Also available at arXiv:1305.0215 [physics.data-an] <http://arxiv.org/abs/1305.0215>_

Basic Usage:

For the simplest, typical use cases, this tells you everything you need to know:

```python
import powerlaw
data = array([1.7, 3.2 ...]) # data can be list or numpy array
results = powerlaw.Fit(data)
print(results.power_law.alpha)
print(results.power_law.xmin)
R, p = results.distribution_compare('power_law', 'lognormal')

For more explanation, understanding, and figures, see the paper, which illustrates all of powerlaw's features:
http://arxiv.org/abs/1305.0215
```

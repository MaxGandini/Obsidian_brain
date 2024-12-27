This tutorial provides a short introduction to multivariate transfer entropy (mTE) estimation. Wherever possible, we point to the literature for a more in-depth treatment of the topics discussed. For code examples see the [tutorial section](https://github.com/pwollstadt/IDTxl/wiki#tutorials) in the Wiki.

## IDTxl _mTE_ algorithm

### Input

IDTxl expects an input data set consisting of samples (i.e., observations or realisations) of at least two processes. IDTxl provides a flexible data structure which is compatible with different experimental/theoretical scenarios:
* samples can be collected over time as a time series;
* multiple replications of a single sample can be collected (a replication is intended as a physical or temporal copy of the process, or a single experimental trial);
* samples can be collected both over time and over replications to form an ensemble of time series, which is treated as a 3D structure. (See also [Wollstadt, 2014, PLOS 9(7)](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0102833) and [Gomez-Herrero, 2015, Entropy](http://www.mdpi.com/1099-4300/17/4/1958) for details on the estimation of TE from ensembles of time series.)

At the current stage, we assume that each process is sampled at discrete time steps and using the same sampling rate.

### Goal

For any given target process, the goal of _mTE_ estimation is to infer the **set** of source processes in the network (also denoted as 'parent' processes) that collectively contribute to the computation of the target's next state. These sources are defined as *relevant* for the target.

### Overview of mTE calculation and the greedy algorithm

TE quantifies the amount of information (i.e. the reduction of uncertainty) that the past of a source process _X_ provides about the current value of a target process _Y<sub>n</sub>_, in the context of  _Y_'s own past. In a multivariate setting, a _set_ of sources  _**X**_={_**X**<sub>i</sub>_, i=1,...,M} is provided. We define the mTE from  _**X**<sub>i</sub>_ to _Y_ as the information that the past of _**X**<sub>i</sub>_ provides about _Y<sub>n</sub>_, in the context of both _Y_'s past and all the other relevant sources in _**X**_. The challenge is then to define and identify the relevant sources. In principle, the mTE from _**X**<sub>i</sub>_ to _Y_ could be computed by conditioning on _all_ the other sources in the network, i.e., _**X**_ \ _**X**<sub>i</sub>_. However, in practice, the size of the conditioning set must be reduced in order to reduce the dimensionality of the problem (also described as tackling the 'curse of dimensionality'). The idea is to restrict the conditioning set by finding and including the 'relevant' sources only (i.e., the sources that participate with _X<sub>i</sub>_ in reducing the uncertainty about _Y<sub>n</sub>_, in the context of  _Y_'s own past) . The set of relevant sources will be denoted as _**Z**_.

How to infer _**Z**_ from _**X**_ ? A brute force algorithm would require to test all the _2<sup>|**X**|</sup>_ subsets of _**X**_ for optimality, which is intractable even for a small number of sources. Instead, IDTxl employs a greedy algorithm and iteratively builds **Z** by maximising a conditional mutual information criterion: first, a set of candidate variables _c ∈ **C**_ is defined from the pasts of the sources _**X**_; then, **Z** is built by iteratively including the candidate variables _c_ that provides statistically-significant, maximum information about the current value _Y<sub>n</sub>_, conditioned on all the variables that have already been selected. More formally: at each iteration, the algorithm selects the past variable _c ∈ **C**_ that maximises the conditional mutual information _I(c ; Y<sub>n</sub> | **Z**)_ and passes a statistical significance test (more on the statistical tests below). The set of selected variables forms a **multivariate, non-uniform embedding** of **X** ([Faes, 2011, Phys. Rev. E](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.83.051112)).

### Defining a set of candidate variables

The candidate set of past variables **C** is defined by the user by providing the maximum lag parameter for the target and for the sources. The maximum lag restricts the number of past variables in the target and sources time-series that are tested for inclusion in **Z**. Importantly, IDTxl tests the variables from the target's past first, before testing the variables from the sources' past<sup>1</sup>. In the figure below, _l<sub>3</sub>_ denotes the maximum lag for the sources' past, _l<sub>1</sub>_ the minimum lag for the sources' past, and _l<sub>2</sub>_ is the maximum lag for the target's past:

![[multivariate_te_network.png]]

The minimum lag for the target is always set to 1 sample to ensure self-prediction optimality ([Wibral, 2013, PLOS 8(2)](https://www.ncbi.nlm.nih.gov/pubmed/23468850)).

Note that IDTxl requires no further parameters beyond the max lags and the parameters for statistical testing (estimator type, number of permutations, and critical alpha level). Statistical significance provides an adaptive stopping criterion for parents selection. Statistical testing of the estimated conditional mutual information is necessary to assess whether the estimated value is significantly different from zero: non-zero estimates may occur for independent variables due to the finite number of samples and the estimator bias (see also [Vicente, 2011, J. Comp. Neurosci., 20(1)]() and [Kraskov, 2004, Phys. Rev. E 69(6)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.69.066138)).

Currently, for estimating (conditional) mutual information information from continuous data a Gaussian as well as the Kraskov-Stögbaur-Grassberger estimator [Kraskov, 2004, Phys. Rev. E 69(6)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.69.066138) are implemented. For discrete data, a plug-in estimator is used (e.g., [Hlavackova-Schindler, 2007, Phys. Report, 441](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.183.1617&rep=rep1&type=pdf)).
See the tutorial page [CMI estimators](CMI-Estimators) for further details on available estimators.

An example of a possible embedding **Z** returned by the algorithm is shown in the figure below (filled rectangles indicate selected variables):

![[multivariate_te_network_all.png]]

### IDTxl's greedy algorithm for mTE estimation

The greedy algorithm operates in five steps:

1) Initialise **Z** as an empty set and consider the candidate sets for _Y_'s past (**C**<sub>Y</sub>) and _**X**_'s past (**C**<sub>X</sub>).

2) Select variables from **C**<sub>Y</sub><sup>1</sup>:
    * For each candidate, c ∈ **C**<sub>Y</sub>, estimate the information contribution to _Y<sub>n</sub>_ as _I(c ; Y<sub>n</sub> | **Z**)_
    * Find the candidate with maximum information contribution, _c*_, and perform a  significance test<sup>2</sup>; if significant, add _c*_ to **Z** and remove it from  **C**<sub>Y</sub>. We use the [maximum statistic](https://github.com/pwollstadt/IDTxl/wiki/Theoretical-Introduction#maximum-statistic) to test for significance while controlling the FWER (family-wise error rate).
    * Terminate if _I(c* ; Y<sub>n</sub> | **Z**)_ is not significant or **C**<sub>Y</sub> is empty.

3) Select variables from **X**'s past (_i.e._, from **C<sub>X</sub>**):
    * Iteratively test candidates in **C<sub>X</sub>** following the procedure described in step 2.

4) Prune **Z**: Test and remove redundant variables in **Z** using the [minimum statistic](https://github.com/pwollstadt/IDTxl/wiki/Theoretical-Introduction#minimum-statistic). The minimum statistic computes the conditional mutual information between every selected variable in **Z** and the current value, conditional on all the remaining variables in **Z**. This test is performed to ensure that the variables included in the early steps of the iteration still provide a statistically-significant information contribution in the context of the final parent set **Z**. See [Lizier, 2012, Max Planck Preprint No. 25](https://www.mis.mpg.de/preprints/2012/preprint2012_25.pdf).

5) Perform statistical tests on the final set **Z**:
    * Perform an [omnibus test](https://github.com/pwollstadt/IDTxl/wiki/Theoretical-Introduction#omnibus-test) to test the collective information transfer from all the relevant (informative) source variables to the target: _I(**Z<sub>X</sub>** ; Y<sub>n</sub> |**Z**<sub>Y</sub> )_. The resulting omnibus p-value is later used for correction of the FWER at the network level.
    * If the omnibus test is significant, perform a [sequential maximum statistic](https://github.com/pwollstadt/IDTxl/wiki/Theoretical-Introduction#sequential-maximum-statistic) on each selected variable _z ∈ **Z**_ to obtain each variable's final information contribution and p-value

Finally, the mTE between a single source _X<sub>i</sub>_ and target _Y_ can be computed from the inferred non-uniform embedding **Z**: collect from **Z** all of _X<sub>i</sub>_'s selected past variables, __X<sub>i</sub>__, and calculate the mTE as _I(**X<sub>i</sub>** ; Y<sub>n</sub> | **Z**\\**X<sub>i</sub>**)_. Note that time lag between  _X<sub>i</sub>_'s selected past variables and the current value at time _n_ indicates the information-transfer delay ([Wibral, 2013, PLOS 8(2)](https://www.ncbi.nlm.nih.gov/pubmed/23468850)). The delay can be estimated as the lag of the past variable which provides the maximum individual information contribution (the maximum contribution is indicated either by the maximum raw TE estimate or by the minimum p-value over all variables from that source).

Repeat the greedy algorithm for each node in the network. For theoretical and
some practical runtimes, see the [Runtimes and Benchmarking](Runtimes-and-Benchmarking) page.

Note further that the proposed approach to multivariate TE estimation is sometimes also
termed _conditional_ transfer entropy [Bossomaier, 2016](https://www.springer.com/de/book/9783319432212).

## Statistical tests used in the mTE algorithm

### Maximum statistic

The maximum statistic is used to test the information contribution of a candidate variable to the target's current value. The maximum statistic mirrors the greedy selection process and is used to control the FWER when selecting the relevant past variables to include in **Z**. The statistic works as follows:

Assume we have picked the candidate variable _c*_ (from the set of candidates **C**) which provides the maximum information contribution to the target, _i.e._, _I(c* ; Y<sub>n</sub> | **Z**)_. The following algorithm is used to test _I(c* ; Y<sub>n</sub> | **Z**)_ for statistical significance:
1. for each _c ∈ **C**_, generate a surrogate time-series _c'_ and calculate _I(c' ; Y<sub>n</sub> |**Z**)_
2. pick the maximum surrogate value _I(c' ; Y<sub>n</sub> |**Z**)_ among all surrogate estimates
3. repeat steps 1 and 2 a sufficient<sup>3</sup> number of times to obtain a distribution of maximum surrogate values
4. calculate a p-value for _c*_ as the fraction of surrogate values larger than _I(c* ; Y<sub>n</sub> | **Z**)_ and compare against the critical alpha-level.

Note that surrogate distributions can be derived analytically for Gaussian estimators, so that steps 1-3 can be omitted.

### Minimum statistic

The minimum statistic is used to prune the set of selected source candidates, _**Z**<sub>X</sub>_, after the inclusion of the candidates has terminated. The pruning step removes the selected variables that have become redundant in the context of the final set _**Z**_. The minimum statistic works similarly to the maximum statistic:

Assume we have picked the selected variable _z*_ from _**Z**<sub>X</sub>_ that has minimum information contribution _I(z* ; Y<sub>n</sub> | **Z**\\z*)_. The following algorithm is used to test if _I(z* ; Y<sub>n</sub> | **Z**\\z*)_ is still significant in the context of **Z**:
1. for each _z ∈ **Z**<sub>X</sub>_, generate a surrogate time-series _z'_ and calculate _I(z' ; Y<sub>n</sub> |**Z**\z*)_
2. pick the minimum estimate _I(z' ; Y<sub>n</sub> |**Z**\z*)_ among all surrogate estimates
3. repeat steps 1 and 2 a sufficient number of times to obtain a distribution of minimum surrogate values
4. calculate a p-value for _z*_ as the fraction of surrogate values that is larger than _I(z* ; Y<sub>n</sub> | **Z**\\z*)_ and compare against the critical alpha-level.

Note that surrogate distributions can be derived analytically for Gaussian estimators, so that steps 1-3 can be omitted.

### Omnibus test

The omnibus test is used to test the total information transfer from all the selected source variables, _**Z**<sub>X</sub>_, to the target _Y<sub>n</sub>_:

1. permute realisations of _Y<sub>n</sub>_ to obtain Y'<sub>n</sub> and calculate _I(**Z**<sub>X</sub> ; Y'<sub>n</sub> | **Z**<sub>Y</sub>)_
2. repeat step 1 a sufficient number of times
3. calculate the omnibus p-value as the fraction of surrogate values larger than _I(**Z**<sub>X</sub> ; Y<sub>n</sub> | **Z**<sub>Y</sub>)_ and compare against the critical alpha-level.

Note that surrogate distributions can be derived analytically for Gaussian estimators, so that steps 1-2 can be omitted. The omnibus test's p-value is used to control the FWER at the level of links in the network via FDR-correction ([Benjamini et al. (1995)](http://www.math.tau.ac.il/~ybenja/MyPapers/benjamini_hochberg1995.pdf)).

### Sequential maximum statistic

If the omnibus test finds significant total information transfer,
_I(**Z**<sub>X</sub> ; Y<sub>n</sub> | **Z**<sub>Y</sub>)_, into the target,
the sequential maximum statistic tests each selected source variable in
the final set _**Z**<sub>X</sub>_. The sequential maximum statistic works similarly to the maximum statistic. The difference is that the surrogate values are ordered by magnitude, which results in a distribution of maximum values, a distribution of second-largest values, a distribution of third-largest values, and so forth. The selected variables are sorted by their individual information contribution. The variable with the largest information contribution is compared against the maximum distribution, the variable with the second-largest contribution against the second-largest distribution, and so forth. As soon as a variable is no longer significant compared to its surrogate distribution of equal rank, that variable and all the other variables of lower rank are removed from the candidate set.

---

<sup>1</sup> We first find all relevant variables in the target's own past; otherwise, the information from the sources' pasts may be overestimated later (see [Wibral, 2013, PLOS 8(2)](https://www.ncbi.nlm.nih.gov/pubmed/23468850) for a discussion of this self-prediction optimality). Moreover, this approach is consistent with the distributed-computation modelling framework, whereby the information storage is computed first, followed by the information transfer.

<sup>2</sup> In IDTxl, statistical testing of estimated quantities is usually carried out by performing a test against a distribution estimated from surrogate data. The distribution is obtained by first permuting data to obtain surrogate data, and second re-estimating the quantity from surrogate data. This is repeated a sufficient number of times to obtain a test-distribution of estimates from surrogate data. The original estimate is then compared against this distribution. A p-value is obtained as the fraction of surrogate estimates that are more extreme than the original estimate. If an estimator with a known test-distribution is used (e.g., Gaussian), surrogate estimates can be created analytically to save computing time.

<sup>3</sup> The number of permutations is considered sufficient if it theoretically allows obtaining a p-value that is smaller than the critical alpha-level. The p-value is calculated as the fraction of surrogate values larger than the tested quantity. In the most extreme case, where no surrogate value is larger, the p-value is calculated as (1/number of permutations). This is the lowest obtainable p-value in the test. If the critical alpha level is lower than (1/number of permutations), the test can never return a significant result. Hence, the number of permutations and critical alpha-level should be set such that alpha > 1/no. permutations.

## Toy example: multivariate transfer entropy estimation in IDTxl

As an example of mTE estimation, consider the following toy network, where nodes represent (stochastic) processes and arrows represent interactions between processes:

![Example network _mTE_ estimation](images/multivariate_te_network_all.png)

Let _Y_ be the current target of interest. Nodes highlighted in blue represent the set of _relevant_ sources **Z**_={_X<sub>1</sub>_, _X<sub>3</sub>_, _X<sub>4</sub>_}_, _i.e._ the sources that contribute to the target's current value _Y<sub>n</sub>_.

Estimating the mTE into the target _Y_ requires inferring the set **Z** containing the relevant sources (or parents) of _Y_. Once **Z** is inferred, we can compute the mTE from a single process into the target as a conditional transfer entropy, which accounts for the potential effects of the remaining relevant sources. Formally, the mTE from a single source (e.g., _X<sub>3</sub>_) into _Y_ is defined as the TE from _X<sub>3</sub>_ to _Y_, conditioned on **Z** and excluding _X<sub>3</sub>_:

![Example network _mTE_ estimation](images/multivariate_te_network.png)

In order to infer mTE for each source-target pair in the network, the process of mTE estimation is repeated for each node in the network, i.e., the algorithm iteratively treats each node in the network as the current target and infers its relevant sources in the network.

## Further network inference algorithms implemented in IDTxl

In addition to mTE, IDTxl implements further algorithms for network inference. In the beginning, we assumed a multivariate setting with a single target process, _Y_, and a set of source process, _**X**_. We defined the mTE from a source _**X**<sub>i</sub>_ to _Y_ as the information the past of _**X**<sub>i</sub>_ provides about _Y<sub>n</sub>_, in the context of both _Y_'s past and the past of all  other relevant sources in _**X**_. We used the described greedy approach to build the set, _**Z**_, of relevant past variables. We now additionally define

- **bivariate transfer entropy (bTE)** as the information the past of a single source _X_ provides about about _Y<sub>n</sub>_ in the context of _Y<sub>n</sub>_’s past alone;
- **bivariate mutual information (bMI)** as the information the past of a single source _X_ provides about about _Y<sub>n</sub>_ without considering _Y<sub>n</sub>_’s past;
- **multivariate mutual information (mMI)** as the information the past of a single source _**X**<sub>i</sub>_ provides about about _Y<sub>n</sub>_  in the context of all the other relevant sources in _**X**_, without considering _Y<sub>n</sub>_’s past.

IDTxl provides algorithms to estimate these quantitites. The algorithms use the described [greedy strategy](https://github.com/pwollstadt/IDTxl/wiki/Theoretical-Introduction#idtxls-greedy-algorithm-for-mte-estimation) to build a non-uniform embedding from the respective candidates with the goal to maximise the information the set of selected variables, _**Z**_, has about _Y<sub>n</sub>_. The algorithms use the maximum statistic to determine whether a variable provides statistically significant information about _Y<sub>n</sub>_ in the inclusion step. Then the algorithms use the minimum statistic to prune the set of selected variables. The final set Z of selected variables is then tested using the omnibus test and sequential maximum statistics. See also the [documentation](http://pwollstadt.github.io/IDTxl/html/idtxl_network_inference.html) and the [tutorials](https://github.com/pwollstadt/IDTxl/wiki#tutorials) for further details.
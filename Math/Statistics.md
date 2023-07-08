# [Overview](http://d2l.ai/chapter_preliminaries/probability.html#sec-prob)
Probability is the mathematical field concerned with reasoning under uncertainty. 

The use of probabilities to describe the frequencies of repeatable events (like coin tosses) is fairly uncontroversial. In fact, frequentist scholars adhere to an interpretation of probability that applies only to such repeatable events. By contrast Bayesian scholars use the language of probability more broadly to formalize our reasoning under uncertainty. 

Bayesian probability is characterized by two unique features: (i) assigning degrees of belief to non-repeatable events, e.g., what is the probability that the moon is made out of cheese?; and (ii) subjectivity. While Bayesian probability provides unambiguous rules for how one should update their beliefs in light of new evidence, it allows for different individuals to start off with different prior beliefs.

Statistics helps us to reason backwards, starting off with collection and organization of data and backing out to what inferences we might draw about the process that generated the data. Whenever we analyze a dataset, hunting for patterns that we hope might characterize a broader population, we are employing statistical thinking.

## Basics
- Outcome (z): a precise description of the state of the world (as far as our model is concerned) and cannot be split any further
- Outcome/Sample Space (Ω): 
- Event (A): subset of sample space (grouping of outcomes we are interested in)
- Probability Function/Probability/Probability Measure (P): mapping from events onto real values that satisfies the axioms
- Kolmogorov Axioms: P(A) >= 0; P(S) = 1; Aᵢ∩Aⱼ≠0 → P(Aᵢ∪Aⱼ)=P(Aᵢ)+P(Aⱼ)

> See Math notes about measure 

> Also see Cox's theorem as an alternative axiom for Bayesian Probability

### Frequentism VS Bayesian
defines an event's probability as the limit of its relative frequency in many trials (the long-run probability). Probabilities can be found (in principle) by a repeatable objective process (and are thus ideally devoid of opinion). In the classical interpretation, probability was defined in terms of the principle of indifference, based on the natural symmetry of a problem, so, e.g. the probabilities of dice games arise from the natural symmetric 6-sidedness of the cube. This classical interpretation stumbled at any statistical problem that has no natural symmetry for reasoning.

In the frequentist interpretation, probabilities are discussed only when dealing with well-defined random experiments. For any given event, only one of two possibilities may hold: it occurs or it does not. The relative frequency of occurrence of an event, observed in a number of repetitions of the experiment, is a measure of the probability of that event. This is the core conception of probability in the frequentist interpretation.

A claim of the frequentist approach is that, as the number of trials increases, the change in the relative frequency will diminish. Hence, one can view a probability as the limiting value of the corresponding relative frequencies.



### Conditional and Joint Probability
- P(A|B): $\frac{P(A intersect B)}{P(B)}$, probability of A in the universe of B
- P(A, B): P(A intersect B)=P(A)⋅P(B|A) multiplication rule
- P(A)=$\frac{P(A)⋅P(B|A)}{P(B|A)}=\frac{P(A,B)}{P(B|A)}$
- P(A)=$\sum_{i}P(A, B_i)=\sum_{i}P(A|Bᵢ)⋅P(Bᵢ)$ Total probability theorem


![](/images/prob1.png)

> Note that A and B are events and P is probability measure function

### (Conditional) Independence
- Independence: P(A|B)=P(A)->P(A, B)=P(A)⋅P(B)
- Conditional independence: P(A|B,C)=P(A|C)->P(A,B|C)=P(A|C)⋅P(B|C)

> Proof of conditional independence: $P(A|B,C)=P(A|C)=\frac{P(A,B,C)}{P(B,C)}=\frac{P(A,B,C)}{P(C)⋅P(B|C)}=\frac{P(A,C)}{P(C)}\iff\frac{P(A,C)⋅P(B|C)}{P(C)}=\frac{P(A,B,C)}{P(C)}=P(A|C)⋅P(B|C)$

#### Pairwise & Mutual Independence
![](/images/pairwiseIndependence.png)

### Random Variable
- Random Variable: An assignment of a value (number) to every possible outcome. Formally, a mapping from sample space to real numbers (from headings of coin to 0 and 1)

Every probability model comes with its sample space (and a probability). It is often left out of the discussion because all the action is carried out by random variables, but it always lurks underneath.

### Probability Distribution
A probability distribution is a mathematical description of the probabilities of events, subsets of the sample space.

However, when dealing with random variables, we often use the image of X as the sample space instead of domain of X. This way it's easier to understand probability of events that have been quantified and the sample space becomes a numerical set instead of arbitrary non-numerical values like heads or tails.

The most general descriptions is in the form of P: A->R where A is related to sample space Ω. So when using the general probability function/measure form, A is the σ-algebra of Ω. And in the case of using random variables which is more common, A is the image of Ω under random variable X which is a numerical set. 

Key takeaway is that anything of the form P: A->R satisfying certain conditions are probability distributions since the describe probability of outcomes. A plain capital P mapping events to R, PMF and PDF are all probability distributions.

### PMF & PDF
- PMF: Probability mass function is the probability distribution of a discrete random variable. It is the function p: R to [0,1] defined by $p_X(x)$ = P(X=x) which is P({ω∈Ω s.t. X(ω)=x}) where P is a probability measure. It's normally written as p(x)
- PDF: $P(a \le X \le b)\\=P(\{ω∈Ω\ s.t.\ a\le X(ω)\le b\})\\=\int_{a}^{b}f_X(x)dx\\$ $f_X(x)⋅δ \approx P(x \le X \le x+δ) $


> Note: Probability function maps **event** to values (real number), RV maps **outcome** to values, PMF maps **values** to values.

> Note: PMF is lower case p while probability measure is capital P.

> Note: in p(x) x should be X=x which gives the set of solutions to X=x.  
![](/images/rvInverseImg.png)

### Joint & Conditional Distribution
- Joint PMF: $p_{X,Y}(x,y)\\=P(X=x\ and\ Y=y)\\=P(\{ω∈Ω\ s.t.\ X(ω)=x\}∩\{ω∈Ω\ s.t.\ Y(ω)=y\})$
- Conditional PMF (Single RV): $p_{X|A}(x)\\=P(X=x|A)\\=\frac{P(\{ω∈A\ st\ X(ω)=x\})}{P(A)}$
- Conditional PMF (2 RV): $p_{X|Y}(x|y)\\=P(X=x|Y=y)\\=P(\{ω∈Ω\ st\ Y(ω)=y\})\\=\frac{P(\{X=x\}∩\{Y=y\})}{P(y)}$

![](/images/pdf1.png)



> Note that X and Y should be defined on the same sample space. When pairing random variables, we create tuples of their outcomes as element of the new sample space (Though in reality everything is always in the same big sample space, we normally ignore most irrelevant states).

> Note that when you have multiple RV, you could essentially combine them to a single random vector/element with a complex outcome space but that entangles information and is not good for modeling and inference. 

> Note that conditional probability/distribution is defined on joint probability/distribution. There are some other definitions.

### Mean & Variance
- E(X): $∫x⋅f_X(x)dx=∫X(e)⋅P(e)de$ where e ∈ E
- Var(X): E[(X-EX)²]=E(X²)-EX²
- Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)
- Chebyshev’s inequality
- Covariance: $E[(X-E[X])⋅(Y-E[Y])]=E(XY)-E(X)E(Y)=∫∫f_{xy}(x,y)(x-μ_x)⋅(y-μ_y)dxdy$
- Random variables whose covariance is zero are called uncorrelated.
- Covariance Matrices: covariance can only be calculated between two variables, use covariance matrix represents covariance values of each pair of variables in multivariate data

![](/images/probE.png)
![](/images/mrv1.png)

> Mean & Variance are properties of the image of events under random variable X. Not properties of the events themselves. Thus to make these properties meaningful wrt the underlying random events which we truly want to measure, the mapping X should assign meaningful values to corresponding events.


## Distributions
http://d2l.ai/chapter_appendix-mathematics-for-deep-learning/distributions.html#exponential-family

X~N(0,1) means random variable X follows a probability distribution N(0,1). Though it really means that the underlying sample space of X follow the probability function N(0,1). 

x~P(X) means a value x sampled from distribution P

### Bernoulli
![](/images/bernoulli.png)

### Binomial
the binomial distribution with parameters n and p is the discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability p) or failure (with probability q=1-p). A single success/failure experiment is also called a Bernoulli trial or Bernoulli experiment, and a sequence of outcomes is called a Bernoulli process; for a single trial, i.e., n = 1, the binomial distribution is a Bernoulli distribution.

### Poisson
Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
![](/images/poisson.png)

> The difference between binomial and poisson is that poisson views the experiment process as continuous (binomial with p->0 and n->infinity)

## Exponential Family

## Law of Large Numbers
Sample mean converges to population mean

## Central Limit Theorem
Distribution of sample mean is normal


# Stochastic Process
A stochastic process is defined as a collection of random variables defined on a common probability space (Ω, F, P) where Ω is a sample space, F is a σ-algebra, and P is a probability measure; and the random variables, indexed by some set T, all take values in the same mathematical space S, which must be measurable with respect to some  σ-algebra Σ

## Bernoulli
In probability and statistics, a Bernoulli process is a finite or infinite sequence of binary random variables, so it is a discrete-time stochastic process that takes only two values, canonically 0 and 1. The component Bernoulli variables Xi are identically distributed and independent.

## Markov
A discrete-time Markov chain is a sequence of random variables X1, X2, X3, ... with the Markov property, namely that the probability of moving to the next state depends only on the present state and not on the previous states.

The possible values of Xi form a countable set S called the state space of the chain.

> X encodes the states in its values and in most real world cases should be a random element


# Bayes
## Bayes' Theorem
P(A|B)=P(B|A)P(A)/P(B)

Although Bayes' theorem is a fundamental result of probability theory, it has a specific interpretation in Bayesian statistics. In the above equation, A usually represents a proposition (such as the statement that a coin lands on heads fifty percent of the time) and B represents the evidence, or new data that is to be taken into account (such as the result of a series of coin flips). P(A) is the prior probability which expresses one's beliefs about A before evidence is taken into account. The prior probability may also quantify prior knowledge or information about A. P(B|A) is the likelihood function, which can be interpreted as the probability of the evidence B given that A is true. The likelihood quantifies the extent to which the evidence B supports the proposition A. P(A|B) is the posterior probability, the probability of the proposition A after taking the evidence B into account. Essentially, Bayes' theorem updates one's prior beliefs P(A) after considering the new evidence B.

> Note that we use probability and probability distribution interchangeably. In a single trial, we have P(A) as a distribution, B is fixed so P(B|A) is maps parameters to values. The resulting P(A|B) is also parameter to value and requires a simple function multiplication.


# [Statistical Inference](https://en.wikipedia.org/wiki/Statistical_inference)
Statistical inference is the process of using data analysis to infer properties of an underlying distribution of probability. Inferential statistical analysis infers properties of a population, for example by testing hypotheses and deriving estimates. It is assumed that the observed data set is sampled from a larger population.

## Estimator
An "estimator" or "point estimate" is a statistic (that is, a function of the data) that is used to infer the value of an unknown parameter in a statistical model. A common way of phrasing it is "the estimator is the method selected to obtain an estimate of an unknown parameter". The parameter being estimated is sometimes called the estimand.

Suppose a fixed parameter θ needs to be estimated. Then an "estimator" is a function that maps the sample space to a set of sample estimates. An estimator of 
θ is usually denoted by the symbol $\hat\theta$

### Bayes Estimator


## MLE & MAP
### Maximum Likelihood Estimation
In statistics, maximum likelihood estimation (MLE) is a method of estimating the parameters of an assumed probability distribution, given some observed data. This is achieved by maximizing a likelihood function so that, under the assumed statistical model, the observed data is most probable. The point in the parameter space that maximizes the likelihood function is called the maximum likelihood estimate.

Likelihood function: L(θ): θ↦R = f(y; θ) where f is a distribution modeled as a parametric family and y is the observed data sample. Note that θ∈Θ where Θ is parameter space, subset of Euclidean space. More on this in comparison with MAP.

The goal of maximum likelihood estimation is to find the values of the model parameters that maximize the likelihood function over the parameter space

> Recall: a parametric family or a parameterized family is a family of objects (a set of related objects) whose differences depend only on the chosen values for a set of parameters

### Maximum a Posteriori Estimation
In Bayesian statistics, a maximum a posteriori probability (MAP) estimate is an estimate of an unknown quantity, that equals the mode of the posterior distribution.

Likelihood function: θ↦R = f(x | θ) where x is the observation. Note θ is viewed here as a random variable. 

Since we have f(θ), we can get posterior using bayes rule. Then we choose θ as the mode of the posterior distribution f(θ|x) ∝ f(x|θ)⋅f(θ)




# ML
## Naive Bayes
Digit classification. Have image x want P(y|x) where y is a number from 0-9. Problem: compute P(y|x).

1. compute P(y|x) for every x (basically collecting all possible 32x32 images and assign probability to each one). Too large and no learning.
2. argmaxP(y|x)=argmaxP(x|y)P(y). P(x|y)=P(x1|y)⋅P(x2|x1,y)⋅...P(xd|x1,...xd-1,y). Still too 2^d computation
3. assume that each pixel is independent of each other. P(x|y)P(y) becomes ΠP(xᵢ|y)p(y). This is just a dxn matrix where element at (d,n) is P(xd=1|y=n)

Now we can estimate P(xᵢ|y) for every pixel. We count the number of occurrences for each of the n digits and divide it by the total amount of data.

## [Variational Bayeisan](https://blog.evjang.com/2016/08/variational-bayes.html)
Hidden variables can be interpreted from a Bayesian Statistics framework as prior beliefs attached to the observed variables. For example, if we believe X is a multivariate Gaussian, the hidden variable Z might represent the mean and variance of the Gaussian distribution. The distribution over parameters P(Z) is then a prior distribution to P(X).

### [ELBO](https://calvinyluo.com/2022/08/26/diffusion-tutorial.html)
- Motivation: maximize p(x) with a latent model but p(x) is intractable through marginal over all latents.
![](/images/elbo.png)
- Why is ELBO lower bound for logp(x): KL is non negative.
- Why maximize ELBO: p(x) is a constant, so maximizing ELBO simultaneously minimizes KL of posterior (which can't be minimized directly without ground-truth posterior). We want to learn posterior because it models underlying latent structure of observed data.
- Interpretation of 15: probability of x is p(x,z)/p(z|x). If we replace p(z|x) with q(z|x), then p(x) will drop. The amount of drop is KL of p(z|x) and q(z|x).


### VAE
![](/images/vaeLoss.png)
ELBO can be further decomposed into 2 terms which correspond to a reconstruction and prior matching term. 
![](/images/vaeIntuition.png)

### Hierarchical VAE

### Diffusion


# Information Theory
## [Information](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
Measurement of uncertainty/randomness. How much more I know about the thing or how surprized I am after an event happens.

### Entropy
Suppose we have a set of possible events whose probabilities of occurrence are p1, p2,... pn. These probabilities are known but that is all we know concerning which event will occur. Can we find a measure of how much “choice” is involved in the selection of the event or of how uncertain we are of the outcome?

If there is such a measure, say H(p1, p2,... pn), it is reasonable to require of it the following properties:
1. H should be continuous in the pi.
2. If all the pi are equal, pi = 1/n, then H should be a monotonic increasing function of n. With equally n likely events there is more choice, or uncertainty, when there are more possible events.
3. If a choice be broken down into two successive choices, the original H should be the weighted sum
of the individual values of H.

The only H satisfying the three above assumptions is of the form: H=-KΣpᵢlogpᵢ

### Self-Information
I(x)=-log(P(X=x))

base 2: bit; base e: nat.

> Note that information is used to describe events and entropy for random variable/system

### Information as Bits
To get a sense of relationship between information as digital bits and happenings of events, it's easier to use a probabilistic example. If a 4 face die has outcomes with following distribution: 1 (1/8); 2 (1/8); 3 (1/4); 4 (1/2) then first and second event has 3 bits information, the third 2, and fourth has 1. If we throw the die 1000 times we expect to record roughly 125 1s and 2s, 250 3s and 500 4s. The recording would take 1750 bits and that's exactly entropy of the die throwing (1.75) times 1000. On the other hand if we just represent the 4 events with 4 different binary numbers (2 bits), we are essentially treating every event as equally possible (1/4) and this requires 2000 bits.

This means that in practice, if a random variable/system has high entropy, it is more random, and it requires more space to record/transmit it. If an event associated with the random variable has low probability, it means then recording it once would take more space. Optimally, entropy * number of recording = number of bits to transmit.

### Joint Entropy
H(X,Y) = Ep(X,Y)[log(p(x,y))]

Max(H(X), H(Y)) <= H(X,Y) <= H(X)+H(Y)

### Conditional Entropy
![](/images/cond-entropy.png)

Example:
> suppose there are 16 images of 4 categories (each category with 10 images). X is the random variable mapping image to a number or to pixel values and Y from category label to number. Both PMF are uniform so H(X)=4 and H(Y)=2. Now since each image has exactly 1 label, $p_{Y|X}$=1/0, H(Y|X)=0 and H(X,Y)=4. This agrees with H(Y|X)=H(X,Y)-H(X) and indicates that X contains all the information about Y. On the other hand, $p_{X|Y}$=1/4 and H(X|Y)=2. H(X|Y)=H(X,Y)-H(Y), indicating that knowing label gives some but not all information about X. As an aside, if we want X and Y to be independent, then each image must be equally likely assigned any label, creating a sample space of 16*4 outcomes that have equal non zero probability (compared with 16).

## Mutual Information
![](/images/mutual-info.png)

- I(X,Y)=T(Y,X)
- I(X,Y)>=0
- I(X,Y)=0 if X and Y are independent i.e. H(X,Y)=H(X)+H(Y)=H(X|Y)+H(Y|X) which is analogous to p(x,y)=p(x)*p(y)=p(x|y)*p(y|x). Notice that log term in H changed multiplication to summation.
- I(X,Y)=H(X)=H(Y) if X and Y are completely dependent (X is an invertible function of Y).

Point wise mutual information:

$pmi(x,y)=log\frac{p_{X,Y}(x,y)}{p_X(x)p_Y(y)}$

This can be seen as measuring amount of surprise of seeing two things happening together compared to seeing them happen separately. Note that pmi can be positive and negative.

### KL (Kullback–Leibler)
$D_{KL}(P||Q)=E_{x\sim P}[log\frac{p(x)}{q(x)}]$

- KL(P,Q)!=KL(Q,P)
- KL(P,Q)>=0, KL(P,Q)=0 if P=Q
- if there is an x such that p(x)>0 and q(x)=0, KL=∞

![](/images/forward_vs_reversed_KL.png)

### Cross Entropy
$CE(P,Q)=-E_{x \sim P}[log(q(x))]$

$CE(P,Q)=H(P)+D_{KL}(P||Q)$

### Jensen-Shannon Divergence
$JSD(P||Q)=\frac{D(P||M)+D(Q||M)}{2},\ where\ M=\frac{P+Q}{2}$

### Relationships
The following are equivalent:
- Maximize predictive likelihood 
- Minimize CE
- Minimize KL


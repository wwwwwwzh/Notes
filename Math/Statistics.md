# [Overview](http://d2l.ai/chapter_preliminaries/probability.html#sec-prob)
Probability is the mathematical field concerned with reasoning under uncertainty. 

The use of probabilities to describe the frequencies of repeatable events (like coin tosses) is fairly uncontroversial. In fact, frequentist scholars adhere to an interpretation of probability that applies only to such repeatable events. By contrast Bayesian scholars use the language of probability more broadly to formalize our reasoning under uncertainty. 

Bayesian probability is characterized by two unique features: (i) assigning degrees of belief to non-repeatable events, e.g., what is the probability that the moon is made out of cheese?; and (ii) subjectivity—while Bayesian probability provides unambiguous rules for how one should update their beliefs in light of new evidence, it allows for different individuals to start off with different prior beliefs.

Statistics helps us to reason backwards, starting off with collection and organization of data and backing out to what inferences we might draw about the process that generated the data. Whenever we analyze a dataset, hunting for patterns that we hope might characterize a broader population, we are employing statistical thinking.

## Basics
- Outcome (z): a precise description of the state of the world (as far as our model is concerned) and cannot be split any further
- Outcome/Sample Space (Ω): 
- Event (A): subset of sample space (grouping of outcomes we are interested in)
- Probability Function/Probability/Probability Measure (P): mapping from events onto real values that satisfies the axioms
- Kolmogorov Axioms: P(A) >= 0; P(S) = 1; Aᵢ∩Aⱼ≠0 → P(Aᵢ∪Aⱼ)=P(Aᵢ)+P(Aⱼ)

> Also see Cox's theorem as an alternative axiom for Bayesian Probability

### Conditional and Joint Probability
- P(A|B): P(A intersect B)/P(B), probability of A in the universe of B
- P(A, B): P(A intersect B)=P(A)P(B|A) multiplication rule
- P(A)=P(A)P(B|A)/P(B|A)=P(A,B)/P(B|A)
- P(A)=Σp(A|Bᵢ)p(Bᵢ) Total probability theorem
- Independence: p(A|B)=p(A)->p(A intersect B)=p(A)*p(B)

![](/images/prob1.png)

> Note that A and B are events and P is probability function


### Random Variable
- Random Variable: An assignment of a value (number) to every possible outcome. Formally, a mapping from sample space to real numbers (from headings of coin to 0 and 1)

Every probability model comes with its sample space (and a probability). It is often left out of the discussion because all the action is carried out by random variables, but it always lurks underneath.

### Probability Distribution
A probability distribution is a mathematical description of the probabilities of events, subsets of the sample space.

However, when dealing with random variables, we often use the image of X as the sample space instead of domain of X. This way it's easier to understand probability of events that have been quantified and the sample space becomes a numerical set instead of arbitrary non-numerical values like heads or tails.

The most general descriptions is in the form of P: A->R where A is related to sample space. So when using the general probability function/measure form, A is the set of all subsets E ⊂ X whose probability can be measured. And in the case of using random variables which is more common, A is the image of event space under random variable X which is a numerical set. 

Key takeaway is that anything of the form P: A->R satisfying certain conditions are probability distributions since the describe probability of outcomes. A plain big P mapping events to R, PMF and PDF are all probability distributions.

### PMF & PDF
- PMF: Probability mass function is the probability distribution of a discrete random variable. It is the function p: R to [0,1] defined by $p_X(x)$ = P(X=x) which is P({ω∈Ω s.t. X(ω)=x}) where P is a probability measure. It's normally written as p(x)
- PDF: $P(a \le X \le b)\\=P(\{ω∈Ω\ s.t.\ a\le X(ω)\le b\})\\=\int_{a}^{b}f_X(x)dx\\$ $f_X(x)⋅δ \approx P(x \le X \le x+δ) $


> Note: Probability function maps **event** to values (real number) while PMF maps **values** to values.

> Note: PMF is lower case p while probability is capital P.

> Note: in p(x) x should be X=x which gives the set of solutions to X=x.  

### Joint & Conditional Distribution
- Joint PMF: $p_{X,Y}(x,y)\\=P(X=x\ and\ Y=y)\\=P(\{ω∈Ω\ s.t.\ X(ω)=x\}∩\{ω∈Ω\ s.t.\ Y(ω)=y\})$
- Conditional PMF (Single RV): $p_{X|A}(x)\\=P(X=x|A)\\=\frac{P(\{ω∈A\ st\ X(ω)=x\})}{P(A)}$
- Conditional PMF (2 RV): $p_{X|Y}(x|y)\\=P(X=x|Y=y)\\=P(\{ω∈Ω\ st\ Y(ω)=y\})\\=\frac{P(\{X=x\}∩\{Y=y\})}{P(y)}$

![](/images/pdf1.png)



> Note that X and Y should be defined on the same sample space. When pairing random variables, we create tuples of their outcomes as element of the new sample space (Though in reality everything is always in the same big sample space, we normally ignore most irrelevant states).

> Note that conditional probability/distribution is defined on joint probability/distribution. There are some other definitions.

### Mean & Variance
- E(X): $∫x⋅p_X(x)dx=∫X(ω)⋅P(ω)dω$
- Var(X): E[(X-EX)²]=E(X²)-EX²
- Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)
- Chebyshev’s inequality
- Covariance: ∫(xᵢ-μx)(yⱼ-μy)pᵢⱼ=E(XY)-E(X)E(Y)
- Covariance Matrices: covariance can only be calculated between two variables, use covariance matrix represents covariance values of each pair of variables in multivariate data

![](/images/probE.png)
![](/images/mrv1.png)

> Mean & Variance are properties of the image of events under random variable X. Not properties of the events themselves. Thus to make these properties meaningful wrt the underlying random events which we truly want to measure, the mapping X should assign meaningful values to corresponding events.


# Distributions
http://d2l.ai/chapter_appendix-mathematics-for-deep-learning/distributions.html#exponential-family

Probability function describes probability distribution. So both PMF and PDF define probability distributions. Note that probability distribution can take different forms.

X~N(0,1) means random variable X follows a probability distribution N(0,1). Though it really means that the underlying sample space of X follow the probability function N(0,1). 

x~P(X) means a value x sampled from distribution P
## Bernoulli
![](/images/bernoulli.png)
## Binomial

## Poisson
![](/images/poisson.png)
## Exponential Family

## Law of Large Numbers
Sample mean converges to population mean

## Central Limit Theorem
Distribution of sample mean is normal



# ML
## Naive Bayes
Digit classification. Have image x want P(y|x) where y is a number from 0-9. Problem: compute P(y|x).

1. compute P(y|x) for every x (basically collecting all possible 32x32 images and assign probability to each one). Too large and no learning.
2. argmaxP(y|x)=argmaxP(x|y)P(y). P(x|y)=P(x1|y)⋅P(x2|x1,y)⋅...P(xd|x1,...xd-1,y). Still too 2^d computation
3. assume that each pixel is independent of each other. P(x|y)P(y) becomes ΠP(xᵢ|y)p(y). This is just a dxn matrix where element at (d,n) is P(xd=1|y=n)

Now we can estimate P(xᵢ|y) for every pixel. We count the number of occurrences for each of the n digits and divide it by the total amount of data.

## [Variational Bayeisan](https://blog.evjang.com/2016/08/variational-bayes.html)
VB methods allow us to re-write statistical inference problems (i.e. infer the value of a random variable given the value of another random variable) as optimization problems (i.e. find the parameter values that minimize some objective function).

Hidden variables can be interpreted from a Bayesian Statistics framework as prior beliefs attached to the observed variables. For example, if we believe X is a multivariate Gaussian, the hidden variable Z might represent the mean and variance of the Gaussian distribution. The distribution over parameters P(Z) is then a prior distribution to P(X).

### [ELBO](https://calvinyluo.com/2022/08/26/diffusion-tutorial.html)
- Motivation: maximize p(x) with a latent model but p(x) is intractable through marginal over all latents.
![](/images/elbo.png)
- Why is ELBO lower bound for logp(x): KL is non negative.
- Why maximize ELBO: p(x) is a constant, so maximizing ELBO simultaneously minimizes KL of posterior (which can't be minimized directly without ground-truth posterior). We want to learn posterior because it models underlying latent structure of observed data.



### VAE


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


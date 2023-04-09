# [Overview](http://d2l.ai/chapter_preliminaries/probability.html#sec-prob)
Probability is the mathematical field concerned with reasoning under uncertainty. 

The use of probabilities to describe the frequencies of repeatable events (like coin tosses) is fairly uncontroversial. In fact, frequentist scholars adhere to an interpretation of probability that applies only to such repeatable events. By contrast Bayesian scholars use the language of probability more broadly to formalize our reasoning under uncertainty. 

Bayesian probability is characterized by two unique features: (i) assigning degrees of belief to non-repeatable events, e.g., what is the probability that the moon is made out of cheese?; and (ii) subjectivity—while Bayesian probability provides unambiguous rules for how one should update their beliefs in light of new evidence, it allows for different individuals to start off with different prior beliefs.

Statistics helps us to reason backwards, starting off with collection and organization of data and backing out to what inferences we might draw about the process that generated the data. Whenever we analyze a dataset, hunting for patterns that we hope might characterize a broader population, we are employing statistical thinking.

## Basics
- Outcome (z)
- Outcome/Sample Space (S): 
- Event (A): subset of sample space
- Probability function (P): mapping from events onto real values
- Axioms: P(A) >= 0; P(S) = 1; Aᵢ∩Aⱼ≠0 → P(Aᵢ∪Aⱼ)=P(Aᵢ)+P(Aⱼ)
- Random Variable: mappings from an underlying sample space to a set of (possibly many) values (from headings of coin to 0 and 1)
- P(X): P(X∈S) = P({ω∈Ω | X(ω)∈S})
- P(X|Y): P(X∪Y)/P(Y)

> Note that X are sometimes described as random variables and sometimes as events

## Mean & Variance
- E(X): ∫x⋅f(x)dx=∫P(ω)⋅X(ω)dω
- Var(X): E[(X-EX)²]=E(X²)-EX²
- Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)
- Chebyshev’s inequality
- Covariance: ∫(xᵢ-μx)(yⱼ-μy)pᵢⱼ=E(XY)-E(X)E(Y)
- Covariance Matrices: covariance can only be calculated between two variables, use covariance matrix represents covariance values of each pair of variables in multivariate data

> Note: Probability function maps event not value to probability values. P(X=1) is a shorthand for P({ω∈Ω | X(ω)=1}) or P(X⁻¹(1))

# Distributions
http://d2l.ai/chapter_appendix-mathematics-for-deep-learning/distributions.html#exponential-family

A probability distribution is a probability function. So both PMF and PDF define probability distributions.

X~N(0,1) means random variable X follows a probability distribution N(0,1). Though it really means that the underlying sample space of X follow the probability function N(0,1). 
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

This means that in practice, if a random variable/system has high entropy, it is more random by definition, and it requires more space to record/transmit it. If an event associated with the random variable has low probability, it means then recording it once would take more space. Optimally, entropy * number of recording = number of bits to transmit.

## Mutual Information
### Joint Entropy
H(X,Y) = Ep(X,Y)[log(p(x,y))]

Max(H(X), H(Y)) <= H(X,Y) <= H(X)+H(Y)

### Conditional Entropy
![](/images/cond-entropy.png)
### Mutual Information
![](/images/mutual-info.png)
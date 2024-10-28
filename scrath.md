good e

really realy
idk 
anyway
the
i be
lot of

doing

actually
somebody
please/pleaze
tweenty
one of them
situation/sijuation

start & end of phone call
ask for car

what u up to
he just be doin shit
what u doin

interesting
restaurant
yes




i think it's about time we call it a day
i think it's pretty much all we have for today
i think we have already gone through what we need to go through for today
i'll hit you up on when we gonna meet next time 


take care
hope everything goes well for u
hope u have a good time in _


gym

first time meeting
summer
chatting
gaming
in car
shopping
bye

group





# Embodied
- Embodiment and AI
- The embodiment process, do we count  every output of the transformation from source domain to maybe amodal representation, the whole thing as the embodied representation
- In languuage processing, words are tokenized. Tokens may seem amodal at first, but they behave embodied: cats and dogs and other furry animals may share similarities in certain feature dimentsions; red objects like apple and a red t-shirt may do the same. If this is considered embodied, then abstract concepts are automatically embodied. Concepts like circular or valuable can be shown to exist close to each other in token space. Moreover, if we consider the itermidiary layers, concepts like time and space are also proven to exist.  
- Helen Keller argument of embodied cognition. Embodied theory posits that activation of modaility specific area is necessary and sufficient for embodied cognition. However, If someone is deprived of certain modailities, would their cognition be embodied?
- spatial relationship of grammar, and in different langauges.
- language (words) learning as improving embodiment
- embodied poem: poems you cite often, which you have mixed so many feelings  and situations in, are greatly embodied [The Experience of Beauty of Chinese Poetry and Its Neural Substrates](https://pubmed.ncbi.nlm.nih.gov/30186210/)



# Blog
## Fourier
- addition of matrices to current one
- "Special properties of the Fourier basis, namely orthogonality, make inverting this matrix as easy as taking a complex conjugate"
- FFT
- consider how to add the continuous in, maybe just mention it
- Kronecker-delta functions

## Laplace
### References

###
- [Any invertible linear operator can be conceptualized as a change-of-basis. The Laplace transform is an invertible linear operator on the vector space of 𝐿2
functions. Laplace is not orthogonal](https://math.stackexchange.com/questions/3190961/how-is-the-laplace-transform-a-change-of-basis/3537213#3537213)
- An invertible matrix need not be orthogonal

## Lagrangian
### Fermat and Light

### Parametrized path
x=(x(t), y(t))

###
https://en.wikipedia.org/wiki/Noether%27s_theorem


## Shorts
### Dot and Cross Product
- "Two (non-parallel) vectors define a plane, and only in three dimensions, **the direction and orientation of a 2D plane can be uniquely determined by a vector perpendicular to it. That is, in 3D there is a natural map between planes through the origin (defined by pairs of non-parallel vectors) and vectors up to a scalar multiple**." https://math.stackexchange.com/questions/349907/cross-product-intuition
- "The concept of the axis of rotation does not generalize to higher dimensions. What does generalize is the plane perpendicular to it. This plane perpendicular to the axis of rotation is invariant (it gets mapped to itself) under rotation", "It is the duality between planes and axes (map between a pair of vectors and a single vector perpendicular to them) that allows us to talk about the axis of rotation in 3D."
- "A moving charge at position 𝑟⃗ with velocity 𝑢⃗ creates a rotating force at the origin attempting to rotate the velocity vector of any charge at the origin in the 𝑟⃗-𝑢⃗ plane. But since in 3D we can identify rotations with their axis instead of their plane, which we love to do because vectors are simpler mathematical objects with known rules than planes, we define this force in terms of a vector 𝐵⃗ that points outside of this plane. That is the magnetic field"
- [3b1b](https://www.youtube.com/watch?v=BaM7OCEm3G0)
- https://en.wikipedia.org/wiki/Cross_product#Geometric_meaning

### Convolution
-  multi of polynomial: the (t-x) means getting the diagonal components

Fourier:
- cos convolve with cos and 2 cos and 2cos conv 2cos
- sin convolve sin. (minus sign and complex conjugate)
- delta

# For myself
### Function/Data
What's a function, in application sense? The structure of the world mandates that hidden structure in time and space are related to those observable. Given the appearance of a guy we want to predict his character, given the weather now we want to know that for tommorow. 

When learning, we are learning these structures, appearing as functiioins. A linear function can be used for both spatial and temporal tasks (housing priice is a spatial task). 

Now what part of a function is a data point? Likely it's an x-y pair. Area-price, or time-behavior.


### History of statistics (from status, state of a country) and probability
- Summary: statistics and probability have always been intertwined. **3 branches** of effort converged to modern theory of probability. First is the study of **gambling** where probability were getting defined as a fraction, and where statistics were getting vaguely defined as the long term results of the games. Second is the study of **large amounts of data that were not completely accurate**, beginning with astronomical data and demographic data. This led to the study of distribution of errors, which led to **normal distribution** and methods of least squares. The third was from heat, and the related industrial revolution. The **kinetic theory of gas** naturally led to the convergence to the previous study of large amount of data. All three converged during the 19th century resulting in a theory that says: despite its chaotic appearance, **randomness are in fact controlled by fine structures**, just like those under Newtonian mechanics and mathematical structures. Thus randomness can be studied like any mathematical structures. The first of these structures was **expected value** rooted in gambling problems and later led to Bernoulli's **law of large numbers**. In this case a single value, the mean, gives orders to randomness. Later by studying errors of observations, a complete distribution emerged and led to **normal distribution and central limit theorem**. 
- cont. Bernoulli's Ars Conjectandi and Moivre's Doctrine of Chance were istrumental. Bayes published a paper in response to Doctrine of Chance. Combinotorics problems rooted in games have led to covergence with number theory and early forms of fuction analysis with series expasions. Characteristic fuctions and generating funnctios.
- https://en.wikipedia.org/wiki/Stochastic_process#History
- https://en.wikipedia.org/wiki/History_of_statistics
- https://en.wikipedia.org/wiki/probability 
- game of chance, combinatorics based and mostly intuition based for things like calculatiing the fraction/probability, see [problem of points](https://en.wikipedia.org/wiki/Problem_of_points). It can be seen that basic notions like expected value was far from intuitive in those times.
    - More on problem of points:
    - The players contribute equally to a prize pot, and agree in advance that the first player to have won a certain number of rounds will collect the entire prize.
    - The starting insight for Pascal and Fermat was that the division should not depend so much on the history of the part of the interrupted game, as on the possible ways the game might have continued. A player with a 7–5 lead in a game to 10 has the same chance of eventually winning as a player with a 17–15 lead in a game to 20, and Pascal and Fermat therefore thought that interruption in either of the two situations ought to lead to the same division of the stakes. **In other words, what is important is not the number of rounds each player has won so far, but the number of rounds each player still needs to win in order to achieve overall victory.**
    - Pascal's analysis here is one of the **earliest examples of using expected values instead of odds** when reasoning about probability. Shortly after, this idea would become a basis for the first systematic treatise on probability by Christiaan Huygens.
- Life Annuities, Mortality, other natural observations. This is all about observing phenomena that are not as certain as the stars but follow certain non deterministic laws such that given long enough time or great enough number the laws become deterministic.
- Ars Conjectandi: expected value, Bernoulli trials, law of large number, " From the outset, Bernoulli wished for his work to demonstrate that combinatorics and probability theory would have numerous **real-world applications** in all facets of society, ... and would serve as a **rigorous method of logical reasoning under insufficient evidence**, as used in courtrooms and in moral judgements. It was also hoped that the theory of probability could provide comprehensive and consistent **method of reasoning, where ordinary reasoning might be overwhelmed by the complexity of the situation**."
    - Bernoulli differs from the school of thought known as frequentism, which defined probability in an empirical sense. As a counter, he produces a result resembling the law of large numbers, which he describes as predicting that the **results of observation would approach theoretical probability as more trials were held**. in contrast, **frequents defined probability in terms of the former**. Bernoulli was very proud of this result, referring to it as his "golden theorem", and remarked that it was "a problem in which I've engaged myself for twenty years". This early version of the law is known today as either Bernoulli's theorem or the weak law of large numbers
- Note that it has crystallized that despite being out of control (you can't control tomorrow's weather), and non-predictable (you don't know tomorrow's weather given everything you can know), randomness shows a certain determinism in the long term. See [gambler's ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin) and the above Bernoulli theorem. This long term determinism is predicatble and can be studied like mathematical structures. From a mysticism perspective, the chaos or randomness of the world is made of such underlying structures (the world is made of number (a special type of)). This paves the way for the study of probability to be incorporated to mathematics.
- Energy, gas, entropy, which were non statistical at the time, were later developed into kinetic theory of gases by Maxwell, in which he modelled the gas particles as moving in random directions at random velocities (1859). Clausius, Ludwig Boltzmann and Josiah Gibbs. Albert Einstein's mathematical model for Brownian movement.
- Process like Bernoulli, random walk, poisson gave intuition to more profound structures that, with increase in abstraction, naturally gave rise to a more rigorous mathematical field.
- Measure theory and probability theory: in 1900, David Hilbert presented a list of mathematical problems, where his sixth problem asked for a mathematical treatment of physics and probability involving axioms.
- More and more fields began to use this new approach, [genetics](https://en.wikipedia.org/wiki/Ronald_Fisher), physics, economy, demography, information theory, and most importantly quantum physics. 

More on Random walk:
- In 1880, Danish astronomer Thorvald Thiele wrote a paper on the method of least squares, where he used the process to study the errors of a model in time-series analysis. The work is now considered as an early discovery of the statistical method known as **Kalman filtering**
- The French mathematician Louis Bachelier in his 1900 thesis modeled price changes on the Paris stock exchange, without knowing the work of Thiele.
- In 1905, Albert Einstein published a paper where he studied the physical observation of Brownian motion or movement to explain the seemingly random movements of particles in liquids by using ideas from the kinetic theory of gases. Einstein derived a differential equation, known as a **diffusion equation**, for describing the probability of finding a particle in a certain region of space
- Einstein's work, as well as experimental results obtained by Jean Perrin, later inspired Norbert Wiener in the 1920s[292] to use a type of measure theory, developed by Percy Daniell, and Fourier analysis to prove the existence of the Wiener process as a mathematical object


## Notes
### Adding Trig Functions
https://www.desmos.com/calculator/f78m1f5knh

We shall focus on 2 trig functions. The general form is acos(w1t+h1)+bcos(w2+h2)
- Same frequency (w1=w2): result has same frequency, basically scaled and shifted version of cos
- Same phase and amplitude different frequency: frequency difference changes shape of curve. If amplitude difference is big, the curve looks smoother.

### Statistical Modeling of Time Series
- RV
- iid
- stochastic/random process as collection of RVs
- Signal is an instantiation of a random process
- If 2 signal are assumed iid, we can analyze covariance btw 2 RVs
- a stationary process is a stochastic process whose unconditional joint probability distribution does not change when shifted in time. Consequently, parameters such as mean and variance also do not change over time. 
- consider the stochastic process as a markov chain, if the chain changes then it's non stationary. For example, chirp is not.
- https://otexts.com/fpp2/stationarity.html

### Covariance Matrix
Alwways remember  that data and distributions/functions are the same thing. The value/probability from a function is calculated exactly by number of data.

If x is a direction vector, xSx represents the variance (or weighted variance) of the data in the direction of x. In other words, it gives variance of data if projected onto x.

https://distill.pub/2019/visual-exploration-gaussian-processes/

Examples of cov matrix and xSx:
- This S means its completely correlated: ![](/images/cov-1-1-1-1.png) Note that the direction in 1,-1 is 0, meaning that variance in that direction is 0: ![](/images/cov-1-1-1-1S.png)
- From these 2 examples you see how correlated the distribution is depends on the ratio of variance of covariance: ![](/images/cov-2-1-1-2.png) Here variance is clearly bigger in 1,1 direction: ![](/images/cov-2-1-1-2S.png)
- This is not postive semi-definite and therefore no distrubution can have this cov matrix: ![](/images/cov-1-2-2-1S.png)


In the context of multivariate statistics, S can be seen as transforming a standard normal random vector into a vector with the covariance structure described by S

In relation to least squares and PCA: in least squares you have x and y and you want a matrix A such that Ax and y is closest. 

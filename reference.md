# By Subject
---
# Economy/Finance
See log 2024.10.5

> No one ever made a decision because of a number. they need a story.  --Daniel Kahneman

## Traditional
### Valuation
- [MIT Valuation class](https://www.youtube.com/watch?v=tjNJx2244Lc&list=PLUkh9m2BorqmtIQKZ1jv3uuZDM_bQIICg)

### [Investopedia Technical Analysis Series](https://www.investopedia.com/terms/t/technical-analysis-of-stocks-and-trends.asp)

What is TA:
- Analysis of historical data
- Technical analysts generally believe that prices move in trends and history tends to repeat itself when it comes to the market's overall psychology.
- The core principle underlying technical analysis is that the market price reflects all available information that could impact a market. As a result, there's no need to look at economic, fundamental, or new developments since they're already priced into a given security.


Dow theory: 
- The Dow Theory is a financial theory that says the market is in an upward trend if one of its averages (e.g., industrials or transportation) advances above a previous important high and is accompanied or followed by a similar advance in another average.
- There are six main components to the Dow Theory:
    1. The Market Discounts Everything
    2. primary trends (year), such as a bull or bear market. secondary trends (weeks to months). minor trends (days to weeks)
    3. Primary trends have 3 phases
        - (Bull) Accumulation: Prices and volume up
        - Public participation (or big move) phase
        - Excess phase
        - (Bear) Distribution phase
        - Public participation phase
        - Panic (or despair) phase
    4. For a trend to be established, indices or market averages must confirm each other
    5. Trends must be confirmed by volume (low vol means weakening trend)
    6. Reversals in primary trends can be confused with secondary trends; a possible reversal must be confirmed by comparing indexes.

    > Charles Dow relied solely on closing prices

Trend
- the prices of financial assets generally trend upward or downward; 
    > If people were rational, then support and resistance levels wouldn’t work in practice!
- the price needs to touch the trendlines at least three times.  
- Polarity: A previous support level will sometimes become a resistance level when the price attempts to move back up. 
- Support and resistance zones are likely to be more significant when they are preceded by steep advances or declines.
- Trend is also used in fundamental analysis

Support and Resistance
- Support and resistance can be found in all charting time periods
- If the price moves in the wrong direction (breaks through prior support or resistance levels), the position can be closed at a small loss. If the price moves in the right direction (respects prior support or resistance levels), the move may be substantial.
- Vol: The more buying and selling that has occurred at a particular price level, the stronger the support or resistance level is likely to be. 
- Round numbers: many inexperienced traders tend to buy or sell assets when the price is at a round number. Also, many target prices or stop orders set by either retail investors or large investment banks are placed at round price levels. 
- Moving average is similar to support ![](/images/ma_as_support.webp)
- Fibonacci sequence ![](/images/fib.webp)

Pullback, Retracement, Consolidation
- Most reversals involve some change in a security’s underlying fundamentals that force the market to re-evaluate its worth. Traders use MA, trendlines, and trading bands to flag the point at which a pullback could become reversal.

[Breakout](https://www.investopedia.com/terms/b/breakout.asp):
- A breakout refers to when the price of an asset moves above a resistance area, or moves below a support area.
- Breaking a resistance means others who sell at the resistance have exited and others who hope for breakout are now buying. This should be confirmed by vol
- Breakouts are commonly associated with ranges or other chart patterns, including triangles, flags, wedges, and head-and-shoulders.

Relative Strength:
- While the goal of value investing is to buy low and sell high, the goal of relative strength investing is to buy high and sell even higher. As such, relative strength investors assume that the trends currently displayed by the market will continue for long enough to allow them to realize a positive return


#### Indicators 
Overlays:
- Bollinger Bands: 20 day MA with 2 std ![](/images/bollinger-bands.webp)
- MACD

Oscillators:
- RSI: 
- Stochastic Oscillator
> In general, the RSI is more useful during trending markets, and stochastics more so in sideways or range-bound markets.3
- ROC: generally not used for trading purposes, but rather to simply alert traders that a trend change may be underway.
- MFI (volume-weighted RSI)

Divergence:


#### Patterns
- Stick Sandwich 
- Doji
- Spinning Top

## Option Strategies
### Mine
bullish covered call
- buy a put immediately 
- when price went down, roll down and use the new money to buy underlying so when price goes up you can roll back with a likely net gain. sell the put and use the money to DCA underlying or buy call


# Blockchain
## Learning
Problems of traditional finance or what blockchain can solve
- someone can change the truth. 
- maybe something about inflation

## DEX
### AMM
- suppose a coin is minted with 100 coin 100 usd lp. k=10000
- the price shown would be 1
- now if i want to buy 10 coins i need to pay 10000/90-100=11.111, slippage is 11.1%
- now lp has 90 coins and 111.11 usd. price shown is 1.23457
- now if i provide all coins to lp i also need to provide 12.3457 usd
- lp now has 100 coins and 123.457 usd and k=12345, price shown is still 1.23457
- now if someone buys 10 coins he need to pay 12345/90-123.45=13.7167. slippage is still 11.1%. 
- but i hadn't provided liquidity, price would be 10000/80-111.11=13.89 and slippage is 12.5%. So bigger lp makes slippage lower.
- lp has 90 coins and 137.1667 usd.
- if both the dev and i remove liquidity dev will get 90% and i 10% or dev 123.4 and i 13.7. i lose 11.1+12.3-13.7=9.7 and the other guy 13.7. 13.7+9.7=123.4-100=23.4 is thus what the dev gained.

### Resources
- [investopedia series](https://www.investopedia.com/terms/b/blockchain.asp)
- [Vitalik blog](vitalik.eth.limo)

# Quant
## Ideas
- [Vitalik blog](vitalik.eth.limo)
### Bridge News Bot
Whenever a new coin, particularly mid cap coins, briges, it creates temporary arbitrage opportunities as many people don't know how bridgiing works. This happened to both mars and doge and in both cases thousands can be arbitraged without risk.

### Ensemble model
- model the price directly as buy and sell, in other words, we model the order book, assuming fn(t) number of agents. Each agent has a fa(t) function indicating buy or sell amount at time t. The task is to model these 2 functions.

### Dynamics Model/RL

### News model
- Celebrity or unexpected event. Remember the two price pumps of $TRUMP (GRC and Trump support of crypto). If we can get the news fast and check validity and gauge its influence, this can be good buy indicator.
- Colaboratiion: note for the big KOLs. Also sometiems when a coin is mass buying out KOLs, it means it's preparing to pump. Risk control can potentially guarentee return.

### Indicators
- impulse response:
    - after btc/sol/eth sudden drop/rise
    - after btc/sol/eth sideway
    - after btc/sol/eth long drop/rise
- meme cross-correlation
    - if meme a rises, prob of meme b rise in t days.
- response after sudden rise
- ordered response of groups of memes
- correlation btw x sentiment and actual

### Technical Model
Memes follow certain patterns simpler than stocks. Maybe it's possible to create an algorithm that mathematically get rid of all risks 

### Cabal Model
Using onchain information, telegram, x to predict which cabal group is behind a project; further to identify potential moves by cabals.


## Crypto Specific
[vida](https://www.zhihu.com/question/615961251/answer/3377989786)
### Data Source
General
- [apify](https://apify.com/templates/python-start)
- [yahoo finance intro](https://algotrading101.com/learn/yfinance-guide/)
- [coin gecko](https://www.coingecko.com/learn/python-query-coingecko-api)
- [py crypto compare](https://github.com/lagerfeuer/cryptocompare?tab=readme-ov-file)
- [py coinbase](https://github.com/David-Woroniuk/Historic_Crypto)

Telegram
- [rt tg](https://github.com/sabber-slt/telegram-real-time)
- [Telethon](https://github.com/LonamiWebs/Telethon)

X
- [havent' check](https://www.kaggle.com/code/kaushiksuresh147/twitter-data-extraction-for-ipl2020)
- [havent' check](https://www.kaggle.com/datasets/gautamchettiar/bitcoin-sentiment-analysis-twitter-data)
### Tutorials
- [ether python bot](https://medium.com/@crjameson)
- [ether sandwitch](https://medium.com/@rjaloudi)
- [radium bot github search](https://github.com/topics/raydium-bot?l=python&o=desc&s=stars)
- https://chainstack.com/solana-python-tutorial-querying-and-analyzing-data-from-raydium/
- https://www.youtube.com/@moondevonyt

## General
### Backtesting
- [looks nice library](https://github.com/polakowo/vectorbt)

### Recources
- book (Quantitative Finance and Risk Management: A Physicist's Approach)
- book (Paul Wilmott Introduces Quantitative Finance): read this before the Physicist's Approach book, this is from intro to finance to deep stuff
- book (also by Paul Wilmott, The mathematics of financial derivatives)
- book (brownian motion calculus)
- collections (https://github.com/PlamenStilyianov/FinMathematics/tree/master)
- [science researcher, search "The Capital Asset Pricing Model" and above includes many quant modeling](https://gregorygundersen.com/blog/)
- [python all kinds of stock code](https://medium.com/@crisvelasquez)
- [algotrading sub wiki](https://www.reddit.com/r/algotrading/wiki/index/#wiki_strategy)



## Kaggle
### Data
- [news](https://www.kaggle.com/datasets/aaron7sun/stocknews)

### Tutorial
- [timeseries extensive intro](https://www.kaggle.com/code/neomatrix369/everything-you-can-do-with-a-time-series-stocks)
- [XRBoost](https://www.kaggle.com/code/zonghao/predicting-stock-returns-by-xgboost)
- [top solutions](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/discussion/541003)
- [G-research top 2 answer](https://www.kaggle.com/competitions/g-research-crypto-forecasting/discussion/323098)


# Physics
## Mechanics
[taylor solutions](https://stemjock.com/taylorcm.htm?srsltid=AfmBOopdOKiKrV92Aoo75qMnO8lXN9gmUDkQeaXi0cbGXHgBFPQYZqV0)
### Coordinate Systems
- [some graphs of functions in polar coordinate](https://ximera.osu.edu/mooculus/calculus2/introductionToPolarCoordinates/digInIntroductionToPolarCoordinates)
### Angular Momentum
- [comprehensive guide to why we use it](https://math.stackexchange.com/questions/349907/cross-product-intuition)
### Lagrangian
- [history of least action Veritasium](https://www.youtube.com/watch?v=Q10_srZ-pbs): Hero of Alexandria, Fermat, Maupertuis principle of **mvs** given start and end point in space, Euler improvement to **∫mvds** constrained on constant E and equal E. Lagrange and Hamilton: ∫mv²dt=∫2Tdt=∫[T-V+E]dt so δ∫[T-V]dt=-Eδt=0 (same time constraint). Not sure why E is constant for all paths.
- minimize 2T while ensuring conservation of energy (define V as E-T) so T-V is 2T-E. Bc E is constant this doesn’t change the minimization. Therefore minimizing 2T is same as minimizing T-V if you view V as just a constant-T. But when you give V a meaning, T-V means conservation of energy. if L=2T, we get essentially p'=0 meaning constant momentum. If you want to introduce forces, you need to account for where the extra T comes from, so you need V as a source of change in momentum. Since T+V is conserved, you can replace T with E-V. Of course you can replace 0.1T with 0.1E-0.1V and get something like 10F=ma, but that's just changing unit of force or length. 
- Theoretical minimum has extremely beginner friendly proof of Euler-Lagrange purely with delta. 
- [intro to differential with entropy example](https://mbernste.github.io/posts/functionals/)
- [good intro euler-langrange](https://gregorygundersen.com/blog/2020/05/10/euler-lagrange/)
- https://profoundphysics.com/constraints-in-lagrangian-mechanics/
- https://profoundphysics.com/lagrangian-vs-newtonian-mechanics-the-key-differences/

Calculus of Variation: see math section

### Hamiltonian

### Hamilton-Jacobi
- [blog not comprehensive but links to another source](https://www.samartigliere.com/physics/other-classical-mechanics/hamilton-jacobi-equation/)
- a paper that introduces HJE is in control papers folder (on local file system)
- comprehensive book on least action is in the physics book folder(on local file system)

## Chaos
### General Material
- for overview, use Taylor, classical mechanics.
### Fluid
- [](https://ciechanow.ski/)



## Light
### Interference
[hologram](https://www.youtube.com/watch?v=EmKQsSDlaa4)

# Control
- Optimal control theory: If a trajectory is optimal, then every subsequence of the trajectory is also optimal.

### HJB
Consider a system $\dot{x}(t) = f(x(t), u(t), t)$ and define:
- cost: ${J(u(•)) = \int_{t_0}^{t_f}L(x(s);u(s);s) ds + \phi(x(t_f);t_f)}$ 
    - u(•) means u is a function so J is a functional. Therefore, this is similar to least action except that the argument x in L has to be calculated from the dynamics equations.
    - L is the running cost
    - phi is the terminal cost
- cost-to-go: ${J^*(x;t) = \min_{u(•)} \int_t^{t_f}L(x(s);u(s);s) ds + \phi(x(t_f);t_f)}$ this is cost to go to the destination from x and t, according to optimal control theory, at any point in time, the decision you make should minimize the cost-to-go

The objective is to minimize cost which is a functional. This should remind you of calculus of variation and Hamiltonian mechanics. This is combined with theory of optimality so opptimizing cost is converted to optimizing immediate cost and future cost to go.

Derivation:
- $J^*(x, t)$
- ${J^*(x, t) = \min_u \left[ L(x, u, t) \Delta t + J^*(x + \dot{x} \Delta t, t + \Delta t) \right]}$
- $J^*(x(t + \Delta t), t + \Delta t) \approx J^*(x, t) + \frac{\partial J^*}{\partial t} \Delta t + \nabla J^* \dot{x}\Delta t$
- ${J^*(x, t) = \min_u \left[ L(x, u, t) \cdot \Delta t + J^*(x, t) + \frac{\partial J^*}{\partial t} \Delta t + \nabla J^* \cdot \dot{x} \Delta t \right]}$
- ${\frac{\partial J^*(x, t)}{\partial t} + \min_u \left[ L(x, u, t) + \nabla J^*(x, t) \cdot f(x, u, t) \right] = 0}$ The thing inside min is Hamiltonian
- ${u^*(t) = \arg \min_u \left[ L(x, u, t) + \nabla J^*(x, t) \cdot f(x, u, t) \right]}$

Implications:
- HJB gives 

Example:




### Resources
- [best intro; travelling cost example; discrete and linear](https://people.kth.se/~kallej/eecs291e/lecture21.pdf)

# Math
## Unclassified
### Convolution
- [intro convolution with cookie example](https://www.youtube.com/watch?v=aEGboJxmq-w)

## General
### Math books to read
https://www.3blue1brown.com/blog/book-recommendations

## Basic Analysis
### Calculus
- [derivative with Fermat visual 3b1b style](https://www.reddit.com/r/math/comments/llsw8a/calculating_slope_without_derivativeslimits/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- [potentially useful for real analysis](https://www.reddit.com/r/learnmath/comments/8ipe0u/comment/dytvvkt/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- [notes with graphs for intro real analysis](https://math.fel.cvut.cz/en/mt/pagee1.htm)

### Elementary Functions
Conic functions:
![](/images/conic.png)
- [Feynman why orbits are elipse](https://www.youtube.com/watch?v=xdIjYBtnvZU)
- [why eclipse in conic section 3b1b](https://www.youtube.com/watch?v=pQa_tWZmlGs)
- [parabola animation](https://www.reddit.com/r/3Blue1Brown/comments/ddygcw/manim_animation_parabola/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- [shadows and sun and hyperbola](https://www.youtube.com/watch?v=TfoTBKSIzlM)
- [intro hyperbola](https://www.youtube.com/watch?v=HnHnEnkZpJA)
- [Hyperpolic functions potentially quantum physics with philosophical isights](https://www.youtube.com/watch?v=WL8l16SWp7g&t)

Log and e: 
- [log visual, antishapeshifter, 1/x](https://www.youtube.com/watch?v=G0Fa5Zl-Z3c)

## Functional Analysis
- [23 pages textbook starting from Fourier](https://courses.mai.liu.se/GU/TATM85/FA-history.pdf)

## Transforms
### Fourier
- [a good general introduction for advanced learner](https://databookuw.com/)
- ${\displaystyle {\widehat {f}}(\xi )=\int _{-\infty }^{\infty }f(x)\ e^{-i2\pi \xi x}\,dx.}$
- [Euler's formula with introductory group theory](https://www.youtube.com/watch?v=mvmuCPvRoWQ)
- [Fourier transform as linear algebra](https://www.youtube.com/watch?v=7Vma1G2p6A8)
- $\mathcal{F}\left\{\frac{d^n}{dt^n} f(t)\right\} = (i \omega)^n F(\omega)$
- $\frac{d}{d\omega} F(\omega) = -i \int_{-\infty}^{\infty} t f(t) e^{-i \omega t} \,$ which is Fourier transform of -itf(t), ie: $\frac{d}{d\omega} F(\omega) = \mathcal{F}\{ -i t f(t) \}$

### Laplace
- [high level intuition on laplace](https://qr.ae/p2HJrb)
- [great outline](https://math.stackexchange.com/questions/3190961/how-is-the-laplace-transform-a-change-of-basis/3537213#3537213) and https://math.stackexchange.com/questions/428408/physical-interpretation-of-laplace-transforms

### Discrete Fourier
- [DFT reducible](https://www.youtube.com/watch?v=yYEMxqreA10)
- [FFT reducible](https://www.youtube.com/watch?v=h7apO7q16V0)

### Z

## *Transforms in Engineering
### Window Function
- a mathematical function that is zero-valued outside of some chosen interval.
- The reasons for examining segments of a longer function include detection of transient events and time-averaging of frequency spectra
- Hann window
- Gaussian window

### Windowed Fourier Transform
Definition:
- Forward: ${\displaystyle \mathbf {STFT} \{x(t)\}(\tau ,\omega )\equiv X(\tau ,\omega )=\int _{-\infty }^{\infty }x(t)w(t-\tau )e^{-i\omega t}\,dt}$
- Inverse: 
### Wavelet Transform
Definition:
- ${\displaystyle X_{w}(a,b)={\frac {1}{|a|^{1/2}}}\int _{-\infty }^{\infty }x(t){\overline {\psi }}\left({\frac {t-b}{a}}\right)\,\mathrm {d} t}$
- a is scale, b is translation, so a essentially represents frequency (1/f). 
- if $\psi = e^{\frac{it}{a}}$ then it's basically the same as fourier transform.
- psi is called the mother wavelet and the scaled and translated versions are daughter wavelets
- Inverse: ${\displaystyle x(t)=C_{\psi }^{-1}\int _{0}^{\infty }\int _{-\infty }^{\infty }X_{w}(a,b){\frac {1}{|a|^{1/2}}}{\tilde {\psi }}\left({\frac {t-b}{a}}\right)\,\mathrm {d} b\ {\frac {\mathrm {d} a}{a^{2}}}}$
- inverse is beyond understanding for now

Introduction:
- [very good intro on frequency analysis and wt from climate background](https://www.jstor.org/stable/26232616)
- [great post of birth data with code and intepretation](https://www.kaggle.com/code/asauve/a-gentle-introduction-to-wavelet-for-data-analysis)

Applications:
- [dwt dnn dow paper with preliminary](https://www.iccs-meeting.org/archive/iccs2018/papers/108610377.pdf)
- [dwt and nn predict DOW blog](https://medium.com/@crisvelasquez/riding-the-waves-of-stock-prices-with-wavelet-transform-signals-in-python-e2e81217f9fd)

## Group Theory
- [Euler's formula with introductory group theory](https://www.youtube.com/watch?v=mvmuCPvRoWQ): additive and multiplicative groups of real and complex numbers and symmetries that leave the number line or plane invariant. The definition of i^2=-1 defines the stretching mechanism on the complex plane, with multiplying by i corresponding to a (unit) rotation symmetry. Exponentiation is an isomorphism between the additive and multiplicative groups. With the definition of $x^{(a+b)}=x^ax^b$, sliding the additive number line is same as stretching the multiplicative number line. Thus in the complex plane, sliding along the complex line is the same as stretching by that complex number and when along i, it is rotation.
- see Brilliant->Group Theory for intro


### Space
Inner product space
- any matrix A can define a inner product like this: $\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^T A \mathbf{v}.$
- a vector space has basis vectors and thus dimension regardless of inner product. People assume these together because right after they learn vector space they are thaught how to dot product 2 vectors. Note that all dot products are inner products by definition. Also note that linear transformations can also be defiend without inner product. The bracket notation and the trick of writing vector prodcut of a and b by seperating their basis are defined on inner product space. 

Dual vector space
- any vector space V has a corresponding dual vector space (or just dual space for short) consisting of **all** linear forms on V together with the vector space structure of pointwise addition and scalar multiplication by constants
- a linear form (also known as a linear functional, a one-form, or a covector) is a linear map[nb 1] from a vector space to its field of scalars (often, the real numbers or the complex numbers).
- Note that when you have |a> from a vector space, <a| is a convenient notation that means they are elementwise equal. 

Metric Space
- In mathematics, a metric space is a set together with a notion of distance between its elements, usually called points. The distance is measured by a function called a metric or distance function.

### Topology


## Geometry
[chengtong qiu intro and history](https://www.youtube.com/watch?v=g0yufksQMJU): only Euclid, or the Greeks, made the systems of foundamental laws where all results follow; harmony and simplicity; 

## Linear Algebra
- [visual matrices general](https://www.youtube.com/watch?v=4csuTO7UTMo)
- [visual Gauss elimination](https://www.youtube.com/watch?v=bnC848ie16Q)

### Determinant
Definition:

History:
- A determinant was originally defined as a property of a system of linear equations. 
- Given: $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_1 \\x_2\end{pmatrix}=\begin{pmatrix}y_1 \\y_2\end{pmatrix}$, using equation 1, $x_1 = \frac{y_1 - b x_2}{a}, \quad \text{provided \( a \neq 0 \)}$ substitude into eq.2 $c(\frac{y_1 - b x_2}{a}) + d x_2 = y_2$ simplify to $\frac{c y_1 - c b x_2}{a} + d x_2 = y_2$ or $c y_1 - c b x_2 + a d x_2 = a y_2, (c b - a d) x_2 = c y_1 - a y_2$, so $x_2 = \frac{a y_2 - c y_1}{ad - bc}, x_1 = \frac{d y_1 - b y_2}{ad - bc}$ if ad=bc, the solution needs to satisfy $0 = a y_2 - c y_1, 0 = d y_1 - b y_2$ these two equations actually mean one equation: y1=(b/d)y2. 

Another way:
- if ad=cb, $x_2 = \frac{y_1 - \frac{a}{c} y_2}{b - \frac{a d}{c}}=\frac{y_1 - \frac{a}{c} y_2}{b - \frac{b c}{c}}=\frac{y_1 - \frac{a}{c} y_2}{0}$ is undefined unless y1=(a/c)y2.

## Optimization
### Linear Programming
- [great simple intro with graphs](https://medium.com/@mengsaylms/a-brief-introduction-to-linear-programming-2107e769a1fe)

## Stochastic Calculus
interpreting ∫f dX as a limit of partial sums of integral is tricky, because these partial sums won't converge in the usual way that standard partial sum estimates for the integrals of continuous / Riemann integrable functions behave.

Riemann-Stieljes integral is a generalization of the standard Riemann integral, which allows you to put different weights to different intervals in the partition used to compute the Riemann integral. This weight usually comes from a function (usually a nondecreasing, continuous function). In stochastic calculus, we want to do something similar except we replace this monotone weight function with a random variable (typically a brownian motion).

https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma

### Ito's Lemma
Taylor

Example:
imagine a discrete random walk X(t). Let Y(t)=X^2. Now imagine the first step at t=0 and X=0 is +1. So at t=1, X=1 and Y=1. dY(0)=1 but 2X(0)dX=0. This is corrected by the second order 0.5\*2\*dt=1. Let's walk further. Say X(2)=2 so Y(2)=4. dY(1)=3=2\*1+1. X(3)=1 and Y(3)=1. dY(2)=-3=4\*-1+1. 

Now let Y=X^3 so ito's lemma gives dY=3X^2dX+3Xdt. Again X(0)=0, and X(1)=1, Y(1)=1. dY=1=0+0



Expectation:
Let Y(t)=f(X(t)). In deterministic calculus, E[Yt]=f(E[Xt])=E[f(Xt)] for all t. However, take the example of Y=X^2 where X is wiener. E[X] is always 0, but E[Y] is E[X^2]=t. 

## Calculus of Variation
> On multivariate function where the variables are dependent: let $y=f(x,t)=x^2-t, x=t^2$. For example, we want y=0 by setting dy to 0. $\delta y=\frac{\partial y}{\partial x}\delta x+\frac{\partial y}{\partial t}\delta t=2x\delta x-\delta t$, since x and t are dependent, their variations are as well $\delta x=2t\delta t$. So $\delta y=2x2t-1\delta t=0$, $4xt=1\ or\ 4x^3=1$


### Euler-Lagrange
$A=\int L(q,\dot q, t)dt$

$\delta L=\frac{\partial L}{\partial q}\delta q+\frac{\partial L}{\partial \dot q}\delta \dot q+\frac{\partial L}{\partial t}\delta t  \\ 
\delta L = \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \frac{d (\delta q)}{dt} \\ 
\delta S = \int_{t_1}^{t_2} \left[ \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) \right] \delta q dt$

# Statistics and Probability
See Log 2024.10.12 for overview

## Measure Theory
- [intuitive intro](https://mbernste.github.io/posts/measure_theory_3/): "Measure theory is all about abstracting the idea of “size”. What do we mean by size? Size is a number that we attribute to an object that obeys a specific, intuitive property: if we break the object apart, the sizes of the pieces should add up to the size of the whole."
- [definition based posts](https://random-walks.org/intro.html)
### General Definitions
- $\sigma$-algebra:
a collection of subsets of a given set that satisfies the following properties:
    1. Contains the empty set
    2. Closure under complement
    3. Closure under countable unions
    > These also imply closure under set intersections, differences, and symmetric differences

    > Intuitively, σ-algebra divides the object F into pieces.

- Measure $\mu: \mathcal{F} \to [0, \infty]$
    1. $\mu(\emptyset) = 0$
    2. $∀A∈F,μ(A)≥0$
    2. $\mu\left( \bigcup_{n=1}^{\infty} A_n \right) = \sum_{n=1}^{\infty} \mu(A_n)$

    > A measure assigns each piece (as represented by the σ-algebra) a "size"
- Measurable Space $(\Omega, \mathcal{F})$ a set and its σ-algebra
- Measure Space $(\Omega, \mathcal{F}, \mu)$
- Measurable Function: Given measurable spaces $(F, \mathcal{F})$ and $(H, \mathcal{H})$ a function $f: F \to H$ is a measurable function iff $\forall A \in \mathcal{H}, f^{-1}(A) \in \mathcal{F}$, note that $f^{-1}(A) = \{ f^{-1}(y) \mid y \in A \}$
    > transfers a measure from the domain's measurable space to the codomain's measurable space. $\forall A \in H,\mu(f^{-1}(A))$ is defined
- Simple function: 
- Lebesgue integral: For the Lebesgue integral, a rectangle is formed for each value in the function’s codomain. A crucial difference between the Reimann integral and the Lebesgue integral is that the Lebesgue integral works for functions whose domain is non-numeric

### Probability Measure
- Outcome space ($\Omega$): set of outcomes/things that might happen (always remember that everything depends on space-time)
- Event space (sigma-algebra of outcome space)
- A probability space $(\Omega, E, P)$ is a measure space where $P(\Omega)=1$
- Random variable: 
    - $X: \Omega \to R$. As a measurable function $\forall A \in \mathcal{R}, X^{-1}(A) \in E$.
    - ${\displaystyle P(X=a):=P(X^{-1}(\{a\}))=P(e)=P(w|X(w)=a)}$ for example: ${\displaystyle P(score>60)=P\{X^{-1}((60, 100])\}=P(w|60<X(w)<=100)}$
    - Continuous Random Variable: this requires a sigma-algebra on the real numbers and the choice is the Borel sigma-algebra
- Probability mass function: ${\displaystyle p_{X}(x)=P(X=x)}$
- Probability density function:
    - s
- Expectation: $E(X) := \int_{\Omega} X \ dP$


## Common Techniques
### Basic Transformations
Normalization:

Whitening:
- https://gwpy.github.io/docs/stable/examples/timeseries/whiten/

### Source/Latent Separation
There are source S=[s1(t), s2(t), ...], and observaton X=[x1(t), x2(t), ...]. X=AS. Now you want S from X. S=BX, you want B which is inverse of A.

#### PCA
principal components constitute an orthonormal basis in which different individual dimensions of the data are linearly uncorrelated. PCA-based dimensionality reduction tends to minimize that information loss. Maximizes variance (second-order statistics)
- [PCA visual](https://setosa.io/ev/principal-component-analysis/)

#### ICA
Minimization of mutual information and Maximization of non-Gaussianity (higher-order statistics)
- [ICA very comprehensive and semi rigorous tutorial paper](https://www.cs.jhu.edu/~ayuille/courses/Stat161-261-Spring14/HyvO00-icatut.pdf): want to find independent components->want non-gaussian sources->opitmize non-gaussianity with kurtosis and negentropy
- [ica intro short no proof eeg](https://loonylabs.org/2021/06/03/intro-to-ica/): ![](/images/pca-vs-ica-highlighted.png)



### ANOVA

### Detection Theory
![](/images/f1.png)
- Accuracy: TP+TN/Total
- True positive rate (TPR), recall, sensitivity (SEN), probability of detection, hit rate, power: TP/P
- True negative rate (TNR), specificity (SPC), selectivity: ⁠TN/N
- Balanced accuracy: TPR+TNR/2
- Precision: TP/TP+FP
- F1: 2*TP/(2*TP + FP + FN)=2(precision*recall)/(precision+recall)
- ${\displaystyle F_{\beta }=(1+\beta ^{2})\cdot {\frac {\mathrm {precision} \cdot \mathrm {recall} }{\beta ^{2}\cdot \mathrm {precision} +\mathrm {recall} }}}$

Sensitivity index (d'):
- separation between means: ${d'={\frac {\left\vert \mu _{a}-\mu _{b}\right\vert }{\sigma }}}$
- measures a participant's ability to distinguish between the presence (signal) and absence (noise) of a stimulus. d' = Z(hit rate) - Z(false alarm rate) where Z means z-score for the probability. A higher d' means better sensitivity

Criterion score (d):
- c = -0.5 × [Z(hit rate) + Z(false alarm rate)]
- c measures the participant's decision threshold or bias—how likely they are to say "Yes, the signal is present" regardless of whether it's actually there.
- A low criterion means they are liberal and tend to say "Yes" more often, leading to more hits but also more false alarms.



## Distributions
### Basic
- [great interactive multivariate Gaussian intro](https://distill.pub/2019/visual-exploration-gaussian-processes/): covariance matrix off diagnal values is the slope; Gaussian distributions are closed under conditioning (Bayesian) and marginalization ![](/images/2-variate-gaussian.png)

## Time Series 
### Basic Models
Gaussian Process (infinite dimensional Gaussian distribution, zero mean): ![](/images/gp-cond.png)
- [best intro to gaussian process](https://thegradient.pub/gaussian-process-not-quite-for-dummies/)
- [deeper interactive visual Gaussian process](https://distill.pub/2019/visual-exploration-gaussian-processes/):  ![](/images/gp-kernels.png)
- [GP python code from scratch and packages](https://domino.ai/blog/fitting-gaussian-process-models-python)
- [time series forecasting tutorial paper 26 pages](https://www.robots.ox.ac.uk/~sjrob/Pubs/Phil.%20Trans.%20R.%20Soc.%20A-2013-Roberts-.pdf)
- [interactive gp online](https://www.tmpl.fi/gp/)
- [ultimate guide with visual interaction and derivation and application](https://infallible-thompson-49de36.netlify.app/)

### Applications
- [comprehensive book on data processing UW professor](https://databookuw.com/)
- [comprehensive book on forecasting](https://otexts.com/fpp2)
- [STL](https://www.statsmodels.org/stable/examples/notebooks/generated/stl_decomposition.html): ![](/images/stl.png)

## Probability Theory
### Moments
- Raw moment about c: ${\displaystyle \mu _{n}=\int _{-\infty }^{\infty }(x-c)^{n}\,f(x)\,\mathrm {d} x.}$
- Central moment: ${\displaystyle \mu _{n}= {E} \left[(X- {E} [X])^{n}\right]=\int _{-\infty }^{+\infty }(x-\mu )^{n}f(x)\,\mathrm {d} x.}$
- Normalized/standard moment (n-th central moment divided by σ^n): ${\displaystyle {\frac {\mu _{n}}{\sigma ^{n}}}={\frac { {E} \left[(X-\mu )^{n}\right]}{\sigma ^{n}}}={\frac { {E} \left[(X-\mu )^{n}\right]}{ {E} \left[(X-\mu )^{2}\right]^{\frac {n}{2}}}}.}$

Common moments:
- Mean mu: first raw moment
- Variance: second central moment
- Skewness gamma: standardized third central moment. Left skewed distributions (the tail of the distribution is longer on the left) will have a negative skewness.
- Kurtosis kapa: standardized fourth central moment. measure of the heaviness of the tail

### Characteristic Function
- ${\displaystyle \phi_X(t) = \mathbb{E}[e^{itX}] = \int_{-\infty}^{\infty} e^{itx} f_X(x) \, dx}$

Expectation: 
- ${\displaystyle \frac{d\phi_X(t)}{dt} = i\int_{-\infty}^{\infty} xe^{itx} f_X(x) \, dx}$
- ${\displaystyle \frac{d\phi_X(0)}{dt} = i\int_{-\infty}^{\infty} x f_X(x) \, dx=iE[X]}$ 
- Note that since X is real valued, its fourier transform is conjugate symmetric, so the derivative at 0 is 0 for real component, but there's a non 0 derivative in complex axis if there's a shift in phase of the frequency components, the shift corresponds to the shift of center of mass of the distribution, ie, expectation.

Variance: 
- $\frac{d^2\phi_X(t)}{dt^2} = -\int_{-\infty}^{\infty} x^2e^{itx} f_X(x) \, dx$
- $\frac{d^2\phi_X(0)}{dt^2} = -\int_{-\infty}^{\infty} x^2 f_X(x) dx=-E[X^2]$
- $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$
- The second derivative is a non positive real number. When it's 0, the original distribution is delta, and it's fourier transform is 1, whose characteristic function derivatives are always 0 (0 mean, 0 variance etc). The more negative it is, the more spiky the transform at 0. On the other extreme, if the second derivative were -inf, the transform is delta, and the original distribution would be flat (uniform across -inf to +inf), which indeed has inf variance.

In general: $\frac{d^k\phi_X(0)}{dt^k} = i^kE[X^k]$

- Relating to general FT, $\frac{d}{d\omega} F(\omega) = -i \int_{-\infty}^{\infty} t f(t) e^{-i \omega t} \,$ which is Fourier transform of -itf(t), ie: $\frac{d}{d\omega} F(\omega) = \mathcal{F}\{ -i t f(t) \}$

Taylor expansion: 
- $\phi(k) = \int_{-\infty}^{\infty} p(x) e^{ikx} \, dx = \int_{-\infty}^{\infty} p(x) (1 + ikx - \frac{k^2x^2}{2} + \dots) =  1 + ik \mathbb{E}[x] - \frac{k^2}{2} \mathbb{E}[x^2] + \dots$
- Intuition: from one perspective, if you don't know about the concept of mean or variance etc, Taylor of Fourier of distribution gives approximation of the distribution. Taylor is local. Fourier encodes frequency. So Taylor of Fourier near 0 is good at low frequency. 

### Moment Generating Function (MGF)
Definition:
- $M_X(t) = \mathbb{E}[e^{tX}]= \int_{-\infty}^{\infty} e^{tx} f_X(x) \, dx$
- cf: $\phi_X(t) = \mathbb{E}[e^{itX}]$. 
- Relation to CF: M(it)=phi(t) or $M_X(t) = \phi_X(-it)$

Property:
- Generating moments: $\frac{d^n M_X(t)}{dt^n} \bigg|_{t=0} = \mathbb{E}[X^n]$
- Sum of RVs: since convolution becomes multiplication after Fourier transform, summing RVs becomes multiplication of their MGFs. $M_{S_n}(t) = \mathbb{E}\left[e^{t S_n}\right] = \mathbb{E}\left[e^{t \sum_{i=1}^{n} X_i}\right].$
- Normal distribution: $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}.$ -> $M_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} \, dx = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(x^2 - 2tx)} \, dx = \frac{e^{\frac{t^2}{2}}}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{(x - t)^2}{2}} \, dx.$  The thing inside the integral is gaussian. So $M_X(t) = e^{\frac{t^2}{2}}.$

Taylor: 
- $M_X(t) = \mathbb{E}\left[ e^{tX} \right] = \mathbb{E}\left[ 1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \cdots \right]$

CLT:
- Let $Y_i = \frac{X_i - \mu}{\sigma}$, $S_n = \frac{1}{\sqrt{n}} \sum_{i=1}^{n} Y_i$
- $M_{S_n}(t) = \mathbb{E}\left[e^{t S_n}\right] = \mathbb{E}\left[e^{\frac{t}{\sqrt{n}} \sum_{i=1}^{n} Y_i}\right]=\left( \mathbb{E}\left[e^{\frac{t}{\sqrt{n}} Y_1}\right] \right)^n = \left( M_{Y_1}\left( \frac{t}{\sqrt{n}} \right) \right)^n.$ Note here that adding 2 RVs is convolution of the distributions and multiplications of their transform.
- $M_{Y_1}\left( \frac{t}{\sqrt{n}} \right) \approx 1 + \frac{t^2}{2n} + o\left( \frac{1}{n} \right).$
- $M_{S_n}(t) = \left( 1 + \frac{t^2}{2n} + o\left( \frac{1}{n} \right) \right)^n$. Note this crucial step where the higher order moments/higher frequency components of the original distribution diminish under the n exponential. This is a consequence of the $\frac{1}{\sqrt{n}}$ normalization and is explored more in the CLT section below. 
- $\left( 1 + \frac{t^2}{2n} \right)^n \approx \exp\left( \frac{t^2}{2} \right) \quad \text{as } n \to \infty.$

Normal distribution:
- $M={\displaystyle e^{t\mu +{\frac {1}{2}}\sigma ^{2}t^{2}}}$
- $M=e^{\frac {1}{2}t^{2}}$ for standard normal.
- $\int e^{\frac {1}{2}x^{2}}e^{tx}dx=\int e^{(\frac {1}{2}x+t)x}dx$

Resources:
- [moments visuals](https://gregorygundersen.com/blog/2020/04/11/moments/)

### Law of Large Numbers
Weak law:
- statement: $P(|\frac{X_1+X_2+...)}{n-\mu}|>ε)→0, n→ \infin, \forall ε>0$
- proof (algebraic): $
{\tilde{X}=(X_1+X_2+...+X_n)/n} \\
{E(\tilde{X})=n\mu/n=\mu} \\
{Var(\tilde{X})=n\sigma^2/n^2=\sigma^2/n} \\
{P(|\tilde{X}-E(\tilde{X})|>ε)≤\sigma^2/nε^2} \\ 
$ last step by Chebyshev's inequality which states: ${P(|X - E(X)| > \epsilon) \leq \frac{\text{Var}(X)}{\epsilon^2}}$

### CLT
- statement: $\frac {({\bar {X}}_{n}-\mu )}{\frac {\sigma }{\sqrt {n}}}$ approaches normal distribution as n approaches infinity.

> Note that the law of large numbers is a law producing a number while CLT produces a distribution. Thus when thinking about real world phenomena, you only need to imagine keep drawing samples (a simple for loop) for law of large number to appear but for CLT, you have to repeat drawing the many samples many times (a nested for loop).



Quotes:
- **I know of scarcely anything so apt to impress the imagination as the wonderful form of cosmic order expressed by the "Law of Frequency of Error".** The law would have been personified by the Greeks and deified, if they had known of it. It reigns with serenity and in complete self-effacement, amidst the wildest confusion. The huger the mob, and the greater the apparent anarchy, the more perfect is its sway. **It is the supreme law of Unreason.** Whenever a large sample of chaotic elements are taken in hand and marshalled in the order of their magnitude, an unsuspected and most beautiful form of regularity proves to have been latent all along. -Francis Galton

Proof:
- intuition: when you add many iid RVs you get a normal distribution as per MGF proof. If you divide by n, you get a single number bc n is too big. If you divide by n square root then you get a distribution bc it's not as big. The boundary exponent is 1/2 and anything bigger collapse the distribution to mean while anything smaller makes the distribution's variance infinite.
- characteristic function: see characteristic function/CLT or MGF/CLT section for details.

> Proof of the boundary exponent with MGF: ${M_{Y_n}(t) = \mathbb{E} \left[ e^{t Y_n} \right] = \mathbb{E} \left[ e^{t \frac{S_n - n \mu}{n^{\alpha}}} \right]} = \left( \mathbb{E} \left[ e^{t \frac{X_1 - \mu}{n^{\alpha}}} \right] \right)^n. \\ 
{\mathbb{E} \left[ e^{t \frac{X_1 - \mu}{n^{\alpha}}} \right] = \mathbb{E} \left[ 1 + t \frac{X_1 - \mu}{n^{\alpha}} + \frac{t^2}{2} \frac{(X_1 - \mu)^2}{n^{2\alpha}} + O\left( \frac{1}{n^{3\alpha}} \right) \right].} \\
{\mathbb{E} \left[ e^{t \frac{X_1 - \mu}{n^{\alpha}}} \right] = 1 + \frac{t^2 \sigma^2}{2 n^{2\alpha}} + O\left( \frac{1}{n^{3\alpha}} \right)} \\
{M_{Y_n}(t) \approx \exp \left( n \cdot \frac{t^2 \sigma^2}{2 n^{2\alpha}} \right) = \exp \left( \frac{t^2 \sigma^2}{2 n^{2\alpha - 1}} \right)}
$ If a < 1/3, O^n diverges meaning the  higher order moments grow to infinity. If a < 1/2, O^n collapses but M diverges also meaning infinite higher order moments. If a > 1/2, O^n collapses to 0, meaning the distribution. Only when a = 1/2 will $M_{Y_n}(t) \approx \exp \left( \frac{t^2 \sigma^2}{2} \right)$. In general, a = 1/n! collapse nth moment. 

## General Resoures
### Books
### Website
- [](https://random-walks.org/)


# Information Theory
## Concepts
### Entropy

> Note that ln(0.1x) = ln(x)+ln(0.1), ln(x)=ln(0.1x)+2.3 Therefore 0.1x is much smaller than ln(0.1x)



# Cognitiive
## Embodied
- [time representation embodied in space](https://www.sciencedirect.com/science/article/pii/S001002770700087X): asymetrical relatiionship (lightyear); clever expriments (growing lines with misleading duration-displacement relatoinship)


# Neuro
## EEG
### Classification
Traditional:
- [eeg to emotion with traditional processing](https://bcmi.sjtu.edu.cn/~blu/papers/2014/2.pdf)
- [SSVEP](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4640776/): 60 characters/min
- [p300 speller](https://ieeexplore.ieee.org/document/1454155)
- [eeg to color with muse 2](https://arxiv.org/pdf/2008.07092)

DL:
- [hands on eeg to 4 words](https://justlv.medium.com/using-ai-to-read-your-thoughts-with-keras-and-an-eeg-sensor-167ace32e84a)
- [BELT: pretrained eeg encoder SOTA?](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10649644)
- [more nuanced improvement of above, same PI](https://arxiv.org/pdf/2408.04679)
- [eeg to robot control, same PI](https://arxiv.org/pdf/2410.02141)
- [transformer eeg to open text](https://arxiv.org/pdf/2112.02690): ![](/images/eeg-to-text-res.png)
- [diffusion eeg to image](https://arxiv.org/pdf/2410.02780v1)
- [recreating what's seen eeg to text coder to diffusion](https://arxiv.org/abs/2309.07149)
- [eegmmidb with NN and application in typing](https://arxiv.org/pdf/1709.08820): classifying 4 action intents. 7 characters/min for typing app.

### Spectrum Analysis
Alpha:
- [speed of alpha predicts visual temporal resolution](https://doi.org/10.1016/j.cub.2015.10.007): 

## MRI
### Classification
- [mri LLM to sentence from imagined or perceived sentence or video](https://www.nature.com/articles/s41593-023-01304-9)

## Theory of Learning/Memory
- [neural reuse](https://pubmed.ncbi.nlm.nih.gov/20964882/)

## Computational
### Introduction
- [advanced lecture](https://www.cns.nyu.edu/~rinzel/CMNSS10/)
- [sources?](https://www.cns.nyu.edu/~eero/teaching.html)

### Predictive Coding
Rao 1999
- feedback connections from a higher- to a lower-order visual cortical area carry predictions of lower-level neural activities, whereas the feedforward connections carry the residual errors between the predictions and the actual lower-level activities.

## Anatomical
### Mapping
- [neuronal wiring diagram of a complete fly brain](https://www.nature.com/immersive/d42859-024-00053-4/index.html)

## Frohlich lab onboarding/biomedical research involving human
### Safety Plans
- [SV](https://ehs.cloudapps.unc.edu/LabSafetyPlan/Controller?mode=processViewPlan&id=202416216)
- [MEJ](https://ehs.cloudapps.unc.edu/LabSafetyPlan/Controller?mode=processViewPlan&id=202416190)
### IRB training
- belmont report: 1. respect for persons (informed consent, protection of vulnarable groups) 2. beneficence (no harm, maximize benefit and minimize harm) 3. justice (fair distribution of benefits and burden)
![](/images/belmont.png)

### Responsible Research Conduct (RRC)
- Misonduct: Fabrication, Falsification, Plagirism
- Authorship
- Mentor-Mentee relationship building
- Data management
- Peer review
- Animal study
- Conflicts of Interest and Commitment
- Collaborative Research, patent, company and national fund
- human study, Common Rule

### UNC EHS https://ehs.unc.edu/training/orientation/clinic/
- Tubercolosis, transmission, development, skin test and treatment
- HIV, HAV (Hepatitis A), HBV, HCV
- fire
- biohazard, specimens, medial wastes, exposure control
- personal protetive equipments
- needle
- chemicals, distinct hazard and labeling

### COLUMBIA-SUICIDE SEVERITY RATING SCALE (C-SSRS)
- SUICIDAL IDEATION
- Actual Attempt:
A *potentially* self-injurious act committed with at least *some wish* to die, as a result of act. 

### GCP (good clinical practice) for Clinical Trials with Investigational Drugs, Biologics and Devices
- belmont report
- International Conference for Harmonisation->International Council for Harmonisation: ICH is an attempt to streamline the process for developing and marketing new drugs internationally.
- process for drug development. Investigational New Drug (IND). New drug applications. 
![](/images/IND-1.jpg)
![](/images/IND-2.jpg)
- Guideline for Good Clinical Practice (GCP) or ICH E6; “Clinical trials should be conducted in accordance with the ethical principles that have their origin in the Declaration of Helsinki, and that are consistent with GCP and the applicable regulatory requirement(s).
- obligations of a sponsor-investigator
- usage of investigational new drugs
- informed consent
- audits and inspections
- Adverse Events

- devices, significant risk device, class I, II, III; 510(k) (Premarket Notification), PMA (Premarket Approval), Investigational Device Exemption application (IDE)
- investigator obligations,Contract Research Organization (CRO)


## Tools
### EEG Streaming
- [openvibe](https://openvibe.inria.fr/discover/)

### General Data Streaming
- LSL: server based, the outlet starts multiple TCP and UDP servers and inlet requents stream

### Physiological data processing
Software:
- NFBLab
- MNE
- https://www.neuroexplorer.com/
Suggestions:
- https://sccn.ucsd.edu/wiki/Makoto's_preprocessing_pipeline
- [ICA labeling independent compoennts from eeg (diipole)](https://labeling.ucsd.edu/tutorial/labels): ![](/images/IC-labeling.png)


### Dataset
- [eegmmidb: eeg data for real and imagined hand and foot control based on 4 stimulus directions](https://archive.physionet.org/pn4/eegmmidb/)
- [ZuCo: eeg and gaze data when reading texts](https://arxiv.org/abs/1912.00903)

- [P300 EEG data](https://www.nature.com/articles/s41597-022-01509-w)

## Anatomy
### Videos
- [100 MICRO MRI](https://www.youtube.com/watch?v=I0fjPyk1eHM&list=PLlL7CEMX5bxzl1TqkJRK3pMV4Ax6By4bN&index=6)

## Unclassified
- [llm to predict neuroscience research result and help with direction](https://braingpt.org/)

## Logistics
### Potential Research
- https://enyanglab.org/
- https://blender.cs.illinois.edu/publications/

# Language
## Latin
- [meter](https://hypotactic.com/latin/index.html?Use_Id=met1)
### Metamorphoses
- [sing with lyre](https://www.youtube.com/watch?v=UlfRPgL2MXg)
- [metamorphosis meter read with eng translation](https://www.youtube.com/watch?v=FBwwNXbaznQ&t=48s)

## Theory
### Semantic Distance
https://stackoverflow.com/questions/399200/calculating-the-semantic-distance-between-words

# Health
## Top Hat
- VO2max: maximum liter of O2 per minute
- Aerobic vs anaerobic: Fats, carbohydrates and proteins can be used for fuel during aerobic metabolism; only carbohydrates in anaerobic and without oxygen
- \>=5days/week of moderate intensity exercise for 30m/d for an accumulated total of 150 minutes or more of exercise per week
- moderate intensity exercises are estimated at 50-70% of your Max Heart Rate
- 3 or more days per week of vigorous intensity exercise for 20+ minutes per day for an accumulated total of 75 minutes or more of exercise per week
- vigorous intensity exercises are estimated at 70-85% of your Max Heart Rate

### Nutrition
- 45-65% of daily calories from carbohydrates, 25-35% of daily calories from fat, with <10% from saturated fat and 10%–35% of calories from protein.
- Carbohydrates are classified as sugar, starch and fiber. **Sugar** is a type of simple carbohydrate, which is digested rapidly and causes a surge of energy, followed by a crash once metabolized.  **Starches** are complex carbohydrates which take the body longer to break down and therefore provide a more sustained amount of energy and don’t cause a crash. Common examples are whole-grain bread, legumes and food high in fiber. Fiber is a crucial type of carbohydrate as it can’t be digested fully and therefore helps to maintain intestinal health.
- In general, it is best to limit consumption of simple carbohydrates and opt for complex carbohydrates and fiber when possible.
- Healthy fats are typically unsaturated and include nuts, seeds, some types of fish, walnuts and peanut butter. Fats with less health benefits often have large amounts of saturated fats and include butter, ice cream, and some red meat
- 45g grams of protein perday
- adequate intake of 2,700 ml/day for young women (ages 19-30) and 3,700 ml/day for young men (ages 19-30) which is about 11-15 cups per day.
- vitamin:  [vitamins and minerals](https://www.hsph.harvard.edu/nutritionsource/vitamins/)


### Transtheoretical Model
Precontemplation, Contemplation, Preparation, Action, and Maintenance

Barriers:
- Lack of time: The idea of “go big or go home” does not apply to exercise! You do not need to dedicate a large amount of time to exercise; you simply just need to move! 
- lack of energy: just do it
- fear of injury: A pre-participation risk assessment for physical activity, in the form of a PAR-Q

Setting a "SMART" goal (specific, measurable, achievable, realistic, timely)

# Computer
## Graphics
- [great interactive visual guide to everything](https://ciechanow.ski/lights-and-shadows/)(https://ciechanow.ski/cameras-and-lenses/)(https://ciechanow.ski/curves-and-surfaces/)

### 3D ML Models
- [NeRF]
- [Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf)
- [text to 4d with Gaussian](https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/): 1. multiview text-guided latent diffusion model MVDream and the general text-to-image latent diffusion model Stable Diffusion during score distillation 2. optimize the 3D Gaussians 3. combine the text-to-video and the text-to-image models and optimize the deformation field to generate the temporal dynamics

# AI 
## General Notes
### Book Notes
CS229:
- h is the hypothesis, or our approximate function
- θ is parameter 
- J is cost function. eg MSE: ${J(\theta)=1/2\sum_{i}{(\theta^Tx_i-y_i)^2}}$
- linear model: $h(x)=\theta^Tx$
- LMS update: ${\theta_j:=\theta_j+\alpha(y^i-h_{\theta}(x^i))x_j^i}$
- superscript is sample number usually i from 0 to d; subscript is data dimension also i from 0 to n

## Traditional
### SVM
See CS229 notes

## NN Basics

### Autoencoder
- impose a bottleneck in the network which forces a compressed knowledge representation of the original input.
> if weights were linear, this is similar to PCA
- techniques to impose the bottleneck
    - less nodes in middle layers. no explicit regularization term. 
    > note that even when middle layer has 1 node, the network can still learn no representation by simply having a good decoder that memorized all mappings from unique numbers of the middle node to images
    - sparse activation to encourage using less middle layer nodes. L1 reg or KL of a bernoulli where p is desired percentage of activation of a certain neuron.
    - denoising autoencoder
    - contractive: enforce small derivative of hidden layer activation wrt input. Model contracts a neighborhood of inputs into a smaller neighborhood of outputs. reg is Frobenius of Jacobian


### VAE
- make latent of autoencoder a dstribution instead of single number. eg. Mona Lisa's "smile" latent should be a wide distribution instead of a definitive number
- another motivation is the problem of powerful decoder mentioned above: ![](/images/vae-reg.png)
- to use a distribution instead of number as latent, a statistical trick needs to be applied, which results in this loss: $min[L(x, \hat{x}) + \sum_j KL(q_j (z|x)||p (z))]$
- training also involves a reparametrization trick: ![](/images/vae-reparam.png)
- clustering result comparision: ![](/images/vae-clustering.png)


### Diffusion as Score based model
[author's blog, score based](https://yang-song.net/blog/2021/score/)
- score function: gradient of the log probability density function
- p(x) requires a normalizing constant Z which is iintractable: ${s_\theta (x) = \nabla_{x} \log p_\theta (x ) = -\nabla_{x} f_\theta (x) - \underbrace{\nabla_x \log Z_\theta}_{=0} = -\nabla_x f_\theta(x)}$ 
- The key challenge is the fact that the estimated score functions are inaccurate in low density regions, where few data points are available
- solution is to add Gaussian noise to produce low prob data 

### CLIP
![](/images/clip.png)
Both encoders are pretrained transformers. Text encoder is GPT like while image encoder is based on a vision transformer. Training involves cross-modal similarity loss and weight updates jointly on the two encoders

### Word2Vec & GloVe
![](/images/word-2-vec.png)
note that there are two embedding matrices for context and non context word. Otherwise similar words will have similar embed with themselves AND next words and this repeats so everyone has same embed. 

### ELMo: Context Matters
- A word has multiple meanings depending on context
- Instead of using a fixed embedding for each word, ELMo looks at the entire sentence before assigning each word in it an embedding. 
- It uses a bi-directional LSTM trained on language modeling task

### Transformer
arch

normalization
- Byte-Pair Encoding or WordPiece for raw words mapped to unique int ids (30k–50k subword types)
-  $\text{InputVec}_i = \text{TokenEmbedding}_i \times \sqrt{d_\text{model}}+\text{PositionEmbedding}_i$
- $ \text{LayerNorm}(h) = \frac{h - \mu}{\sigma} \odot \gamma + \beta$, h is the individual input vector 1xd, gamma and beta are learnable params
> batch normalization is tricky to apply to sequence models (like transformers) where each input sequence can be a different length. Second, layer normalization is trivial to parallelize when doing distributed training, whereas batch normalization requires extra communication overhead between gpus because the batch is split up.

> Note that mean of a vector is beta and var gamma squared. There's a property of such vectors X. $|x|^2=\sum^n x_i^2=n\frac{\sum^n (x_i-\beta)^2-\beta^2+2x_i\beta}{n}=nVar(x)-n\beta^2+2\beta\sum x_i$.  Attention computes the dot product of 2 such vectors, $\sum^n x_i y_i=n\frac{\sum^n x_i y_i}{n}$. If x and y are 0 mean, then their dot product is nCov(x,y). If they are further of unit variance, then dot product equals nCorr(x,y)
- drop out, MHA, Residual connection

## Inside NN
See Intelligence section below
### Loss Landscape

### Representation Manifold
- [best visual intro](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)

### Representation
- [linear representation hypothesis](https://arxiv.org/abs/2311.03658): high-level concepts are represented linearly as directions in some representation space
- [UNIVERSAL NEURONS IN GPT2](https://arxiv.org/abs/2401.12181): 
    - 1-5% of neurons are universal. they usually have clear interpretations. deactivating attention heads, changing the entropy of the next token distribution, and predicting the next token to(not) be within a particular set. 
    - Olah et al. (2020b) propose three speculative claims regarding the interpretation of artificial neural networks: that features—directions in activation space representing properites of the input—are the fundamental unit of analysis, that features are connected into circuits via network weights, and that features and circuits are universal across model
    - semantic features neurons corresponding to coherent topics (Lim and Lauw, 2023), concepts (Elhage et al., 2022a), or contexts (Gurnee et al., 2023).

### World Models
- [SORA doesn't learn physical law](https://phyworld.github.io/)

## Practicality

## Tuning
### LOTTERY TICKET HYPOTHESIS
Train a network, prune low magnitude weights, revert the rest to initialization state, train again, iterate several times.

When randomly reinitialized, winning tickets perform far worse, meaning structure alone cannot explain a winning ticket’s success.

One possible explanation for this behavior is the good initial weights are close to their final values after training—that in the most extreme case, they are already trained. However, experiments show the opposite—that the winning ticket weights move further than other weights.

we hypothesize that the structure of our winning tickets encodes an inductive bias customized to the learning task at hand. Cohen & Shashua (2016) show that the inductive bias embedded in the structure of a deep network determines the kinds of data that it can separate more parameter-efficiently than can a shallow network

#### Early Bird Tickets
we discover for the first time that the winning tickets can be identified at a very early training stage, which we term as Early-Bird (EB) tickets, via low- cost training schemes

## Other Topics
### Audio Transformer
[wav2vec2](https://arxiv.org/abs/2006.11477)
- convnet encoder on spectrogram

[openai whisper](https://cdn.openai.com/papers/whisper.pdf)
- Mel spectrogram + conv
- encoder-decoder

# Intelligence
## Representation/concept
It's observed that neural networks, from LLM to basic MLP with a few dozen neurons (Hinton Nature), from autoencoders to RNNs, and with all learning paradiams from classification to RL and diffusion, there are activations of certain neurons that match our intuitive understanding of concepts. It feels to good to be true that one neuron can tell if an input is about a male or female, or that the input is about somthing old or new. 

We first need to understand why. Why do they "have to" develop these concepts. Or why do WE have to develop these concepts. Theoretically, the network can perfectly fit the distribution without developing such intuitive features, just as we humans can think about each person as competely distinct things without the help of labels such as species or genders. To understand why we need such features we first analyze the differences when we do and do not abstract such regularities. We will use a the seemingly controversial example of deciding what to say when seeing a stranger. We have a concept of nationality and it's intuitive to use whatever language you believe is the person's native language based on your nationality guess. In contrast, if we don't use such a nice feature, but focus on, say, the length of his middle finger or the color of his lips, then even if we could end up using the right language based on these strange features, it would require a more complex decision rule. We should further develop a quantitative description of this example. Suppose that one nationality correspond to exactly one language preference, then we can say that the language we need to use depends exclusively on his nationality. It's important then to understand things that are "excluded" when making this decision. For example, it may not depend at all on their finger length or lip color. We borrow from physics and say that one's language preference is symmetric under change of lip color or finger length. Symmetric just mean being the same under those actions. 

Once we established that it's good to have this feature extraction ability, we can ask how. 



### Concept as Symmetry

## Linear
### Concept Algebra
- Y: set of images, 
- X: set of prompts, 
- C: set of latent variabels used to generate X from Y, st $P(y \mid X = x) = \int P(y|C = c)P(C=c|X=x)dc$
- C is complicated so we introduce Z that's C-measurable. So Z maps C to Z which is the σ-algebra of ℤ which is the set of concepts (that's easier to work with than the set C)
- now instead of using P(c|X) which describes how prompts induce latent distribution, we use P(c|Z). To define the situation in which information of Z is same as that of X, we define the notion of "sufficency". A set of concepts ℤ1,...ℤk is sufficient for a prompt X if 
- $p(y |X=x) = \sum_{z_{i:k}} p(y | z_{1:k} )p(z_{1:k} | X=x)$ note how the integral over C becomes sum over Z 

# Engineering
## AI
### Computer Use
Computer Use (Anthropic)
- screenshot based, move cursor (so OS wide)

Operator/Computer Using Agent/CUA (openai)
- 

Manus


Browser Use
- optional screenshot, mainly DOM tree parser. 

A5-Browser-Use
- chrome extention with server side Browser Use 

CrewAI

Atomic Agents

## Automation
Also see AI-Computer Use
### Browser
beautifulsoup

selenium webdriver 
- [tutorial](https://youtu.be/NB8OceGZGjA)


## AR
### Interaction
- [contact lens RF detection](https://www.nature.com/articles/s41467-024-47851-y)
- [SSVEP](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4640776/): 60 characters/min
- [color muse 2](https://arxiv.org/pdf/2008.07092)
- voice:
- head/hand/foot movement
- gaze
- Facial Gestures
- Pose Detection
- EMG sensors 


## Brain Hacks
### EEG Interpretation
- [typing mega thread](https://openbci.com/forum/index.php?p=/discussion/206/openvibe-p300-speller-tutorial-questions)
- [indian boy thread](https://anushmutyala.medium.com/muse-101-how-to-start-developing-with-the-muse-2-right-now-a1b87119be5c)

### Muse IO
- [some online viewing and eeg experiment](https://eegedu.com/)
- [web muse viewer](https://muse-eeg-app.firebaseapp.com/)
- [web muse](https://medium.com/@castillo.io/muse-2016-headband-web-bluetooth-11ddcfa74c83)
- [web muse blog and eeg intro](https://medium.com/neurotechx/a-techys-introduction-to-neuroscience-3f492df4d3bf)

# Dynamics of Brain
- [critical brain hypothesis](https://www.youtube.com/watch?v=hjGFp7lMi9A)

# Music
## Tools
- [online frequency analyzer](https://www.maztr.com/audiospectrumanalyzer)


-------------------------------



# Life Tools
##
### Math Animation 
https://github.com/ManimCommunity/manim/






# By Source
## Books
### The man who solved the market (Simons biography)

### Investments
An investment is the current commitment of money or other resources in the expectation of reaping future benefits.

### RL


### Analysis I and II
See references/books/Analysis

## Online Classes
### Hinton Old Coursera



### [Classical Mechanics]

### Quantum Mechanics



### Statistical Mechanics
See references/classes/TM-StatMech.md

### Particle Physics
evolution of the concept of particle

energy of photon
- wave length, frequency and speed of light: $\boldsymbol{\lambda f=c}, 2\pi f=\omega, \lambda\omega=2\pi c,\boldsymbol{\omega=\frac{2\pi c}{\lambda}}$
- $E=\hbar\omega$
- total energy of harmonic oscillator is determined by both amplitude squared and frequency, but energy of radio  wave is dependent on just amplitude squared. However, individual photon energy depend on only frequency. Radio waves are made by lots of photons. This is a question.

unit

momentum


### Eth.build
[eth.build illustration on all basics](https://www.youtube.com/list=PLJz1HruEnenCXH7KW7wBCEBnBLOVkiqIi)

### Khan Macro

### Khan Finance
- APR and effective APR
- credit system (retailer pays to visa, issuing bank and acquirer): ![](/images/credit-system.png)
- payday loans (very high interest, ~700 APR)
- Personal bankruptcy
    - chapter 7 straight bankruptcy. 10 year on credit record, some debt like student loan can't be forgiven
    - chapter 13 reorganization. 10 year credit record. repayment plan and 3-5 years to pay back.

- present value, future value, discount rate, interest rate (discount rate is used to determine the present value of future cash flows while interest rate is the cost of borrowing money) (The interest rate and discount rate might differ due to factors like inflation, risk premium, or differing compounding conventions.)

housing
- personal balance sheet, equity=asset-liability

## Brilliant
### Crypto

### Group Theory

## Websites
### Ethereum & web3


## Online Videos
### [Hologram](https://www.youtube.com/watch?v=EmKQsSDlaa4)
- we need the whole EM field from the scene
- at 20:44, great animation on diffraction grating  

## Papers
### Representation

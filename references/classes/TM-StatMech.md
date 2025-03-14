# Conclusion
- This portion of Statistical mechanics is based primarily on two laws: symmetry of configuration and conservation of energy. 
- Symmetry of state and configuration is a foudamental law that determines probability of phisical phenomena. It states that head and tail have equal probability or any configuration of states for many particles is equally likely. The intuition is that a coin landing on head or tail is physically indistinguisible, ie they are the exact same thing, and thus have the same physical properties (for our interest, the property of landing with a probability). Everything else about probability of states or configurations and thus entropy follows naturally from probaiility theory. 
- Conservation of energy constriants the probability disrtibuiton. It states how configurations should flow btw each other, ie, it provides the transition probability of a markov process. Intuitively a configuration where all particles are stacked at one place is very unlikely because potential energy will create a high transition probability that moves this configuration to a more diffused one. Thus the property of energy is like weight of one side of a coin. Energy "breaks" the perfect symmetry of configurations and assigns "weight" to different configurations. But the foundamental idea of perfect symmetry is still neseccery.

> Special note on 2nd law: the 2nd law does NOT state that entropy will ALWAYS increase or not decrease. It is empirical or at best statistical, stating that entropy will very LIKELY to increase.

> Special note on entropy: Entropy measures uncertainty. when people use the example of tidy vs messy room, they confuse configuration, system and state. The room, as composed of your books and desks and cloths etc, or quantitatively all momentum and positions of all molecules thereof, is the system. A specific arrangement of things in your room, or a specific list of numbers for all those momenta and positions of the molecules, is a state. A system doesn't have entropy. A state doesn't have entropy. A configuration does. A configuration is a collection of states described by letting certain numbers of things in the system (call it subsystem) in certain states. A system has an entropy only when it's in equilibrium where it is in a specific configuration. But entropy can also be defined by a system together with what you know about the system (which essentially gives you a configuration). This has the practical meaning of *entropy as what you don't know about what you WANT to know*. For example, if you know the exact state of a system, then it's 0 entropy. If you know it's one of 2 states, it's log0.5 entropy. Note that in thermoequilibrium, the entropy comes from probability of a molecule in a certain state, not from probability of particular congrete state, thought that  can be calculated from the former. 

> more on entropy: The **phase space** trajectory of such system will be confined to a hypersurface where Hamiltonian is constant or not confined but follow boltzmann distribution (each point in phase space has prob according to the distribution). We can draw a volume and if we know prob of the system being in each state within, then we can calculate the entropy associated with this knowledge of the sytem. But this entropy is not the equilibrium entropy which has energy constraint. This entropy is more about information or what we know about the system. We need to be careful about saying what we know. Knowing the room is a room dramatically reduces entropy since it's a very different configuration than a pure box of particles. Knowing the energy constraint and whether equilibrium is reached is also informative.

> Systems: note that there are different kinds of ensembles. It's important to know what you want to know so you know what to measure. In this lecture **microcanonical and canonical ensembles** are used in this order.

> On coin flip: when using coin flip analogy we have to be careful because there are only two states and entropy is parametrized by one variable (prob of up or down). When solving the constraint optimization such system will have a one solution independent of entropy, or it has only one configuration that  satisfy  the energy constraint (think about drawing a vertical line on y=f(x), you get only one intersection). This is different in any higher dimension. There will be many configurations that satisfy energy constraint but are not max entropy. 

# Introduction
> both quantum and classical mechanics have perfect predictability in the sense that we know the 'initial conditions' and 'laws of evolution' perfectly and will predict its evolution perfectly in a 'closed system'. Statistical mechanics deals with situations when we DON'T know the initial conditions perfectly or don't know the laws of motion or when we don't have a closed system. In those situations we resort of probability. And probabilty theory works well when we have a large number of things

> **Probabilities are usally taken to be equal for configuratoins which are related to each other by some symmetry.** When there's no symmetry, you may be able to use symmetry from some deeper underlying theory. But in absence of this, probabilty is only measureed by experiment. Another way to calculate probability has to do with evolution of a system. If a system transitions among several states, then without knowing the initial condition, finding the system in each state has equal prob because we assume a "symmetry" in evolution (constant transition time which also means same time spent in each state)
- conservation of information,  (note that friction just means it's hard to track where the information went but it's still there and never lost). - **model system**: Another description of the symmetry argument is if a system have N states and M < N have uniform 1/M prob. Then after any time, there will still be M states having 1/M prob though which states have these prob may have changed. Entropy for this is logM
- conservation of entropy: if we can follow the evolution in infinite detail. Increase  in entropy literally means we are starting to lose track of measurement and our ignorance is going up.
- lioville's theorem says the volume in phase space doesn't change so the number M remains (for the friciton example, the object's phase volume might converge to only p axis, meaning they all stop, but the firction provider's phase space volume will expand)
- entropy: $-\int p(x_i)log(x_i)dx_i$, log is base e
- n coins: nlog2. 
- n coins where we know all coins except one are heads: logn 
- addditivity of entropy when systems don't correlate (logAB=logA+logB)
> quantum mechanics deals with uncertainty in pure state and statistically mechanics deal with uncertainty implcit in mixed states

## boltzmann constant
- temperature and energy: E=3/2kt where t is in Kelvin. k=1.4x10^-23J/K. T=kt which now has same unit of energy
- Carnot entropy is a function of energy and inverse temperature (Kelvin) and Boltzmann entropy is dimensinless. So $S_{boltzman}=\frac{1}{k}S_{carnot}$

## primer on temperature
- dE=TdS

# boltzman distribution and partition function
> most of statistical mechanics is about partition function and derivatives
- suppose we have *N identical systems*, which you can think of as N atoms. Each can occupy a certain state among *n states*, which you can think of as all the combinations of positions and momenta. For a given set of n1,n2,... where n1 denotes the number of systems in state 1, the number of ways to configure the N systems where n1 systems are in state 1 and n2 systems are in state 2 etc, hereafter denoted $\Omega$ is $\boldsymbol{\Omega=\frac{N!}{n_1!n_2!...}}$
- using Stirling approx, where N!=$N^Ne^{N}$, the number of configs are $\frac{N!}{n_1!n_2!...}=\frac{N^Ne^{-N}}{\Pi n_i^{n_i}e^{-n_i}}=\frac{N^Ne^{-N}}{e^{-N}\Pi n_i^{n_i}}=\frac{N^N}{\Pi n_i^{n_i}}$
> proof: multiplication is easier with log so we take $logN!=\sum_{x=1}^N logx$ which is approximately area under logx from 1 to N. Antiderivative of logx is xlogx-x so we have 1+NlogN-N. So $N!=e^{1+NlogN-N}=e^{-1}N^Ne^{-N}$, (the first part is somehow negligible?)
- At every next instant, this configuration of systems partitioned to states will change. Accodring to *symmetry*, any configuration is equally likely. As always, you can think of this as either many N systems presented altogether or one N systems propagating over a long time. Either way, you can count through space or time how many times a certain configuration (defined by the set of ni) appears. If one configuration offers more ways for the systems to partition itself into such set of states, then it's more likely to be observed. 
- Thus the partition that provides the *maximum number of ways to rearrange the system* (if system a and b are in state 1 and c in state 2 then switching state of a and c preserves the parition, ie, still 2 systems in state 1 and 1 in state 2) is the most likely partition. When we have that configuration, ni/N will be the probability, when the systems are at that maximum configuration, of finding a random system at state i. 
- maximizing $\frac{N^N}{\Pi n_i^{n_i}}$ involves lots of multiplications. So we use log and get $NlogN-\sum n_i log{n_i}$. Now ni/N=Pi. so $NlogN-\sum n_i log{n_i}=-N\sum P_i log{P_i}$ which is N times entropy.
- thus **the mostly likely configuration has maximum entropy among all possible configurations**. So think about many N systems, one configuration will be observed most many times, and the entropy of that configuratiion is highest among entropies of all other configurations. Of course entropy fluctuates (capped at max entropy) and there are chances when extremely unlikely configurations (low entropy) happen. 
- We will be discussing this most likely configuration or this max  entropy condition becausue **2nd law of thermodynamics** tells us that at equilibrium the systems tend to max entropy. 
- In addition, we can study how Omega varies as we change the configuration by studying the differential of the log of Omega({ni}), $\delta log(\Omega({n_i}))=\frac{\partial log\Omega}{\partial n_i}\delta n_i+\frac{\partial^2 log\Omega}{2\partial n_i^2}\delta n_i^2$. We want to see how a change in configuration at max entropy change the omega. At max entropy (denoted by the set of $\{\hat n_i\}$), the first derivative is 0, the second derivative term is  $\delta log\Omega({n_i})_{\hat n_i}=\frac{\partial^2 log\Omega}{2\partial n_i^2}\delta n_i^2=\frac{\partial^2 NlogN-\sum \hat n_i log{\hat n_i}}{2\partial n_i^2}\delta n_i^2=-\frac{\partial^2 \hat n_i log{\hat n_i}}{2\partial n_i^2}\delta n_i^2=-\frac{1}{2\hat n_i}\delta n_i^2$. This corresponds to a distribution (Omega over entropy) of $e^{-\frac{\delta n_i^2}{2\hat n_i}}$ which is gaussian with variance n hat. The coefficient of variation or relative fluctuation,  defined by sigma compared to mean, is $\frac{\sqrt{\hat n_i}}{\hat n_i}$ which approaches 0 as N (therefore the ns) goes to infinity.
- > this 
- Then we have the *total prob constraint and the total energy constraint*. We solve with **lagrange multiplier**. Recall that LM enforces same direction of objective function and constraint and you should think of this only in multiple dimensions ![](/images/Lagrange-Multipliers.png)
- we **minimize negentropy**: $\sum P_i logP_i + \alpha (\sum P_i - 1) + \beta (\sum P_iE_I - E)$ derivative of this has to be 0 wrt any Pi so $1+logP_i+\alpha+\beta E_i=0, \boldsymbol{P_i=e^{1+\alpha}e^{-\beta E_i}=\frac{1}{Z}e^{-\beta E_i}}$. This gives you the set of ni at maximum entropy. Beta will be the inverse temperature since it's the multipier related to total energy.
- The Pi is the **Boltzmann distribution**. The Boltzmann distribution describes the most probable distribution of particles under thermal equilibrium
- $\sum P_i=1=\sum \frac{1}{Z}e^{-\beta E_i},\boldsymbol{Z=\sum e^{-\beta E_i}}$. Z is the **partition function**. It contains all macroscopic information about the system.

### Coin flip
- make N coin flips and get Nh number of heads. The number of ways to make Nh heads and Nt tails is $\frac{N!}{N_t!N_h!}$. log it and with Stirling appox get $NlogN-(N_hlogN_h+N_tlogN_t)$. We know by law of large numbers that Nt gets closer to Nh. This means that by some probability law, the log of number of ways to distrbute heads and tails increase up to Nlog2 (so number of ways is 2^N), where log2 is a unit of entropy. 

### Beta is inverse temperature
- $\frac{dZ}{d\beta}=-\sum E_ie^{-\beta E_i}$ 
- $E = \sum P_iE_i=\frac{1}{Z}\sum e^{-\beta E_i}E_i=-\frac{1}{Z}\frac{dZ}{d\beta}=-\frac{d{logZ}}{d\beta}$ 
- $S = -\sum P_i logP_i=-\sum P_i[-logZ-\beta E_i]=logZ+\beta E$
- Recall that dS=1/TdE. $dS =\beta dE+d\beta E+\frac{d{logZ}}{d\beta}d\beta=\beta dE+d\beta [-\frac{d{logZ}}{d\beta}+\frac{d{logZ}}{d\beta}]=\beta dE$. So we see **1/T is beta**

### List of variables so far
- $T=1/\beta$
- $\boldsymbol{P_i = \frac{1}{Z} e^{-\beta E_i}}$
- $\boldsymbol{Z = \sum e^{-\beta E_i}}$
- $\boldsymbol{E = -\frac{d{logZ}}{d\beta}}$
- $\boldsymbol{S =logZ+\beta E}$

# Z, E, S of Ideal gas
> Note that there are 2 kinds of Z used. Or formally 2 kinds of ensembles. Before this section all the Z E S etc are **microcanonical**, meaning they deal with single particle. E is average energy of one particle and S is uncertainty involved in one particle's state. From this section on, a state might refer to the state of the whole ensemble, or the box of particles. This is **canonical ensemble**. So E of a state refers to combined energy where each particle is at a certain microstate in the previously defined sense. The transition can be thought of as focusing on a part of a closed system (sampling from the closed system) so this part can have variable total energy. 
- N gas particles spaced far enough (so energy is just kinetic) in box with volume V 
- we want the partition function: $\boldsymbol{Z = \sum e^{-\beta E_i}}$. 
- i is a state number and a state here means an element of the set (R3 X R3)^N (3 dimensions of positions and momenta). This is an uncountable set so we need to integrate over (R3 X R3)^N: $Z=\int e^{-\beta E_i} d^{3N}xd^{3N}p$
- A specific state (x1,...x3N,p1,...p3N) has energy dependent on all molecules' kinetic energy $E_i=\frac{1}{2m}\sum_{n=1}^{3N} p_n^2$. 
- Now we need a way to facterize the multipications inside the integral. First, $\int e^{-\beta \frac{1}{2m}\sum_{n=1}^{3N} p_n^2} d^{3N}p$ has nothing to do with the x integration so they can be treated separately. Notice that both parts include N identical molecules with only the 3 dimensions having different range. Ignoring the constants $\int e^{-\sum_{n=1}^{3N} p_n^2} d^{3N}p=\int [e^{-p_1^2}e^{-p_2^2}e^{-p_3^2}]^N d^{3N}p$. The x part is just the volume V. We divide by a factor of N!?
- $Z=\frac{V^N}{N!}[\int e^{-\frac{\beta}{2m}p^2} dp]^{3N}$ the inside part is gaussian inegration and evaluates to sqrt(pi) so with a change of variable we have $let\ q^2=\frac{\beta}{2m}p^2,\ so\ q=\sqrt{\frac{\beta}{2m}}p,\ Z=\int e^{-\frac{\beta}{2m}p^2} dp=\sqrt{\frac{2m}{\beta}}\int e^{-q^2} dq=\sqrt{\frac{2m\pi}{\beta}}$
- >$Z=\frac{V^N}{N!}(\frac{2m\pi}{\beta})^{\frac{3N}{2}}=(\frac{eV}{N})^N(\frac{2m\pi}{\beta})^{\frac{3N}{2}}=\boldsymbol{(\frac{e}{\rho})^N(\frac{2m\pi}{\beta})^{\frac{3N}{2}}}$ where rho is density of gas. So Z is proportional to V and T.
- $logZ=Nlog(\frac{e}{\rho})+\frac{3}{2}Nlog(\frac{2m\pi}{\beta})=N[1-log(\rho)+\frac{3}{2}log(\frac{2m\pi}{\beta})]=\boldsymbol{-\frac{3}{2}Nlog(\beta)+const}$
- $E=\boldsymbol{\frac{3}{2}NT}$
- $\boldsymbol{S =logZ+\beta E=N[-\frac{1}{2}-log(\rho)+\frac{3}{2}log(\frac{2m\pi}{\beta})]}$, proportional to N and T, and V
> Important: for idea gas, given any 2 of Z,P,V,E,S,T you know the rest (given N fixed)

# Pressure
- Hemoltz free energy: E-ST=-TlogZ, this is from S=beta E+logZ
- > Math interlude: we want to find E and S as functions of T and V. But before that, we solve some general multivariate culculus problems involving E,S as functions of T,V, the meanings of the variables don't matter:
    - differential: $\delta E=\frac{\partial E}{\partial T}\delta T+\frac{\partial E}{\partial V}\delta V$
    - fixed dependent variable: $\frac{\partial E}{\partial V}|_{S}\\=\frac{\partial E}{\partial T}|_{V}\frac{\partial T}{\partial V}+\frac{\partial E}{\partial V}|_{T}\frac{\partial V}{\partial V}\\=\frac{\partial E}{\partial S}\frac{\partial S}{\partial T}|_{V}\frac{\partial T}{\partial V}+\frac{\partial E}{\partial V}|_{T}$.  the fixed S means dS=0 or $\delta S=\frac{\partial S}{\partial T}|_V\delta T+\frac{\partial S}{\partial V}|_T\delta V=0,\\ \frac{\partial T}{\partial V}=-\frac{\partial S}{\partial V}|_T/\frac{\partial S}{\partial T}|_V\\$ so $\frac{\partial E}{\partial S}\frac{\partial S}{\partial T}|_{V}\frac{\partial T}{\partial V}+\frac{\partial E}{\partial V}|_{T}\\=-\frac{\partial S}{\partial V}|_T\frac{\partial E}{\partial S}|_{V}+\frac{\partial E}{\partial V}|_{T}$
- Now imagine a box of particles with a piston on top. If the piston somehow moves up, its energy went up and did so as a result of decrease in energy of the particles: dE=-PdV. This defines pressure: $\boldsymbol{P=-\frac{dE}{dV}|_S}$. Here P and V are **conjugate thermodynamic variable** as defined by derivative of E wrt one variable under constant entropy equals another.
> the system is **adiabatic**, meaning the piston moved slowly and no heat went in to the system, or equivalently entropy stays the same
- usually we want a function of T instead of S: $P=-\frac{\partial E}{\partial V}|_{T}+\frac{\partial S}{\partial V}|_TT=-\frac{\partial E-TS}{\partial V}|_T=-\frac{\partial TlogZ}{\partial V}|_T=T\frac{\partial logZ}{\partial V}|_T$ This defines ppressure as derivative of Hemoltz free energy wrt V at constant temperature
- In ideal gas, $logZ=Nlog(\frac{eV}{N})+\frac{3}{2}Nlog(\frac{2m\pi}{\beta})$ last time we were interested in S and E and E depends on derivative of logZ wrt beta. This time we want derivatve wrt V, so: $logZ=Nlog(V)+const, T\frac{\partial logZ}{\partial V}|_T=TN/V,\ or\boldsymbol{PV=NT},or\boldsymbol{P=\rho T}$

# Fluctuations
- we have a box of gas IN EQUILIBRIUM WITH THE ENVIRONMENT. All the macrostate varables fluctuates constantly. So far we had been discussing the AVERAGE of those variables. Now we want the VARIANCE.
- We treat E as a random variable. $Var(E)=<\Delta E^2>=<E^2>-<E>^2$. Recall that $<E> = \sum P_iE_i=\frac{1}{Z}\sum e^{-\beta E_i}E_i=-\frac{1}{Z}\frac{dZ}{d\beta}=-\frac{d{logZ}}{d\beta}$. Average of (E sqaured) is just average of function of E and probability theory gives: ${<E^2> = \sum P_iE_i^2=\frac{1}{Z}\sum e^{-\beta E_i}E_i^2=\frac{1}{Z}\frac{d^2Z}{d\beta^2}}$. Note that this is the variance of the distribution of E at max entropy. You can think of the variance as measuring the energy of a ramdomly sampled particle from the box. 
- Therefore 
$\begin{align}
\text{Var}(E) &= \langle E^2 \rangle - \langle E \rangle^2 \tag{1} \\ 
&= \frac{1}{Z} \frac{d^2 Z}{d\beta^2} - \frac{1}{Z^2} \left(\frac{dZ}{d\beta}\right)^2 \tag{2} \\
&= \frac{\partial}{\partial \beta} \frac{1}{Z} \frac{\partial Z}{\partial \beta} \tag{3} \\
&= -\frac{\partial E}{\partial \beta} \tag{4} \\
&= -\frac{\partial E}{\partial T} \frac{\partial T}{\partial \beta} \tag{5} \\
&= \frac{\partial E}{\partial T} T^2 \tag{6} \\
&= C T^2 \tag{7}
\end{align}$ C is heat capacity and measures rate of change of energy per temperature change. (2) to (3) through product rule; (3) to (4) as E=-dlogZ/d beta; (4) to (6) to convert beta to inverse temeprature
- since E=3/2NT, C=3/2N

# Non ideal gas (potential energy)
> The trick of statistcal mechanics is to find a way to write things in terms of a series and get rid of higher order terms since your variables are almoost always asymptotic.
- recall $Z=\int e^{-\beta E_i} d^{3N}xd^{3N}p$. Ei has now changed and depends on both p and x so previous factorization of V is invalid. Luckily, the new E is sum of previous kinetic energy and new potential energy so we can still factor out the 2 terms in the integral
- We define the new E to be $E_i=\sum_{j=1}^n\frac{2}{m} p_j^2 + \sum_{n>m}u(|x_n-x_m|)$ where n>m is a shortcut for a double sum. The potential term is assumed to be smaller.
- $Z=\int e^{-\beta (K+U)} d^{3N}xd^{3N}p$ factorizes to $Z=\int e^{-\beta T} d^{3N}p\int e^{-\beta U}d^{3N}x$. The first part is just the old logZ for ideal gas without the V^N term because the dx terms have been factorized with potential. We give it an V^N so the front part becomes original Z0. As a result we devide the second part by V^N.
- > Math interlude: $\int_y\int_x (x+y)dxdy\\ \neq \int_y (y+\int_x xdx)dy=\int_x xdx+\int_y y dy\\=\int_y \int_x x \,dx \,dy + \int_y \int_x y \,dx$
- The new potential part considers all situations of particles in different places. We approximate it by considering just u btw 2 particles. $\int e^{-\beta \sum_{a>b} u(x_a,x_b)}d^3x_ad^3x_bd^{3(N-2)}x$. We don't factorize this time and instead use the fact that u is very small, so e^-x can be approximated with 1-x. The above becomes $\int 1-(\beta \sum_{a>b} u(x_a,x_b))d^3x_ad^3x_bd^{3(N-2)}x=V^N-\beta \int \sum_{a>b} u(x_a,x_b)d^3x_ad^3x_bd^{3(N-2)}x=V^N-\frac{N^2}{2}\beta V^{N-2} \int u(x1,x2)dx_1dx_2$. The last part is VU0. This divided by V^N is $1-\frac{N^2}{2V}\beta U_0$
- > Math interlude: log(1-x)=-x when x is small
- $logZ=logZ_0+log[1-\frac{N^2}{V}\beta U_0]=logZ_0-\frac{N^2}{2V}\beta U_0$
- $E=-\frac{\partial logZ}{\beta}=\frac{3}{2}NT+\frac{N^2}{2V}U_0=N(\frac{3}{2}T+\frac{N\rho}{2}U_0)$
- $P=-\frac{\partial TlogZ}{\partial V}|_T=T\frac{\partial logZ}{\partial V}|_T=\rho T+\frac{N^2}{2V^2} U_0$

# Heat and work
> Heat and work is not functions of the system (of any of the macrostate variables) just like your gas tank is not a function of the landscape
> Math interlude: exact differential. A differential in 2d is $dF=F_xdx+F_ydy$. So dF is a linear form/covector of 2d space. But not all dF(x,y) are results of differential of a function F. For example $dF=-ydx+xdy$, a circular rotational vector field (with x-y component of the field Fx and Fy). This cannot be mapped back to a function. 
- We have seen that $dE=-PdV|_S$ and also $dE=TdS|_V$. Both of them have conditions. First needs to be volume constant, second needs to be adiabatic.  
- First law of thermodynamcis: $dE=-PdV|_S+TdS|_V \text{ or } =dW+dQ$ There seems to be a contradiction since both parts require the other to be 0. But we imagine an ideal process where we first change volume a tiny bit but keep entropy fixed then change entropy a tiny bit keeping volume fixed. (entropy change can be done by heating the box)
> Recall that given any 2 of Z,P,V,E,S,T you know the rest (given N fixed)
- We want to know if Q, or heat, is an exact differential of E and W or equilavently E and V. 
- $dE=-PdV|_S+dQ,dQ=dE+PdV|_S$. We use curl test: $\frac{dQ}{dE}=1,\frac{dQ}{dEdV}=0,\frac{dQ}{dV}=P$. If Q were a function, derivative of P wrt V must be 0. However, PV=NT so it's not 0. Therefore Q is not a function of E and V.

## Speed of sound in ideal gas
- E gives total energy which in ideal gas is total kinetic energy. $E=0.5Nmv^2=1.5NkT,v^2=3Tk/m$. 
- $P=\rho kT,\frac{dP}{d\rho}=kT$ so $\frac{dP}{md\rho}$ also gives speed squared. The factor of 3 is not explained. Note that this only works in ideal gas because we used PV=NT.

## Energy of oscillator in heat bath

## ultraviolet catastrophe and QM oscillator
- at high enough temperature the quantum energy equals classical

# 2nd Law
## 2nd law and Poincaré recurrence theorem
- for statistical derivation of 2nd law see boltznmann distribution section.
- tension between reversibility of foundamental laws of physics and irreversibility of the observational property of complex systems 
- The empirical observation of seconnd law is due to **coarse graining and Chaos** (coarse graining in quntum mechanics is inevitable) ![](/images/coarse-graining-chaos.png) For example, if you know that a system might be in two phase space point with equal prob, then entropy of the system for you is log0.5. If after a long time, you completely lost track of where your molecules are, then you might say that every phase space point is equally likely. But that is wrong because you have the information that a long time has passed and the system might be in equilibrium, which sets a maximum entropy of the system together with the energy constraint, and that entropy is always lower than entropy obtained by assuming uniform phase space distribution.
- **Poincaré recurrence theorem**: prob of all molecules in a box go to one side of the box: assuming complete symmetry, (1/2)^3N
- so a system will always go to a low entropy configuration eventually. However, this doesn't contradict 2nd law because *2nd law is statistical and allows for a probability for entropy to decrease*. See https://en.wikipedia.org/wiki/Fluctuation_theorem

## cosmology and philosophy
- boltzman brain: Zermelo advanced a theory that the second law of thermodynamics was absolute rather than statistical. Zermelo bolstered his theory by pointing out that the *Poincaré recurrence theorem* shows statistical entropy in a closed system must eventually be a periodic function; therefore, the Second Law, which is always observed to increase entropy, is unlikely to be statistical. To counter Zermelo's argument, Boltzmann said that *the universe started for some unknown reason in a low-entropy state*. 
- Is history real: It's possible that the current state of world has just arise from a random fluctuation. That is, there is no history of the universe nor mankind but it just happens that this particular state that rose from randomness includes everyone having the memory of themselves and the books and all information storing media in a state of having what we call history. The point is that it's extremely unlikely to have a coherent history if we are indeed just formed. 
- Life seems to decrease entropy but it increase entropy elsewhere. Also there's a flow of energy from the sun that can create structures just like water flow can create vortices.

# Spin Models
## 1-D magnet array
- N magnets up or down, sigma(i) gives 1 or -1 for up and down states. Up and down are symmetric.
- We have n ups and m downs or N-n downs. Number of ways for n ups is N!/(n!m!). 
- Suppose magnets don't intereact and energy is from some external magnetic field uH. Energy is +uH for up and -uH for down. So total energy is (n-m)uH
- $Z=\sum_n \frac{N!}{n!(N-n)!}e^{-\beta(n-m)\mu H}$ define $x=e^{-\beta\mu H}, y=e^{+\beta\mu H}$, $Z=\sum_n \frac{N!}{n!(N-n)!}x^ny^{N-n}$. This is the *binomial expansiion* of $(x+y)^N$. So $Z=(\frac{e^{-\beta\mu H}+e^{+\beta\mu H}}{2})^N2^N=2^N\cosh(\beta\mu H)^N$
- magnetization $M=<n-m>/N$ so $<E>=MNuH$. <> means average
- E=$-\frac{\partial logZ}{\partial \beta}=-\frac{\partial const+N log[\cosh(\beta\mu H)]}{\partial \beta}=-N\frac{\sinh(\beta\mu H)}{\cosh(\beta\mu H)}\mu H$ 
- M=$-\frac{\sinh(\beta\mu H)}{\cosh(\beta\mu H)}=-\tanh \beta\mu H$. ![](/images/magnetization.png) This is a function of T. This has no phase transition since the system is too simple. Note that mu H could be either sign denoting direction of external field

## 1-D Ising Model
- energy between each pair magnet i and i+1 is $-j\sigma(i)\sigma(i+1)$. Since nature favors low energy, the minus sign means the magnets like to align. 
- $Z=\sum_{\sigma} e^{\beta j \sum_i \sigma(i)\sigma(i+1)}$. This is a sum over all states of the 1-d array. We apply a **trick**: let ${\sigma(i)\sigma(i+1)=u(i)}$. u can be either +1 or -1, Z becomes $Z=\sum_u e^{\beta j \sum_i u(i)}=(e^{-\beta j}+e^{\beta j})^{N-1}=[2\cosh(\beta j)]^{N-1}$. This is exactly the same as the magnet array without interaction above, but the magnetization is replaced by u. So **average magnetization or $<\mu>=<\sigma(i)\sigma(i+1)>=\tanh(\beta j)$**
- Thus 1-d Ising model is exactly the same as just 1d array of magnets with external field and no interaction. This idea of repllacing interaction by constant external field will become mean field approx in next section
- The average magnetization can be taken as conditional probability of successfully transmitting a signal from ith magnet to the next one. We can also ask what's the probability of successfully transmitting from ith to i+nth magnet. The trick is to observe $<\sigma(i) \sigma(i+n)>=<\sigma(i)\sigma(i+1)\sigma(i+1)\sigma(i+2)\sigma(i+2)... \sigma(i+n)>=<u(i)u(i+1)...u(i+n-1)>$ Since each u is independent the average of product is product of average, or $<\sigma(i) \sigma(i+n)>=<u>^{n-1}=\tanh(\beta j)^{n-1}$. 

## High dimensional Ising Model
- a magnet in a d-dimensional lattice has 2d neighbors
- again assume magnets like to align the energy of each magnet is $-j\sigma\sum_{neighbors}\sigma$. 
- That summation will be hard to solve when put into Z. We use **mean field approximation** which says at equilibrium, the interactions between particle, or here the influence from neighbors, can be approximated as an external field, where the strength of the field is the mean value of influence from each particle. Here we use $\bar{\sigma}$ to denote the average influence from one neighbor. The energy of each magnet becomes $-j\sigma 2d \bar{\sigma}$.  Note that in the 1d case the sum is 1. 
- $<\sigma>=\tanh(j 2d \beta \bar{\sigma})$, since every magnet is the same, average of sigma is just sigma bar so ${\bar{\sigma}=\tanh(2 j d \beta \bar{\sigma})}$. Replace $2 j d \beta \bar{\sigma}$ by y we have ${\frac{Ty}{2 j d}=\tanh(y)}$. Note that this is just an equation and we want to solve for y. Note that this means average of a spin is the average of its neighbors. Also note tanh derivative at 0 is 1
- ![](/images/ising-phase-transition.png). When temperature is high we have only one solution at y=0=tanh(y), meaning the alignment is random. But at a certain temperature there will be a solution at tanh(y)>0 meaning there will be some alignment. When temperature is close to 0 tanh(y) will be close to eiither +1 or -1 meaning almost perfect alignment. 
- The other solution at 0 is unstable. We can analyze this with a dynamics approach. Remember that dynamics is given by transition probability given by boltzmann distribution. First we rederive the average of sigma from average of u. $<u>=P(u=-1)*-1+P(u=+1)*+1$. $P(u_i = -1) = \frac{e^{-\beta J }}{e^{\beta J } + e^{-\beta J }}$. So $<u>=\frac{-e^{-\beta J }+e^{\beta J }}{e^{\beta J } + e^{-\beta J }}=\tanh\beta J$
- Why phase transition appears at d=2: in one dimension, each energy state can have much more configurations (xoxxxxxx is the same as xoooooxxx or however many o you put). So even when temperature is very high there are very many configurations available. (further analysis needed)
- If there's external field B we simply add the sigma B energy and get $<\sigma>=\tanh((j 2d \beta + B)\bar{\sigma})$ which shifts the tanh to the left. This also proves that the solution at 0 is unstable because a tiny nudge to the system magnitizes the system

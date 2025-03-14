(https://www.youtube.com/playlist?list=PL47F408D36D4CF129) 
# 1
- conservation laws and acceptable laws of motion. predictability and reversibility in terms of resolving power. 
- vectors and coordinate system, polar coordinate

# 2 Dynamics
- Aristotle's law of motion F=mv tested on spring produces x=e^-t so it's irreversible because when there will be a t where x is indistinguisable (given finite resolving power) from 0, thus if x=0 you don't know where it comes from. 
- Newton's law, inertial frame, define F, m and a using springs. state with x and p. phase space and dynamics of motion as 2 first order DEs. Harmonic oscillator. 
- **time reversion**. imagine something dropping to ground from infinite height and choose t=0 arbitarily. x(t) will show this thing dropping, as t increases; x(-t) will show this thing rising, as t increases. So swapping t with -t is the natural way to reverse progressioin of physical events. Now for Newton, $v(-t)=\frac{dx(-t)}{d(-t)}=-\frac{dx(-t)}{dt}$, meaning that v as derivative of x(-t) at -t is inverse of v as derivative of x(t) at -t. What's interesting is that acceleration and thus force is unchanged $a(-t)=\frac{d^2x(-t)}{d(-t)^2}=\frac{d^2x(-t)}{dt^2}$, meaning a as second derivative of x(-t) at -t is the same as a as derivative of x(t) at -t. For example, imagine an object accelerating to the ground and play it in reverse. The object flies up quickly and gradually comes to a stop, showing downward gravity in both cases. Actually, the reverse of dropping is like firework to sky. In conclusion, Newtonian laws of motion are time-reversal symmetric, meaning you can't tell if which direction time is going. In contrast, if F=mv, then reversing time also reverses all forces.

# 4 System of particles, momentum
- state of a system: everything you need to know to precisely predict the future, given laws of motion. (a trick to select state is to ask what do we need at the very beginning)
- phase space, configuration space+momentum space
- the 3rd law, conservation of momentum

# 5 Energy
- The basic principle—call it the potential energy principle-asserts that all forces derive from a potential energy function denoted V(x)
- would be nice to introduce how energy was invented from greeks' living force to measure of motion to mv^2 and then to height equivalence of work and formulation of V as related to height at which an object will have gained K=V. 
- conservation by showing dE/dt=0
- It is quite possible to imagine force laws that do not come from differentiating a potential energy function, but nature does not make use of such nonconservative forces.
- V defined to satisfy conservation of energy
- how types of energy relate to K and V

# 6 Action
- convert initial state of x and p to initial and final x
- benefit: easy transformation btw reference frames
- generalized conjugate momentum and example in polar coordinate,  
- more on polar coordinate: ${x=rcos\theta,\ y=rsin\theta}$ ${\dot{x} = \frac{dx}{dt} = \dot{r} \cos\theta - r \dot{\theta} \sin\theta}\\ {\dot{y} = \frac{dy}{dt} = \dot{r} \sin\theta + r \dot{\theta} \cos\theta}$ ${v^2 = \dot{r}^2 (\cos^2\theta + \sin^2\theta) + r^2 \dot{\theta}^2 (\sin^2\theta + \cos^2\theta) + 2 \dot{r} r \dot{\theta} (\cos\theta \sin\theta - \sin\theta \cos\theta)}\\v^2 = \dot{r}^2 + r^2 \dot{\theta}^2.$
- cyclic coordinate (coordinates not in V term and therefore subject to 0 total force on that coordinate axis/conserved momentum)

# 7 **symmetry and conservation laws**
- A symmetry is an active coordinate transformation that does not change the value of the Lagrangian.
- $\delta L=\sum_i\frac{\partial L}{\partial q_i}\delta q_i+\frac{\partial L}{\partial \dot{q_i}}\delta \dot{q_i}\\= \sum_i \dot{p_i}\delta q_i+p_i\delta \dot{q_i}\\=\sum_i\frac{d}{dt}p_i\delta q_i=0\\$ so **$\sum_ip_i\delta q_i$ is a conserved quantity**. For example, if delta is 1 as in pure translation, then the conserved quantity is total momentum
- double pendulum and recipe for lagrangian problem: 1) choose coordinates 2) find K and V

# 8 Hamiltonian
- $\frac{dL}{dt}=\frac{\partial L}{\partial q}\frac{dq}{dt}+\frac{\partial L}{\partial \dot{q}}\frac{d\dot{q}}{dt}+\frac{\partial L}{\partial t}\\= \dot{p}\dot{q}+p\ddot{q}+\frac{\partial L}{\partial t}\\= \frac{d}{dt}p\dot{q}+\frac{\partial L}{\partial t}$
- define $H=p\dot{q}-L$. We have  $\frac{dH}{dt}=-\frac{\partial L}{\partial t}$. H is constant if L is not explicitly dependent on time. H is also the energy since $p\dot{q}=m\dot{p}^2=2K$ so H=2K-K+V=E
- $-\dot{p}=\frac{\partial H}{\partial q},\ \dot{q}=\frac{\partial H}{\partial p}$
- convenience of having first order system and simple phase plane
- note that H is based on L and uses result of EL equation

# 9 Liouville and Poisson bracket
- Liouville: ${\displaystyle \rho \sum _{i=1}^{n}\left({\frac {\partial {\dot {q}}_{i}}{\partial q_{i}}}+{\frac {\partial {\dot {p}}_{i}}{\partial p_{i}}}\right)=\rho \sum _{i=1}^{n}\left({\frac {\partial ^{2}H}{\partial q_{i}\,\partial p_{i}}}-{\frac {\partial ^{2}H}{\partial p_{i}\partial q_{i}}}\right)=0,}$
- Poisson bracket: ${\{f,g\}=\sum _{i=1}^{N}\left({\frac {\partial f}{\partial q_{i}}}{\frac {\partial g}{\partial p_{i}}}-{\frac {\partial f}{\partial p_{i}}}{\frac {\partial g}{\partial q_{i}}}\right)}$
- $\dot{f}=\sum _{i=1}^{N}\left({\frac {\partial f}{\partial q_{i}}}{\dot{q_i}}-{\frac {\partial f}{\partial p_{i}}}{\dot{p_i}}\right)=\{f,H\}$
- $\dot{q_k}=\{q_k,H\}, \dot{p_k}=\{p_k,H\}$

# 10 Poisson bracket, angular momentum and symmetry
- Axioms: 
    - {A,B}=-{B,A}, {A,A}=0
    - 
- Properties
    - $\{q_i,p_j\}=\delta_{ij}$
    - 

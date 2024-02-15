> One ought to stop every once in a while and think, "What do they really mean". -Feynman
# Subjects in Math
> The glory of mathematics is that we do not have to say what we are talking about. -Feynman
## Nature of Infinity---
---
Infinity and finity create each other.
## Optimization
### Linear Approximation and Newton's Method
$f'(x)≈\frac{f(x)-f(a)}{x-a}\\
f(x)≈f(a)+f'(x)⋅(x-a), linear function\\
x=\frac{f(x)-f(a)}{f'(x)}+a$


## Trigonometry 
When that smart guy started to nudge the edges of a triangle while fixing the vertex, the fate of humanity started rotating with the edge. Trigonometry has since been coupled with angle and rotation, and what's special about rotation? You always come back. It's a revelation given by the universe about periodicity.

### Trigonometry and Circle
Trigonometric functions, sine and cosine for example, are fundamentally related to circle and therefore periodicity. On the one hand, these functions are defined with respect to angle of a triangle. When you increase the angle, you eventually get back to the start angle, thus we have periodicity in trigonometric functions as a result of their definitions. On the other hand, chords and other lines within a circle has been studied long before trigonometry. Angles of triangles inside or outside the circle with varying side length or angles were well recorded and formed a natural basis for trigonometric functions defined within a unit circle.

### Derivative of Sine
![](/images/d-sin.png)
Note first that we are trying to calculate derivative of sinθ wrt θ. Sine maps angle to R. We could define the unit of the domain of sine as degree or radian. We'll show that only by using radian will we have the property dsin=cos.

In the image, we see that the small triangle has hypotenuse of length h. The smaller angle is θ, which is a consequence of having two such triangles inside a unit circle. Δy=cosθ⋅h.

If we use radian, h=Δθ, Δy/Δθ=cosθ as we wish.

If however we use degree, we have $Δy/Δθ=\frac{cosθ⋅Δθ⋅2π}{360Δθ}=\frac{cosθ⋅2π}{360}$

### Arcsin, Arccos, and Their Derivatives
$sin(sin^{-1}(y))=y \\
cos(sin^{-1}(y))\frac{dsin^{-1}(y)}{dy}=1 $

arcsin(y) gives an angle where its opposite side is y. cos of that angle is the adjacent side which by Pythagorean theorem is root of 1-y². Therefore, $\frac{dsin^{-1}(y)}{dy}=\frac{1}{\sqrt{1-y^2}}$

Similarly, $cos(cos^{-1}(y))=y \\
-sin(cos^{-1}(y))\frac{dcos^{-1}(y)}{dy}=1 $

So derivative of arccos differs from arcsin just by a minus sign. What does this mean? arcsin+arccos has derivative 0, so arcsin+arccos is a constant. And what is that constant? π/2.
### Sine and e
Natural periodicity has two forms. Things that repeat with a definite period and things that change (grow or decay) by a definite fraction for a definite period. We count year and day with the regular rotation of celestial bodies and we defined their period to be "time". One day means one rotation of earth. We can also count another form of periodicity, for example radioactive decay. We define a time period to be the time required for a certain element to decay to a certain fraction. If we have 1 gram now, we expect after time T it will be 0.8, after another T 0.64 and so on. So naturally, there seems to be some connection between exponential and periodic functions. 

## e
### Why e
Exponential growth exists in nature. It's a testimony of how nature divides time to seemingly infinitely small intervals and given certain constraints, entities seem to behave independently. 

In compound interest, at any moment within that year, we have M money. It's rate of growth is $lim_{n->∞}\frac{M\times(1+1/n)-M}{1/n}=M$. Any growth like this, that grow a fixed percentage of self CONTINUOUSLY, can be described as $\frac{dy}{dx}=cy$, which can be solved by an infinite series that's equivalent to or sometimes defined to be $e^{cx}$.

#### More on compound interest
- $lim_{n->∞}(1+\frac{1}{n})^n=e$
- $lim_{n->∞}(1+\frac{2}{n})^n=e^2$
- $lim_{n->∞}(1+\frac{1}{n})^{2n}=lim_{n->∞}(1+\frac{2}{2n})^{2n}=e^2$

This implies that having a continuous 200% interest rate for one year is the same as having a 100% rate for 2 years. In differential form, the former is $y'=2y,y=e^{2x},x=1,total=e^2$ and the later $y'=y,y=e^x,x=2,total=e^2$. Or we see that the 100% rate for two years is first 100% for one year which is e and we put it to bank again and start with e for one year which is $lim_{n->∞}e⋅(1+\frac{1}{n})^n$ or e⋅e=e². This turns out to be the property that defines a exponential function where f(a+b)=f(a)⋅f(b)

### Definition of Exponential
- Integer exponent to real: recursive definition. $a^b=a⋅a^{b-1},a^0=1$
- Root: $a^{1/b}=sup\{y∈R,y≥0,y^b<a\}$
- Rational exponent: $a^{b/c}=(a^{1/c})^b$
- Real exponent: $x^⍺=\lim_{n->∞}{x^{(q_n)}}$ where (qₙ) is a sequence of rationals converging on ⍺

### Definition of Natural Exponential Function
- eˣ= 1+x+x²/2+x³/6+...+xⁿ/n!
- eˣ= $\lim_{n->∞}{(1+x/n)^n}$

### Definition of Exponential Function based on e
$bˣ:=e^{xln(b)}, dbˣ/dx=ln(b)bˣ$

### Logarithm
Logarithm undoes action of exponential. If we know something has exponential growth, and if we have observations of its quantity, then we can get the time since this growth started by using logarithm.

$ln(eˣ)=e^{ln(x)}=x$

### Derivative of Log
We know from the start that $dx^n/dx=nx^{n-1}$. This produces derivatives in the form of x^n, n={...,2,1,0,-2,-3,...}. We never get x⁻¹. We get this derivative from ln(x).

### Log Graph
- Suppose we have a relationship like $y=A10^{cx}$. We can draw $logy=logA+cx$ which is a straight line.
- Numerical derivative: 

## Infinity in Math
### Sin and e
https://betterexplained.com/articles/imaginary-multiplication-exponents/

Euler's formula: eⁱˣ=isin(x)+cos(x). Corollary: $e^{iπ}=1$

### Sin, e, π, Calculus, Binomial Theorem, and Combinatorics
Taylor expansion of $(x+1)^p=1+px+\frac{p(p-1)}{2!}x^+\frac{p(p-1)(p-2)}{3!}x^3+...+\binom{p}{n}x^n$, which is exactly the result obtained by applying binomial theorem.

If p>0 and N, the expansion is finite. 

If p<0 or is fraction, the expansion is infinite. With binomial theorem, we can now approximate a^n/m, like root of any number, with ease. Note how similar this is to the solution of area problems by the Greeks: most prominent terms are added first, smaller and smaller parts are added later ad infinitum and the limit is the area; the parts being smaller and smaller ensures approximation quality. 

Newton calculated Pi with binomial theorem and his method of fluxion, which at the time was just for finding area under the curve. Remember that a circle has an analytical expression: (x-a)²+(y-b)²=r². For carefully chosen circles, y can often be written as $x^{0.5}(1+cx)^{0.5}$, the second part is an infinite power series by the binomial theorem.


### Area Under 1/x

### Infinite Series and Functions
The old area problem can be solved with infinite series. By bringing in symbolic algebra, these infinite series can be turned into functions that represent different areas of the same kind. 

Why Taylor series can approximate almost any function? Because any function has an anti-derivative function which can be thought to represent area under the that function. Any area can theoretically be calculated by method of exhaustion, which in essence adds most prominent and easy to calculate part followed by smaller and smaller parts ad infinitum until the whole area is exhausted. This in essence is an infinite series. 

> Newton used the method of infinite power series to solve the integral problem and computed π as an example.
### Infinite Series
- Geometric: 1+1/2+1/4+1/8+... Generally: $\frac{1}{1-x}=1+x+x^2+x^3+...\ where\ x<1$
- 1+1/2+1/3+1/4+... Generally: $-ln(1-x)=x+x^2/2+x^3/3+...\ where\ x<1$. Note this is the anti-derivative of geometric series.

## Arithmetics
### Multiplication and Square
- (a+b)(c+d)=ac+ad+bc+bd: Use a rectangle with base and height a+b and c+d to show that the area is composed of 4 smaller rectangles corresponding to the 4 terms on the RHS of the equation
- (x+y)(w+z)=xw+xz+yw+yz: here we replace numbers with variables and prepare for next equation. Here xywz can be viewed as unit length so the rectangle in first equation becomes a square.
- (x+x'+x''+...)(y+y'+y''+...): Use a square table to represent the result by summing all entries in the square matrix. This sum can be computed by first getting a 1-square, then 2-square, etc. 

### Binomial Theorem
- Relationship between Pascal triangle and combinatorics

## Complex Number
### Cubic
### Complex Number and Gravity

## Euler's Formula
### Series Expansion
### Feynman
- Log10
- loge
- 10^s,s->0
- 10^si,s->0
- e^si,s->0


# Math and Nature
> a habit of keeping the eyes open to every thing that is going on in the ordinary course of the business of life has oftener led, as it were by accident,...to useful doubts, and sensible schemes for investigation and improvement, than all the more intense meditations of philosophers, in the hours expressly set apart for study -Rumford

> It is a strange coincidence that nearly all the fundamental work concerned with the nature of heat was done by non-professional physicists who regarded physics merely as their great hobby. -Einstein

The laws of physics, the names we assign to certain aspects of nature, force, mass, speed, light, atom, etc, are all but imaginations, guesses, or beliefs. We believe that there are some identifiable things underlying the mechanism of this world and we can understand the relationship between them. It's not about what we believe, is everything number? is the universe a function? is light wave or particle? but the fact that we believe in something  in such an uncertain and disguising world, some structure out of chaos, some simplicity and beauty out of complexity, that set the foundation of natural science, and shaped the course of humanity.  

## Coordinate System
### Decomposition of Force
Note that a force of magnitude root of 2 achieved the effect of 1+1. 

It's amazing that a number with a direction works exactly under the laws of trigonometry and normal arithmetics.

On a history note, Newton and early mechanics used decompositioin of quantiteis that have "directions". On each direction everything works as if we live in a world without notion of space or rotation (a 1 demensioinal space) and normal numbers along would suffice all computations of the world. 

### Dot/Scalar Product

### F=ma, F=-ma, F⟂ma
Note that the minus sine is often oversimplifying. The sign means direction is involved and should be understood in the context of rotation. If a=-b it means a=iib which means b rotating 90 degrees twice. 

### Orthogonal Basis and Complex Number
Why can we represent complex number as two perpendicular lines just like normal x-y coordinate system? Cartesian system has a central property: the two coordinates are orthogonal. You can't get one from the other. Does real and imaginary parts of complex number satisfy this? Yes. You can't get i just by adding real numbers and vice versa. Thus, as long as you have orthogonal things, even things like pants and shirts, you can plot them just like n-dimensional Euclidean space. This idea connects geometry and number. 

It also raises the ontological question about how numbers represent the universe. Following the projection theory of Plato, if we say numbers are behind the shadows, i.e. all we see are merely shadows casted by numbers, then this real play of numbers behind the shadows are themselves shadows of a greater category of numbers. Real numbers are shadows of complex numbers. Complex numbers operate a delicate puppet play that casts as real numbers which in turn casts as every physical phenomena we see. So is there something even deeper behind complex numbers? Perhaps finding that will further our understanding of world a lot (think about how easy it is for us 3d beings to manipulate 2d things, imagine what we can do on this 3d world when we have full control of 4 or 5d). 

## Growth Functions
> Relationship between numbers shows how one thing affects the other. Relationship of numbers is modeled with functions.

Given growth rate, how large quantity I get after a certain period of time.

### Zero
No growth rate, quantity stays the same

### Linear
Constant growth rate, quantity increases linearly. Example, distance with no force.

### Power/Polynomial (n>1)
Example, distance with constant force.

### Exponential
Growth done by multiplying with a constant number. Can be seen as adding constant number of copies of self. Example, population growth. 

> After differentiating we get growth rate, or what is being added at a given time. Note that for power functions, the quantity being added is still a function of time, but for exponential functions, the quantity added is proportional to itself. The difference can be understood as power function modeling process governed by external factors but exponential functions governed by internal factors.
> Exponential growth of 2ˣ in discrete time has the property that at each timestamp, the growth from now to next timestamp will be exactly itself. This is a remarkable property revealing some fundamental natural process like division of cell. In continuous time, the function that has this property is eˣ where at each timestamp, the growth rate will be eˣ, or that the growth from now to next infinitesimally near timestamp is itself times the infinitesimal interval. It underlies natural processes at a finer scale where objects change continuously. 

### Factorial

## Approximation/Abstraction
> To me, these wiggles hold a larger lesson. I see them as a metaphor, a fable about the nature of modeling real phenomena with calculus. If we try to push the resolution of our measurements too far, if we look at any phenomenon in excruciatingly fine detail in time or space, we will start to see a breakdown of smoothness.

## Differential Equation
### e
For a growth that has constant percentage of self as rate of growth, i.e. dy/dt=my, $y=ce^{mt}$ is the solution.

### Sine and Cosine
For a process that has second derivative, rate of rate of change, as a negative constant percentage of self, i.e. $d²y/dt²=-ω²y$, the solution is $Acos(ωt-Δ)$. Note that to think in the lens of exponential functions, the function that satisfies the condition is $ce^{iωx}$. No real exponent can achieve this (proof). 

> Second derivatives come up everywhere in physics and engineering. So that’s why sine waves are so well suited. For sine waves, two derivatives boil down to mere multiplication by –1. 

> To a physicist, what’s remarkable about sine waves (in the context of the vibration and heat flow problems) is that they form standing waves. Most waves are a combination of many frequencies. In that respect, a standing wave is pure, not a mixture.

Let's analyze how a spring is related to a circle. We study a simple case where k=m=1 so that x''=-x. What this means is that the acceleration is -x. If x is away from origin, its speed will go to origin and pass the origin so the mass will then go to the origin. This process means periodicity: whenever you are away from the equilibrium, you are pushed back to it. What has periodicity? A circle.

[Simple Harmonic Motion(SHM) & Circular Motion](https://www.youtube.com/watch?v=JSBw-JyFgZk) But why a circle? Many things go in loops. Any loop has periodicity. What's special about a circle? When looked from one side, we see a motion identical to SHM. The speed of this motion, its derivative, is governed by the same function as the wave shifted 90 degrees. And its acceleration is that shifted 180 degrees, which is its exact opposite. 
### Periodicity
It's usually taken for granted that things can repeat. We can walk straight, turn back and return to the same point. We can go on a roller coaster and after a trilling ride take off at where we started. It's possible in another universe that when we walk, the space changes, the world is changed by the walk, so that we can not go to where we started. Or in a world where we cannot turn back, there's no notion of rotation, we have to keep going. 

Periodicity is fundamentally related to space time. We happen to live in a universe where we identify two operations, translation and rotation, that 

### Linear Combination of Derivatives
ay+by'+cy''+...=0. Solve with e^cx where c is the root that solves a polynomial

### Spring
- Without friction: -ky=my'' where the left side is Hooke's spring force and right side is Newton's F=ma. Rewrite this as $d²y/dt²=-\frac{k}{m}y$
- With frication
- With external force

[SHM demo](https://www.desmos.com/calculator/tjhwhq38rl)
### Pendulum

### Population
### Heat

### String

### Sound
energy, linear motion of wave front, sine of single particle, sine of one patch, 
https://youtu.be/DUPLRe5PHvE?si=DBzZwOFKJ6bNWpfp
## Music
### Basic Music Theory
The standard frequency is 440hz corresponds to A4. An octave higher means doubling the frequency. There are 12 notes called semitones for each octave. Since an octave means doubling, one note higher should correspond to something analogous in exponential scale. This is fundamentally a result of human ear where we process absolute pitch in a log manner. So if 440hz is scale 1, 880 should be 2, i.e. what we hear=log₂(pitch/220). Now what is scale 1+1/12 which should be one note higher than A4? 13/12=log₂(B4/220), B4=$220*2^{13/12}=440*2^{1/12}≈440*1.05946$. So each time we get up an semitone, we multiply the previous semitone's frequency by 1.05946. 

Some jargons:
- Middle C: Center of Grand Staff. Easy to recognize and used as educational tool.
- Musical scale: 8 notes from the note chosen e.g. Major C scale from C to C. The 8 notes A-G-A is a consequence of ancient tradition and human hearing. Two notes octaves apart are perceived by humans as high similar (same pith class).
- Pythagorean tuning: using only octave and fifth for tuning. Choose 7 Notes.
- Major scale: whole, whole, half, whole, whole, whole, half
- Minor scale: whole, half, whole, whole, half, whole, whole
- Interval: a difference in pitch between two sounds. 1:1 (unison), 2:1 (octave), 5:3 (major sixth), 3:2 (perfect fifth), 4:3 (perfect fourth), 5:4 (major third), 6:5 (minor third). Intervals with small-integer ratios are often called just intervals, or pure intervals.

### History of Tuning

### Overtone/Harmonics

### Music and Psychology
https://www.youtube.com/watch?v=LF6M_aNAIeo
### Harmony

### Chladni Patterns

## Universal Gravitation
> ... one of the most far-reaching generalizations of the human mind. While we are admiring the human mind, we should take some time off to stand in awe of a nature that could follow with such completeness and generality such an elegantly simple principle as the law of gravitation.

### Gravitation and Sine
Imagine a disk where the edge is the orbit of a planet and the sun is at the center. The force between sun and planet is a constant. At different location around the orbit, the decomposition of force along x and y axis is exactly -cos and -sin. It means the acceleration along x axis is -cos and y -sin. It also means the speed would be -sin and cos, and position cos and sin.
## Chaos
> Chaotic systems are not random — they’re deterministic and hence predictable in the short run — but in the long run, they’re so sensitive to tiny disturbances that they look effectively random in many respects. 

> It’s important to understand what’s new about this. People always knew that big complex systems like the weather were hard to predict. The surprise was that something as simple as a spinning top or three gravitating bodies was similarly unpredictable.

# Patterns in Math
### Pascal's Triangle
The young Newton, when his thinking turned to the expansion of the binomial, was able to devise a formula for generating the binomial coefficients directly, without the tedious process of constructing the triangle down to the necessary row. Further, his inherent belief in the persistence of patterns suggested to him that the formula that correctly generated coefficients for binomial powers like (a + b)^2 or (a + b)3 should work just as well for powers like (a + b)^1/2 or ( a + b)^-3.

# Probability
https://physics.stackexchange.com/questions/33344/is-the-universe-linear-if-so-why

When we use probability intuitively, we are really not using any of the 3 axioms and we should forget them first to get a good intuition.

We think of relative probability. When I walk in a straight line, it's never a straight line, and I don't know how likely will I follow a certain curved path. We do know that if I'm sober, I will more likely to walk within a certain range from the center of the road than to walk mostly on the edge of the road, given that I want to go straight. 

Some of us also have thee notion of variability. We say that something is highly uncertain or there's lot to take into account. It means that we roughly know it might turn out this or that way, but we won't be surprised by either or even by something we didn't plan for at all. 

## Interpretations of Randomness
> The true logic of this world is in the calculus of probabilities. -Maxwell
### God Plays Dice
This means there's "true" randomness in the structure of the universe. It implies that the universe itself doesn't know what will happen. 

There are two interpretations of this true randomness. One is that the universe has no idea what will happen, i.e. your dice would just as likely give you 1 million consecutive heads as any other sequence of outcomes. It means that even a distribution doesn't exist before it happens. Another is that there IS a distribution, but how real outcomes are drawn from that distribution is random, i.e. the probability of heads or tails are both one half but you can never calculate exactly when will it be heads or tails. It seems now that the later is the true mechanism behind the universe.

### God Doesn't Play Dice
This is older and maybe easier to understand. Since Newton, people think of the universe as a giant clock (clock because it was considered the most intricate machinery at the time). If you know the current state and all influences applied on it at the current moment, you will know exactly its next state and you can repeat this and predict how this system will be in any future time (See Laplace's demon). Einstein favored this view and was often criticized for. Under this view, usage of probability is merely a convenience for describing behaviors with partial knowledge. 

## Interpretations of Probability as a Science
### Bayesian
Estimate from common sense (prior knowledge of the world and the specific problem) what the distribution is like. It doesn't matter if you believe in true randomness or not. Statistics is a way of making better guesses for humans. If you believe in true randomness, then you are estimating that randomness, if you don't then you are using past observations to inform the future.

### Frequentist

## Symmetry
### Pascal's Triangle

# History of Math and Physics
> in Aristotelian doctrine, everything below the moon was held to be corruptible and imperfect, and everything beyond the moon was perfect, eternal, and unchanging. Newton shattered this paradigm.
## Calculus
### Finding Area
https://apcentral.collegeboard.org/courses/resources/calculus-before-newton-and-leibniz

quadrature, area under curve, volume swept by curve, slope of tangent to a spiral->summation of polynomials

Quadratic and cubic polynomials had existed for well over a thousand years, but expressed as areas and volumes. It was not even clear what a fourth power would mean. Higher-degree polynomials emerged almost simultaneously around the year 1000 in the Middle East, India, and China.

Two 11th-century contemporaries, Abu Bakr al-Karaji in Baghdad and Jia Xian (a Chinese court eunuch) studied polynomials of high degree, found methods for extracting roots, and discovered what we today call Pascal's triangle. Al-Karaji gave the first known proof of the formula for the sum of cubes—also one of the earliest known examples of a complete proof by induction.

[Fermat area under polynomial using r->1](https://files.eric.ed.gov/fulltext/EJ720046.pdf)

### Geometry, Function, and Physics
A curve was viewed as a geometric object and people studied the curve itself, without assigning any meaning to the curve or putting it in an xy-plane.

The merging of algebra and functions with geometry happened when Descartes invented the coordinate plane. This allowed the study of geometry to use algebraic tools and the study of algebra to be visualized. 

With the plane, Descartes and Fermat found ways to calculate tangent lines on almost any curve. Note that at this point, people still don't associate curves with natural processes, they are still mostly geometric objects. 

Newton transformed tangent into derivative and turned the study of curve into study of change, often as a function of time. Newton thus merged natural philosophy with mathematics and geometry. In one way, inspiration from motion tested by Galileo inspired the fundamental theorem of calculus. In the opposite way, calculus allowed Newton to discover universal gravitation and to a greater extent, laws of universe that concisely yet universally underlying every observation. 

Thus we entered the era of motion. Before calculus, math and physics modeled the world statically. Motion of planets are studied with static geometric shapes and numbers. Equations are set up between quantities that represent state of objects at a certain timestamp. After calculus, we began to model changes or flows. Philosophically, we were no longer obsessed with "the moment" that we could never capture (poems about present instantly becomes past). It also raises the question about whether the universe is composed of states or transitions (is time an illusion?). Imagine a force applied on an object. Does the universe calculate the acceleration resulted by the force and place the object in a different space at the next discrete timestamp, or there's no timestamp or even time at all, (state changes, changes do not, so states are perishable, but changes are eternal)


### Derivative
Leibniz viewed derivative in a dy/dx sense where he was doing pure algebra with some fictional numbers (infinitesimal). Newton, however, viewed everything as a function of time. His derivative is the flow of an event.

#### Formal Derivative
Note that the rigorous movement of mathematics come in about 19th and early 20th century. 

In early calculus, the use of infinitesimal quantities was thought unrigorous and was fiercely criticized by several authors. In his work Weierstrass formalized the concept of limit and eliminated infinitesimals.  Following the work of Weierstrass, it eventually became common to base calculus on limits. Bernhard Riemann used these ideas to give a precise definition of the integral. It was also during this period that the ideas of calculus were generalized to the complex plane with the development of complex analysis.

### Continuous System
> Unless I am much mistaken, it would exceed the force of human wit to consider so many causes of motion at the same time. -Newton

## Rigorous Math
### Infinity
- Induction
- Epsilon-Delta definition of limit
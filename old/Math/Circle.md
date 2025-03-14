## Circles and Triangles
### Circular Motion

### sin and cos and their Derivatives in Circular Motion

### Periodicity of Circle and Trigonometric Functions

## Feynman
### e as Taylor Expansion

### 10ˣ

### ln

### 10ⁱˣ

### sin and cos

### eⁱˣ

## e and circle
### e as Growth
exponential growth, 2^x->e^x


### Coordinate System with i 

### e in Circular Motion
consider that e^ix=a+ib. In our complex number coordinate, we can simply write (a,b), like in a regular 2-D plane. Now what's the derivative of e^ix, or in what direction is e^ix going? It's ie^ix, or ia-b, or -b+ia represented as (-b,a). (-b,a) dot (a,b)=0, which means they are perpendicular. That is, at any x, the function e^ix is changing in a direction perpendicular to its position vector (vector from origin to position). Note that in addition to being perpendicular, they are also equal in magnitude.

If we had 2^ix, it's derivative would be i2^ixln2. If we had a point (a,b), the derivative vector on that point would be (-ln2b,ln2a), which is still perpendicular to position vector. However, they are not equal in magnitude. Just as in regular exponential functions, 2^x and e^x differ by how the function and its derivative are related. Only e^x has derivative exactly equal to itself. Here we see again that only e^ix has derivative exactly equal to itself in magnitude. Another way to put this is that e^ix traverses the circle in 2pi time (returns to (1,0) when x=2pi), and 2pi is also the circumfrence of the circle, so it runs at unit speed. 

Note that we are in a unit circle because $e^{ix}e^{-ix}=1=(a+bi)(a-bi)=a^2+b^2$ (e^-ix=a-bi because in the definition of i^2=1, (-i)^2 is also 1, so in a equation changing signs before every i maintains equality)

A final note. If we have $e^{(a+bi)x}$, it's derivative would be $(a+bi)e^{(a+bi)x}$. If we have a point (x,y), it's direction of change is (ax-by, bx+ay). Dot product the two gives a(x^2+y^2) which is positive is a is positive. A positive position dot direction means its going outward, like a spiral. 

![](/images/sign-dot-product.png)
![](/images/complex-spiral.png)

So in summury, anything of the form ra^ix draws a circle of radius r. a^ix draws a unit circle. When a=e, the drawing moves at unit speed. If we use e^iπx, one circle takes 2 units of time which is even more convinient. 




### 

# Uncategorized
- The question: why is it that something about repeatedly multiplying with itself, and something about sides of triangles, are related. (by circle (mythtical) and periodicity (logical))

- both exponential and periodic function has a property. If I walk into a room with 16 rabits and wait for a day there will be 32 rabbits. But I don't really care about the exact number. I only care that the space my rabbits occupy doubled. If you walk into this room now, and also don't care about the exact number of rabbits, then tommorow you'll observe the same thing as I observed: the rabbits doubled. This doubling happens irrespective of time: no matter when you ccome in, a day after they will always double. Now how can this be related to periodic  events, like alternation of days and nights? If I see that it's noon right now, I will for certain observe noon 24 hours from now. If you come 24 hours later, you'll observe noon 24 hours after you starts the timer. Something remains the same after a certain time. Here the location of the sun is always the same 24 hours from now, no matter when you start the timer. In the rabbit case, the number of new rabbits compared to original rabbits stays the same, no matter when you record it, as long as the time interval is the same. This can lead to a formulation of why circles can be represented as exponentials and vice versa. 





# Primer on e
a growth that depends on itself. e arises natually in continuous growth. Note you can write e^x as 2^{x/ln(2)}, but ln(2) also depends on e. So you have to have e in continuous settings, which is the setting our universe uses.

also introduce taylor expansion

## Note on power functions
If f(x)=x^2, f(2x)=2^2*x*2, f(4x)=16x^2, f(8x)=64x^2. 

# Visual Introduction to Complex Exponential and Euler's Formula
Continue reading if you have wondered and failed to grasp the intuition of: why cos and sin and a circle, which represent periiodicty, can be represented as an exponential, which seems to only represent really fast growth; what actually is a complex number and why it is a complex number that appeared in Euler's formula; what does complex exponential [example] even mean? how do multiply something real an imaginary number times; why complex exponentials are ubiquios in math and engineering such as in Fourier and Laplace transform. Hopefully this artiicle can help you understand these questions more intuitively and visually.

If you google theese problkems, you'll likely, at the end of the day, be directed to EUler's great formula: [formula]. Chances are, you are taught how to derive it using Taylor expansion [link]. I'm slow in that kind of thinking, therefore I'll start with the also famous understadnign of Euler's formula, but a graphical one: [graph]

The next few paragraphs will answer two questions: what does complex expoentials mean, and how do you connstruct an algebraic expression that's equal to cos+isin. We'll start with the second. We'll construct an expression that equals cos+isin with the requirement that there can be only basic algebraic operations like addition, substraction, multiplication, division, exponentiation and logarithm.

The first concept here is periodicty. I'll begin by briefly noting the metaphisical significance of this concept. You might think that your life and our world are linear, that things just progress forward from one point to another, without turning back. However, the world has many elements that are periioidic. The largest peroid of our daily life is day, ie, the sun periodically rise and fall. There are also seasons, and all effects that come with seasons. You might feel good in spring and depressed in wniter and this repeats. Leaves become green in spring and dies in winter. More abstractly, your life sometimes get better and sometimes worse; the world sometimes become peaceful and sometimes go crazy. The point is that the universe is full of cycles that are as small as periodic vibration of atoms and as big as motions of galaxies. Hopefully, that explains why engineers use cos and sin so often: you need periodic functions to describe a world full of periodic phenomena. Therefore, constructing cos+isin now becomes constructing periiodic functions. Conversely, by constructing such function you'll see why complex exponentials are periodic.

What does periodic mean? It means you are returning. If you walk in a circle, you are always returning to where you started, so is walking back and forth. Let's trying building a functiion of time that describes going back and forth. To go back and forth, the most important thing is that you need to know when to go back and when to go forth. You need to keep track of your STATES, here how far you are away from the starting point. In addition, you want to change your motion at certain states. Since your state is your posiition, motiion is the derivative of posiiton, and change of motion is second derivative of position. Therefore, we want our function to relate states to change of change of states. Let's name our function x=f(t) where t is time and x is position. Can we do a simple polynomial like x=at^2+bt? Let's see what is its change of change of state. x''=2a. 

So let's analyze a circle. The first thing you should notice is that it's 2-dimensional. That poses the first problem to our cconstruciton. An algebraic expression of real numbers will always produce a real number that lie on the same real number line. Therefore, the first step in building a circle is to introduce somethiing not on real number line. 



All trig functions are easier to think about as projections of cirles. For example, the phase of a sin function just means starting the rotation with a certain angle [image]. Think about acost+bsint, what's the shape of this function. It's hard to visualize this in your head directly from this equaition. But if you think about it as two arms conneccted this way: [image], then rotating this whole thing will be equivalent to rotating a vector from origin to the end of B.


to represent 2 states you need 2 types of numbers. 

## Primer on e^i
### World of Change and Periodicity
exponential (like 2^x) and complex exponential functions (like 3^ix) are ubiqutous. Why? What's special about them?

There are two properties of the world that underlie many natural phenomena: change depends on state and periodicity.

It's most intuitive to think of the world as a function of time, where at each time the world is in a certain state. At the next instant, the world will move into a different state. State is just any descripton of the world and you can imagine it to be where everything is. Now, you know that change is eternal. As time goes by, state changes. The important observation is that the way state changes depends on the state. An classical example is population growth, where the state is the current population. The change of population will be people born over a period of time (simple model, immortal men). This change depends on how many people there is right now. More people at the moment will give biirth to more kids. This is universal. If you want to know how will the positioin of your computer change over the next instant, you need to know where it is right now. If it's over the edge of your desk, then you know there will be a change of its position. If it sits tight on your desk, you know its position will not change at the next instant. This was also expressed in Newton's laws. You probably know that if you know an object's current position and velocity along with all forces it's experiencing, then you can calculate its change of velocity, therefore its new velocity and therefore its new position at the next instant. The extreme manifestation of this is determinism, where if you have a supercomputer and give it the description of the world right now with every detail, it will calculate the future. Whether this is true or not, you should get a sense that how things change depends on what they are now.

Periodicity means that things, while in perpetual change, returns to states it has been every once in a while. For example, the temperature may rise, and rise for a long time if you're enterring summer, but it will always fall back, since the earth orbits the sun every year. Periodicity is more ubiqutous than you think. Your life has ups and downs, you are sometimes in a good relationship, sometimes bad, sometimes no relationship, and maybe back in a good one again, your state of mind follows patterns of day (you are energetic at a certain time in a day and sleepy at others), and the world goes through times of peace and war. It could even be claimed that everything is periodic. To understand this, it should first be understood that periodicty can add up. If you are generally more energetic in the morning and drowsy in the afternoon, and if you are generally more energetic during summer than winter, then you are likely to be very energetic during summer mornings,  neutrtal during summer afternoons and winter mornings, and very drowsy in winter afternoons. The fast daily period is added to the slower yearly period. The fast and slowness is decribed by frequeny. You can add as many periodicity of different frequencies as you want. The more you add, the more complex phenomena you can describe. 

> OPTIOINAL: There are generally 2 questions regarding the claim that everything is periodic. First is like: the production of human civilization seems to be always going up. The explanation is that we might have an extremely slow periodicty in addition to the periods of cennturies and decacdes, such that we are still on the rising phase but in the far future humans might be decline. Second is like: if I suddenly get a raise, my life is "elevated" and that breaks the periodic struccture. That is harder to explain intuitively but mathematiccally, it could be proven that, with enough (infinite to be precise) periodicities adding up altogether, you will describe that kind of phenomenon.

### Exponentials for state dependency
Now let's dive into the math and see how those natural phenomena make it necessary for us to invent exponentials and complex exponentials.

We'll use t, or time, as the independent variable since intuitively, time flows independent of anything else. We use x, or state, as the dependent variable according to convention. Be careful how you interpret x if you've only seen functions of the form y=f(x). A function x=f(t) describes what states you are in as time flows. 

Functions you are most familiiar with, like x=t or x=t², are not state dependent. The change of x=t, aka its derivative with respect to t, is 1. Real world situation is like counting how many days you have lived. You add one every day, no matter how many days you have lived. In other word, the state, or how many days you have lived, has nothing to do with how that state will change. t² is similar in that its derivative is 2t. Again x's cchange is not dependent on x itself. 

Without any mathematical rigor, I'll claim that the best functiion to account for state dependency is exponential functions. For example, 2ᵗ has derivative of ln(2) times 2ᵗ, or ln(2) tiimes itself. If you are unconfortable with infinitesimals, image you have 8 rabbits which multiply themselves every year. It means next year you will have 16, and the year after 32. The change, or increase of number of rabbits, IS the number of rabbits. As an aside, eᵗ has the property that its derivative is exactly itself, which is a continuous version of the rabbits phenomenon we described (imagine that instead of every year, they give birth to a fractional of a rabbit every instant). Since nature is iin fact mostly continuous, we use e as the lower left part of exponential functions most often, hence the name natural base.

### Complex Exponential for periodicity
There's an interesting relationship between state dependency and periodicity. If you are a periodic function, you are essentially walking back and forth. No matter how far you go up or down, you have to turn back at some point, otherwiise you are not periodic. To periodicly turn back and forth, you have to know where you are right now, ie, your next move depends on your current state. Note that this is only one way to make sense of why exponential functions are related to periodicity. 

Now the more complex topic is indeed the complex number. Previously I said that in order to have periodic motion, your next move has to depend on your current state. This is actually inaccurate. Suppose that I'm walking back at forth. When I'm at the farthest point in one direction, I need to start moving back. But at that farthest point, I'm actually stopping, before I reverse my walking direction and start accelarating. The rule is therefore: the change of state (speed) should be 0 when the state is in either of the farthest points. This means at that point, I just stop, and because I'm still at that point, I continue to stop, ad infinitum. The correct way to go back and forth is to further specify the change of change of state, or accelaration if we focus on the moving example. The new way to write the rule for going back and forth would be: when the state is at the farthest point, change of state (speed) is 0, but change of change of state is non-zero. 


### Cos, Sin, Circle, and Euler's Formula
This section will be completely self contained. But if haven't read the previous  sections, I still want to emphasize that first, since 



## Fourier Series
### Describe an Apple
How do you descibe an apple? You might first think about the big features, like being red and round. Then you might remember that it's not precisely round because there's some bent-in part at the top. At a closer look, you see irregular bulges and indentation accrooss the apple's surface. The idea is, to descibe soemthing, you zoom in gradually instead of starting with every small detials. That's one way to think about fourier transform: You decompose a function to its building blocks, from large blocks to small ones. 

Before going further, make sure that you can grasp the idea that "anything can be described by a function" or "the universe is a function". An image is a function from 2d pixel coordinates to triplets of colors (rgb). A piece of audio is a function from time to loudness. Your action is a big complex function from numerous variables like the state of a cell in your heart to numerous outputs like length of a muscle cell on your arm.

So we have lots of different functions to describe things, and we want to decompose them into smaller building blocks. The question at hand is: what building blocks should we use? 

In the primer on e^i section, we talked about periodicity. For reasons explained there, all our natural phenomena can be seen as periodic or made of smaller periodic phenomena. Therefore the functions we use to describe them are also periodic in nature. Therefore we should use periodic functions as building blocks.

### 
The periodic function we are all familiar with is the sine or cosine function. As mentioned in periodicity, periodic functioins of different frequency can be added to create more interesting functions. Below is an illustruatioin of a "square" wave that can also be represented as summation of many sine waves:

So the idea is that we can use many sine or cosine waves to build complex functions. But what sine and cosine functions exactly are we choosing? By that I mean this: a sine function can be stretched vertically by multiplicatioin with a number; or it can be stretched horizontally by making what's inside sin() go faster, for example by using sin(2t); or it can be shifted by adding a so called phase, somethiing like sin(t+90°). These three operations can be applied to cos() as well. 

From school you might know that some of these functions can be converted to each other when you choose the right stretching or shifting. Your schoolwork migth include things like what is sin(2x)+2cos(2x+pi) or sin(x)+sin(2x). The next section will disccuss how this is done visually, without any trignometric equations you were asked to memorize. And hopefully you can immediately answer questions like those above in your head afterwards. 

### Everything on a Circle
From the primer you know that sine is the y-axis projectiion of the dot on the circle and cosine the x-axis projetion. [animation]

Let's know see the effect of the 3 operations mentioned above. 

The first is stretcching vertically, this is done by increasing the radius of the circle. The radius, or in plain trignometry, the number before sin or cos, is called amplitude. The effect looks like this:

Increasing the number before the independent variable makes the dot go faster. Remember that t can be seen as actually time the dot has been moving on the circcle, so from the animation below we see that at time=2pi, the dot completed one cycle. But for the faster dot, it completed the cycle at time=pi. In other word, the period of sin or cos is now pi instead of 2pi, making them oscillating twice as fast. The number is called frequency.

The cool part is the so called phase. Previously the dot started on the x axis, so that at time=0, its x-axis projection, or its corresponding cos value is 1, and its y-axis projection,, or its sin value, is 0. This matches what cos(0) and sin(0) really are. If we have cos(t+θ), where θ is any angle you like (note that θ is not related to t, your independent variable, such that cos(t+θ) means for every t you choose, a fixed offset θ will be added before going into the cos() function), then at time 0, the output should be cos(θ). In other words, with a θ offset, your starting positoin on the circle should be (cos(θ), sin(θ)). That just corresponds to movnig the dot θ degree or radian counterclockwise. The rotation part stays the same. Only the starting point changed. Below is the animatiion.

Now before going further, you should notice that for any trig function, you only need a line to represent it. The angle between your line and x axis is offset, the length is amplitude, and the frequency is its imaginary rotating speed which you can draw with an arrow or anything you want. 

In case you haven't noticed, if you start the dot on the y axis and make it move counterclockwise, its x-axis projection will be -sin and y-axis projection will be cos. What does that mean? It means cos shifted 90 degree or π/2 is -sin and sin shifted π/2 is cos. By shiftiing π/2 I mean sin(t+π/2). You should try starting your dot on different places on the circle and see what trig function its projection traces. [animation]

Another fun thing to do with the circle is to add two trig functoins. Here's the animatioin when you have multiple trig functions added together.

Here comes an important fact. If you have a function asin(t)+bcos(t), where a and b are two numbers, what graph will thsi functoin have? Sinice sin is just -cos shifted by π/2, it can be represented like this (we used to say siin is projection on y-axis, but for the rest of the article, we use only the x-axis to represent our function of intrest): [animation]

Now adding the two is just sticking the two arms together. Since they have the same frequency, they rotate together (there's always this 90 degree angle between the arms): [animation]

If you connect the endpoint of the second arm to the origin, you'll see that the two functions added together is equivalent to another function which has a bigger amplitude and is shifted clockwise. 

equivalance of sine offset and asin+bcos
teach property of e with graph: 1)derivative, 2)e^ae^b=e^a+b 
equivalannce to e^i
general fourier series in sin and cos
convert to e
example of sin, sin+sin2t

inverse problem
projection with disrete trig
book proof
example of sin


## Applications
### cos(x+θ), asin(x)+bcos(x),e^(θ+x)i
show cos(x+θ)=asin(x)+bcos(x) within circle
then show e
then show fourier series
then use the example of sin and calculate fourier series with e
### Integrating cos

### integrating cos²(x)
$cos^2(x)=(\frac{(e^{xi}+e^{-xi})}{2})^2=1/4[e^{2xi}+e^{-2xi}+2]$

$\int_{2\pi}^0{cos^2(x)}dx=\int_{2\pi}^0{1/4[e^{2xi}+e^{-2xi}+2]}dx=\pi$

use circle approach

equivalence with traditional trignomitry.
$\int_0^{2\pi} \cos^2(x) \, dx = \int_0^{2\pi} \frac{1 + \cos(2x)}{2} \, dx=\frac{1}{2} \left(\int_0^{2\pi} 1 \, dx + \int_0^{2\pi} \cos(2x) \, dx\right)=\pi+0$

### integrating cos(x)*cos(x+θ)
$cos(x)cos(x+θ)=\frac{(e^{xi}+e^{-xi})}{2}\frac{(e^{xi}e^{θi}+e^{-xi}e^{-θi})}{2}=1/4[e^{2xi}e^{θi}+e^{-2xi}e^{-θi}+e^{-θi}+e^{θi}]$

$\int_{2\pi}^0{cos(x)cos(x+θ)}dx=\int_{2\pi}^0{1/4[e^{2xi}e^{θi}+e^{-2xi}e^{-θi}+e^{-θi}+e^{θi}]}dx=\int_{2\pi}^0{1/4[e^{-θi}+e^{θi}]}dx=\int_{2\pi}^0{1/2[cos(θ)]}dx=\pi cos(θ)$

use circle approach
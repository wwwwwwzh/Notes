# Continuous Topics
## Math (Group, Ring, Field, Space)
[The Very Basics of Groups, Rings, and Fields](https://www-users.cse.umn.edu/~brubaker/docs/152/152groups.pdf)

<img width="600" alt="Screen Shot 2022-12-27 at 8 11 28 PM" src="https://user-images.githubusercontent.com/36484215/209751312-d5187ff2-2716-4fc7-b93c-354f42ef69d2.png">

It seems that set theory and other associated number theories are the foundamentals of applied math I was looking for. They provide mathematically rigorous definitions (formal languages) to things.

### Vector Space



### [Inner Product Space](https://en.wikipedia.org/wiki/Inner_product_space)
a real vector space or a complex vector space with an operation called an inner product. The inner product of two vectors in the space is a scalar.

### Dual Space
- Any vector space V has a corresponding dual vector space (or just dual space for short) consisting of all linear forms on V, together with the vector space structure of pointwise addition and scalar multiplication by constants.
- A linear form or a covector is a linear map from a vector space to its field of scalars (e.g. R^n->R)
- Transpose of a vector v is a linear form ⍺ such that ⍺(v)=<v,v>

> Dot product of two vectors x and y is often written as x^Ty where it is actually this: (1) x^T is a matrix representing the linear map ⍺ such that ⍺(x)=<x,x>; y is a matrix representing a vector from the same vector space as x; the mapping ⍺ transforms y to a scalar and by definition of covector ⍺(y)=<x,y>. (2) x^T is actually not a vector transpose, but the transpose of a matrix representing the vector x; y is a matrix representing a vector; by definition of matrix multiplication, the product is a scalar representing the dot product of the two underlying vectors.

### [Affine Space](https://en.wikipedia.org/wiki/Affine_space)
<img width="1073" alt="Screen Shot 2022-12-28 at 10 03 57 AM" src="https://user-images.githubusercontent.com/36484215/209847134-ee2e37ee-3611-4855-8576-602114afc5dd.png">

### Euclidean Space
https://en.wikipedia.org/wiki/Euclidean_space#Motivation_of_the_modern_definition

## Math (Function/Mapping) -------
A map or mapping is a function in its general sense.
### Function
A function from a set X to a set Y assigns to each element of X exactly one element of Y.

### Linear Mapping （Linear Operator)
<img width="1091" alt="Screen Shot 2022-12-28 at 1 24 17 PM" src="https://user-images.githubusercontent.com/36484215/209868110-d10b668f-37c4-4b8e-ba1f-40b0e6ebc2a9.png">

- A linear mapping is usually represented by a matrix. 
- A matrix is just some numbers but in this case it can represent a function. A n by 1 or 1 by n matrix usually represents a vector.
- "Matrix multiplication was first described by the French mathematician Jacques Philippe Marie Binet in 1812, to represent the composition of linear maps that are represented by matrices."
- A linear map L is often written as L[⋅] to refer to the function itself rather than function evaluated at a particular point.

### Homomorphism
Homomorphisms of vector spaces are also called linear maps

<img width="1245" alt="Screen Shot 2022-12-28 at 1 19 11 PM" src="https://user-images.githubusercontent.com/36484215/209867613-878b666e-e178-4a60-b896-b57e173638be.png">

## Math (Geometry) --------
Geometry (from Ancient Greek γεωμετρία (geōmetría) 'land measurement'; from γῆ (gê) 'earth, land', and μέτρον (métron) 'a measure') is, with arithmetic, one of the oldest branches of mathematics. It is concerned with properties of space such as the distance, shape, size, and relative position of figures.

Until the 19th century, geometry was almost exclusively devoted to Euclidean geometry, which includes the notions of point, line, plane, distance, angle, surface, and curve, as fundamental concepts.

> Arithmetic (from Ancient Greek ἀριθμός (arithmós) 'number', and τική [τέχνη] (tikḗ [tékhnē]) 'art, craft') is an elementary part of mathematics that consists of the study of the properties of the traditional operations on numbers—addition, subtraction, multiplication, division, exponentiation, and extraction of roots.

## Math (Calculus & Optimization) --------
### Approximation
- Linear: F(x)=F(x0)+∇F(x)⋅(x-x0) ⟺ F(x)=Ax+B
- Quadratic: F(x)=F(x0)+∇F(x)⋅(x-x0)+1/2⋅(x-x0)H(x-x0) ⟺ F(x)=xAx+Bx+C
- Taylor: F(x)=Fⁿ(x)⋅Δxⁿ/n!
- Fourier: 

> It seems that optimization is about finding linear combination of well behaved non linear functions

> Fourier takes inner product of its basis on the whole function while Taylor focuses on neighborhood of a point. This makes Fourier more "global".

> Saved for later understanding: A holomorphic function in an annulus containing the unit circle has a Laurent series about zero which generalizes the Taylor series of a holomorphic function in a neighborhood of zero. When restricted to the unit circle, this Laurent series gives a Fourier series of the corresponding periodic function. (This explains the connection between the Cauchy integral formula and the integral defining the coefficients of a Fourier series.)

### Differential
<img width="200" alt="Screen Shot 2022-12-30 at 7 37 41 PM" src="https://user-images.githubusercontent.com/36484215/210122588-4d94d0ae-8d6e-45a4-a9b6-d91fd757ea34.png">

### Hessian
- Hessian of function f is Hf where (Hf)ᵢⱼ=d²f/dxᵢdxⱼ
- H is symmetric 
- H is Jacobian of ∇f

### Extrema Test with Hessian
<img width="920" alt="Screen Shot 2022-12-29 at 1 05 15 PM" src="https://user-images.githubusercontent.com/36484215/210006200-88c83527-6335-49cb-b4a4-b56bf0537905.png">

- x0 is the point of interest. v is a random direction in Rn. If ∇f(x)=0 and H(x) is positive definite, we know any v will result in increase at x0 so x0 is local minimum.
- You can also use determinant of Hessian to check if a point is saddle, local minima or maxima. The determinant tells you about eigenvalues of H. Trace tells you if they have same sign.


### Lagrangian (Optimization with Constraints)
- Problem: find extrema of f(x) subject to constraint g(x)=b
- Intuition 1: contour of f(x)=extrema is tangent to level set of g(x), or gradient g is parallel to gradient of f.
- Intuition 2: The intersection of f and g is a surface. A small perturbation that takes a point on this surface to another point on the surface will not change f if the point is extrema. Conversely, if the point is not extrema, a small perturbation can maintain the point on surface while changing f.
- Lagrangian multiplier: ∇f=λ∇g. λ is gradient of f(b), meaning that λ is the rate of change of the extrema we found with respect to the constant in constraint g.
- The Lagrangian: L(x,λ)=f(x)-λ⋅g(x). Solution to ∇L=0 is the extrema because ∇L=0 encapsulates both parallel condition (∇Lx) and constraint (∇Lλ)

Lagrangian example:

<img width="400" alt="Screen Shot 2022-12-30 at 12 01 00 PM" src="https://user-images.githubusercontent.com/36484215/210103979-06801692-0744-4a12-a61b-13e298300807.png">
<img width="400" alt="Screen Shot 2022-12-30 at 12 00 48 PM" src="https://user-images.githubusercontent.com/36484215/210103961-995fd334-d2b8-4dab-ab3c-85b42044aa6e.png">

### Unconstrained Optimization
- Gradient descent

## Math (Variational Calculus)
### Functional
- a functional is a certain type of function.
- In linear algebra, it is synonymous with linear forms, which are linear mapping from a vector space V into its field of scalars
- In analysis, a functional maps from space X to scalar. Here specifically from function to scalar.

### Differentiation under Integral Sign
<img width="300" alt="Screen Shot 2022-12-30 at 5 24 28 PM" src="https://user-images.githubusercontent.com/36484215/210119566-85190b11-d833-4701-b169-5fe087807601.png">

### Integration by Parts
<img width="400" alt="Screen Shot 2022-12-30 at 5 46 29 PM" src="https://user-images.githubusercontent.com/36484215/210120051-a589c91a-a02b-437d-ba8c-2233d805d76a.png">

### Gateaux Derivative
- Problem: finding extrema of a functional F(f). 
- Intuition: functional doesn't have a gradient like functions so can't do things like setting ∇f=0. Want something similar. Recall in linear algebra a differential at x0 is dfₓ₀(v)=lim h→0 f(x₀+hv)-f(x₀)/h. When x is extrema, differential of f at x is 0 for any v. Similarly, for a functional, when f is extrema for F, dFf(h)=dF(f+hg)/dh=0, meaning that at f, adding a small amount of any function g will not change F. dFf(h) is scalar to scalar and have a close form formula after using Differentiation under Integral Sign and Integration by Parts. It will contain an object concerning f and a plain g(x). Setting it to 0 means that object of f=0.


<img width="795" alt="Screen Shot 2022-12-30 at 7 50 57 PM" src="https://user-images.githubusercontent.com/36484215/210122814-29bd3244-3179-4a50-a232-8164bf264183.png">


-------------------------------------------------------------------------------------------------------------------------------

## Graphics
### Color and Radiometry
https://www.pbr-book.org/3ed-2018/Color_and_Radiometry/Radiometry
https://computergraphics.stackexchange.com/questions/7503/what-is-the-difference-between-radiance-and-irradiance-in-brdf

- Q (joule J) is energy. A photon at wavelength λ carries energy hc/λ
- ϕ (J/s or watt W) is radiant flux, also known as power, is the total amount of energy passing through a surface or region of space per unit time: dJ/dt
- E (W/m²) is average density of power over the area A: dϕ/dA. This quantity is either irradiance (E), the area density of flux arriving at a surface, or radiant exitance (M), the area density of flux leaving a surface. 
- Solid angle, radian, and steradian (sr). One sr is how much angle 1 unit area covers a unit sphere, like radian is the angle coverd by one unit length on a unit circle. In spherical coordinate, you can view solid angle as θ⋅ϕ or just a direction. Differential solid angle dw can be seen as area on unit sphere. Integrating solid angle over unit sphere is written as $$\int_\Omega d\omega$$ but is really just $$\int_0^{2\pi}\int_0^{\pi} \sin\theta d\theta d\phi$$ The entire sphere subtends a solid angle of 4πsr, so sometimes integration is written as $$\int_{4\pi} f(x) d\omega$$
- Ω is set of directions over unit sphere
- I (W/sr) is intensity, here angular density of emitted power. Intensity describes the directional distribution of light, but it is only meaningful for point light sources.
- L (W/sr/m²) is radiance, is flux density per unit area, per unit solid angle. E acounts for only spatial distribution of power, not directional. L can be defined as dE/dω where E is irradiance at the surface that is perpendicular to ω. L can also be defined as dϕ/dωdA⟂ where dA⟂ is dA projected along the direction of dω. Try understanding this with surfaces illuminated by many directional lights.

> Calculus review: Difference between area/time/solid angle, sqaured meters/seconds/steradians, and point/timestamp/direction. Power (flux density) at a point or radiance at a particlular direction are zero because they are defined differentially. You have to move the point to cover some area or move the direction to cover some solid angle to integrate power or irradiance. When integrating something, we say we integrate (quantity of measurement) and we are adding infinitesimal (unit of measurement) over the initegral range (e.g. integrate time/mass/angle by adding small seconds/kilograms/radians). 

### BRDF
> Calculus Review: dx is h->h and dy is really f'(x(h))dx(h) or f'(x)dx. In multivariable calculus, df(xᵢ) means f'xᵢ(x)dxᵢ. df itself would be a vector of gradients. dy has same unit as y.
#### Radiance and Irradiance
Irradiance can be computed by integrating radiance over Ω. 
<img width="200" alt="Screen Shot 2022-12-21 at 8 32 46 PM" src="https://user-images.githubusercontent.com/36484215/209056734-01c365f1-13d9-46bb-887b-ee8e96526326.png">

#### BRDF
The relationship can be defined as a constant for every (ωi,ωo,p) based on the linearity assumption from geometric optics: the reflected differential radiance is proportional to the irradiance. 

<img width="700" alt="Screen Shot 2022-12-22 at 10 22 41 AM" src="https://user-images.githubusercontent.com/36484215/209201522-c2f04a6b-ee4f-4e5f-9d51-dd17c53d4c4a.png">


#### BRDF, BTDF, BSDF, BSSRDF
BSDF (note the S²):

<img width="500" alt="Screen Shot 2022-12-20 at 10 17 41 AM" src="https://user-images.githubusercontent.com/36484215/208737610-a207eb4a-c3a4-4845-ac69-8c277a0f2a07.png">

BSSRDF:

<img width="327" alt="Screen Shot 2022-12-22 at 10 50 43 AM" src="https://user-images.githubusercontent.com/36484215/209206038-671e7573-c914-4598-8773-ab6e2d2cd45f.png">

<img width="500" alt="Screen Shot 2022-12-20 at 10 30 14 AM" src="https://user-images.githubusercontent.com/36484215/208740005-257de391-aee3-4e2f-9cb3-7e9ec331c9ca.png">

- BRDF is the upper hemisphere, BTDF is lower. BRDF+BTDF=BSDF
- BRDF for a perfect mirror (reflection) and BTDF for perfect material separation surface (refraction) is a delta function
- It seems that BSDF is more physically based because "Reflection is a form of scattering". However I feel more physics knowledge is needed to really understand assumptions behind these models.
- BSSRDF is a summarized representation modeling the outcome of various reflection and volumetric scattering processes.
- Can use fourier basis for BRDF.

#### Rendering Equation
<img width="500" alt="Screen Shot 2022-12-22 at 12 26 56 PM" src="https://user-images.githubusercontent.com/36484215/209220242-7de61b62-a02c-4247-a8dd-832e8d09507b.png">

tr(p,w) is the transport function that returns the point hit by a ray from p with direction w.

<img width="500" alt="Screen Shot 2022-12-22 at 12 30 50 PM" src="https://user-images.githubusercontent.com/36484215/209220806-22332cb9-225e-4634-8659-5bf251028796.png">

I hope I can understand the later part of the slides
#### Microfacet
https://www.pbr-book.org/3ed-2018/Reflection_Models/Microfacet_Models

#### BRDF in Modern Renderer
- Albedo Map: diffuse
- Normal Map: 
- Specularity Map: amount of light reflected
- Glossiness Map: "roughness near reflection direction"
- Roughness Map: microfacet related
- Metalness Map: metallic properties as exhibited by real physical materials

### Volume Scattering
- Absorption: the reduction in radiance due to the conversion of light to another form of energy, such as heat
- Emission: radiance that is added to the environment from luminous particles
- Scattering: radiance heading in one direction that is scattered to other directions due to collisions with particles


<img width="400" alt="Screen Shot 2022-12-22 at 1 55 37 PM" src="https://user-images.githubusercontent.com/36484215/209232735-d70fb620-d38d-463d-9565-39e261908301.png">

Part of the radiation can pass the object unchanged, which is called transmission, part of it can change direction without a change in energy/frequency, which is called scattering, and part of it can disappear with the energy transferred to the object, which is called absorption. Both scattering and absorption remove radiation from the beam and are together called extinction.

<img width="500" alt="Screen Shot 2022-12-22 at 1 55 17 PM" src="https://user-images.githubusercontent.com/36484215/209232685-741b8794-7f22-409b-beed-5045a95c5ebf.png">


### Environment Map 
Assumption is all light infinite far. Reflection map->diffuse map. box vs sphere map.

## School Related
### Course Plan
- Visual or Performing Arts: APPL 110 (Introduction to Design and Making)
- Literary Arts: Cicero

### Interested
- ECON 415 Market Failure
- Hist 158 Early Modern Europe
- HIST 266 history of warfare
- HIST 315 NATION BUILDING LATIN AMERICA
- HIST 340 ETHICS AND BUSINESS IN AFRICA
- HIST 538 MIDDLE EAST & THE WEST


-------------------------------------------------------------------------------------------------------------------------------

# Logs
## 12.19
### sherical harmonic 

<img width="200" alt="Screen Shot 2022-12-19 at 4 43 09 PM" src="https://user-images.githubusercontent.com/36484215/208555184-85d131f8-bfdd-402f-924f-b145467e3f6e.png">

ω = (sinθ*cosφ,sinθ*sinφ,cosθ)

basically a basis for sherical functions like fourier basis

### projection matrix (reviewing Roni's slides)
<img width="300" alt="Screen Shot 2022-12-19 at 5 24 44 PM" src="https://user-images.githubusercontent.com/36484215/208559444-a1df7cd3-3423-4590-8fa1-64dd07c854de.png">

Note that image plane doesn't change size

<img width="300" alt="focal length and ratio" src="https://user-images.githubusercontent.com/36484215/208560712-78b6cd10-949e-446a-8d1b-c3646280e610.jpg">

Note that when f→∞, this becomes orthographical projection and ratio will be 2.

## 12.20-22 (reading pbr book)
### BRDF
### Others
- [Mach bands](https://en.wikipedia.org/wiki/Mach_bands)
- Thor 4 is really bad. 
- Beam search in translation (balance between greedy search and resource constraint)
- Log is a really interesting function. When x is too big, it makes x grow slower. When x is too small, it makes x shrink slower. Everything is within a more controllable range. 

## 12.21
### Machine Translation
- statistical translation:
- [RNN encoder decoder](https://arxiv.org/pdf/1406.1078.pdf): "Unlike the traditional phrase-based translation system which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation."
- [Attention](https://arxiv.org/pdf/1409.0473.pdf): "the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly"
- Self attention: replace RNN with dot product
- Transformer: more complex than I thought. wonder what intuition guided them

## 12.22-23
### PixelRNN
masked convolution + row LSTM to predict next pixel given all previous pixels

### GANS
#### GANS

#### DCGAN

#### [StyleGAN](https://arxiv.org/pdf/1812.04948.pdf)
the generators continue to operate as black boxes, and the understanding of various aspects of the image synthesis process, e.g., the origin of stochastic features, is still lacking. The properties of the latent space are also poorly understood, and the commonly demonstrated latent space interpolations provide no quantitative way to compare different generators against each other.

####

> Note: upsampling+conv is favored over transposed conv to avoid checkerboard artifacts. https://distill.pub/2016/deconv-checkerboard/

## 12.24-25
### Think
- Kanzi the ape
- “The primate vocal tract is ‘speech ready,’ but ... most species don’t have the neural control to make the complex sounds that comprise human speech,” Dunn writes for The Conversation.
- Deaf people think in sign language or imagined sounds or visual stuff
- Blind people: echolocation, spatial understanding, other sensory information
- https://waitbutwhy.com/table/person-with-no-senses
- criticacl period for language (or really intelligence) development. Nervous system stops growing (real brain learning?)

Sensory or external stimuli is needed to start things. Curiosity and other premitive desires (survival, imitation, some are uniqu to individuals, some learned) to drive internal processing. Memory?

## 12.26-29
### Eating
Not eating after 12.25 dinner makes me starve early in the morning and feel bad throughout the day. Ate at 12.26 but still not good after 12.27 breakfast. Took a walk and ate lunch much better. Slept and all good. Ran short late afternoon. 28 morning stomach feeling funny 2p. 29 morning better 2p.  Ran afternoon.

### Math
- Group theory, spaces, review linear algebra
- Einstein notation
- Unconstrained optimization (f'=0 & positive definite Hessian) and why 1/2 for second order derivative (area of triangle)
- Constrained optimization (Lagrange multiplier)
- It seems that SVM is a more traditional way to do optimization but intuition guided neural network somehow is more flexible

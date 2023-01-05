# Math
## Group, Ring, Field, Space
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

-------------------------------------------------------------------------------------------------------------------------------

## Function/Mapping
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

-------------------------------------------------------------------------------------------------------------------------------

## Calculus & Optimization
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


-------------------------------------------------------------------------------------------------------------------------------

## Variational Calculus
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


# [Curve](https://groups.csail.mit.edu/gdpgroup/assets/6838_spring_2021/chapter3.pdf)
## 2D Curve
### Definition
<img width="600" alt="Screen Shot 2023-01-05 at 7 31 19 AM" src="https://user-images.githubusercontent.com/36484215/210803825-5162d662-bc71-47c3-9bd1-4952cae1bc9f.png">

Example: unit circle
<img width="200" alt="Screen Shot 2023-01-05 at 7 32 38 AM" src="https://user-images.githubusercontent.com/36484215/210804119-ceb84953-9d21-476e-a19e-c24e1cefd167.png">
### Parameterized Curve
- Motivation: On the one hand, the fact that curves are geometric objects dictates that we represent curves as sets C ⊆ Rn. But since we eventually want to compute derivatives along C, we have to link it back to calculus through use of a local parameterization.
- A parameterized curve in Rn is the image (or trace) of a differentiable function γ : (a, b) → Rn, where −∞ ≤ a < b ≤ ∞ and γ'(t) ≠ 0 for all t ∈ (a, b).

### Parameterization by Arc Length
- Motivation: remember a curve is a set of points C, we want to define geometric measurements near points p ∈ C. Also we are using a local parameterization γp(t), so we want to measure γ in a way that measurement on γ is the as measuring C. For this to make sense, different parameterizations of γ must define the same curve, otherwise, meansurement on γ is about a specific function γ rather than on C.
- Reparameterization: Suppose φ(t) : (ã,˜b) → (a, b) is a smooth, bijective function. Geometrically, γ˜(t) := γ ◦ φ(t) = γ(φ(t)) traces out the same curve
- Velocity: <img width="200" alt="Screen Shot 2023-01-05 at 7 54 51 AM" src="https://user-images.githubusercontent.com/36484215/210809204-9dc492a4-d8de-4d5a-892c-fe18c563a9ad.png"> Different parameterizations of γ lead to different γ' so velocity is not a property of the curve
- Arc length: <img width="400" alt="Screen Shot 2023-01-05 at 7 57 46 AM" src="https://user-images.githubusercontent.com/36484215/210809909-9fcfb452-00d7-4ef9-a73b-987b10a82ea5.png"> If γ is parameterized by arc length, Any measurement written in terms of the function γ(s) and its derivatives is a property of the local geometry of the oriented curve C at the point p := γ(s)
- Parameterization by Arc Length: <img width="570" alt="Screen Shot 2023-01-05 at 8 00 37 AM" src="https://user-images.githubusercontent.com/36484215/210810550-53645734-acd1-4587-8c88-6a7e127602ed.png">

> Note that we are defining a particular parameterization so that we know v(s) is always 1.
### Tangent, Normal, Frenet Equations
- T(s)=γ'(s). Because ||γ'(s)||= 1, T(s)=cosθ(s)e1 + sinθ(s)e2
- N(s)=T'(s)=θ'(s)[−sinθ(s)e1 + cos θ(s)e2]=κ(s)N(s). κ(s):= θ'(s), is the signed curvature. It means of how much of the normal is the curve changing its direction. You can construct a curve just with κ(s). 
- Frenet: <img width="300" alt="Screen Shot 2023-01-05 at 8 08 51 AM" src="https://user-images.githubusercontent.com/36484215/210812465-aaaa1674-6a82-455f-90c9-0879cb087cd6.png">
- The Frenet equations is "coordinate free", it writes the derivatives of T and N in the {T, N} basis!

### Fundamental Theorem of the Local Theory of Plane Curves
If two curves have the same curvature κ(s), they are the same up to rotation and translation.

### Winding Number
<img width="231" alt="Screen Shot 2023-01-05 at 8 15 04 AM" src="https://user-images.githubusercontent.com/36484215/210813925-2f79a0a6-b9c5-49cf-ac7a-16f326dd4652.png">

## 3D Curve
### Lemma
- ||v(t)||=1->v'(t)⋅v(t)=0
- v(t)w(t)=0->v'(t)w(t)=-v(t)w'(t)
- both by product rule
### B, 3D Frenet
- Since we are in R3, given two orthogonal vectors T(s) and N(s), we can define a third binormal vector B(s) via B(s) := T(s) × N(s).
- {T, N, B} form an orthonormal basis
- Frenet: <img width="300" alt="Screen Shot 2023-01-05 at 8 23 18 AM" src="https://user-images.githubusercontent.com/36484215/210815751-89a6f142-2e23-4124-9983-119418c97607.png">
-  the curvature κ(s) of a curve in three dimensions measures in-plane bending, while the torsion τ(s) measures how much the curve spirals out of the plane.

# Group, Ring, Field, Space
[The Very Basics of Groups, Rings, and Fields](https://www-users.cse.umn.edu/~brubaker/docs/152/152groups.pdf)

<img width="600" alt="Screen Shot 2022-12-27 at 8 11 28 PM" src="https://user-images.githubusercontent.com/36484215/209751312-d5187ff2-2716-4fc7-b93c-354f42ef69d2.png">

## Group
### Power Set
Power set of a set S is the set of all subsets of S, including the empty set and S itself

## Space
In mathematics, a space is a set (sometimes called a universe) with some added structure. While modern mathematics uses many types of spaces, such as Euclidean spaces, linear spaces, topological spaces, Hilbert spaces, or probability spaces, it does not define the notion of "space" itself.

### Vector Space
- A vector space over a field F is a set V together with two binary operations that satisfy the eight axioms. the elements of V are commonly called vectors, and the elements of F are called scalars.

> Easier version: a set with its elements closed under addition and scalar multiplication. Remember that "closed under" means for any two elements in the set, the output of the defined binary operation between them is also in the set.


### [Inner Product Space](https://en.wikipedia.org/wiki/Inner_product_space)
a real vector space or a complex vector space with an operation called an inner product. The inner product of two vectors in the space is a scalar.

### Dual Space
- Any vector space V has a corresponding dual vector space (or just dual space for short) consisting of all linear forms on V, together with the vector space structure of pointwise addition and scalar multiplication by constants.
- A linear form or a covector is a linear map from a vector space to its field of scalars (e.g. R^n->R)
- Transpose of a vector v is a linear form ⍺ such that ⍺(v)=<v,v>

> Dot product of two vectors x and y is often written as x^Ty where it is actually this: (1) x^T is a matrix representing the linear map ⍺ such that ⍺(x)=<x,x>; y is a matrix representing a vector from the same vector space as x; the mapping ⍺ transforms y to a scalar and by definition of covector ⍺(y)=<x,y>. (2) x^T is actually not a vector transpose, but the transpose of a matrix representing the vector x; y is a matrix representing a vector; by definition of matrix multiplication, the product is a scalar representing the dot product of the two underlying vectors.

### Metric space
- a metric space is a set together with a notion of distance between its elements, usually called points. The distance is measured by a function called a metric or distance function.
- The most familiar example of a metric space is 3-dimensional Euclidean space with its usual notion of distance.

### Measure Space
A triple (X, A, μ) where X is is a set, A is a σ-algebra on the set X, and μ is a measure on (X, A)

#### σ-algebra
a σ-algebra (also σ-field) on a set X is a nonempty collection Σ of subsets of X closed under complement, countable unions, and countable intersections.

Formal:
Σ⊆Power set of X and satisfies 3 properties:
1. X ∈ Σ
2. if A ∈ Σ, then X \ A ∈ Σ
3. if A1, A2, ... in  Σ, then A1∪A2∪... in Σ

#### Measurable Space
(X, A)

#### Measure
μ: A->R and satisfies certain conditions similar to axioms of probability.

![](/images/measure.png)

Common measures:
- The counting measure is defined by μ(S) = number of elements in S.
- A probability measure is a measure with total measure one – that is, P(X)=1. A probability space is a measure space with a probability measure.


### [Affine Space](https://en.wikipedia.org/wiki/Affine_space)
<img width="1073" alt="Screen Shot 2022-12-28 at 10 03 57 AM" src="https://user-images.githubusercontent.com/36484215/209847134-ee2e37ee-3611-4855-8576-602114afc5dd.png">

### Euclidean Space
https://en.wikipedia.org/wiki/Euclidean_space#Motivation_of_the_modern_definition

### Topological space
- A topological space is a set whose elements are called points, along with an additional structure called a topology, which can be defined as a set of neighbourhoods for each point that satisfy some axioms formalizing the concept of closeness.
- Open sets: 1) In a metric space (a set along with a distance defined between any two points), an open set is a set that, along with every point P, contains all points that are sufficiently near to P (that is, all points whose distance to P is less than some value depending on P). 2) More generally, an open set is a member of a given collection of subsets of a given set

### Manifold 
- a manifold is a topological space that locally resembles Euclidean space near each point. More precisely, an n-dimensional manifold, or n-manifold for short, is a topological space with the property that each point has a neighborhood that is homeomorphic to an open subset of n-dimensional Euclidean space.

A function f: X to Y between two topological spaces is a homeomorphism if it has the following properties:
- f is a bijection (one-to-one and onto),
- f is continuous,
- the inverse function f^-1 is continuous (f is an open mapping).

-------------------------------------------------------------------------------------------------------------------------------

# Function/Mapping
A map or mapping is a function in its general sense.
## Function
A function from a set X to a set Y assigns to each element of X exactly one element of Y.

## Linear Mapping （Linear Operator)
<img width="1091" alt="Screen Shot 2022-12-28 at 1 24 17 PM" src="https://user-images.githubusercontent.com/36484215/209868110-d10b668f-37c4-4b8e-ba1f-40b0e6ebc2a9.png">

- A linear mapping is usually represented by a matrix. 
- A matrix is just some numbers but in this case it can represent a function. A n by 1 or 1 by n matrix usually represents a vector.
- "Matrix multiplication was first described by the French mathematician Jacques Philippe Marie Binet in 1812, to represent the composition of linear maps that are represented by matrices."
- A linear map L is often written as L[⋅] to refer to the function itself rather than function evaluated at a particular point.

## Homomorphism
Homomorphisms of vector spaces are also called linear maps

<img width="1245" alt="Screen Shot 2022-12-28 at 1 19 11 PM" src="https://user-images.githubusercontent.com/36484215/209867613-878b666e-e178-4a60-b896-b57e173638be.png">

-------------------------------
# Geometry 
Geometry (from Ancient Greek γεωμετρία (geōmetría) 'land measurement'; from γῆ (gê) 'earth, land', and μέτρον (métron) 'a measure') is, with arithmetic, one of the oldest branches of mathematics. It is concerned with properties of space such as the distance, shape, size, and relative position of figures.

Until the 19th century, geometry was almost exclusively devoted to Euclidean geometry, which includes the notions of point, line, plane, distance, angle, surface, and curve, as fundamental concepts.

> Arithmetic (from Ancient Greek ἀριθμός (arithmós) 'number', and τική [τέχνη] (tikḗ [tékhnē]) 'art, craft') is an elementary part of mathematics that consists of the study of the properties of the traditional operations on numbers—addition, subtraction, multiplication, division, exponentiation, and extraction of roots.

--------------------------------------------------

# Calculus & Optimization
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

### Newton's Method
- Use second order derivative to approximate f(x+t)≈f(x)+f'(x)t+f''(x)t²/2
- Find minimum of this approximation by setting gradient to 0: f'(x)+f''(x)t=0
- t=-f'(x)/f''(x) and setting x' to x+t gives minimum to this approximation
- iteratively apply this until convergence

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


--------------------------------------------------

# Variational Calculus
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

![](/images/gateaux1.jpeg)
![](/images/gateaux2.jpeg)
<img width="795" alt="Screen Shot 2022-12-30 at 7 50 57 PM" src="https://user-images.githubusercontent.com/36484215/210122814-29bd3244-3179-4a50-a232-8164bf264183.png">

-------------------------------------------------------------------------------------------------------------------------------

# Linear Algebra
## Rank
The column rank of A is the dimension of the column space of A, while the row rank of A is the dimension of the row space of A.

Column rank and the row rank are always equal

A matrix is said to have full rank if its rank equals the largest possible for a matrix of the same dimensions, which is the lesser of the number of rows and columns.

rank(AB) ≤ min(rank(A), rank(B))

### Rank-Nullity Theorem
Dim(Null space of A) + Dim(Column Space of A) = Number of Columns of A

## Eigen
Sum(eigenvalues) = trace

### Diagonalization
A=XΛX⁻¹. This means A as a linear transformation has the effect of moving its eigen basis λ times. In transformation Ab, X⁻¹b gives coordinates of b in X (eigen) basis. Λ stretches each basis. X transform b back to original basis.

#### Condition
Have n linearly independent eigenvectors. This follows the definition that in A=XΛX⁻¹ X must be invertible. Another way is to check if the algebraic multiplicity of each eigenvalue equals its geometric multiplicity. e.g. if eigenvalue λ appears twice (meaning there's a term when solving eigenvalues that involves (x-λ)²) it's corresponding eigenvectors must span 2d (two independent vectors).

#### Orthonormal Diagonalization
Orthonormal (orthogonal) matrices are matrices in which the column vectors form an orthonormal set (each column vector has length one and is orthogonal to all the other colum vectors).

Symmetric matrices have orthonormal diagonalization

### Differential Equation


## Positive Definite Matrix
[Summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/6e1f793f6c25fd39e002c100e278bf1b_MIT18_06SCF11_Ses3.4sum.pdf)

When x^TAx > 0, observe that the function it represents is convex since its second derivative is 2A which is positive definite. 

### Where to get
Most matrices are nxm, but when we do projection, we often get A^TA which is square and symmetric and positive definite (if full rank).

### Eigenvalues and Definiteness 
For x^TAx, if we use eigenvector of A as x, we have λx^Tx. We can see that the resulting sign is defined by λ since x^Tx is positive except at 0. So if an eigenvector of A is negative, the corresponding eigenvector, when used as x here, gives negative result. Conversely, if we have all eigenvalues to be positive, the corresponding eigenvectors give all positive results.

For more general cases, replace A with XΛX⁻¹ and write as (x^TX)Λ(X⁻¹x). (x^TX)^T=X^Tx. So for our previous observation to hold true for all x, X^T must equal X⁻¹. This is true when A is symmetric. 

### Extrema & Hessian
When first derivative of a function is 0 and second derivative is positive, we have a minimum. For multivariable functions, the condition for second derivative matrix is positive definite instead of all positive entries. This is because, let Δx be a small nudge in some direction, then HΔx gives a small change of gradient and this times Δx again gives a small change of function output in that direction. Thus if H is PD, ΔxHΔx always give positive change no matter what direction you nudge. Conversely, negative definite Hessian when gradient is 0 implies maxima.

This is also why the test involves fxx*fyy-2fxy (determinant). If det < 0, then we know for sure one eigenvalue is negative and the other is positive and this is a saddle point. If det > 0, it might be both eigenvalues are positive or both negative. Then since product(eigenvalues)=det, we only need to know either fxx or fyy to know the other.

## Similar Matrices
Def: A=M⁻¹BM. If A and B similar, they have same eigenvalues and same number of eigenvectors.

M can be seen as change of basis matrix. The effect of M is to first change from A space into B space and M⁻¹ converts it back. If we write A and B both as XΛX⁻¹, observe that X and X⁻¹ are also only changing basis. So The actual effect of the transformation is controlled by Λ.

Note that to make similar matrices you just need any matrix and multiply any invertible matrix and its inverse on each side.

If A=M⁻¹BM then B=MAM⁻¹=(M⁻¹)⁻¹AM⁻¹=U⁻¹AU.

### Jordan Form
-However, if you choose a *non diagonalizable matrix* to start with, e.g. [[4,1],[0,4]] notice that its eigenvalues are 4 and 4 but the diagonal matrix [[4,0],[0,4]] itself is not similar to it. [[4,1],[0,4]] is a jordan form and its family are [[4,N],[0,4]] while [[4,0],[0,4]] is a family by itself.

> Proof: M⁻¹λIM=λI so diagonal matrix with identical diagonal terms are similar only to itself. If a matrix with identical eigenvalues λ but has different number of eigenvectors is similar to λI, then A=M⁻¹λIM. But M⁻¹λIM=λI has n eigenvectors and is a contradiction.

Note that any matrix of any family of Jordan forms is non diagonalizable. However, Jordan form can diagonalize them as nearly as it could. 

An implication is that a matrix with all identical eigenvalues which is not multiple of identity is not diagonalizable and thus not in the family of that eigenvalue times identity. 

### Jordan's Theorem
every square matrix A is similar to a Jordan matrix J, with Jordan blocks on the diagonal

## SVD
A=XΛX^T where X is orthonormal works only for symmetric square matrix. Want something similar for any matrix. AX=ΛX^T transforms an orthonormal basis of row space of A, i.e. X^T, to an orthonormal basis of column space of A with a multiplier. Since A is diagonalizable, row and column space are the same (?).

For a general matrix A, we want an orthonormal basis of row space of A, denoted V, that can be transformed to a stretched orthonormal basis of column space of A, denoted U. AV=ΣU, or A=UΣV^T.

The effect of Ax is then equal to UΣV^Tx or UΣV⁻¹x. x is first projected to an orthonormal basis of row space of A, stretched at each dimension sigma times and projected to column space of A. 

![](/images/svd.png)

### Non Full Rank Case
For null space of A we have some v where Av=0 or Av=0u. This is easily incorporated to SVD where some sigma in the diagonal matrix are 0. Note that u can also be 0 but we complete U to be an orthonormal basis.

### How to Compute
Observe that for any matrix A, AA^T is square, symmetric and positive semidefinite. So AA^T=VSV⁻¹. Similarly A^TA=USU⁻¹. (eigenvalue of AB is the same as of BA since A(BA)v=λAv=(AB)Av=>ABv=λv)

### Dimension
Normally for mxn matrix A we have U: mxn, Σ: nxn, V: nxn but sometimes U is mxm and Σ mxn. Some part of U in latter case represent an orthonormal basis for left null space of A.

### PCA
> Stats Note: Covariance of X and Y = E[(X-E[X])(Y-E[Y])]=E[XY]-E[X]E[Y]. When X and Y have 0 mean, cov=E[XY]

Given data X of nxp, compute covariance matrix=X^TX/(n-1). 

## Pseudoinverse
- Full column rank: A^TA is full rank and invertible. (A^TA)⁻¹A^TA=I, so (A^TA)⁻¹A^T is left inverse of A.
- Full row rank: AA^T is full rank and invertible. AA^T(AA^T)⁻¹=I, so A^T(AA^T)⁻¹ is right inverse of A.
- Any matrix: the mapping from row space to column space is one to one. 

1. SVD: invert the "good" part of Σ -> Σ⁺. 

-------------------------------------------------------------------------------------------------------------------------------

# Fourier
### Overview
https://math.stackexchange.com/questions/1020231/fourier-series-of-real-valued-functions
- Express any function as combination of simpler functions. Here these functions are sinusoids of different frequencies and phases. f(x)=ΣᵢAᵢsin(2πix+ϕᵢ)
- Sin and cos are related by phase (sin(2πix+ϕᵢ)=cos(2πix+ϕᵢ+π/2)). So sinusoids of different frequencies and phases can be expressed as sin and cos of different frequencies. f(x)=a₀/2+Σᵢaᵢcos(2πix)+bᵢsin(2πix)
- Sin(2πix) and cos(2πix) are orthogonal. so sin and cos of different frequencies form an orthonormal basis for functions. Dot product of f(x) and sin or cos gives the magnitude/coordinate of the function that particular base. Here the magnitude (aᵢ and bᵢ) is found by integrating f(x)sin(nx) along common period.
- Use eⁱⁿˣ to express a⋅cos(nx)+b⋅sin(nx). Since eⁱⁿˣ=cos(nx)+i⋅sin(nx), there are imaginary parts for the trigonometry functions. However, if we integrate from -L to L instead of 0 to L (L is common period), because e-ⁱⁿˣ=cos(nx)-i⋅sin(nx), we get conjugates that cancels out the imaginary parts. 
- So now we can write f(x) as Σₘ from -L to L Aₘ⋅eⁱmˣ where A is a complex number. Note that A an be computed by computing the dot product between f(x) and e⁻ⁱmˣ, so for real f, A has both real and imaginary parts, and A₋ᵢ, Aᵢ are conjugates, thus when translating to f(x)=a₀/2+Σᵢaᵢcos(2πix)+bᵢsin(2πix) this form, a and b are reals.  

### Calculate F(ω) Directly on Fourier Series
<img width="400" alt="Screen Shot 2023-01-29 at 3 14 35 PM" src="https://user-images.githubusercontent.com/69565972/215355999-5197b36c-064e-486e-b02e-759b3aa62820.png">
<img width="400" alt="Screen Shot 2023-01-29 at 3 14 42 PM" src="https://user-images.githubusercontent.com/69565972/215356002-6570587f-e56e-423c-927c-5d91c4181963.png">

### Calculate F(ω) with Complex Exponential 
https://see.stanford.edu/Course/EE261/137 (last 10 mins proves A=f⋅e⁻ⁱπˣ from f=ΣAeⁱπˣ)

<img width="400" alt="Screen Shot 2023-01-29 at 3 15 52 PM" src="https://user-images.githubusercontent.com/69565972/215356043-01dcea2d-2a95-433d-8c95-ba4c5ee73ec5.png">

### Asin(nx+ϕ) from Psin(nx)+Qcos(nx)
<img width="300" alt="Screen Shot 2023-01-29 at 3 16 25 PM" src="https://user-images.githubusercontent.com/69565972/215356064-0e94d617-770f-4093-b2e9-aa5e51d0997d.png">

### Frequency Convolution Theorem 
https://www.tutorialspoint.com/frequency-convolution-theorem


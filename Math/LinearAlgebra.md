
# Linear Algebra
## Rank
- The column rank of A is the dimension of the column space of A, while the row rank of A is the dimension of the row space of A.
- Column rank and the row rank are always equal
- A matrix is said to have full rank if its rank equals the largest possible for a matrix of the same dimensions, which is the lesser of the number of rows and columns. i.e. rank(AB) ≤ min(rank(A), rank(B))

### Column, Row, Left and Right Null Space 

### Rank-Nullity Theorem
Dim(Null space of A) + Dim(Column Space of A) = Number of Columns of A

## Eigen
### Eigenvector
v is an eigenvector of linear transformation T iff T(v)=λv

Sum(eigenvalues) = trace
Product(eigenvalues) = determinant

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

When x^TAx > 0, observe that the function f(x)= x^TAx is convex since its second derivative is 2A which is positive definite. 

### Where to get
Most matrices are nxm, but when we do projection, we often get A^TA which is square and symmetric and positive definite (if full rank).

### Eigenvalues and Definiteness 
For $x^TAx$, if we use eigenvector of A as x, we have $λx^Tx$. We can see that the resulting sign is defined by λ since $x^Tx$ is positive except at 0. So if an eigenvalue of A is negative, the corresponding eigenvector, when used as x here, gives negative result. Conversely, if we have all eigenvalues to be positive, the corresponding eigenvectors give all positive results.

For more general cases, replace A with $XΛX⁻¹$ and write $x^TAx$ as $(x^TX)Λ(X⁻¹x)$. $(x^TX)^T=X^Tx$. So for our previous observation to hold true for all x, $X^T$ must equal $X⁻¹$. This is true when A is symmetric. 

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
- Full column rank: $A^TA$ is full rank and invertible. $(A^TA)⁻¹A^TA=I$, so $(A^TA)⁻¹A^T$ is left inverse of A.
- Full row rank: $AA^T$ is full rank and invertible. $AA^T(AA^T)⁻¹=I$, so $A^T(AA^T)⁻¹$ is right inverse of A.
- Any matrix: the mapping from row space to column space is one to one. 

1. SVD: invert the "good" part of Σ -> Σ⁺. 

# Orthogonal Complements
V Perpendicular to a subspace X. $\vec{v}• \vec{x} = 0$for every x in X.

## Theorems
- Every member of null space of A is orthogonal complement to every member of row space of A, $C(A^T)^\perp=N(A)$
- $Dim(V) + Dim(V^\perp) = n, V \in R^n$
- $(V^\perp)^\perp=V$

## Base changing with orthogonal bases:

M = {v1, v2, ..., vn}, S = Standard basis

$[\vec{x}]_S,[\vec{x}]_M=\begin{bmatrix}
[\vec{x}]_M•v_1/|v_1|\\
[\vec{x}]_M•v_2/|v_2|\\
...\\
[\vec{x}]_M•v_n/|v_n|\\
\end{bmatrix}$


# Orthonormal Bases
A = {v1, v2, ..., vn}
Definition: A is an orthonormal basis if vi•vj = 0 for i≠j, vi•vi = 1. 

All vectors are orthogonal to each other and are normalized.

## Base changing with orthogonal bases:

M = {v1, v2, ..., vn}, S = Standard basis

$[\vec{x}]_S,[\vec{x}]_M=\begin{bmatrix}
[\vec{x}]_M•v_1\\
[\vec{x}]_M•v_2\\
...\\
[\vec{x}]_M•v_n\\
\end{bmatrix}$


> Orthonormal transformation preserves length (pure rotation)

## Inverse
$C^{-1}=C^T$

# Projection
## Why project?
Ax = b may have no solution. The vector Ax is always in the column space of A, and b is unlikely to be in the column space.
So, we project b onto a vector p in the column space of A and solve Axˆ = p. 

## General Case
Projection for any b on A={v1,v2,...,vn}:

Projection of b minus b (e) is perpendicular to A, thus:

$
\begin{aligned}
A^T(b − A\hat{x})&=0 \\
A^Tb&=A^TA\hat{x},(Normal\ Equation) \\
\hat{x}&=\frac{A^Tb}{A^TA} \\
&=(A^TA)^{-1}A^Tb \\
=>projA(\vec{b})&=A(A^TA)^{-1}A^T\vec{b}
\end{aligned}$

More:
https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/least-squares-determinants-and-eigenvalues/projections-onto-subspaces/MIT18_06SCF11_Ses2.2sum.pdf 

## Orthogonal Projection
No different from general case

## Orthonormal Projection
V is a subspace of Rn. A is orthonormal basis for V.
For any vector x in Rn, x=projA(x)+w.

Projection of x on any vector v in A is x•v*v.

$A^TA=\begin{bmatrix}
1 & v_1•v_2 & ... & v_1•v_n \\
v_1•v_2 & 1 & ... & v_2•v_n \\
...\\
v_1•v_n & ... & ... & 1\\
\end{bmatrix}$

When v are orthogonal to each other, $A^TA=I$

$projA(\vec{x})=AA^T\vec{x}$

This can be explained as adding together projections of x on each columns of A. A transpose x gives the length of projection on each base and this times A gives the vector.


## Gram-Schmidt Process
Purpose: Find orthonormal basis A for any subspace spanned by V={v1,v2,...vn}.

Idea: Use one vector from original basis vectors to get the first normal vector, then project another vector onto the normalized vector. Normalize the second vector minus the projection to get the second normal vector. Repeat the process to get all orthonormal vectors. 

$\vec{a}_n=normalize(\vec{v}_n- \sum_{j=1}^{n-1} (\vec{v}_n•\vec{a}_j)\vec{a}_j)$

## Least Square Solutions
 $\hat{x} = (A^TA)^{-1}A^Tb$
 

# Quadratic Form

## Optimization

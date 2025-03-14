# Geometry


[CMU graphics course](https://youtu.be/MakhXtIX2YM)

## Implicit vs Explicit
### Definitions
- Implicit representation of geometry can be described a function f. All points satisfying f(x,y,z)=0 belong to the shape.
- Explicit representation of geometry is the image of a function f: R2->R3;(u,v)->(x,y,z)
### Implicit Examples
- Algebraic surfaces: surface is zero set of polynomials in x,y,z
- Constructive solid geometry
- Blobby surfaces and blending distance functions
- Level set: methods above requires closed form which is impossible for complex shapes. So store a grid of values approximating a function 
- Fractals (Mandelbrot set)

### Explicit Examples
- Point cloud: most intuitive
- Polygon mesh: triangle/quad. can be seen as point cloud with defined interpolation
- Control points

### Compare
- Implicit representation is compact. Calculating distance is easy. But hard to sample points on surface (have to test points)
- Explicit representation means knowing every point already so sampling is easy. Other operations are more expensive

## Line & Surface
### Bernstein Basis & Bezier Curve
recall that linear interpolation is f(t)=(1-t)f0+tf1. This can be seen as constructing f(t) with basis {1-t, t}, f0 and f1 are the coordinates of f(t). Similarly, we can construct higher order interpolations with non linear basis. The simplest one is {1, t, t^2,...}. We use an extension of basis {1-t, t} which when n=3 is {t^3, ,3t^2(1-t), 3t(1-t)^2, (1-t)^3}

<p float="left">
  <img width="300" alt="Screen Shot 2023-01-08 at 8 44 01 AM" src="https://user-images.githubusercontent.com/36484215/211202567-2a0bcd56-aee1-4727-9138-91f4d1b57c22.png">
  <img width="300" alt="Screen Shot 2023-01-08 at 8 45 38 AM" src="https://user-images.githubusercontent.com/36484215/211202653-0a4b90c6-7ecd-41fe-b7b7-62802e66e2ef.png">
  <img width="300" alt="Screen Shot 2023-01-08 at 8 47 41 AM" src="https://user-images.githubusercontent.com/36484215/211202743-1fcfb9eb-977a-4075-a223-f664407a20ac.png">
</p>

### Tensor Product & Bezier Patch
(f⊗g)(u,v)=f(u)g(v)

<img width="400" alt="Screen Shot 2023-01-08 at 9 03 03 AM" src="https://user-images.githubusercontent.com/36484215/211203560-76ab93a4-57cc-4a21-a945-99436b7915b1.png">

## Manifold
### Intuition
<img width="400" alt="Screen Shot 2023-01-08 at 1 50 04 PM" src="https://user-images.githubusercontent.com/36484215/211215908-60dc5ca3-7b2d-4fc0-8655-f6798f308e93.png">


## Storing Shapes in Computer
### Ideas
- Extending image grid to 3D is expensive, use surface instead.
- Surfaces are manifolds, which are well defined so easier to store.
- Our shapes are planes/triangles locally, so store all planes/triangles.
- We also want some operations to be fast (collapsing, clipping...) so use a structure with faster local querying.

### Methods
- Polygon soup: simplist, store coordinates of the 3 vertices of all faces (faces x 3 x 3)
- Adjacency list: 2 list, one for all vertices, one for all faces with reference to list 1
- Incidence matrix: 2 matrices. edges x vertices, 1 means this edge touches this vertex. faces x edges. Extremely big.
- Halfedge: linked list like. 
<img width="200" alt="Screen Shot 2023-01-08 at 1 59 38 PM" src="https://user-images.githubusercontent.com/36484215/211216301-56230103-ef7b-45a3-91d2-0c6d90126139.png">

### Storing Sparse Matrix
<img width="500" alt="Screen Shot 2023-01-08 at 1 58 56 PM" src="https://user-images.githubusercontent.com/36484215/211216267-9da215ed-ed89-492c-a088-68fb570223d6.png">


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
- T'(s)=θ'(s)[−sinθ(s)e1 + cos θ(s)e2]=κ(s)N(s). κ(s):= θ'(s), is the signed curvature. It means of how much of the normal is the curve changing its direction. You can construct a curve just with κ(s). 
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

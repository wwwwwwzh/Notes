# Math

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

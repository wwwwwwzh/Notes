
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
- Implicit representation is compact. Calculating distance is easy. But hard to sample points on surface
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

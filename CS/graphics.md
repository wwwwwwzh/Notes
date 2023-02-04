# Graphics
## Color and Radiometry
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

## BRDF
> Calculus Review: dx is h->h and dy is really f'(x(h))dx(h) or f'(x)dx. In multivariable calculus, df(xᵢ) means f'xᵢ(x)dxᵢ. df itself would be a vector of gradients. dy has same unit as y.
### Radiance and Irradiance
Irradiance can be computed by integrating radiance over Ω. 
<img width="200" alt="Screen Shot 2022-12-21 at 8 32 46 PM" src="https://user-images.githubusercontent.com/36484215/209056734-01c365f1-13d9-46bb-887b-ee8e96526326.png">

### BRDF
The relationship can be defined as a constant for every (ωi,ωo,p) based on the linearity assumption from geometric optics: the reflected differential radiance is proportional to the irradiance. 

<img width="700" alt="Screen Shot 2022-12-22 at 10 22 41 AM" src="https://user-images.githubusercontent.com/36484215/209201522-c2f04a6b-ee4f-4e5f-9d51-dd17c53d4c4a.png">


### BRDF, BTDF, BSDF, BSSRDF
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

### Rendering Equation
<img width="500" alt="Screen Shot 2022-12-22 at 12 26 56 PM" src="https://user-images.githubusercontent.com/36484215/209220242-7de61b62-a02c-4247-a8dd-832e8d09507b.png">

tr(p,w) is the transport function that returns the point hit by a ray from p with direction w.

<img width="500" alt="Screen Shot 2022-12-22 at 12 30 50 PM" src="https://user-images.githubusercontent.com/36484215/209220806-22332cb9-225e-4634-8659-5bf251028796.png">

I hope I can understand the later part of the slides
### Microfacet
https://www.pbr-book.org/3ed-2018/Reflection_Models/Microfacet_Models

### BRDF in Modern Renderer
- Albedo Map: diffuse
- Normal Map: 
- Specularity Map: amount of light reflected
- Glossiness Map: "roughness near reflection direction"
- Roughness Map: microfacet related
- Metalness Map: metallic properties as exhibited by real physical materials

## Volume Scattering
- Absorption: the reduction in radiance due to the conversion of light to another form of energy, such as heat
- Emission: radiance that is added to the environment from luminous particles
- Scattering: radiance heading in one direction that is scattered to other directions due to collisions with particles


<img width="400" alt="Screen Shot 2022-12-22 at 1 55 37 PM" src="https://user-images.githubusercontent.com/36484215/209232735-d70fb620-d38d-463d-9565-39e261908301.png">

Part of the radiation can pass the object unchanged, which is called transmission, part of it can change direction without a change in energy/frequency, which is called scattering, and part of it can disappear with the energy transferred to the object, which is called absorption. Both scattering and absorption remove radiation from the beam and are together called extinction.

<img width="500" alt="Screen Shot 2022-12-22 at 1 55 17 PM" src="https://user-images.githubusercontent.com/36484215/209232685-741b8794-7f22-409b-beed-5045a95c5ebf.png">


## Environment Map 
Assumption is all light infinite far. Reflection map->diffuse map. box vs sphere map.

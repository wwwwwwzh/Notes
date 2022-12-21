## 12.19
### sherical harmonic 

<img width="266" alt="Screen Shot 2022-12-19 at 4 43 09 PM" src="https://user-images.githubusercontent.com/36484215/208555184-85d131f8-bfdd-402f-924f-b145467e3f6e.png">

ω = (sinθ*cosφ,sinθ*sinφ,cosθ)

basically a basis for sherical functions like fourier basis

### projection matrix (reviewing Roni's slides)
<img width="530" alt="Screen Shot 2022-12-19 at 5 24 44 PM" src="https://user-images.githubusercontent.com/36484215/208559444-a1df7cd3-3423-4590-8fa1-64dd07c854de.png">

Note that image plane doesn't change size

<img width="500" alt="focal length and ratio" src="https://user-images.githubusercontent.com/36484215/208560712-78b6cd10-949e-446a-8d1b-c3646280e610.jpg">

Note that when f→∞, this becomes orthographical projection and ratio will be 2.

## 12.20 (reading pbr book)
### Color and Radiometry
https://www.pbr-book.org/3ed-2018/Color_and_Radiometry/Radiometry
https://computergraphics.stackexchange.com/questions/7503/what-is-the-difference-between-radiance-and-irradiance-in-brdf

- Q (joule J) is energy. A photon at wavelength λ carries energy hc/λ
- ϕ (J/s or watt W) is radiant flux, also known as power, is the total amount of energy passing through a surface or region of space per unit time
- E (W/m^2) is average density of power over the area A: ϕ/A. This quantity is either irradiance (E), the area density of flux arriving at a surface, or radiant exitance (M), the area density of flux leaving a surface. 
- Solid angle, radian, and steradian (sr). One sr is how much angle 1 unit area covers a unit sphere, like radian is the angle coverd by one unit length on a unit circle. In spherical coordinate, you can view solid angle as θ⋅ϕ or just a direction. Differential solid angle dw can be seen as area on unit sphere. Integrating solid angle over unit sphere is written as $$\int_\Omega d\omega$$ but is really just $$\int_0^{2\pi}\int_0^{\pi} \sin\theta d\theta d\phi$$ The entire sphere subtends a solid angle of 4πsr, so sometimes integration is written as $$\int_{4\pi} f(x) d\omega$$
- Ω is set of directions over unit sphere
- I (W/sr) is intensity, here angular density of emitted power. Intensity describes the directional distribution of light, but it is only meaningful for point light sources.
- L (W/sr/m^2) is radiance, is flux density per unit area, per unit solid angle. E acounts for only spatial distribution of power, not directional. L can be defined as dE/dω where the area used in E is in the same direction as ω. L can also be defined as dϕ/dωdA⟂ where dA⟂ is dA projected along the direction of dω. Try understanding this with surfaces illuminated by many directional lights.

### BRDF
#### Radiance and Irradiance

#### BRDF, BTDF, BSDF, BSSRDF
BRDF is the upper hemisphere, BTDF is lower. BRDF+BTDF=BSDF

BRDF for a perfect mirror (reflection) and BTDF for perfect material separation surface (refraction) is a delta function

BSDF (note the S^2):

<img width="600" alt="Screen Shot 2022-12-20 at 10 17 41 AM" src="https://user-images.githubusercontent.com/36484215/208737610-a207eb4a-c3a4-4845-ac69-8c277a0f2a07.png">

BSSRDF:

<img width="717" alt="Screen Shot 2022-12-20 at 10 30 14 AM" src="https://user-images.githubusercontent.com/36484215/208740005-257de391-aee3-4e2f-9cb3-7e9ec331c9ca.png">

It seems that BSDF is as physically based as BSSRDF but BSSRDF seems more natrual.

Can use fourier basis for BRDF.

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

### Environment Map 
Assumption is all light infinite far. Reflection map->diffuse map. box vs sphere map.


### Others
[Mach bands](https://en.wikipedia.org/wiki/Mach_bands)

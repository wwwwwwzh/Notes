- **symmetry** of a shape is a **rigid transformation** (functions) that maps itself back. the more symmetries an object has, the more “symmetric” we think it is.
- These symmetries (of I and 0-1 doublets) as rigid transformations and mod2 additions, when combined, show certain algebraic structures that are identical, therefore we'll try grouping these symmetries ![](/images/I-group.svg) ![](/images/01-group.svg)
- note that since symmetries are just functions, we can have symmetries of symmetriies. For example, the identity symmetry of any above symmetries output themselves
- we are interested in the properties of our system of symmetries
    - identity: There is a symmetry I with the property thatI\*S=S\*I=S for all symmetries
    - inverse Given any symmetry S, there is a symmetry T such thatS\*T=T\*S=I.
    - commutativity and commutativity doesn’t always hold in our systems of symmetries
    - Associativity does hold
- > Nineteenth century mathematicians discovered many examples of algebraic systems satisfying these three axioms, and realized that instead of studying all of these systems separately, we could look at systems that satisfy these axioms in the abstract.
- group: an abstract object with a “multiplication operation” defined, that satisfies the three axioms.

Symmetries of 3-d object
- 9 type I rotations (face to face)
- 8 type II rotations (corner to corner)
- 6 type III rotations (edge to edge)
- *proof that the 24 rotational symmetries are all there are:  A cube has four diagonals. Every rotation results in a distinct permutations of the diagonals. 4!=24.
- 24 reflections

A **group** is a set G, together with a binary function *:G×G→G satisfying the following four axioms 
- (Closure) For any elements g and h in G, the result g∗h is also in G 
- (Identity) There is an element e∈G such that, for all g∈G, e∗g=g and g∗e=g
- (Inverses) For each g∈G, there is an element of G denoted $g^{−1}$ that satisfies $g*g^{−1}=e$ and $g^{−1}*g=e$
- (Associativity) For any elements g, h and j∈G, we have (g∗h)∗j=g∗(h∗j).

- now we know the set of symmetries on I is a group with composition operation
- **dihedral group** Dn: set of symmetries on a regular n-gon (n reflections and n rotations) with composition operation
- **permutation/symmetric group** Sn: set of permutations on the set {1,2,...,n} under the composition operation. For example, all ways to shuffle a deck of cards is S52
- **cyclic group** Zn: set of functions (element-wise mod n add) on {0,1,...n-1} under operation of addition mod n. Rotations on n-gon is also Zn.

- **Order** of element g: smallest k for which g^k=e
- Exampels:
    - rotations on equilateral triangle: k=3, reflections: k=2
    - Quaternion: {±1,±i,±j,±k} forms a group with eight elements using multiplication (ijk=-1), known as the quaternion group Q8.
    - 12 music notes of a chromatic scale
- An **isomorphism** (equal shape) between two groups is a bijective map preserving the group operations.
- Examples:
    - The aforementioned symmetries of I and mod2 addition are Klein groups.
    - Z12 is isomorphic to rotations on regular docecadron
    - {±1,±i} is isomorphic to the 4 matrices
- **Subgroup**: Let G be a group. A subset H⊆G is a subgroup if it forms a group under the multiplication operation alread defined for G.
- If G and H are groups, then G×H, the **Cartesian product**, is naturally a group, under the operation (g,h)\*(g',h')=(g\*g',h\*h'). eg. S3 x S4 is a subgroup of S7
- Lagrange's theorem says that if G is a finite group, and H is a subgroup of G, then the size of H is a divisor of the size of G. 
- Coset: if G is R3 and H is the xy-plane, the cosets are all the planes paralle to the xy-plane. It turns out these cosets are all the same size, one of which is H itself, and they partition G. Lagrange's theorem follows.

- Abelian group: group that commutes


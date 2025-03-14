Measuring a spin
- we want to measure something that has either +1 or -1 state, just like a coin. But the measurement affects the state and different measurements give different state measure.
- The ﬁrst interaction with the apparatus A prepares the system in one of the two states. Subsequent experiments conﬁrm that state. So far, there is no diﬀerence between classical and quantum physics.
- if we prepares the spin in one state, and turn the apparatus up side down, we measure the opposite state. The fact that we turned the apparatus in space implies that the state might also be associated with direction in space. The easiest explanation is that the state is a vector denoting space and the measurement gives component of the state vector along its orientation
- to test this, we prepare the spin in the up state and rotate the apparatus clockwise so it aligns with the horizonal axis. We expect 0. But it gives +1 or -1 randomly. We could say that the device is only capable of producing the 2 numbers and the alignment on x axis is not infinitely precise, so sometimes it's more aligned to up and sometimes down. But after the horizontal measurement, we can rotate A back to upright position and it will not always measure +1. This means that the **measurement changes the spin**. As for whether the measurement is really random, we could say that our alignment is not precise, but we can repeat the experiment along any direction and the result will always be random. This means **quantum mechanical systems are truely random**.
- More interestingly, if we go back to horizonal measurement after the up preparation, we find that the expected measurement is 0. in fact, if we rotate A any angle theta after up preparation and measure it, the result is statistically biased so that the average value is cos θ.
- conclusion on this observation: If we begin with A oriented along m (unit vector) and conﬁrm that σ = +1, then subsequent measurement with A oriented along n gives the statistical result 〈 σ 〉 = n·m.

Axioms
- For a classical system, the space of states is a set (the set of possible states), and the logic of classical physics is Boolean. In quantum mechanics, boolean algebra will not hold. This is very surprising because boolean logic has been a logic used to give "truth", which is the foundation of everything. 
- Boolean operator OR is symetric. We test it on the spin. let A be the proposition that sigma x is 1 and B be sigma z is 1. We can test is either is true separately. But if test A or B, then the order of measurement affects the result since measurement changes the state. So OR is not symmetric here.
- As for AND. (A and B) is not conﬁrmable because the second piece of the experiment interferes with the possibility of conﬁrming the ﬁrst piece.
- > note that the inability to know A and B is an example of uncertainty principle
- The space of states of a quantum system is not a mathematical set; it is a complex vector space. The main difference is the closure properties, the addition operator and various properties of complex numbers. 

Brackets
- In quntum mechanics, elements of a vector space is called a ket and represented as columns
- bra is the an element of the complex conjugate vector space 

quantum state
- knowing a quantum state means knowing as much as can be known about how the system was prepared. The obvious question to ask is whether the unpredictability is due to an incompleteness in what we call a quantum state.
- when we measure the state with apparatus and read the +1 or -1, that's all we can know, or all there is about the state
- we want to build a representation of a quantum state given our observations of the quantum behaviors. Why we use vector space to represent the space is an interesting history worthy of a note of its own
- the current behavior of the spin necessiates a 2d compelx vector representation based on some group theory of rotation (search so, su and double covering)
- define up-down, left-right, in-out as basis (each pair is a basis).
- use column vector to represent the vectors

Foundamental theoreum
- 4 principles
    1. 
    2.

- observable quantities are equal to their own complex conjugates, ie, they are real. As a consequence, quantum mechanical observables are represented by hermitian operators. 

Spin Operator
- Pauli matrices: $\sigma_1 = \begin{pmatrix} 0 ; 1 \\ 1 ; 0 \end{pmatrix},\quad\\
\sigma_2 = \begin{pmatrix} 0 ; -i \\ i ; 0 \end{pmatrix},\quad \\
\sigma_3 = \begin{pmatrix} 1 ; 0 \\ 0 ; -1 \end{pmatrix}.$
- Together with the identity matrix, they are also the quaternions. If you multiply each by i and denote by q1,q2,q3, you'll get q1q2=-q3 like ijk=-1

Dynamics
> Classical determinism allows us to predict the results of experiments. The quantum evolution of states allows us to compute the probabilities of the outcomes of later experiments.

> The average, or expectation value, of an observable is the closest thing in quantum mechanics to a classical value.
- U(t): time develop operator: |Ψ(t)〉 = U(t)|Ψ(0)〉.
- Because the states form a vector space, U must be linear operator (explanation needed). In addition, U must follow the minus first law and preserve distinction: 〈Ψ(0)|Φ(0)〉= 0 ->〈Ψ(t)|Φ(t)〉= 0 
- From these U must be unitary: U†U=I.  In physics lingo, time evolution is unitary.
- When studying incremental change, we make sure U(e) is close to I: $U(\epsilon) = I − i\epsilon H$. From unitarity: $U^{\dagger}(\epsilon) = I + i\epsilon H^{\dagger}$. Then H is a Hermitian operator, so it's an observable
- Generalized Schrodinger
- Expectation of a measurement
- Quantum dynamics is deterministic in terms of expectation of measurement

- commutator: LM-ML=[L,M]=-[M,L]




2 spins
- 2 observables, L and M, to describe the state. Do not think about matrices and columns yet.
- when we measure the state of the 2 spins, the resulting state will be eigenvector for both L and M. We call it simultaneous eigenvector of L and M. L and M must commute, ie, [L,M]|state> = 0. [L,M]=0 iff L and M commute
- wave function as coefficients of orthonormal basis
- represent any Hermitian matrix L as combination of Pauli and identity matrices: $L = aσ_x+ bσ_y+ cσ_z+ dI$
- commutator of any two of pauli matrices is the third matrix times 2i, so Pauli matrices don't commute



Tensor Product
- tensor product (of V and W) is a vector space denoted V⊗W where there exists a function f st each (v,w) pair can be bilinearly mapped to element of V⊗W, ie, f(v,w)=v⊗w, or f: V X W -> V⊗W. If Bv and Bw are sets of basis for V and W, basis for V⊗W is all bv⊗bw where bv is element of Bv 


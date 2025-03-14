
# Analysis I
> The construction of number systems in this book is not complete. It's possible to construct natural numbers with Peano axioms and we can either postulate that such a system exists because it's intuitively linked to the physical world, or invent some other logical arguments (note that the Peano axioms are themselves part of a larger logical construction so we could say some given logic are enough alone with the axioms). The standard way, which is also this book's way, is to invent sets and treat natural numbers as a set using an axiom, so that all subsequent treatment of number systems are all within set logic.

> Note that the goal of this volume is to build calculus from a set theoretic perspective, ie, building from just mathematical logic and set axioms, with a useful definition of the continuum of reals. It's possible to build an equivalent version of calculus completely free from sets, but with some other fundamental axioms, for example, axioms of geometry, where one needs to prove the continuum of points on a line. 

### Mathematical (propositional) logic
1. every well-formed statement is either true or false, but not both.
2. **Statements** are diﬀerent from **expressions**. Statements are true or false; expressions are a sequence of mathematical symbols which produces some mathematical object
3. One can make statements out of expressions by using **relations** such as =, <, ≥, ∈, ⊂, etc. or by using **properties** (such as “is prime”, “is continuous”, “is invertible”, etc.). Note that mathematical statements are allowed to contain English words.
4. One can make a **compound statement** from more primitive statements by using **logical connectives** such as and, or, not, if-then, if-and-only-if, and so forth.

- Structure of proof: Suppose A, then B.
- The above is **propositional or boolean logic**. Mathematical logic is boolean logic with **variable**.
- A variable is a symbol, such as n or x, which denotes a certain type of mathematical object. Usually, the type should be declared.
- the truth of a statement involving a variable may depend on the context of the statement.(This is a modiﬁcation of the rule for propositional logic, in which all statements have a deﬁnite truth value.)
- if we don't set the value of a variable, then it's a **free variable**. Statements with free variables might not have a deﬁnite truth value,
- if we do set the value of a variable, then it's a **bound variable**. Statements with only bound variables must have a deﬁnite truth value
- One can also turn a free variable into a bound variable by using the quantiﬁers **“for all”** or **“for some”**.
> In the history of logic, quantiﬁers were formally studied thousands of years before Boolean logic was. Indeed, Aristotlean logic, developed of course by Aristotle (384BC – 322BC) and his school, deals with objects, their properties, and quantiﬁers such as “for all” and “for some”. A typical line of reasoning (or syllogism) in Aristotlean logic goes like this: “All men are mortal. Socrates is a man. Hence, Socrates is mortal”. Aristotlean logic is a subset of mathematical logic, but is not as expressive because it lacks the concept of logical connectives such as and, or, or if-then (although “not” is allowed), and also lacks the concept of a binary relation such as = or <.
- **Equality** is a relation linking two objects x, y of the same type T. How equality is deﬁned depends on the class T of objects under consideration. However, for the purposes of logic we require that equality obeys the following four *axioms of equality*:
    1. (Reﬂexive axiom). Given any object x, we have x = x.
    2. (Symmetry axiom). Given any two objects x and y of the same type, if x = y, then y = x.
    3. (Transitive axiom). Given any three objects x, y, z of the same type, if x = y and y = z, then x = z.
    4. (Substitution axiom). Given any two objects x and y of the same type, if x = y, then f(x) = f(y) for all functions or operations f. Similarly, for any property P(x) depending on x, if x = y, then P(x) and P(y) are equivalent statements.
> we can deﬁne equality on a class of objects however we please, so long as it obeys the reﬂexive, symmetry, and transitive axioms, and is consistent with all other operations on the class of objects under discussion in the sense that the substitution axiom was true for all of those operations.

> **First-order logic** can quantify over individuals, but not over properties. That is, we can take an atomic sentence like Cube(b) and obtain a quantified sentence by replacing the name with a variable and attaching a quantifier: ∃x Cube(x)
> 
> However, we cannot do the same with the predicate. That is, the following expression: ∃P P(b) is not a sentence of first-order logic, but this is a legitimate sentence of **second-order logic**. Here, P is a predicate variable and is semantically a set of individuals.

### Natural numbers
- Axoim 1: 0 is a natural number
- Axoim 2: if n is a natural number, n++ is a natural number 
- Definition 2.1.3: we define 1 to be 0++, etc
- Axoim 3: n++ != 0 for all natural numebrs (to prevent wrap around. eg. N={0,1,2} where 2++=0)
- Axoim 4: if n++ = m++, n=m. (to prevent 2++=1)
- Axoim (schema) 5: Let P(n) be any property pertaining to a natural number n. Suppose that P(0) is true, and suppose that whenever P(n) is true, P(n++) is also true. Then P(n) is true for every natural number n. (to restrict N to contain only natural numbers)
- > Axiom 5 can be expressed as: ∀P[P(0)∧∀n(P(n)→P(S(n)))→∀nP(n)]. We prove that if we include some elements starting with T, which's not a successor to any natrual number, to the set of natrual numbers, then the set is not the set of natural numbers. Let T be an object such that $T \in n$ and $T \neq 0 ∧ \forall n(T \neq S(n))$. We first choose a P that hold the axiom: Let P(n) be "n is a natural number". P(0)∧∀n(P(n)→P(S(n))) is true thus P(n) is true for all natural numbers. Since we defined T to be a natural number, the axiom holds. Now let P(n) be "n is either 0 or is the successor of some number". P(0)∧∀n(P(n)→P(S(n))) is still true, so by the axiom T needs to be 0 or be a successor to some natural number. But this contradicts our definition, so this set is not the set of natural numbers. 
- > There is something about first or second order logic and axiom schema and i don't know which is my axiom 5. 

- > Axioms **define** a thing that you want to work with and taken to be true. It sets up the stage so you can say something about the thing is true or not. But since axioms define what a thing is, they also define what the thing is not. That's the logic used above. But usually we start by having this thing which is really the thing and ask "is 'T is a natural number' true". 
- Assumption 2.6. (Informal) There exists a number system N, whose elements we will call natural numbers, for which Axioms 2.1-2.5 are true. (this will not be proved)
- Note that this is a **postulate** which can almost be taken as the same as an axiom.
- > Remark, *logic is a very complicated* topic and these should serve as a teaser instead of a formal study of actual construction of natural numbers.
- Remark 2.1.13: No natural number is infinite. Proof: let P(n) be "n is finite". 0 is finite and for any finite number its successor is also finite, so all natural numbers are finite. 
- > Historically, the realization that numbers could be treated axiomatically is very recent, not much more than a hundred years old. Before then, numbers were generally understood to be inextricably connected to some external concept, such as counting the cardinality of a set, measuring the length of a line segment, or the mass of a physical object, etc. This worked reasonably well, until one was forced to move from one number system to another; for instance, understanding numbers in terms of counting beads, for instance, is great for conceptualizing the numbers 3 and 5, but doesn’t work so well for −3 or 1/3 or √2 or 3 + 4i.
- One consequence of the axioms is that we can now deﬁne sequences recursively: if for each n you are given fn: N->N, and a0=c, then there exists a unique sequence/function {an}
- recursive definition of addition 
- Deﬁnition 2.2.7 (Positive natural numbers). A natural number n is said to be positive iﬀ it is not equal to 0. 
- Deﬁnition 2.2.11 (**Ordering** of the natural numbers). Let n and m be natural numbers. We say that n is greater than or equal to m, and write n ≥ m or m ≤ n, iﬀ we have n = m + a for some natural number a. We say that n is strictly greater than m, and write n > m or m < n, iﬀ n ≥ m and n != m. 
- Proposition 2.2.13 (Trichotomy of order for natural numbers). Let a and b be natural numbers. Then exactly one of the following statements is true: a < b, a = b, or a > b.

- multiplication and exponentiation

### Set
- > there is an implicit "is in" predicate which isn't formally defined
- > some axioms here are redundant
- *Axiom 1*: a set is an object (we wait until axiom 7 to say that a natural number is also an object)
- Deﬁnition 3.1.4 (Equality of sets). Two sets A and B are equal, A = B, iﬀ every element of A is an element of B and vice versa.
- *Axiom 2 (empty set)*: there is a set called empty set, for which for all object x, x is not in this set
- Lemma 3.1.6: if there is a non empty set A, then we can find an object that is in A
- *Axiom 3 (singleton)*: for every object a, there is a set, whose only element is a. for every pair of objects a and b, there is a set, whose only elements are a and b.
- *Axiom 4 (pairwise union):* for any two sets A and B, there is a set A ∪ B, called the union of A and B, whose elements consists of all the elements which belong to A or B or both.
- Deﬁnition 3.1.15 (Subsets). Let A, B be sets. We say that A is a subset of B, denoted A ⊆ B, iﬀ every element of A is also an element of B. A is a proper subset of B, denoted A ⊊ B, if A ⊆ B and A = B.
- Proposition 3.1.18 (Sets are partially ordered by set inclusion). Let A, B, C be sets. If A ⊆ B and B ⊆ C then A ⊆ C. If A ⊆ B and B ⊆ A, then A = B. Finally, if A ⊊ B and B ⊊ C then A ⊊ C.
- > There is one important diﬀerence between the subset relation _ and the less than relation <. Given any two distinct natural numbers n, m, we know that one of them is smaller than the other (Proposition 2.2.13); however, given two distinct sets, it is not in general true that one of them is a subset of the other.
- *Axiom 5 (Axiom of speciﬁcation or axiom of separation)*. Let A be a set, and for each x ∈ A, let P(x) be a property pertaining to x (i.e., P(x) is either a true statement or a false statement). Then there exists a set, called { x ∈ A : P(x) is true } (or simply { x ∈ A : P(x) } for short), whose elements are precisely the elements x in A for which P(x) is true. 
- > Axiom 5 is used to create sets from larger sets
- Deﬁnition 3.1.23 (Intersections). The intersection S1 ∩ S2 of two sets is deﬁned to be the set S1 ∩ S2 := { x ∈ S1 : x ∈ S2 } .
- Proposition 3.1.28 (Sets form a **boolean algebra**). see p.42
- *Axiom 3.6 (Replacement)*. Let A be a set. For any object x ∈ A, and any object y, suppose we have a statement P(x, y) pertaining to x and y, such that for each x ∈ A there is at most one y for which P(x, y) is true. Then there exists a set {y : P(x, y) is true for some x ∈ A}, such that for any object z, z ∈{y : P(x, y) is true for some x ∈ A} ⇐⇒ P(x, z) is true for some x ∈ A.
- We often abbreviate a set of the form {y : y = f(x) for some x ∈ A} as {f(x) : x ∈ A} or {f(x)|x∈A}
- *Axiom 3.7 (**Infinity**)*. There exists a set N, whose elements are called natural numbers. 0 is in N. An object n++ assigned is to every natural number n in N, such that the Peano axioms (Axioms 2.1 - 2.5) hold.
- > this axiom guarantees the existence of an infinite set. From this infinite set, one can construct a set that satisfies the Peano axioms (or their equivalent formulations) to serve as the natural numbers. From this we see that numbers such as 3, 5, 7, etc. are indeed objects in set theory,
- *Axiom 3.8 (Universal speciﬁcation)*. (Dangerous!) Suppose for every object x we have a property P(x) pertaining to x (so that for every x, P(x) is either a true statement or a false statement). Then there exists a set { x : P(x) is true }
- > This axiom is also known as the axiom of comprehension. It asserts that every property corresponds to a set;
- *Axiom 3.9 (Regularity)*. If A is a non-empty set, then there is at least one element x of A which is either not a set, or is disjoint from A.
- *Axiom 3.10 (Power set axiom)*. Let X and Y be sets. Then there exists a set, denoted Y X, which consists of all the functions from X to Y , thus f ∈ Y X⇐⇒ (f is a function with domain X and range Y ).
- *Axiom 3.11 (Union)*. Let A be a set, all of whose elements are themselves sets. Then there exists a set ∪A whose elements are precisely those objects which are elements of the elements of A, thus for all objects x ∈ ∪ A ⇐⇒ (x ∈ S for some S ∈ A).
- A consequence of this axiom is that if one has some set I, and for every element α ∈ I we have some set A α, then we can form the union set $∪_{α∈I}A_α$ by deﬁning $∪ A_α:= ∪\{A α: α ∈ I\}$
- The axioms of set theory that we have introduced (Axioms 3.1-3.11, excluding the dangerous Axiom 3.8) are known as the Zermelo-Fraenkel axioms of set theory

### Functions
- Deﬁnition 3.3.1 (Functions). Let X, Y be sets, and let P(x, y) be a property pertaining to an object x ∈ X and an object y ∈ Y , such that *for every x ∈ X*, there is *exactly one y* ∈ Y for which P(x, y) is true (this is sometimes known as the vertical line test). Then we deﬁne the function f : X → Y deﬁned by P on the domain X and range Y to be the *object* which, given any input x ∈ X, assigns an output f(x) ∈ Y , deﬁned to be the unique object f(x) for which P(x, f(x)) is true.
- > Functions are also referred to as maps or transformations, They are also sometimes called morphisms, although to be more precise, a morphism refers to a more general class of object,
- a sequence of natural numbers a 0, a 1, a 2, a 3, . . . is, strictly speaking, a function from N to N, but is denoted by n ↦ a nrather than n ↦ a(n).
- We deﬁne the composition g ◦ f : X → Z of the two functions g and f to be the function deﬁned explicitly by the formula (g ◦ f)(x) := g(f(x)).
- injective (one to one)
- surjective (onto)
- bijective/invertible
- If f is bijective, then for every y ∈ Y , there is exactly one x such that f(x) = y. This value of x is denoted f −1(y); thus f−1 is a function from Y to X. We call f −1 the inverse of f.
- Deﬁnition 3.4.1 (Images of sets). If f : X → Y is a function from X to Y , and S is a set in X, we deﬁne f(S) to be the set f(S) := {f(x) : x ∈ S}; this set is a subset of Y , and is sometimes called the image of S under the map f. We sometimes call f(S) the forward image of S to distinguish it from the concept of the inverse image f −1(S) of S,
- Deﬁnition 3.4.4 (Inverse images). If U is a subset of Y , we deﬁne the set f −1(U) to be the set f −1(U) := {x ∈ X : f(x) ∈ U }.
- > f(f-1(y)) may not be y

### Cartesian Product
- Deﬁnition 3.5.1 (Ordered pair). If x and y are any objects (possibly equal), we deﬁne the ordered pair (x, y) to be a new *object*, consisting of x as its ﬁrst component and y as its second component. Two ordered pairs (x, y) and (x′, y′) are considered *equal* if and only if both their components match
- Deﬁnition 3.5.4 (**Cartesian product**). If X and Y are sets, then we deﬁne the Cartesian product X ×Y to be the set whose elements are ordered pairs, whose ﬁrst component lies in X and second component lies in Y, thus X × Y = {(x, y) : x ∈ X, y ∈ Y } or equivalently a ∈ (X × Y ) ⇐⇒ (a = (x, y) for some x ∈ X and y ∈ Y ).
- > I'm framing this as an axoim for convinience. It should be proved that cartesian product is actually a set from axiom of specification and power set axiom.
- Axiom 3.10 (*Power set axiom*). Let X and Y be sets. Then there exists a set, denoted Y^X, which consists of all the functions from X to Y , thus f ∈ Y^X⇐⇒ (f is a function with domain X and range Y ).
- Lemma 3.4.9. Let X be a set. Then the set { Y : Y is a subset of X} is a set.
- Remark 3.4.10. The set {Y : Y is a subset of X} is known as the **power set** of X and is denoted 2 X. For instance, if a, b, c are distinct objects, we have 2 {a,b,c}= {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}.
- Remark 3.5.10. An ordered n-tuple x 1, . . . , x n of objects is also called an ordered sequence of n elements, or a ﬁnite sequence for short.
- If n is a natural number, we often write X nas shorthand for the n-fold Cartesian product X n:= ∏ 1≤i≤nX. Thus X 1is essentially the same set as X (if we ignore the distinction between an object x and the 1-tuple (x)), while X 2is the Cartesian product X × X. The set X 0is a singleton set { () }
- ?? Lemma 3.5.12 (**Finite choice**). Let n ≥ 1 be a natural number, and for each natural number 1 ≤ i ≤ n, let X ibe a non-empty set. Then there exists an n-tuple (x i) 1≤i≤nsuch that x i∈ X ifor all 1 ≤ i ≤ n. In other words, if each X iis non-empty, then the set ∏ 1≤i≤nX iis also non-empty.

### Cardinality of sets
- the Peano axiom approach treats natural numbers more like ordinals than cardinals. We want an alternative definition of natural numbers as size of sets
- Deﬁnition 3.6.1 (*Equal cardinality*). We say that two sets X and Y have equal cardinality iﬀ there exists a bijection f : X → Y from X to Y . The notion of having equal cardinality is an equivalence relation.
- Remark 3.6.3. The fact that two sets have equal cardinality does not preclude one of the sets from containing the other. For instance, if X is the set of natural numbers and Y is the set of even natural numbers, then the map f : X → Y deﬁned by f(n) := 2n is a bijection from X to Y
- Deﬁnition 3.6.5. Let n be a natural number. A set X is said to have **cardinality** n, iﬀ it has equal cardinality with {i ∈ N : 1 ≤ i ≤ n}. We also say that X has n elements iﬀ it has cardinality n.
- Note that this does not say every set has cardinality of a natural number
- Deﬁnition 3.6.10 (Finite sets). A set is ﬁnite iﬀ it has cardinality n for some natural number n; otherwise, the set is called inﬁnite. If X is a ﬁnite set, we use #(X) to denote the cardinality of X.
- **Theorem 3.6.12**. The set of natural numbers N is inﬁnite. Proof: Suppose for sake of contradiction that the set of natural numbers N was ﬁnite, so it had some cardinality #(N) = n. Then there is a bijection f from {i ∈ N : 1 ≤ i ≤ n} to N. One can show that the sequence f(1), f(2), . . . , f(n) is bounded, or more precisely that there exists a natural number M such that f(i) ≤ M for all 1 ≤ i ≤ n (Exercise 3.6.3). But then the natural number M +1 is not equal to any of the f(i), contradicting the hypothesis that f is a bijection.
- Proposition 3.6.14 (Cardinal arithmetic).

### Integers
- Informally, the integers are what you can get by subtracting two natural numbers; for instance, 3 − 5 should be an integer, as should 6 − 2. This is not a complete deﬁnition of the integers, because (a) it doesn’t say when two diﬀerences are *equal* (for instance we should know why 3 − 5 is equal to 2 − 4, but is not equal to 1 − 6), and (b) it doesn’t say how to do *arithmetic* on these diﬀerences (how does one add 3 − 5 to 6−2?). Furthermore, (c) this deﬁnition is *circular* because it requires a notion of subtraction, which we can only adequately deﬁne once the integers are constructed.
- Deﬁnition 4.1.1 (Integers). An integer is an **expression** of the form a−−b, where a and b are natural numbers. Two integers are considered to be **equal**, a−−b = c−−d, if and only if a + d = c + b. We let Z denote the set of all integers.
- The integers n−−0 behave in the same way as the natural numbers n; Thus we may identify the natural numbers with integers by setting n ≡ n−−0;
- Deﬁnition 4.1.4 (**Negation** of integers). If (a−−b) is an integer, we deﬁne the negation −(a−−b) to be the integer (b−−a). In particular if n = n−−0 is a positive natural number, we can deﬁne its negation −n = 0−−n.
- intergers form a commutative ring
- note that we don't define division on intergers just as we didn't define negation and subtraction on natural numbers

### Rationals
- Deﬁnition 4.2.1. A rational number is an expression of the form a//b, where a and b are integers and b is non-zero; a//0 is not considered to be a rational number. Two rational numbers are considered to be equal, a//b = c//d, if and only if ad = cb. The set of all rational numbers is denoted Q.
- We now deﬁne a new operation on the rationals: **reciprocal**. If x = a//b is a non-zero rational (so that a, b = 0) then we deﬁne the reciprocal = x^−1 of x to be the rational number x^−1:= b//a.
- Rationals form a field because xx^-1=x^-1x=1
- We can now deﬁne the **quotient** x/y of two rational numbers x and y, provided that y is non-zero, by the formula x/y := x × y −1.
- Deﬁnition 4.2.6. A rational number x is said to be positive iﬀ we have x = a/b for some positive integers a and b. It is said to be negative iﬀ we have x = −y for some positive rational y (i.e., x = (−a)/b for some positive integers a and b).
- Deﬁnition 4.2.8 (Ordering of the rationals). Let x and y be rational numbers. We say that x > y iﬀ x − y is a positive rational number, and x < y iﬀ x − y is a negative rational number. We write x ≥ y iﬀ either x > y or x = y, and similarly deﬁne x ≤ y.
- properties of odering and ordered field
- Deﬁnition 4.3.1 (Absolute value). If x is a rational number, the absolute value |x| of x is deﬁned as follows. If x is positive, then |x| := x. If x is negative, then |x| := −x. If x is zero, then |x| := 0.
- Deﬁnition 4.3.2 (**Distance**). Let x and y be rational numbers. The quantity |x − y| is called the distance between x and y and is sometimes denoted d(x, y), thus d(x, y) := |x − y|. For instance, d(3, 5) = 2.
- p.87 for properties of absolute value and distance
- Deﬁnition 4.3.4 (**ε-closeness**). Let ε > 0 be a rational number, and let x, y be rational numbers. We say that y is ε-close to x iﬀ we have d(y, x) ≤ ε.
- Remark 4.3.8. One should compare statements (a)-(c) of this proposition with the reﬂexive, symmetric, and transitive axioms of equality. It is often useful to think of the notion of “ε-close” as an approximate substitute for that of equality in analysis.
- Deﬁnition 4.3.9 (**Exponentiation to a natural number**). Let x be a rational number. To raise x to the power 0, we deﬁne x 0:= 1; in particular we deﬁne 0 0:= 1. Now suppose inductively that x nhas been deﬁned for some natural number n, then we deﬁne x^n+1:= x^n × x.
- Deﬁnition 4.3.11 (**Exponentiation to a negative number**). Let x be a non-zero rational number. Then for any negative integer −n, we deﬁne x^−n:= 1/x^n.
- Proposition 4.4.1 (Interspersing of integers by rationals). Let x be a rational number. Then there exists an integer n such that n ≤ x < n+1. In fact, this integer is unique (i.e., for each x there is only one n for which n ≤ x < n + 1). In particular, there exists a natural number N such that N > x (i.e., *there is no such thing as a rational number which is larger than all the natural numbers*).
- Proposition 4.4.3 (Interspersing of rationals by rationals). If x and y are two rationals such that x < y, then there exists a third rational z such that x < z < y.
- However, there are still "holes" between rationals. For example, x for which x^2=2 is not a rational number.

## Reals
> The need for reals came from calculus. Calculus relies on limit and there's no easy way to define it. Rationals are natural ways to represent numbers because they seem to be infinite and are logically rigorous to work with. Thus one could define a limit naturally by considering a sequence of rational numbers that eventually "settles down" to a number. However, rationals have gaps and our idea of limit cannot tolerate gaps, because we want the limit of numbers to be numbers as well, but the current construction allows limit of rationals that are not rationals. Thus we define the limit themselves as numbers, with a careful definitioin of equivalence relation that bridges rationals and reals.

### Real numbers introduction
> From here on, we study functions. We first study a special group of functions from N to Q that "stablize", or more formally, have "limits", and they form the basis of real numbers. We then use these newly constructed objects and study functions from N to R. 
- there is a fundamental area of mathematics where the rational number system does not suﬃce - that of **geometry** (the study of lengths, areas, etc.). For instance, a right-angled triangle with both sides equal to 1 gives a hypotenuse of √2, which is an **irrational number**, i.e., not a rational number; see Proposition 4.4.4. Things get even worse when one starts to deal with the sub-ﬁeld of geometry known as **trigonometry**, when one sees numbers such as π or cos(1), which turn out to be in some sense “even more” irrational than √ 2. (These numbers are known as transcendental numbers)
- Since **diﬀerential and integral calculus is also intimately tied up with geometry** - think of slopes of tangents, or areas under a curve - calculus also requires the real number system in order to function properly.
- we shall ﬁll in these gaps using **limits** to create the real numbers. The real number system will end up being a lot like the rational numbers, but will have some new operations - notably that of **supremum**

### Cauchy Sequences
- Deﬁnition 5.1.1 (**Sequences**). Let m be an integer. A *sequence* $(a_n)_{n=m}^∞$ *of rational numbers* is any **function** from the set {n ∈ Z : n ≥ m} to Q, i.e., a mapping which assigns to each *integer n* greater than or equal to m, a rational number an. More informally, a sequence $(a_n)_{n=m}^∞$ of rational numbers is a *collection* of rationals a m, a m+1, a m+2,...
- Recall from Deﬁnition 4.3.4 that two rational numbers x, y are ε-close if d(x, y) = |x − y| ≤ ε. 
- Deﬁnition 5.1.3 (**ε-steadiness**). Let ε > 0. A sequence $(a_n)_{n=m}^∞$ is said to be ε-steady iﬀ each pair aj, ak of sequence elements is *ε-close* for every natural number j, k. In other words, the sequence a 0, a 1, a 2, . . . is ε-steady iﬀ d(aj, ak) ≤ ε for all j, k.
- note that ε is a rational number
- Deﬁnition 5.1.6 (**Eventual ε-steadiness**). Let ε > 0. A sequence $(a_n)_{n=m}^∞$ is said to be eventually ε-steady iﬀ the sequence a N, a N+1, a N+2, . . . is ε-steady for some natural number N ≥ 0. In other words, the sequence a 0, a 1, a 2, . . . is eventually ε-steady iﬀ there exists an N ≥ 0 such that d(aj, ak) ≤ ε for all j, k ≥ N.
- Deﬁnition 5.1.8 (**Cauchy sequences**). A sequence $(a_n)_{n=m}^∞$ of rational numbers is said to be a Cauchy sequence iﬀ *for every rational ε > 0*, the sequence is *eventually ε-steady*. In other words, the sequence a0, a1, a2,... is a Cauchy sequence iﬀ for every ε > 0, there exists an N ≥ 0 such that d(a j, a k) ≤ ε for all j, k ≥ N.
- Deﬁnition 5.1.12 (**Bounded sequences**). Let M ≥ 0 be rational. A ﬁnite sequence a 1, a 2,..., a n is bounded by M iﬀ |a i| ≤ M for all 1 ≤ i ≤ n. An inﬁnite sequence is bounded by M iﬀ |a i| ≤ M for all i ≥ 1. A sequence is said to be bounded iﬀ it is bounded by M for some rational M ≥ 0.
- Lemma 5.1.15 (Cauchy sequences are bounded). Every Cauchy sequence is bounded.
- Deﬁnition 5.2.1 (*ε-close sequences*). Let (a n) n=0∞ and (b n) n=0∞ be two sequences, and let ε > 0. We say that the sequence (a n) n=0∞ is ε-close to (b n) n=0∞ iﬀ a n is ε-close to b n for each n ∈ N. 
- Deﬁnition 5.2.3 (**Eventually ε-close sequences**). Let (a n) n=0∞and (b n) n=0∞be two sequences, and let ε > 0. We say that the sequence (a n) n=0∞is eventually ε-close to (b n) n=0∞iﬀ there exists an N ≥ 0 such that the sequences (a n) n=N∞and (b n) n=N∞are ε-close.
- Deﬁnition 5.2.6 (**Equivalent sequences**). Two sequences are equivalent iﬀ for each rational ε > 0, the sequences (a n)n=0 and (b n) n=0∞ are eventually ε-close. 

### Real Numbers
- Deﬁnition 5.3.1 (**Real numbers**). A real number is deﬁned to be an *object* of the form $LIM_{n→∞}a_n$, where $(a_n)_{n=1}^{\infin}$ is a Cauchy sequence of rational numbers. Two real numbers $LIM_{n→∞}a_n$ and $LIM_{n→∞}b_n$ are said to be equal iﬀ (a n) and (b n) are equivalent Cauchy sequences. The set of all real numbers is denoted R.
- > Note that a real number is an object built on a sequence which is a function, which exists by power set axiom. The an after LIM is the function object so we can operate on an directly.
- > All sequences of rational numbers are the set Q^N, which has cardinality of the continuum, which is much larger than rational numbers. There are "more" sequnces than Cauchy sequences and more Cauchy sequences than reals because of the equivalence relation.
- Deﬁnition 5.3.4 (Addition of reals). Let x = LIM n→∞ an and y = LIM n→∞ bn be real numbers. Then we deﬁne the sum x + y to be x + y := LIM n→∞(a n+ b n).
- we encounter problems in defining reciiprocal because the sequence might have 0. 
- Deﬁnition 5.3.12 (*Sequences bounded away from zero*). A sequence (a n) n=1∞of rational numbers is said to be bounded away from zero iﬀ there exists a rational number c > 0 such that |a n| ≥ c for all n ≥ 1.
- every non-zero real number is the formal limit of a Cauchy sequence bounded away from zero
- postive and negative real numbers
- absolute value and distance
- while positive real numbers can be arbitrarily large or small, they cannot be larger than all of the positive integers, or smaller in magnitude than all of the positive rationals: Proposition 5.4.12 (*Bounding of reals by rationals*). Let x be a positive real number. Then there exists a positive rational number q such that q ≤ x, and there exists a positive integer N such that x ≤ N.
- Corollary 5.4.13 (Archimedean property). Let x and ε be any positive real numbers. Then there exists a positive integer M such that Mε > x.
- Proposition 5.4.14. Given any two real numbers x < y, we can ﬁnd a rational number q such that x < q < y.

### Least Upper Bound
- Deﬁnition 5.5.1 (**Upper bound**). Let E be a *subset of R*, and let M be a real number. We say that M is an upper bound for E, iﬀ we have x ≤ M for every element x in E.
- Deﬁnition 5.5.5 (**Least upper bound**). Let E be a subset of R, and M be a real number. We say that M is a least upper bound for E iﬀ (a) M is an upper bound for E, and also (b) any other upper bound M ′ for E must be larger than or equal to M.
- Proposition 5.5.8 (Uniqueness of least upper bound). Let E be a subset of R. Then E can have at most one least upper bound.
- Deﬁnition 5.5.10 (**Supremum**). Let E be a subset of the real numbers. If E is non-empty and has some upper bound, we deﬁne sup(E) to be the least upper bound of E 
- We introduce two additional symbols, **+∞ and −∞**. If E is non-empty and has no upper bound, we set sup(E) := +∞; if E is empty, we set sup(E) := −∞. We refer to sup(E) as the supremum of E, and also denote it by sup E.
- Deﬁnition 5.6.4. Let x ≥ 0 be a non-negative real, and let n ≥ 1 be a positive integer. We deﬁne x 1/n, also known as the nth root of x, by the formula x^1/n:= sup{y ∈ R : y ≥ 0 and y^n ≤ x}.
- Deﬁnition 5.6.7. (*rational exponent*) Let x > 0 be a positive real number, and let q be a rational number. To deﬁne x q, we write q = a/b for some integer a and positive integer b, and deﬁne x q:= (x 1/b) a.

### Sequence of Reals and Limit
- we redefine things previously defined on rationals to reals 
- Deﬁnition 6.1.1 (Distance between two real numbers). Given two real numbers x and y, we deﬁne their distance d(x, y) to be d(x, y) := |x−y|.
- Deﬁnition 6.1.2 (*ε-close real numbers*). Let ε > 0 be a real number. We say that two real numbers x, y are ε-close iﬀ we have d(y, x) ≤ ε.

- Deﬁnition 6.1.3 (**Cauchy sequences of reals**). Let ε > 0 be a *real* number. A sequence (a n) n=N∞ of *real numbers* starting at some integer index N is said to be **ε-steady** iﬀ aj and ak are *ε-close* for every j, k ≥ N. A sequence starting at some integer index m is said to be **eventually ε-steady** iﬀ there exists an N ≥ m such that (a n) n=N∞is ε-steady. We say that (a n) n=m∞is a **Cauchy sequence** iﬀ it is *eventually ε-steady for every ε > 0*.
> Note that a sequence of reals is a function of operations on functions that takes a natural number in and gives 

- Deﬁnition 6.1.5 (**Convergence of sequence to L**). Let ε > 0 be a real number, and let L be a real number. *A sequence of real numbers* is said to be **ε-close to L** iﬀ a n is ε-close to L for every n ≥ N, i.e., we have |a n− L| ≤ ε for every n ≥ N. We say that a sequence (a n)n=m∞ is **eventually ε-close to L** iﬀ there exists an N ≥ m such that (a n)n=N is ε-close to L. We say that a sequence (a n) n=m∞ **converges to L** iﬀ it is eventually ε-close to L for every real ε > 0.

> Note that e closeness is between 2 objects and e steadiness is within a sequence
- L is unique
- Deﬁnition 6.1.8 (**Limits of sequences**). If a sequence (a n) n=m∞converges to some real number L, we say that (a n) n=m∞is convergent and that its limit is L; we write $L = \lim\limits_{n \to \infin} a_n$
- Proposition 6.1.12 (**Convergent sequences are Cauchy**). Suppose that (a n) n=m∞is a convergent sequence of real numbers. Then (a n) n=m∞is also a Cauchy sequence.
- Proposition 6.1.15 (Formal limits are genuine limits). Suppose that (a n) n=1∞is a Cauchy sequence of rational numbers. Then (a n) n=1∞converges to LIM n→∞a n, i.e. $LIM_{n\to \infin} a_n = \lim\limits_{n \to \infin} a_n$ 
- Theorem 6.1.19 (Limit Laws). See p.131

### Extented Number System
- Deﬁnition 6.2.1 (**Extended real number system**). The extended real number system R∗ is the real line R with two additional elements attached, called +∞ and −∞. These elements are distinct from each other and also distinct from every real number. An extended real number x is called ﬁnite iﬀ it is a real number, and inﬁnite iﬀ it is equal to +∞ or −∞. (This deﬁnition is not directly related to the notion of ﬁnite and inﬁnite sets in Section 3.6, though it is of course similar in spirit.)
- > Recall that finite sets have some natural number as cardinality
- Deﬁnition 6.2.2 (Negation of extended reals): −(+∞) := −∞ and −(−∞) := +∞. Thus every extended real number x has a negation, and −(−x) is always equal to x.
- Deﬁnition 6.2.3 (Ordering of extended reals).
- > We only define negation and ordering as arithmatic operations on extended reals
- Deﬁnition 6.2.6 (*Supremum of sets of extended reals*). Let E be a subset of R∗. Then we deﬁne the supremum sup(E) or least upper bound of E by the following rule.
    - (a) If E is contained in R (i.e., +∞ and −∞ are not elements of E), then we let sup(E) be as deﬁned in Deﬁnition 5.5.10. 
    - (b) If E contains +∞, then we set sup(E) := +∞. 
    - (c) If E does not contain +∞ but does contain −∞, then we set sup(E) := sup(E\{−∞}) (which is a subset of R and thus falls under case (a)).

### Suprema of Sequences
- Deﬁnition 6.3.1 (Sup and inf of sequences). Let $(a_n)_{n=m}^∞$ be a sequence of real numbers. Then we deﬁne sup(a n) n=m∞ to be the supremum of the set {a n: n ≥ m}, and inf(a n) n=m∞to the inﬁmum of the same set {a n: n ≥ m}.
- Proposition 6.3.6 (Least upper bound property).
- Proposition 6.3.8 (Monotone bounded sequences converge). Let (an) n=m∞be a sequence of real numbers which has some ﬁnite upper bound M ∈ R, and which is also increasing (i.e., a n+1≥ a nfor all n ≥ m). Then (a n) n=m∞is convergent, and in fact lim an= sup(an) ≤ M

### Limsup, Liminf
- consider 1.1, −1.01, 1.001, −1.0001, 1.00001, . . . .
- Deﬁnition 6.4.1 (**Limit points**). Let (a n) n=m∞be a sequence of real numbers, let x be a real number, and let ε > 0 be a real number. We say that x is **ε-adherent** to (a n) n=m∞ iﬀ there exists an n ≥ m such that a_n is ε-close to x. We say that x is **continually ε-adherent** to (a n)n=m iﬀ it is ε-adherent to (a n) n=N∞ for every N ≥ m. We say that x is a limit point or adherent point of (a n) n=m∞ iﬀ it is continually ε-adherent to (a n) n=m∞for every ε > 0.
- Note that continually ε-adherent means for every starting point of the sequence, you can choose an element of the remaining sequence st the element is ε-close to x. For example, 1 is 0.001-adherent to the above sequence because you can start at 1.001. It is also continoully 0.001-adherent because when N=0 or when you are given the whole sequence, you can still choose the 1.001 to compare to.
- Proposition 6.4.5 (*Limits are limit points*). Let (a n) n=m∞be a sequence which converges to a real number c. Then c is a limit point of (a n) n=m∞, and in fact it is the only limit point of (a n) n=m∞.
- Deﬁnition 6.4.6 (**Limit superior and limit inferior**). Suppose that (a n) n=m∞is a sequence. We deﬁne a new sequence $(a_N^+)_{N=m}^∞$ by the formula a $a_N^+ := \sup(a_n)_{n=N}^∞$ . More informally, aN+ is the supremum of all the elements in the sequence from aN onwards. We then deﬁne the limit superior of the sequence (a n) n=m∞, denoted lim sup n→∞a n, by the formula $\limsup a_n:= \inf(a_N^+)_{N=m}^∞$.
- Proposition 6.4.12.
    - (d) If c is any limit point of (a n) n=m∞, then we have L≤ c ≤ L+.
    - (f) Let c be a real number. If (a n) n=m∞converges to c, then we must have L+ = L− = c. Conversely, if L+ = L− = c, then (a n)n=m∞ converges to c.
- This gives a way to test if a sequence converges: compute its limit superior and limit inferior, and see if they are equal.
- Corollary 6.4.14 (**Squeeze test**). Let (a n), (b n), and (c n) be sequences of real numbers such that an ≤ bn ≤ cn for all n ≥ m. Suppose also that (a n) and (c n) both converge to the same limit L. Then (b n) n=m∞ is also convergent to L.
- Remark 6.4.16. The squeeze test, combined with the limit laws and the principle that monotone bounded sequences always have limits, allows to compute a large number of limits.
- Theorem 6.4.18 (**Completeness of the reals**). A sequence (a n) n=1∞ of real numbers is a Cauchy sequence if and only if it is convergent.
- Remark 6.4.20. In the language of metric spaces (see Chapter B.2), Theorem 6.4.18 asserts that the real numbers are a complete metric space - that they do not contain “holes” the same way the rationals do.

- Deﬁnition 6.6.1 (*Subsequences*). Let (a n) n=0∞and (b n) n=0∞be sequences of real numbers. We say that (b n) n=0∞is a subsequence of (a n) n=0∞iﬀ there exists a function f : N → N which is strictly increasing (i.e., f(n + 1) > f(n) for all n ∈ N) such that $b_n= a_{f(n)} $ for all n ∈ N.
- Proposition 6.6.5 (**Subsequences related to limits**). Let (a n) n=0∞ be a sequence of real numbers, and let L be a real number. Then the following two statements are logically equivalent (each one implies the other): 
    - (a) The sequence (a n) n=0∞converges to L. 
    - (b) *Every* subsequence of (a n) n=0∞converges to L.
- Proposition 6.6.6 (**Subsequences related to limit points**). Let (a n)n=0 be a sequence of real numbers, and let L be a real number. Then the following two statements are logically equivalent. 
    - (a) L is a limit point of (a n) n=0∞. 
    - (b) *There exists* a subsequence of (a n) n=0∞which converges to L.
- Theorem 6.6.8 (Bolzano-Weierstrass theorem). Let (a n) n=0∞be a bounded sequence (i.e., there exists a real number M > 0 such that |a n| ≤ M for all n ∈ N). Then there is at least one subsequence of (a n) n=0∞which converges. In other words, every bounded sequence has a convergent subsequence.

- Deﬁnition 6.7.2 (**Exponentiation to a real exponent**). Let x > 0 be real, and let α be a real number. We deﬁne the quantity x αby the formula x α= lim n→∞x qn, where (q n) n=1∞is any sequence of rational numbers converging to α.


## Series
> Series will be important for things like Rienman sum or Taylor expansion
- Deﬁnition 7.1.1 (**Finite series**). Let m, n be integers, and let $(a_i)_{i=m}^n$ be a ﬁnite sequence of real numbers, assigning a real number a i to each integer i between m and n inclusive (i.e., m ≤ i ≤ n). Then we deﬁne the ﬁnite sum (or ﬁnite series) $\sum_{i=m}^{n} a_i$ by the recursive formula
    - $\sum_{i=m}^{n} a_i := 0$ whenever n < m; i=m n+1 
    - $\sum_{i=m}^{n+1} a_i := \left( \sum_{i=m}^{n} a_i \right) + a_{n+1}$ whenever n ≥ m − 1.
> Note that we previously defined addition as a binary operator but finite series is another object of its own. You can think of it as an object that gets a sequence and two indices and outputs a real number.
- Remark 7.1.2. The diﬀerence between “sum” and “series” is a subtle linguistic one. Strictly speaking, a series is an expression of the form ∑ai; this series is mathematically (but not semantically) equal to a real number, which is then the sum of that series.
- Deﬁnition 7.1.6 (**Summations over ﬁnite sets**). Let X be a ﬁnite set with n elements (where n ∈ N), and let f : X → R be a function from X to the real numbers. Then we can deﬁne the ﬁnite sum $\sum\limits_{x∈X}f(x)$ as follows. We ﬁrst select any bijection g from {i ∈ N : 1 ≤ i ≤ n} to X; such a bijection exists since X is assumed to have n elements. We then deﬁne $\sum\limits_{x∈X}f(x)=\sum\limits_{i=1}^nf(g(i))$
- Proposition 7.1.11 (Basic properties of summation over ﬁnite sets). See p.160
- Lemma 7.1.13.
- Corollary 7.1.14 (*Fubini’s theorem for ﬁnite series*). Let X, Y be ﬁnite sets, and let f : X × Y → R be a function. Then $\sum\limits_{x\in X}\sum\limits_{y\in Y} f(x,y) =\sum\limits_{y\in Y}\sum\limits_{x\in X} f(x,y)$

- Deﬁnition 7.2.1 (**Formal inﬁnite series**). A (formal) inﬁnite series is any expression of the form $\sum\limits_{n=m}^\infin a_n$
- Deﬁnition 7.2.2 (**Convergence of series**). Let $\sum\limits_{n=m}^\infin a_n$ be a formal inﬁnite series. For any integer N ≥ m, *we deﬁne the Nth partial sum SN of this series to be $S_N:= \sum\limits_{n=m}^N a_n$*; of course, SN is a real number. If the sequence $(S_N)_{N=m}^∞$ converges to some limit L as N → ∞, then we say that the inﬁnite series is convergent, and converges to L; we also write $L = \sum\limits_{n=m}^\infin a_n$, and say that L is the sum of the inﬁnite series $\sum\limits_{n=m}^\infin a_n$. If the partial sums SN diverge, then we say that the inﬁnite series is divergent, and we do not assign any real number value to that series.
- Corollary 7.2.6 (**Zero test**). Let $(a_n)_{n=m}^∞$ be a convergent series of real numbers. Then $lim_{n\to \infin}a_n = 0$. However the inverse is not always true.
- Deﬁnition 7.2.8 (**Absolute convergence**). Let ∑an be a formal series of real numbers. We say that this series is absolutely convergent iﬀ the series $\sum\limits_{n=m}^\infin |a_n|$ is convergent.
- for example the series $\sum_{n=1}^\infty (-1)^{n+1}\frac{1}{n} = 1 - \frac{1}{2} + \frac{1}{3}- \cdots$ is convergent but not absolutely convergent.
- Proposition 7.2.9 (*Absolute convergence test*). Let ∑n=m∞ a nbe a formal series of real numbers. If this series is absolutely convergent, then it is also conditionally convergent. Furthermore, in this case we have the triangle inequality $|\sum\limits_{n=m}^\infin a_n| \le \sum\limits_{n=m}^\infin |a_n|$
- Proposition 7.2.12 (**Alternating series test**). Let (an) be a sequence of real numbers which are non-negative and decreasing. Then the series $\sum\limits_{n=m}^\infin (-1)^n a_n$ is convergent if and only if the sequence an converges to 0 as n → ∞.
- Lemma 7.2.15 (**Telescoping series**). Let (an) be a sequence of real numbers which converge to 0, i.e., lim n→∞ an=0. Then the series $\sum_{n=0}^\infin(a_n− a_{n+1})$ converges to a 0.

- To summarize, rearranging series is safe when the series is absolutely convergent, but is somewhat dangerous otherwise. For example, 1/3 − 1/4 + 1/5 − 1/6 + 1/7 − 1/8 + . . . . is conditionally convergent but not absolutely convergent and it converges to a postive value. But if we rearrange to 1/3 − 1/4 − 1/6 + 1/5 − 1/8 − 1/10 + 1/7 − 1/12 − 1/14 + . . . then it converges to a negative value. See Theorem 8.2.8 for Rienmann theorem.

- root and ratio test

## Infinite Sets
- Deﬁnition 8.1.1 (**Countable sets**). A set X is said to be countably inﬁnite/denumerable (or just countable) iﬀ it has equal cardinality with the natural numbers N. A set X is said to be at most countable iﬀ it is either countable or ﬁnite. We say that a set is uncountable if it is inﬁnite but not countable.
- From Proposition 3.6.4 and Theorem 3.6.12, we know that countable sets are inﬁnite; however it is not so clear whether all inﬁnite sets are countable. In particular, we want to know if Z, Q and R are countable. 
- every non-empty set X of natural numbers has a minimum element, denoted min(X)
- Proposition 8.1.5. Let X be an inﬁnite subset of the natural numbers N. Then there exists a unique bijection f : N → X which is increasing, in the sense that f(n + 1) > f(n) for all n ∈ N. In particular, X has equal cardinality with N and is hence countable.
- To summarize, any subset or image of a countable set is at most countable, and any ﬁnite union of countable sets is still countable.
- Corollary 8.1.11. The integers Z are countable: union of N and {f(n):=-n}.
- Lemma 8.1.12. The set A := {(n, m) ∈ N × N : 0 ≤ m ≤ n} is countable. 
- Corollary 8.1.14. If X and Y are countable, then X × Y is countable.
- Corollary 8.1.15. The rationals Q are countable.

- Deﬁnition 8.2.1 (*Series on countable sets*). Let X be a countable set, and let f : X → R be a function. We say that the *series ∑x∈Xf(x) is absolutely convergent* iﬀ for some bijection g : N → X, the sum *∑f(g(n)) is absolutely convergent*. We then deﬁne the sum of ∑x∈Xf(x) by the formula $\sum\limits_{x\in X} f(x) =\sum\limits_{n=0}^{\infin} f(g(n))$
- Theorem 8.2.2 (**Fubini’s theorem for inﬁnite sums**). Let f : N × N → R be a function such that ∑ (n,m)∈N×Nf(n, m) is absolutely convergent. Then $\sum\limits_{n=0}^{\infin}(\sum\limits_{m=0}^{\infin} f(x,y)) =\sum\limits_{m=0}^{\infin}(\sum\limits_{n=0}^{\infin} f(x,y))$
- Lemma 8.2.3 (absolute convergence condition for series on at most countable set). Let X be an at most countable set, and let f : X → R be a function. Then the series ∑x∈Xf(x) is absolutely convergent if and only if $\sup\{\sum\limits_{x\in A}|f(x)| : A ⊆ X, \text{A ﬁnite}\}< \infin$
- **Deﬁnition 8.2.4 (absolute convergence condition for series on uncountable set)**. Let X be a set (which could be uncountable), and let f : X → R be a function. We say that the series ∑ x∈Xf(x) is absolutely convergent iﬀ $\sup\{\sum\limits_{x\in A}|f(x)| : A ⊆ X, \text{A ﬁnite}\}< \infin$
- **Lemma 8.2.5 (sum of absolutely convergent series on uncountable set)** Let X be a set (which could be uncountable), and let f : X → R be a function such that the series ∑ x∈Xf(x) is absolutely convergent. Then the set {x ∈ X : f(x) ≠ 0} is at most countable. (This result requires the axiom of choice, see Section 8.4.)
- Note that this is why pdf cannot be defined st probability of x is f(x). You can find a finite subset of x (here reals) st its infinite sum diverges. 
- Proposition 8.2.6 (*Absolutely convergent series laws*). See p.192. Of interest is (d) If Y is another set, and φ : Y → X is a bijection, then $\sum\limits_{y\in Y} f(φ(y))$ is absolutely convergent, and $\sum\limits_{y\in Y} f(φ(y))=\sum\limits_{x\in X} f(x)$ 
- Lemma 8.2.7. Let ∑an be a series of real numbers which is conditionally convergent, but not absolutely convergent. Deﬁne the sets A+:= {n ∈ N : a n≥ 0} and A−:= {n ∈ N : a n< 0}, thus A+∪A− = N and A+ ∩ A− = ∅. Then both of the series ∑ n∈A+ an and ∑ n∈A− an are not conditionally convergent (and thus not absolutely convergent).
- We are now ready to present a remarkable theorem of Georg Riemann (1826–1866), which asserts that a *series which converges conditionally but not absolutely can be rearranged to converge to any value one pleases*
- **Theorem 8.2.8 （Riemann theorem)**. Let ∑an be a series which is conditionally convergent, but not absolutely convergent, and let L be any real number. Then there exists a bijection f : N → N such that $\sum_{m=0}^∞ a_{f(m)}$ converges conditionally to L.

### Uncountabe Set
> We have just shown that a lot of inﬁnite sets are countable - even such sets as the rationals, for which it is not obvious how to arrange as a sequence. After such examples, one may begin to hope that other inﬁnite sets, such as the real numbers, are also countable - after all, the real numbers are nothing more than (formal) limits of the rationals, and we’ve already shown the rationals are countable, so it seems plausible that the reals are also countable.
- **Theorem 8.3.1 (Cantor’s theorem)**. Let X be an arbitrary set (ﬁnite or inﬁnite). Then the sets X and 2^X cannot have equal cardinality. Proof by contradiction: suppose there is a bijection f: X->2^X. With axiom of separation we know a set A exists: $A:=\{x \in X: x \notin f(x)\}$. A is a subset of X, so there must exist an x st f(x)=A. Since x is an element of X, x may be an element of A. If x is in A, then based on how A is constructed x is not in f(x), or A. If x is not in A, then x should be in A. Thus A doesn't exist, and since if f exists A must exists, f doesn't exist too.
- > Remark 8.3.2. The reader should compare the proof of Cantor’s theorem with the statement of Russell’s paradox (Section 3.2). The point is that a bijection between X and 2 Xwould come dangerously close to the concept of a set X “containing itself”.
- Corollary 8.3.3. 2^N is uncountable.
- Corollary 8.3.4. **R is uncountable.**
- > One could ask whether there exist any sets which have strictly larger cardinality than the natural numbers, but strictly smaller cardinality than the reals. The Continuum Hypothesis asserts that no such sets exist.

### Choice

### Ordered Set





## Continuous Functions on R
> In previous chapters we have been focusing primarily on sequences. A sequencecan be viewed as a function from N to R, i.e., an object which assigns a real number a nto each natural number n. We then did various things with these functions from N to R, such as take their limit at inﬁnity (if the function was convergent), or form suprema, inﬁma, etc., or computed the sum of all the elements in the sequence (again, assuming the series was convergent). Now we will look at functions not on the natural numbers N, which are “discrete”, but instead look at functions on a continuum 1such as the real line R, or perhaps on an interval such as {x ∈ R : a ≤ x ≤ b}. Eventually we will perform a number of operations on these functions, including taking limits, computing derivatives, and evaluating integrals. In this chapter we will focus primarily on limits of functions, and on the closely related concept of a continuous function.

### Subsets of Real Line
- We often want to work on subsets of R. There are more subsets of R than R. We focus on a subset of all subsets/power set of R, the intervals.
- Deﬁnition 9.1.1 (**Intervals**). Let a, b ∈ R∗ be extended real numbers. We deﬁne the *closed interval* [a, b] by [a, b] := {x ∈ R∗ : a ≤ x ≤ b}, the *half-open intervals* [a, b) and (a, b] by [a, b) := {x ∈ R∗ : a ≤ x < b}; (a, b] := {x ∈ R∗ : a < x ≤ b}, and the *open intervals* (a, b) by (a, b) := {x ∈ R∗ : a < x < b}. We call a the left *endpoint* of these intervals, and b the right endpoint.
- the real line R itself is the open interval (−∞, +∞), while the extended real line R∗ is the closed interval [−∞, +∞]. We sometimes refer to an interval in which one endpoint is inﬁnite (either +∞ or −∞) as *half-inﬁnite intervals*, and intervals in which both endpoints are inﬁnite as *doubly-inﬁnite intervals*; all other intervals are *bounded intervals*.

> Now we have something to work on similar to sequences. Note that a subset of reals cannot be a sequence since it's uncountable. But we want to define things we defined on sequences now on intervals.
>  
> Just as sequences of real numbers have limit points, sets of real numbers have adherent points, which we now deﬁne. 
- Copy of Deﬁnition 6.4.1 (**Limit points**). Let (a n) n=m∞be a sequence of real numbers, let x be a real number, and let ε > 0 be a real number. We say that x is **ε-adherent** to (a n) n=m∞ iﬀ there exists an n ≥ m such that a_n is ε-close to x. We say that x is **continually ε-adherent** to (a n)n=m iﬀ it is ε-adherent to (a n) n=N∞ for every N ≥ m. We say that x is a **limit point** or adherent point of (a n) n=m∞ iﬀ it is continually ε-adherent to (a n) n=m∞for every ε > 0.
- Deﬁnition 9.1.5 (**ε-adherent points**). Let X be a subset of R, let ε > 0, and let x ∈ R. We say that x is ε-adherent to X iﬀ there exists a y ∈ X which is ε-close to x (i.e., |x − y| ≤ ε).
- Deﬁnition 9.1.8 (**Adherent points**). Let X be a subset of R, and let x ∈ R. We say that x is an adherent point of X iﬀ it is ε-adherent to X for every ε > 0.
- Deﬁnition 9.1.10 (**Closure**). Let X be a subset of R. The *closure of X*, sometimes denoted $\bar{X}$ is deﬁned to be the set of all the adherent points of X.
- Lemma 9.1.12 (*Closures of intervals*). Let a < b be real numbers, and let I be any one of the four intervals (a, b), (a, b], [a, b), or [a, b]. Then the *closure of I is [a, b]*. Similarly, the closure of (a, ∞) or [a, ∞) is [a, ∞), while the closure of (−∞, a) or (−∞, a] is (−∞, a]. Finally, the *closure of (−∞, ∞) is (−∞, ∞)*.
- Lemma 9.1.13. The closure of N is N. The closure of Z is Z. *The closure of Q is R*, and the closure of R is R. The closure of the empty set ∅ is ∅.
- Lemma 9.1.14 (*limit of subset of X and adherent point*). Let X be a subset of R, and let x ∈ R. Then x is an adherent point of X if and only if there exists a sequence (an), consisting entirely of elements in X, which converges to x.
- Deﬁnition 9.1.15 (*closed subset*). A subset E ⊆ R is said to be closed if $E = \bar{E}$, or in other words that E contains all of its adherent points. From above, we know N, Z, R, ∅ are closed while Q is not.
- Deﬁnition 9.1.18 (**Limit points**). Let X be a subset of the real line. We say that x is a limit point (or a cluster point) of X iﬀ it is an adherent point of X\\{x}. We say that x is an isolated point of X if x ∈ X and there exists some ε > 0 such that |x − y| > ε for all y ∈ X\\{x}.
- Let X be the set X = (1, 2) ∪ { 3 } . Then 3 is an adherent point of X, but it is not a limit point of X
- Deﬁnition 9.1.22 (**Bounded sets**). A subset X of the real line is said to be bounded if we have X ⊂ [−M, M] for some real number M > 0. 
- Thus [a, ∞), N, Z, R, etc are unbounded but closed. (a,b) is bounded but not closed. Q and (a, ∞) and R∖{5} is neither closed nor bounded.
- ?  Theorem 9.1.24 (**Heine-Borel theorem for the line**). Let X be a subset of R. Then the following two statements are equivalent: 
    - (a) X is closed and bounded. 
    - (b) Given any sequence (an) of real numbers which takes values in X (i.e., a n∈ X for all n), there exists a subsequence $(a_{n_j})_{j=0}^∞$ of the original sequence, which converges to some number L in X.

- Deﬁnition 9.2.1 (Arithmetic operations on functions).




### Limit of function
- Deﬁnition 9.3.1 (**ε-closeness**). Let X be a subset of R, let f : X → R be a function, let L be a real number, and let ε > 0 be a real number. We say that *the function f is ε-close to L* iﬀ f(x) is ε-close to L for every x ∈ X.
- Deﬁnition 9.3.3 (**Local ε-closeness**). Let X be a subset of R, let f : X → R be a function, let L be a real number, x0 be an adherent point of X, and ε > 0 be a real number. We say that *f is ε-close to L near x0* iﬀ there exists a δ > 0 such that f becomes ε-close to L when *restricted to the set {x ∈ X : |x − x0| < δ}*.
- Deﬁnition 9.3.6 (**Convergence of functions at a point**). Let X be a subset of R, let f : X → R be a function, let E be a subset of X, x0 be an [adherent point](9.1.8) of E, and let L be a real number. We say that *f converges to L at x0 in E, and write $\lim_{x→x_0; x\in E}f(x) = L$*, iﬀ f, after restricting to E, is [ε-close to L near x0](9.3.3) for every ε > 0. If f does not converge to any number L at x 0, we say that f diverges at x 0, and leave lim x→x0;x∈E f(x) undeﬁned. *Equivalently*: For every sequence (an) which consists entirely of elements of E and converges to x 0, the sequence (f(an)) converges to L. *We say f has limit of L at x0 in E.*
- > Copy of Deﬁnition 6.1.5 (**Convergence of sequence to L**). Let ε > 0 be a real number, and let L be a real number. *A sequence of real numbers* is said to be **ε-close to L** iﬀ a n is ε-close to L for every n ≥ N, i.e., we have |an− L| ≤ ε for every n ≥ N. We say that a sequence (a n)n=m∞ is **eventually ε-close to L** iﬀ there exists an N ≥ m such that (a n)n=N is ε-close to L. We say that a sequence (a n) n=m∞ **converges to L** iﬀ it is eventually ε-close to L for every real ε > 0.
- > note that the convergence of sequence and function both use the same ε for "sandwitching" a set of numbers. For delta, in the sequence case we choose it as an starting index and in function we use it as bound of a subset of domain. 
- note that E is not the set bound by delta, it's just a general restricting set that often depends on what you want to do. See below.
- Remark 9.3.7. In many cases we will omit the set E from the above notation (i.e., we will just say that f converges to L at x 0, or that $lim_{x→x_0}f(x) = L$), although this is slightly dangerous. For instance, it sometimes makes a diﬀerence whether E actually contains x0 or not. To give an example, if f : R → R is the function deﬁned by setting f(x) = 1 when x = 0 and f(x) = 0 when x != 0, then one = has $lim_{x→0; x \in R \text{\textbackslash}\{ 0 \}} f(x) = 0$, but $lim_{x→0;x∈R} f(x)$ is undeﬁned.
- Corollary 9.3.13. a function can have at most one limit at each point
- Example 9.3.21. Let f : R → R be the function f(x)=1 if x ∈ Q f(x)=0 if x not in Q. f(x) has no limit at 0 in R.

### Continuous Function
- Deﬁnition 9.4.1 (**Continuity**). Let X be a subset of R, and let f : X → R be a function. Let x0 be an element of X. We say that f is continuous at x0 iﬀ we have $lim_{x \to x 0; x \in X} f(x) = f(x_0)$. We say that f is continuous on X (or simply continuous) iﬀ f is continuous at x0 for every x0∈X. We say that f is discontinuous at x0 iﬀ it is not continuous at x0.
- Proposition 9.4.7 (**Equivalent formulations of continuity**). Let X be a subset of R, let f : X → R be a function, and let x 0be an element of X. Then the following four statements are logically equivalent: 
    - (a) f is continuous at x 0. 
    - (b) For every sequence (an) consisting of elements of X with $lim_{n→∞}a_n = x_0$, we have $lim_{n→∞}f(a_n) = f(x_0)$. 
    - (c) For every ε > 0, there exists a δ > 0 such that |f(x) − f(x0)| < ε for all x ∈ X with |x − x0| < δ. 
    - (d) For every ε > 0, there exists a δ > 0 such that |f(x) − f(x0)| ≤ ε for all x ∈ X with |x − x0| ≤ δ.
- Proposition 9.4.9 (Arithmetic preserves continuity)
- Proposition 9.4.13 (Composition preserves continuity).

### Left and Right Limits
- Deﬁnition 9.5.1 (**Left and right limits**). Let X be a subset of R, f : X → R be a function, and let x0 be a real number. If x0 is an adherent point of X ∩ (x0, ∞), then we deﬁne the right limit f(x0+) of f at x0 by the formula $f(x_0+) := \lim\limits_{x→x_0;x∈X∩(x_0,∞)} f(x) $
- Proposition 9.5.3 (*Continuity test*). Let X be a subset of R containing a real number x 0, and suppose that x0 is an adherent point of both X ∩ (x0, ∞) and X ∩ (−∞, x0). Let f : X → R be a function. If f(x0+) and f(x0−) both exist and are both equal to f(x0), then f is continuous at x0.
- jump discontinuity (step function), removeable discontinuity (f(0)=1 and 0 elsewhere), asymptotic discontinuity (1/x), oscillatory discontinuities

### Maximum Principle
- Deﬁnition 9.6.1 (**bounded function**). Let X be a subset of R, and let f : X → R be a function. We say that f is bounded from above if there exists a real number M such that f(x) ≤ M for all x ∈ X. We say that f is bounded from below if there exists a real number M such that f(x) ≥ −M for all x ∈ X. We say that f is bounded if there exists a real number M such that |f(x)| ≤ M for all x ∈ X.
- *Lemma 9.6.3*. Let a < b be real numbers, and let f : [a, b] → R be a function continuous on [a, b]. Then f is a bounded function.
- Deﬁnition 9.6.5 (*Maxima and minima*). Let f : X → R be a function, and let x 0∈ X. We say that f attains its maximum at x0 if we have f(x 0) ≥ f(x) for all x ∈ X (i.e., the value of f at the point x0 is larger than or equal to the value of f at any other point in X). We say that f attains its minimum at x 0if we have f(x 0) ≤ f(x).
- Proposition 9.6.7 (**Maximum principle**). Let a < b be real numbers, and let f : [a, b] → R be a function continuous on [a, b]. Then f attains its maximum at some point x max∈ [a, b], and also attains its minimum at some point x min∈ [a, b]. Note that there can be multiple extrema

### Intermediate Value Theorem
- We have just shown that a continuous function attains both its maximum value and its minimum value. We now show that f also attains every value in between.
- Theorem 9.7.1 (**Intermediate value theorem**). Let a < b, and let f : [a, b] → R be a *continuous* function on [a, b]. Let y be a real number between f(a) and f(b), i.e., either f(a) ≤ y ≤ f(b) or f(a) ≥ y ≥ f(b). Then there exists c ∈ [a, b] such that f(c) = y.
- Corollary 9.7.4 (**Images of continuous functions**). Let a < b, and let f : [a, b] → R be a continuous function on [a, b]. Let M := sup x∈[a,b]f(x) be the maximum value of f, and let m := inf x∈[a,b]f(x) be the minimum value. Let y be a real number between m and M (i.e., m ≤ y ≤ M). Then there exists a c ∈ [a, b] such that f(c) = y. Furthermore, we have f([a, b]) = [m, M].

### Monotone
- Deﬁnition 9.8.1 (**Monotonic functions**). Let X be a subset of R, and let f : X → R be a function. We say that f is monotone increasing iﬀ f(y) ≥ f(x) whenever x, y ∈ X and y > x. We say that f is strictly monotone increasing iﬀ f(y) > f(x) whenever x, y ∈ X and y > x.
- Monotone functions obey the maximum principle, but not the intermediate value principle 
- If a function is both strictly monotone and continuous, then it has many nice properties. In particular, it is invertible: 
- Proposition 9.8.3 (**invertible function condition**). Let a < b be real numbers, and let f : [a, b] → R be a function which is both continuous and strictly monotone increasing. Then f is a bijection from [a, b] to [f(a), f(b)], and the inverse f^−1: [f(a), f(b)] → [a, b] is also continuous and strictly monotone increasing.

### Uniform Continuity
- We know that a continuous function on a closed interval [a, b] remains bounded (and in fact attains its maximum and minimum, by the maximum principle). However, if we replace the closed interval by an open interval, then continuous functions need not be bounded any more. An example is the function f : (0, 2) → R deﬁned by f(x) := 1/x. This function is continuous at every point in (0, 2), and is hence continuous at (0, 2), but is not bounded. Informally speaking, the problem here is that while the function is indeed continuous at every point in the open interval (0, 2), it becomes “less and less” continuous as one approaches the endpoint 0.
- For 1/x, one needs a much smaller “δ” for the same value of ε i.e., f(x) is much more “unstable” near 0.1 than it is near 1, in the sense that there is a much smaller “island of stability” around 0.1 as there is around 1. On the other hand, there are other continuous functions which do not exhibit this behavior. For y=2x, the same δ works for every x0. When this happens, we say that the function g is uniformly continuous. More precisely:
- Deﬁnition 9.9.2 (**Uniform continuity**). Let X be a subset of R, and let f : X → R be a function. We say that f is uniformly continuous if, for every ε > 0, there exists a δ > 0 such that f(x) and f(x0) are ε-close whenever x, x0 ∈ X are two points in X which are δ-close.
- > The diﬀerence between uniform continuity and continuity is that in uniform continuity one can take a single δ which works for all x 0∈ X;
- > Note that this notion of size of island of stability is a good segue (Lat. Sequi) to derivative
- Deﬁnition 9.9.5 (*Equivalent sequences*). eventually ε-close for every ε
- Lemma 9.9.7. Let (a n) and (b n) be sequences of real numbers (not necessarily bounded or convergent). Then (a n) and (b n) are equivalent if and only if lim n→∞(an − bn) = 0.
- Proposition 9.9.8. Let X be a subset of R, and let f : X → R be a function. Then the following two statements are logically equivalent: 
    - (a) f is uniformly continuous on X. 
    - (b) Whenever (x n) n=0∞and (y n) n=0∞are two equivalent sequences consisting of elements of X, the sequences (f(x n)) n=0∞and (f(y n))n=0 are also equivalent.
- examples: 1/x: the sequence (1/n) n=1∞and (1/2n) n=1∞are equivalent sequences in (0, 2). However, the sequences (f(1/n)) n=1∞and (f(1/2n)) n=1∞are not equivalent. 
- another example x^2: Consider the sequences (n) and (n + 1/n ). By Lemma 9.9.7, these sequences are equivalent. But the sequences (f(n)) and (f(n + 1/n )) are not equivalent. They are not eventually 2-close
- Proposition 9.9.12. Let X be a subset of R, and let f : X → R be a uniformly continuous function. Let (xn) be a Cauchy sequence consisting entirely of elements in X. Then (f(xn)) is also a Cauchy sequence. This can easily be demonstrated with 1/x example by considering the Cauchy sequence (1/n)
- Proposition 9.9.15. Let X be a subset of R, and let f : X → R be a uniformly continuous function. Suppose that E is a bounded subset of X. Then f(E) is also bounded.

### Limits at Infinity
- Until now, we have discussed what it means for a function f : X → R to have a limit as x → x0 as long as x0 is a real number. We now brieﬂy discuss what it would mean to take limits when x0 is equal to +∞ or −∞.
- Deﬁnition 9.10.1 (**Inﬁnite adherent points**). Let X be a subset of R. We say that +∞ is adherent to X iﬀ for every M ∈ R there exists an x ∈ X such that x > M; we say that −∞ is adherent to X iﬀ for every M ∈ R there exists an x ∈ X such that x < M. In other words, +∞ is adherent to X iﬀ X has *no upper bound*, or equivalently iﬀ sup(X) = +∞.
- Deﬁnition 9.10.3 (**Limits at inﬁnity**). Let X be a subset of R with +∞ as an adherent point, and let f : X → R be a function. We say that *f(x) converges to L as x → +∞ in X*, and write $lim_{x→+∞;x∈X} f(x) = L$, iﬀ for every ε > 0 there exists an M such that f is ε-close to L on X ∩ (M, +∞) (i.e., |f(x) − L| ≤ ε for all x ∈ X such that x > M). Similarly we say that f(x) converges to L as x → −∞ iﬀ for every ε > 0 there exists an M such that f is ε-close to L on X ∩ (−∞, M).
- Note that this deﬁnition is consistent with the notion of a limit lim n→∞ an of a sequence

## Differentiation of Functions
- We can now deﬁne derivatives analytically, using limits, in contrast to the geometric deﬁnition of derivatives, which uses tangents. The advantage of working analytically is that (a) we do not need to know the axioms of geometry, and (b) these deﬁnitions can be modiﬁed to handle functions of several variables, or functions whose values are vectors instead of scalar.

### Differentiability and Derivative
- Copy of Deﬁnition 9.1.5 (**ε-adherent point of set**). Let X be a subset of R, let ε > 0, and let x ∈ R. We say that x is ε-adherent to X iﬀ there exists a y ∈ X which is ε-close to x (i.e., |x − y| ≤ ε).
- Copy of Deﬁnition 9.1.8 (**Adherent points**). ε-adherent to X for every ε > 0.
- Copy of Deﬁnition 9.1.18 (**Limit points**). adherent point of X\\{x}. 
- Copy of Deﬁnition 9.3.1 (**ε-closeness of function to real number**). Let X be a subset of R, let f : X → R be a function, let L be a real number, and let ε > 0 be a real number. We say that *the function f is ε-close to L* iﬀ f(x) is ε-close to L for every x ∈ X.
- Copy of Deﬁnition 9.3.3 (**ε-closeness of function to real number near a point**). Let X be a subset of R, let f : X → R be a function, let L be a real number, x0 be an [adherent point](9.1.8) of X, and ε > 0 be a real number. We say that *f is ε-close to L **near x0*** iﬀ there exists a δ > 0 such that f becomes [ε-close to L](9.3.1) when *restricted to the set {x ∈ X : |x − x0| < δ}*.
 - Basically at a given adherent point and with a given ε, ε-closeness of a function to L within a chosen range around that point. Note we need the "any ε" upgrade for limit.
- Copy of Deﬁnition 9.3.6 (**Convergence of functions at a point**). Let X be a subset of R, let f : X → R be a function, let E be a subset of X, x0 be an [adherent point](9.1.8) of E, and let L be a real number. We say that *f converges to L at x0 in E, and write $\lim_{x→x_0; x\in E}f(x) = L$*, iﬀ f, after restricting to E, is [ε-close to L near x0](9.3.3) for every ε > 0. If f does not converge to any number L at x 0, we say that f diverges at x 0, and leave lim x→x0;x∈E f(x) undeﬁned. Equivalently: For every sequence (an) which consists entirely of elements of E and converges to x 0, the sequence (f(an)) converges to L. We say f has limit of L at x0.

- !! Deﬁnition 10.1.1 (**Diﬀerentiability at a point**). Let X be a subset of R, and let x0 ∈ X be an element of X which is also a [limit point](9.1.18) of X. Let f : X → R be a function. If the limit $\lim\limits_{x→x0;x\in X-\{x_0\}}\frac{f(x) − f(x_0)}{x-x_0}$ [converges to some real number L (at x0 in X)](9.3.6), then we say that f is diﬀerentiable at x0 on X with derivative L, and write f′(x0) := L. If the limit does not exist, or if x0 is not an element of X or not a limit point of X, we leave f′(x0) undeﬁned, and say that f is not diﬀerentiable at x0 on X.
- Note: Compared to limit of a function at a point, first note the usage of limit point instead of adherent point. Then since f(x0) and x0 are numbers, the thing in the limit is just a function. So it's the limit of a specially constructed function at a limit point.
- Example: x^2 ![](/images/analysis-x^2.png)
- Equivalently (replace x-x0 with h, which is bijective): $f'(x_0)=\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$
- Copy of Proposition 9.5.3 (*Continuity test*). Let X be a subset of R containing a real number x0, and suppose that x0 is an adherent point of both X ∩ (x0, ∞) and X ∩ (−∞, x0). Let f : X → R be a function. If f(x0+) and f(x0−) both exist and are both equal to f(x0), then f is continuous at x0.
- Example: differentiability of |x| at 0 is: $\lim\limits_{x\to 0;x\in X-\{0\}} \frac{|x|}{x}$. This limit is not defined: 
    1. |x|/x with x != 0 is not continuous (can be proven by the 4 equivalent continuity condititions in 9.4.7) so it's not differentiable at 0
    2. no matter how we choose delta to restrict the boundary, there will be elements of |x|/x where x is from {x in X: |x-x0|< delta} which are not 1-close to 1 (or -1)


- If a function is diﬀerentiable at x0, then it is approximately linear near x0:
- Proposition 10.1.7 (**Newton’s approximation**). Let X be a subset of R, let x 0∈ X be a [limit point] of X, let f : X → R be a function, and let L be a real number. Then the following statements are logically equivalent: 
    - (a) f is diﬀerentiable at x0 on X with derivative L. 
    - (b) For every ε > 0, there exists a δ > 0 such that f(x) is ε|x − x0| close to f(x0) + L(x − x0) whenever x ∈ X is δ-close to x0, i.e., *we have |f(x) − (f(x0) + L(x − x0))| ≤ ε|x − x0| whenever x ∈ X and |x − x0| ≤ δ*.
- the last sentence says that the error between using the actual f and the linear approximation is arbitrarily small, beacuse ε is arbitrarily small, provided that the approximation is within a delta range defined by ε. In other words, there will always be a local range near x0 when linear approximation is arbitarily close to actual f. In other words, when your interval is small enough, any function is very close to linear. 
- Proposition 10.1.10 (*Differentiability implies continuity*).
- Theorem 10.1.13 (Diﬀerential calculus).
- Theorem 10.1.15 (Chain rule).

### Local extrema and derivative
- Copy of Deﬁnition 9.6.5 (*Maxima and minima*). Let f : X → R be a function, and let x0 ∈ X. We say that f attains its maximum at x0 if we have f(x0) ≥ f(x) for all x ∈ X
- Deﬁnition 10.2.1 (*Local maxima and minima*). Let f : X → R be a function, and let x0 ∈ X. We say that f attains a local maximum at x0 iﬀ there exists a δ > 0 such that the restriction f|X ∩ (x 0−δ,x 0+δ) of f to X ∩ (x0 − δ, x0 + δ) attains a maximum at x 0. 
- Example 10.2.4. Let f : Z → R be the function f(x) = x, **deﬁned on the integers only**. Then f has no global maximum or global minimum (why?), but attains both a local maximum and local minimum at every integer n (why?).

- ! Proposition 10.2.6 (**Local extrema are stationary**). Let a < b be real numbers, and let f : (a, b) → R be a function. If x0 ∈ (a, b), f is diﬀerentiable at x0, and f attains either a local maximum or local minimum at x0, then f′(x0) = 0.
- this proposition does not work if the open interval (a, b) is replaced by a closed interval [a, b]. For example, f(x) = x on [1,2]. Also, the converse of this proposition is false

- Theorem 10.2.7 (**Rolle’s theorem**). Let a < b be real numbers, and let g : [a, b] → R be a continuous function which is diﬀerentiable on (a, b). Suppose also that g(a) = g(b). Then there exists an x ∈ (a, b) such that g′(x) = 0.
- Corollary 10.2.9 (**Mean value theorem**). Let a < b be real numbers, and let f : [a, b] → R be a function which is continuous on [a, b] and diﬀerentiable on (a, b). Then there exists an x ∈ (a, b) such that f′(x) = f(b)−f(a)/b−a.

### Monotone, Inverse
- Proposition 10.3.1. Let X be a subset of R, let x 0∈ X be a limit point of X, and let f : X → R be a function. If f is monotone increasing and f is diﬀerentiable at x 0, then f′(x0) ≥ 0.
- Proposition 10.3.3. Let a < b, and let f : [a, b] → R be a diﬀerentiable function. If f′(x) > 0 for all x ∈ [a, b], then f is *strictly monotone increasing*. If f ′(x) < 0 for all x ∈ [a, b], then f is strictly monotone decreasing. If f ′(x) = 0 for all x ∈ [a, b], then f is a constant function.
- note that extrema and monotone sections both use f' to deduce something about f. This will lead to fundamental theorem of calculus.
- Lemma 10.4.1 (*derivative of inverse function*). Let f : X → Y be an invertible function, with inverse f −1: Y → X. Suppose that x0 ∈ X and y0 ∈ Y are such that y0= f(x0) (which also implies that x0= f−1(y0)). If f is diﬀerentiable at x 0, and f−1 is diﬀerentiable at y0, then (f−1)′(y0) = 1/f′(x0)
- For example $f(x)=e^x, f^{-1}=ln(x), (f^{-1})'(y)=\frac{1}{e^x}=1/y$

### L'Hopital
- Proposition 10.5.1 (**L’Hopital’s rule I**). Let X be a subset of R, let f : X → R and g : X → R be functions, and let x 0∈ X be a limit point of X. Suppose that f(f0) = g(x0) = 0, that f and g are both diﬀerentiable at x0, but g′(x0) != 0. Then there exists a δ > 0 such that = g(x) ≠ 0 for all x ∈ (X ∩ (x 0− δ, x 0+ δ)) − {x 0}, and $\lim\limits_{x→x 0;x \in\{X∩(x_0 -\delta, x_0+\delta)-{x_0}\}}\frac{f(x)}{g(x)}=\frac{f'(x_0)}{g'(x_0)}$
-  Proposition 10.5.2 (**L’Hopital’s rule II**). Let a < b be real numbers, let f : [a, b] → R and g : [a, b] → R be functions which are diﬀerentiable on [a, b]. Suppose that f(a) = g(a) = 0, that g′ is non-zero on [a, b] (i.e., g′(x) ≠ 0 for all x ∈ [a, b]), and lim x→a;x∈(a,b]f′g′(x)(x) exists and equals L. Then g(x) ≠ 0 for all x ∈ (a, b], and lim x→a;x∈(a,b]f(x)g(x) exists and equals L.

## Riemann Integral
### Partition
- Deﬁnition 11.1.1 (**connectedness**). Let X be a subset of R. We say that X is connected iﬀ the following property is true: whenever x, y are elements in X such that x < y, the bounded interval [x, y] is a subset of X (i.e., every number between x and y is also in X).
- Lemma 11.1.4. Let X be a subset of the real line. Then the following two statements are logically equivalent: 
    - (a) X is *bounded and connected*. 
    - (b) X is a *bounded interval*.
- Deﬁnition 11.1.8 (**Length of intervals**). If I is a [bounded interval](11.1.4), we deﬁne the length of I, denoted |I| as follows. If I is one of the intervals [a, b], (a, b), [a, b), or (a, b] for some real numbers a < b, then we deﬁne |I| := b−a. Otherwise, if I is a point or the empty set, we deﬁne |I| = 0.
- Deﬁnition 11.1.10 (**Partitions**). Let I be a bounded interval. A partition of I is a *ﬁnite set P of [bounded intervals](11.1.4) contained in I*, such that *every x in I lies in exactly one of the bounded intervals J in P*.
- Theorem 11.1.13 (**Length is ﬁnitely additive**). Let I be a bounded interval, n be a natural number, and let P be a partition of I of cardinality n. Then |I| = ∑|J|. J∈P
- Deﬁnition 11.1.14 (**Finer and coarser partitions**). Let I be a bounded interval, and let P and P′ be two partitions of I. We say that P′ is ﬁner than P (or equivalently, that P is coarser than P′) if for every J in P′, there exists a K in P such that J ⊆ K.
- Deﬁnition 11.1.16 (**Common reﬁnement**). Let I be a bounded interval, and let P and P′ be two partitions of I. We deﬁne the common reﬁnement P#P′ of P and P′ to be the set P#P′ := {K ∩ J : K ∈ P and J ∈ P′}.

### Piecewise constant function
- Deﬁnition 11.2.1 (*Constant functions*). Let X be a subset of R, and let f : X → R be a function. We say that f is constant iﬀ there exists a real number c such that f(x) = c for all x ∈ X. If E is a subset of X, we say that f is constant on E if the restriction f |E of f to E is constant, in other words there exists a real number c such that f(x) = c for all x ∈ E. We refer to c as the constant value of f on E.
- Deﬁnition 11.2.3 (**Piecewise constant functions I**). Let I be a bounded interval, let f : I → R be a function, and let P be a partition of I. We say that f is piecewise constant with respect to P if for every J ∈ P, [f is constant on J](11.2.1).
- Deﬁnition 11.2.5 (**Piecewise constant functions II**). Let I be a bounded interval, and let f : I → R be a function. We say that f is piecewise constant on I if there exists a partition P of I such that f is [piecewise constant with respect to P](11.2.3).
- Deﬁnition 11.2.9 (**Piecewise constant integral I**). Let I be a bounded interval, let P be a partition of I. Let f : I → R be a function which is piecewise constant with respect to P. Then we deﬁne the piecewise constant integral p.c. ∫[P] f of f with respect to the partition P by the formula $p.c. \int_{[P]}f := \sum\limits_{J \in P} c_J|J|$ where for each J in P, we let cJ be the constant value of f on J.
- Proposition 11.2.13 (*Piecewise constant integral is independent of partition*).
- Deﬁnition 11.2.14 (**Piecewise constant integral II**). Let I be a bounded interval, and let f : I → R be a [piecewise constant function](11.2.5) on I. We deﬁne the piecewise constant integral p.c. ∫I f by the formula $p.c. \int_I f := p.c. \int_{[P]} f$ where P is any partition of I with respect to which f is piecewise constant.
- Theorem 11.2.16 (Laws of integration).

### Upper and Lower Riemann Integral
- We want to deﬁne the Riemann integral ∫I f. To do this we ﬁrst need to deﬁne the notion of upper and lower Riemann integrals. These notions are related to the Riemann integral in much the same way that the lim sup and lim inf of a sequence are related to the limit of that sequence.
- Copy of Deﬁnition 6.4.6 (**Limit superior and limit inferior**). Suppose that (a n) n=m∞is a sequence. We deﬁne a new sequence $(a_N^+)_{N=m}^∞$ by the formula a $a_N^+ := \sup(a_n)_{n=N}^∞$ . More informally, aN+ is the supremum of all the elements in the sequence from aN onwards. We then deﬁne the limit superior of the sequence (a n) n=m∞, denoted lim sup n→∞a n, by the formula $\limsup a_n:= \inf(a_N^+)_{N=m}^∞$.
- Deﬁnition 11.3.1 (**Majorization of functions**). Let f : I → R and g : I → R. We say that g majorizes f on I if we have g(x) ≥ f(x) for all x ∈ I, and that g minorizes f on I if g(x) ≤ f(x) for all x ∈ I.
- The idea of the Riemann integral is to try to integrate a function by ﬁrst majorizing or minorizing that function by a piecewise constant function (which we already know how to integrate).
- ![](/images/analysis-u-l-riemann.png)
- !! Deﬁnition 11.3.4 (**Riemann integral**). Let f : I → R be a bounded function on a bounded interval I. If $\bar{\int}_I f = \underline{\int}_I f$, then we say that f is Riemann integrable on I and deﬁne $\int_I f := \bar{\int}_I f = \underline{\int}_I f$. If the upper and lower Riemann integrals are unequal, we say that f is not Riemann integrable.
- Example of non Riemann integratable funtions: 
    - f(x)=1 if x is Q, -1 if x is not Q. Recall that a partition P is a finite set of bounded intervals and has to include every x. Thus every interval in P that partitions domain of f will include both Q and non Q (because there is a rational btw every 2 irrationals and a irrational btw every 2 rationals. any interval that attempts to only inlude irrationals must start and end in irrationals, but there will always be a rational in between those 2). So constant value of any piecewise constant function that majorizes f will be 1 and for functions that minorize will be -1. 
    - sin(1/x)
- ![](/images/analysis-riemann-sum.png)
- Lemma 11.3.11. Let f : I → R be a bounded function on a bounded interval I, and let g be a function which majorizes f and which is piecewise constant with respect to some partition P of I. Then $p.c. \int_I g ≥ U(f, P)$. Similarly, if h is a function which minorizes f and is piecewise constant with respect to P, then $p.c. \int_I h ≤ L(f, P)$.
- Proposition 11.3.12. Let f : I → R be a bounded function on a bounded interval I. Then $\bar{\int}_I f = \inf\{U(f, P) : \text{P is a partition of I}\} $ and $\underline{\int}_I f = \sup\{L(f, P) : \text{P is a partition of I}\} $
- Theorem 11.4.1 (Laws of Riemann integration).

### Riemann Integrability of Continuous Functions
- Theorem 11.5.1. Let I be a bounded interval, and let f be a function which is uniformly continuous on I. Then f is Riemann integrable.
- Corollary 11.5.2. Let [a, b] be a closed interval, and let f : [a, b] → R be continuous. Then f is Riemann integrable.
- Proposition 11.5.3. Let I be a bounded interval, and let f : I → R be both continuous and bounded. Then f is Riemann integrable on I.
- Deﬁnition 11.5.4. Let I be a bounded interval, and let f : I → R. We say that f is piecewise continuous on I iﬀ there exists a partition P of I such that f |J is continuous on J for all J ∈ P.
- Proposition 11.5.6. Let I be a bounded interval, and let f : I → R be both piecewise continuous and bounded. Then f is Riemann integrable.

### Monotone
- *Proposition 11.6.1*. Let [a, b] be a closed and bounded interval and let f : [a, b] → R be a monotone function. Then f is Riemann integrable on [a, b].
- *Corollary 11.6.3*. Let I be a bounded interval, and let f : I → R be both monotone and bounded. Then f is Riemann integrable on I.
- Proposition 11.6.4 (*Integral test*). Let f : [0, ∞) → R be a monotone decreasing function which is non-negative (i.e., f(x) ≥ 0 for all x ≥ 0). Then the sum ∑n=0∞ f(n) is convergent if and only if $\sup_{N>0}∫_{[0,N]} f$  is ﬁnite.
- Corollary 11.6.5. Let p be a real number. Then ∑n=1∞ n^p converges absolutely when p > 1 and diverges when p ≤ 1.

### Riemann-Stieltjes
- Deﬁnition 11.8.1 (**α-length**). Let I be a bounded interval, and let α : X → R be a function deﬁned on some domain X which contains I. Then we deﬁne the α-length α[I] of I as follows. If I is a point or the empty set, we set α[I] = 0. If I is an interval of the form [a, b], [a, b), (a, b], or (a, b) for some b > a, then we set α[I] = α(b) − α(a).
- Example 11.8.2. Let α : R → R be the function α(x) := x^2. Then α[[2, 3]] = α(3) − α(2) = 9 − 4 = 5, while α[(−3, −2)] = −5. Meanwhile α[{2}] = 0 and α[∅] = 0.
- We sometimes write $α|_a^b$ or $α(x)|_{x=a}^{x=b}$ instead of α[[a, b]].

- Copy of Theorem 11.1.13 (**Length is ﬁnitely additive**). Let I be a bounded interval, n be a natural number, and let P be a partition of I of cardinality n. Then |I| = ∑|J|. J∈P
- **Lemma 11.8.4**. Let I be a bounded interval, let α : X → R be a function deﬁned on some domain X which contains I, and let P be a partition of I. Then we have α[I] = ∑α[J]. J∈P

- Copy of Deﬁnition 11.2.9 (**Piecewise constant integral I**). Let I be a bounded interval, let P be a partition of I. Let f : I → R be a function which is piecewise constant with respect to P. Then we deﬁne the piecewise constant integral p.c. ∫[P] f of f with respect to the partition P by the formula $p.c. \int_{[P]}f := \sum\limits_{J \in P} c_J|J|$ where for each J in P, we let cJ be the constant value of f on J.
- Deﬁnition 11.8.5 (**p.c. Riemann-Stieltjes integral**). Let I be a bounded interval, and let P be a partition of I. Let α : X → R be a function deﬁned on some domain X which contains I, and let f : I → R be a function which is piecewise constant with respect to P. Then we deﬁne $p.c. \int_{[P]} f dα := \sum\limits_{J \in P} c_J α[J]$ where cJ is the constant value of f on J.
- ![](/images/anaylsis-rs.png)

### FTC
- Theorem 11.9.1 (**First Fundamental Theorem of Calculus**). Let a < b be real numbers, and let f : [a, b] → R be a Riemann integrable function. Let F : [a, b] → R be the function $F(x) := \int_{[a,x]} f$. Then F is continuous. Furthermore, if x 0∈ [a, b] and f is continuous at x0, then F is diﬀerentiable at x0, and F′(x0) = f(x0).
- Proof: f is bounded by M. |F(y) − F(x)| ≤ M |x − y|. Now let x ∈ [a, b], and let (xn) n=0∞be any sequence in [a, b] converging to x. Then we have −M |xn− x| ≤ F(xn) − F(x) ≤ M |xn− x| for each n. But −M |x n−x| and M |x n−x| both converge to 0 as n → ∞, so by the squeeze test F(x n) − F(x) converges to 0 as n → ∞, and thus lim n→∞F(x n) = F(x). Since this is true for all sequences x n∈ [a, b] converging to x, we thus see that F is continuous at x. Since x was an arbitrary element of [a, b], we thus see that F is continuous.
- Deﬁnition 11.9.3 (**Antiderivatives**). Let I be a bounded interval, and let f : I → R be a function. We say that a function F : I → R is an antiderivative of f if F is diﬀerentiable on I and F ′(x) = f(x) for all x ∈ I. 
- Theorem 11.9.4 (**Second Fundamental Theorem of Calculus**). Let a < b be real numbers, and let f : [a, b] → R be a Riemann integrable function. If F : [a, b] → R is an antiderivative of f, then f = F(b) − F(a). ∫


# Analysis II
## Metric Space
### Motivation
> Here we deal with convergence on sequences of different types of obejcts so we have limits on those. 
- Intuitively, when a sequence (xn) converges to a limit x, this means that somehow the elements Xn of that sequence will eventually be as close to x as one pleases. One way to phrase this more precisely is to introduce the **distance function** d(x, y) between two real numbers by *d(x, y) := |x-y|*.
- Lemma 12.1.1. Let (xn) be a sequence of real numbers, and let x be another real number. Then (xn) converges to x if and only if $\lim_{n\to \infin}d(x_n, x) = 0$.

### Space
- One would now like to **generalize this notion of convergence**, so that one can take limits not just of sequences of real numbers, but also sequences of complex numbers, or sequences of vectors, or sequences of matrices, or sequences of functions, even sequences of sequences. 
- An efficient way is to work abstractly, defining a very general class of **spaces** - which includes such standard spaces as the real numbers, complex numbers, vectors, etc. - and define the notion of convergence on this entire class of spaces at once. (*A space is just the set of all objects of a certain type* - the space of all real numbers, the space of all 3 x 3 matrices, etc. Mathematically, there is not much distinction between a space and a set, except that *spaces tend to have much more structure than what a random set would have*. For instance, the space of real numbers comes with operations such as addition and multiplication, while a general set would not. 
- It turns out that there are two very useful classes of spaces which do the job. The first class is that of *metric spaces*, the second is *topological space*. 

### Metric Space
- Roughly speaking, a metric space is *any space X which has a concept of distance d(x, y)* - and this distance should behave in a reasonable manner.
- Deﬁnition 1.1.2 (**Metric spaces**). A metric space (X, d) is a space X of objects (called points), together with a *distance function or metric d* : X × X → [0, +∞), which associates to each pair x, y of points in X a non-negative real number d(x, y) ≥ 0. Furthermore, the metric must satisfy the following *four axioms*: 
    - (a) For any x ∈ X, we have d(x, x) = 0. 
    - (b) (Positivity) For any distinct x, y ∈ X, we have d(x, y) > 0. 
    - (c) (Symmetry) For any x, y ∈ X, we have d(x, y) = d(y, x). 
    - (d) (Triangle inequality) For any x, y, z ∈ X, we have d(x, z) ≤ d(x, y) + d(y, z).

Examples
- Example 1.1.4 (**The real line**). Let R be the real numbers, and let d : R×R → [0, ∞) be the metric d(x, y) := |x−y| mentioned earlier. Then (R, d) is a metric space. We refer to d as the **standard metric on R**, and if we refer to R as a metric space, we assume that the metric is given by the standard metric d unless otherwise speciﬁed.
- Example 1.1.5 (**Induced metric spaces**). Let (X, d) be any metric space, and let Y be a subset of X. Then we can restrict the metric function d : X × X → [0, +∞) to the subset Y × Y of X × X to create a restricted metric function d|Y ×Y : Y × Y → [0, +∞) of Y ; this is known as the *metric on Y induced by the metric d on X*. *The pair (Y, d|Y×Y )* is a metric space and *is known the subspace of (X, d) induced by Y* .
- Example 1.1.6 (**Euclidean spaces**). Let n ≥ 1 be a natural number, and let R^n be the space of n-tuples of real numbers: $R^n= \{(x_1,x_2,...,x_n):x_1,...,x_n ∈ R\}$. We deﬁne the **Euclidean metric** (also called the **l2 metric**) $d_{l^2}: R^n \times R^n \to R$ by $d_{l^2}((x_1, \dots , x_n), (y_1, \dots , y_n)) := \sqrt{(x_1 − y_1)^2+ \dots + (x_n− y_n)^2} = [\sum_i^n(x_i− y_i)^2]^{1/2}$. We refer to $(R^n, d_{l^2})$ as the Euclidean space of dimension n.
- Example 1.1.7 (Taxi-cab/l1 metric).
- Example 1.1.9 (Sup norm/l∞ metric). $d_{l^∞}((x_1, x_2, . . . , x_n), (y_1, y_2, . . . , y_n)) := \sup\{|x_i− y_i| : 1 ≤ i ≤ n\}$
- Remark 1.1.10. The l1, l2, and l∞ metrics are special cases of the more general lp metrics, where p ∈ [1, +∞],
- Example 1.1.11 (Discrete metric). Let X be an arbitrary set (ﬁnite or inﬁnite), and deﬁne the discrete metric d discby setting d disc(x, y) := 0 when x = y, and d disc(x, y) := 1 when x = y. Thus, in this metric, all points are equally far apart.

### Convergence of sequences on Metric Space
> Basically, convergence definition is the same for different things except for the distance function. So we just need to define distance on our spaces and automatically we have convergence definition.
- > Copy of Deﬁnition 6.1.5 (**Convergence of sequence to L**). Let ε > 0 be a real number, and let L be a real number. *A sequence of real numbers* is said to be **ε-close to L** iﬀ a n is ε-close to L for every n ≥ N, i.e., we have |an− L| ≤ ε for every n ≥ N. We say that a sequence (a n)n=m∞ is **eventually ε-close to L** iﬀ there exists an N ≥ m such that (a n)n=N is ε-close to L. We say that a sequence (a n) n=m∞ **converges to L** iﬀ it is eventually ε-close to L for every real ε > 0.
- > Copy of Deﬁnition 6.1.8 (**Limits of sequences**). If a sequence (a n) n=m∞converges to some real number L, we say that (a n) n=m∞is convergent and that its limit is L; we write $L = \lim\limits_{n \to \infin} a_n$
- Deﬁnition 1.1.14 (**Convergence of sequences in metric spaces**). Let m be an integer, (X, d) be a metric space and let (x (n)) n=m∞be a sequence of points in X (i.e., for every natural number n ≥ m, we assume that x (n)is an element of X). Let x be a point in X. We say that (x (n))n=m converges to x with respect to the metric d, if and only if the limit lim n→∞d(x (n), x) exists and is equal to 0. In other words, (x (n))n=m converges to x with respect to d if and only if for every ε > 0, there exists an N ≥ m such that d(x (n), x) ≤ ε for all n ≥ N.
- > it is not necessary for the sequence x (n)to be denoted using the superscript (n); the above deﬁnition is also valid for sequences x_n, or functions f(n), or indeed of any expression which depends on n and takes values in X.
- Proposition 1.1.20 (Uniqueness of limits). Let (X, d) be a metric space, and let (x (n)) n=m∞be a sequence in X. Suppose that there are two points x, x′ ∈ X such that (x (n)) n=m∞converges to x with respect to d, and (x (n)) n=m∞also converges to x′ with respect to d. Then we have x = x′.

## Point-set toppology of metric space
- Deﬁnition 1.2.1 (**Balls**). Let (X, d) be a metric space, let x0 be a point in X, and let r > 0. We deﬁne the ball $B_{(X,d)}(x_0, r)$ in X, centered at x 0, and with radius r, in the metric d, to be the set $B_{(X,d)}(x_0, r) := \{x ∈ X : d(x, x_0) < r \}$.
- Deﬁnition 1.2.5 (**Interior, exterior, boundary**). Let (X, d) be a metric space, let E be a subset of X, and let x 0be a point in X. We say that x0 is an interior point of E if there exists a radius r > 0 such that B(x 0, r) ⊆ E. We say that x 0is an exterior point of E if there exists a radius r > 0 such that B(x 0, r) ∩ E = ∅. We say that x 0is a boundary point of E if it is neither an interior point nor an exterior point of E.
- The set of all interior points of E is called the interior of E and is sometimes denoted int(E). The set of exterior points of E is called the exterior of E and is sometimes denoted ext(E). The set of boundary points of E is called the boundary of E and is sometimes denoted ∂E.
- > If x 0is a boundary point of E, then it could be an element of E, but it could also not lie in E; For example, if E is [1,2), then 1 and 2 are boundary points with 1 in E and 2 not in E. 

- Copy of Deﬁnition 9.1.5 (**ε-adherent points**). Let X be a subset of R, let ε > 0, and let x ∈ R. We say that x is ε-adherent to X iﬀ there exists a y ∈ X which is ε-close to x (i.e., |x − y| ≤ ε).
- Copy of Deﬁnition 9.1.8 (**Adherent points**). Let X be a subset of R, and let x ∈ R. We say that x is an adherent point of X iﬀ it is ε-adherent to X for every ε > 0.
- Copy of Deﬁnition 9.1.10 (**Closure**). Let X be a subset of R. The *closure of X*, sometimes denoted $\bar{X}$ is deﬁned to be the set of all the adherent points of X.
- Copy of Deﬁnition 9.1.18 (**Limit points**). Let X be a subset of the real line. We say that x is a limit point (or a cluster point) of X iﬀ it is an adherent point of X\\{x}. We say that x is an isolated point of X if x ∈ X and there exists some ε > 0 such that |x − y| > ε for all y ∈ X\\{x}.
- Deﬁnition 1.2.9 (**Closure**). Let (X, d) be a metric space, let E be a subset of X, and let x0 be a point in X. We say that x0 is an **adherent point of E** if for every radius r > 0, the ball B(x0, r) has a non-empty intersection with E. The set of all adherent points of E is called the closure of E and is denoted $\bar{E}$.
- Proposition 1.2.10. Let (X, d) be a metric space, let E be a subset of X, and let x 0be a point in X. Then the following statements are logically equivalent. 
    - (a) x 0is an adherent point of E. 
    - (b) x 0is either an interior point or a boundary point of E. 
    - (c) There exists a sequence (x n) n=1∞in E which converges to x 0with respect to the metric d.
- Corollary 1.2.11. Let (X, d) be a metric space, and let E be a subset of X. Then E = int(E) ∪ ∂E = X\ext(E).
- Deﬁnition 1.2.12 (**Open and closed sets**). Let (X, d) be a metric space, and let E be a subset of X. We say that E is closed if it contains all of its boundary points, i.e., ∂E ⊆ E. We say that E is open if it contains none of its boundary points, i.e., ∂E ∩ E = ∅. If E contains some of its boundary points but not others, then it is neither open nor closed.
- Proposition 1.2.15 (Basic properties of open and closed sets).

## Relative Topology

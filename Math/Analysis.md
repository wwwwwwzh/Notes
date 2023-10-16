# Set Theory


# Natural Numbers
## Peano Axiom
Defines natural numbers, i.e. what is and what is not natural number
### Second Order
1. 0 is a natural number
2. successor to any natural number is a natural number (from here successor function will be the postfix ++)
3. 0 is not successor to any natural number
4. if two natural numbers x, y where x=y, then (x++)≠(y++), i.e. if (x++)=(y++), then x≠y 
5. if there is a property P pertaining to some natural number, and if P(0) is true and if P(n)->P(n++) for any n, then P(n) is true for any n. 

> Note that axiom 5 means if we have a set M that contains 0 and other things, P(0) is true, P(n)->P(n++) for any n in the set M, but P(n) is not true for every n, then M is not the set of natural numbers since it contradicts axiom 5. 

### Induction Axiom
By axiom 5, (A->B)->A is true is we are inducting on natural numbers. It also means if we want to prove a set is N, then we need to prove (A->B)->A is true.
- assuming A is T, got B is T: A->B is T, whole thing is true implies A is indeed T. 
- assuming A is T, got B is F: A->B is F, whole thing is true implies A can either be T or F.
- assuming A is F: A->B is T, whole thing is true implies A is T, a contradiction.

Note that if A is really true (by this if I mean it's true in every universe that matters), then B also has to be true, and everything implication is true.

### Recursive Definition
Want: define a function that gives a unique value to every natural number.

Bad way: 1) define a function that gives a particular value aₙ to a particular natural number n. 2) define another function that gives a particular value a(ₙ++) to n+1. 3) do this repeatedly for every natural number 

Good way: 1) define a function that gives a particular value a0 to 0. 2) define a function that gives you a(ₙ++) once you know aₙ 3) if aₙ is well defined (unique), then since a function is well defined, and since no other natural number will have successor equal to n++ except n (axiom 4), a(ₙ++) is also well defined 4) by axiom 5, all aₙ is well defined

This means that when defining an operation on N, one needs not define it explicitly for every natural number (e.g. define what n+2 by defining 0+2, 1+2, 2+2...). Instead, we only need to define two things. First is what the operation does on 0 (gives 2 in this case). Then define how to get a(ₙ++) from aₙ (a(ₙ++)=aₙ++). By the proposition of recursive definition, we have thus defined the operation on all N.

#### Example
1. define n+2: a0:=0+2:=2. a(ₙ++):=aₙ++
Proof: set aₙ to n+2. Note that +2 haven't been defined yet, but this doesn't matter. We assume n+2 is well defined, 
2. define n+m: a0:=0+m:=m. a(ₙ++):=aₙ++


## Addition
### Definition
For any natural number n, 1) n+0:=n 2) (n++) + m := (n + m)++.

# Integer

## Equivalence of Formal Subtraction and Subtraction
### Negation
Negation of an integer n: a--b is b--a, denoted -n. In particular, if n=n--0 is a natural number, -n:=0--n

### Subtraction
For integers a and b, a-b:=a+(-b)

### Formal Subtraction and Subtraction Proof
For natural numbers a and b, a-b=a+(-b)=(a--0)+(0--b)=(a+0)--(0+b)=a--b

# Rational 

# Real Number
## Cauchy Sequence
### Sequence
A sequence is a function from [0,) to rational numbers.
### e-steadiness
A sequence is e-steady if all its elements have distance less than or equal to e with any other element. 

## Equivalent Cauchy Sequence

## Formal Limit of Cauchy Sequence

Note that just like we construct integers with multiple natural numbers and a symbol --, we have constructed real number with infinite rational numbers and the LIM symbol

# Limit of Sequence
## Convergence 









# Appendix I: Logic
## Basics


## Propositional Logic
https://plato.stanford.edu/entries/logic-propositional
### Implication

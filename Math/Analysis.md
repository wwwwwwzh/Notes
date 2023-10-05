# Natural Numbers
## Peano Axiom
Defines natural numbers, i.e. what is and what is not natural number
1. 0 is a natural number
2. successor to any natural number is a natural number
3. 0 is not successor to any natural number
4. if two natural numbers x, y where x=y, then (x++)≠(y++), i.e. if (x++)=(y++), then x≠y 
5. if there is a property P pertaining to some natural number, and if P(0) is true and P(n)->P(n++) for any n, then P(n) is true for any n. 

> Note that axiom 5 means if we have a set M that contains 0 and other things, P(0) is true, P(n)->P(n++) for any n in the set M, but P(n) is not true for every n, then M is not the set of natural numbers. 

### Recursive Definition
Want: define a function that gives a unique value to every natural number.

Bad way: 1) define a function that gives a particular value aₙ to a particular natural number n. 2) define another function that gives a particular value a(ₙ++) to n+1. 3) do this repeatedly for every natural number 

Good way: 1) define a function that gives a particular value a0 to 0. 2) define a function that gives you a(ₙ++) once you know aₙ



## Addition
### Definition
For any natural number n, 1) n+0:=n 2) (n++) + m := (n + m)++.

> 
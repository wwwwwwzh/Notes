# Introduction
## Terminologies
### Proposition
- Bearer of truth or falsity.
- Formally, propositions are often modeled as functions which map a possible world to a truth value.


### Argument
An argument is a series of sentences, statements or propositions some of which are called premises and one is the conclusion. The purpose of an argument is to give reasons for one's conclusion via justification, explanation, and/or persuasion.

### Valid Argument
an argument is valid if and only if it takes a form that makes it impossible for the premises to be true and the conclusion nevertheless to be false. It is NOT required for a valid argument to have premises that are actually true, but to have premises that, IF they were true, would guarantee the truth of the argument's conclusion. 

### Sound Argument
In logic or, more precisely, deductive reasoning, an argument is sound if it is both valid in form and its premises are true. In propositional logic, a proof using modus ponens is valid, but sound iff its premises are true.

### Premise
A premise or premiss is a proposition to prove the truth of another proposition called the conclusion. Arguments consist of a set of premises and a conclusion.

An argument is meaningful for its conclusion only when all of its premises are true.

### Axiom
An axiom, postulate, or assumption is a statement that is taken to be true, to serve as a premise or starting point for further reasoning and arguments. 

The precise definition varies across fields of study. In classic philosophy, an axiom is a statement that is so evident or well-established, that it is accepted without controversy or question. In modern logic, an axiom is a premise or starting point for reasoning.


### Proof
In logic and mathematics, a formal proof or derivation is a finite sequence of sentences (called well-formed formulas in the case of a formal language), each of which is an axiom, an assumption, or follows from the preceding sentences in the sequence by a rule of inference.

> Is proof a more rigorous argument?

## Law of Thought
 

## Formal System
A formal system is an abstract structure or formalization of an axiomatic system used for inferring theorems from axioms by a set of inference rules.

A formal system (also called a logical calculus, or a logical system) consists of a formal language together with a deductive apparatus (also called a deductive system). The deductive apparatus may consist of a set of transformation rules (also called inference rules) or a set of axioms, or have both. A formal system is used to derive one expression from one or more other expressions.

In 1921, David Hilbert proposed to use the formal system as the foundation for the knowledge in mathematics.

### Formal Language
A formal language is a set of finite sequences of symbols. Such a language can be defined without reference to any meanings of any of its expressions.

### Formal Grammar
A formal grammar (also called formation rules) is a precise description of the well-formed formulas of a formal language. It is synonymous with the set of strings over the alphabet of the formal language which constitute well formed formulas.

### Formal Proof
In logic and mathematics, a formal proof or derivation is a finite sequence of sentences (called well-formed formulas in the case of a formal language), each of which is an axiom, an assumption, or follows from the preceding sentences in the sequence by a rule of inference.

### Definition
A formal system has the following:

- Formal language: a set of well-formed formulas, which are strings of symbols from an alphabet, formed by a formal grammar (consisting of production rules or formation rules).
- Deductive system: consists of the axioms (or axiom schemata) and rules of inference that can be used to derive theorems of the system.

In set notation, L = (A,Z,I) where
- A is the alphabet, a countably infinite set of elements called proposition symbols or propositional variables.
- Z is a finite set of transformation rules that are called inference rules when they acquire logical applications.
- I is a countable set of initial points that are called axioms when they receive logical interpretations.





# Propositional Logic

## Categorical Proposition
a categorical proposition, or categorical statement, is a proposition that asserts or denies that all or some of the members of one category (the subject term) are included in another (the predicate term).

### Forms
- A: All S are P
- E: No S are P
- I: Some S are P
- O: Some S are not P

### Square of opposition
- immediate inference: the truth or falsity of one of the forms may follow directly from the truth or falsity of a statement in another form.
- -![](/images/square-of-opposition.png)

> Contradiction means negation. Contrary means can't happen at the same time and is weaker than contradiction.

## Syllogism
Aristotle defines the syllogism as "a discourse in which certain (specific) things having been supposed, something different from the things supposed results of necessity because these things are so."

The Aristotelian syllogism dominated Western philosophical thought for many centuries. Syllogism itself is about drawing valid conclusions from assumptions (axioms), rather than about verifying the assumptions. However, people over time focused on the logic aspect, forgetting the importance of verifying the assumptions.

In the 17th century, Francis Bacon emphasized that experimental verification of axioms must be carried out rigorously, and cannot take syllogism itself as the best way to draw conclusions in nature

### Definition
- Major premise
- Minor premise
- Conclusion

Each part is a categorical proposition

# Predicate Logic


# Rules of Inference
## Modus Ponens
In propositional logic, modus ponens, also known as modus ponendo ponens, implication elimination, or affirming the antecedent, is a deductive argument form and rule of inference. It can be summarized as "P implies Q. P is true. Therefore Q must also be true."



# Notes
The fundamental problem of rigorously constructing ideas is that rigor relies on logic, but logic can't be defined by itself, much like the creation problem (how everything is constructed out of "nothing").

# Logical Consequence
## Implication
Implication as a propositional connective is strange because English if is ambiguous. For example, "I will do laundry if it's sunny tomorrow." In this case you assert the implication is true and act according to whether the antecedent is true or not. This is mostly used for planning. "My orange is red, but if it's red, it must be an apple". I might change my opinion of red->apple in this case and deciding if red->apple is true based on identity of my apple/orange is important.

## Rule of Inference About Conditional
### Modus Ponens (Conditional Elimination)
This is the "I will do laundry if it's sunny tomorrow." scenario. The assumption is that the whole sentence is true (evaluates to true). If we assume it's sunny tomorrow, then it logically follows or it's necessary that I will do laundry. 

### Deduction Theorem (Conditional Proof)
In mathematical logic, a deduction theorem is a metatheorem that justifies doing conditional proofs from a hypothesis in systems that do not explicitly axiomatize that hypothesis, i.e. to prove an implication A → B, it is sufficient to assume A as a hypothesis and then proceed to derive B.

### Modus Tollens


# Thoughts
## Logic and Association
Associationistic foundation of logic

# 


# Chem
Atoms are the building blocks of all matter, and all atoms of a specific element have the same behavior

Atoms can come together in countless arrangements and ratios, but when they come together in exactly the way shown above, this is the arrangement we can call a molecule of sugar.

Electrons change hands like money during reactions, so we can think of them as the transactional unit of chemistry.


The idea that the total charge of all molecules has to be the same before and after the reaction is one of the foundational principles of chemistry.


# Symmetry (very good, technical terms a little confusing)
## Contents
If we can't find a property that distinguishes two pieces of a system, then they must have the same behavior.

We will define a symmetry of an object to be a rigid transformation from that object to itself.

An equilateral triangle has 6 symmetries: 3 rotations and 3 reflections.

> a thing is symmetrical if one can subject it to a certain operation and it appears exactly the same after the operation.

> So the proof that an apparatus in a new position behaves the same as it did in the old position is the same as the proof that the equations when displaced in space reproduce themselves. Therefore we say that the laws of physics are symmetrical for translational displacements, symmetrical in the sense that the laws do not change when we make a translation of our coordinates.

Given a shape, if we take the **set of symmetries of the shape**, and consider their composition as a kind of “multiplication,” the following things are true:

(Identity) inverses, associativity

We purposely don’t include commutativity, because it doesn’t hold with all symmetries, including ours.

Nineteenth century mathematicians discovered many examples of algebraic systems satisfying these three axioms, and realized that instead of studying all of these systems separately, we could look at systems that satisfy these axioms in the abstract. This would be like studying all the special cases at the same time. Such a study gives a new perspective on all the special cases.

We have finally come to the idea of the group: an abstract object with a “multiplication operation” defined, that satisfies the three axioms.

### Examples of Groups
dihedral group Dn is the group of symmetries for a regular n-gon which includes reflections and rotations. has n rotational and n reflectional symmetries

The symmetric group Sn is the set of all permutations on the set {1,2,…n}, under the operation of composition. e.g. card shuffle

Cyclic group Zn

# History of Math (very good)
Math is an enormous and almost entirely unknown wilderness of patterns, ideas, and truths. If anyone has led you to believe otherwise, they lied.

The point is this — there are thousands of people who have been a part of building and mapping mathematics, and we can't tell all their stories. In many cases, no one even knows where an idea truly came from.

And, sometimes, the person who now gets credit for a piece of mathematics actually had little — or nothing — to do with its creation.

## Egypt
As with all grand construction projects, the construction of these pyramids required a significant amount of planning and computation, much of it complicated and new. In reality, it's the work of Amenemhat's scribes and engineers that has lasted — far longer than his pyramids, which are mostly ruins now.

### Binary
Ahmes (table of doubling for multiplication) is the very first mathematician whose name we know, and what we actually remember him for is mostly a duplication of work from hundreds of years before his time

## Prime
Prime numbers are like atoms (in the classical sense) — they are the building blocks out of which other numbers can be formed

There's one big problem, though. We know next to nothing about prime numbers themselves 

One of the problems **Eratosthenes** set out to solve was a fundamental one — how do we even figure out which numbers are prime?

Finding primes is hard, but finding composite numbers is easy by comparison. Since every number is either one or the other, if we find all the composite numbers and remove them, then all the numbers left over will be prime.

Although the primes don't have an obvious pattern, that hasn't stopped mathematicians through the centuries from looking for one.

Formulas to generate primes.  despite some temporary successes like these, no formula or generating pattern has ever been found for the primes.

### Nicomachus
Nicomachus of Gerasa, resident of Syria circa 60-120 A.D.,

wrote a textbook called Introduction to Arithmetic, containing one of the earliest examples of Greek multiplication tables,

represented and helped to lead the neo-Pythagoreans — a cult that worshipped arithmetic

Nicomachus believed that the physical world was not made out of atoms but instead out of numbers.

Nicomachus claimed that Introduction to Arithmetic was a manual for “happiness of life,” because it was an instructional guide for the study of the only things in the world that truly mattered — numbers.

His belief in an ordered, numerical universe led Nicomachus to look for (and find) order in numbers. He described many categories and properties of number that had been known prior to his day (many of them proven geometrically by Euclid), but he also described new and elaborate systems of numerical classification.

Any number that seemed to exemplify some property in an extreme way gained Nicomachus’s admiration. Sure, lots of numbers are even. But the **powers of two**  (2,4,8,16,32,…) are the most even numbers because their halves can be evenly divided all the way down to 1

Nicomachus was fascinated by all the patterns he could find in numbers, and he found them everywhere.

The prime powers of two make primes for first few numbers. Although a prime power does not guarantee that the result will be prime, it is true that if n is composite then 2^n−1 cannot be prime.

"if all the numbers were animals, only the perfect numbers were correctly formed. As far as he was concerned, all the other numbers had either too many or not enough parts."

proper divisors, abundant, perfect, deficient numberss

Nicomachus loved patterns so much that he sometimes found them where they didn't really exist.

### Mersenne primes

# Search Engine (interesting custom search engine and good example from scratch)
## catalogs, indexes, and concordances
As long as humans have been writing things down, humans have needed help remembering where things were written down.


clay tablet catalog->bound-catalog->card catalogs

However, card catalogs limit the ways you can search for information. If you want to find all the books by a particular author, they are great. If you want to find all the books published in Pakistan, or all the books that contain the word “puppy,” a card catalog is unlikely to be set up in a way that can help you.

A concordance was like a “search-engine-in-a-book” for a single document or work.

A concordance takes every single word that appears anywhere in a document, puts those words in alphabetical order, and lists every place in the document where those words appear.

It was only worthwhile to make a concordance when people really, really cared about answering this question “Where did I see that word before?”

Unsurprisingly, this was only done for works of particular importance like religious texts

### Index and Binary Search
Indexes are also designed to help the reader find information quickly and easily. A complete and truly useful index is not simply a list of the words and phrases used in a publication (which is properly called a concordance), but an organized map of its contents, including cross-references, grouping of like concepts, and other useful intellectual analysis.

Want: quickly looking up words and quickly inserting new words.

## Crawling the web
Where do you find web pages to put in your web search engine?

The answer involves graphs. And spiders.

Links->graph

explore the graph of the web (BFS)->Web spiders

In the late 1990s, Google invented page rank

## Searching
- AND, NOT, OR
- Exact phrase ("")

# ANN
## Contents
### intro
- a little connection ANN and NN
- basic one layer MLP (interactive)
- 2 layer
- digit recog interactivie

### Vision 
- context guessing
- nice optical illusions (maybe more insights behind phoonmena)
- very nice basic examples introducing pixels
- nice intro to edge detection
- "Later in the course, we'll see that this idea arises organically within neural networks. They even learn filters that optimize information processing for a particular database of images."

### Identifying shapes
- circle triangle square
- count neighbors (too sensitive)
- edge walk
- coarse edge walk
- In fact, in a 20×20 binary pixel image, there are already more possible pixel configurations than there are atoms in the universe. 
- [suggestion] harris corner detector or introduce any traditional CV methods?

### Tic-tac-toe
- Learning requires exploring new actions to complete a task. Trying the same wrong action doesn't lead to learning. Learning is faster when feedback not only tells you when you're wrong, but also how wrong you are.
- We just need to design a computer that can explore the space of board states, while giving it meaningful feedback on its moves. This is similar to how your brain learns.
- match box computer (physical stone picking as prob model)
- After this stroke of good luck, the matchbox computer loses more games, but around game 30, it's no longer consistently losing.
- no insight (?)
- Like Michie's matchbox computer, ANNs learn to perform challenging tasks by making small changes in response to feedback over a large number of exploratory attempts.

### Decision box
- play 1 or 2 and sum 
- mimics OR logic
- laser to build the logic
- then build AND
- then XOR
- why not add real history to this

### Activation Arithmetics
- count winner (0-1 activation, not clear why use this example)
- change laser strength
- The scale of the bias and the scale of the inputs are related.
- sum and decide 

### Decision Boundry (why the quitting example)
- So far, you've configured the Decision Box to count and add. It also mimics the behavior of logic gates — the building blocks of computer processors. In this lesson, we are going to teach the Decision Box to make predictions. We'll configure its LED to light up when a prediction is likely to be true.
- The LED on the Decision Box is activated when the activation condition is met
- predict quitting of robot based on #wins and lost
- When you want to make a prediction from data, it often helps to plot it.
- There's no guarantee that placing a decision boundary based on data you've collected previously will tell you something useful about the future, but this approach is often how neural nets make predictions.
- Placing a decision boundary is how a neuron, or a neural network, makes predictions from data.
- I1+I2 to I1-I2 as new decision bond

### XOR
- two neurons that do opposite things
- combine and do 2 layers
- why not give graph of deciison bond at end

### Marble Classification 
- Many tasks can be viewed as classification tasks with the right perspective.
- you can't tell which marbles are defective by how they look. But maybe there's some measurable set of properties that will let you predict which marbles are defective.
- Picking Features
- tangling features (joint prob)
- binary input with weight to decimal input with "unit conversion factor" so we can control slope (very strange way to introduce weight and input)
- linear bond finding

### Sigmoid (introducing probabilistic prediction)
- we'd like to design an egg classifier to predict how likely — or unlikely — it is that an egg belongs to a particular chicken.
- Probability helps us quantify this uncertainty.
- Now, we'll introduce another way of thinking about a neuron — as a mathematical function from inputs to numbers from 0-1

### Training with feedback
To use a neuron as a binary or probabilistic classifier, we first need to place a decision boundary between the two classes of your training data on a scatterplot. But what happens if there's no way to make a scatterplot of your data?

In this lesson, we’ll piece together guidelines for making classifiers flying blind, without any graphical cues. 

In this lesson, we will construct a set of rules to train your classifier — without a plot.

Binary neurons don't provide any feedback about how wrong your configuration is.

When we make changes to a configuration, we should at least know if a change brings us closer to the desired output.

Let's try building this gate again, but with a sigmoid neuron,

the output is always responsive to changes in the bias, but the weight only influences the output for inputs that are 1

If you have enough examples that are not inconsistent with one another, then this is a task perfectly suited for a neuron.

[maybe introduce how anything can be quantized and how input and error live on a smooth function so we can adjust things]

There may be many configurations that satisfy all the training data. Other times, there's no possible configuration, and the goal becomes finding a configuration that minimizes the number of training examples that produce erroneous output.

Finding weights and a bias for a set of examples is a delicate balancing act.

### Hidden Layers and Spiral (good interactive)
- xor again and now they have graph
- The hidden-layer neurons transform the input combinations so that the output neuron need only apply basic logical functions to perform the correct classification.
- After placing the decision boundaries around groups of points from the pink and green classes, all that's left is to configure the AND and OR logic performed by the output neuron
- brrief mention of overfitting

### Curve fitting (regression intro)
- decision to numerical value prerdiction
- It turns out that curve fitting — mimicking the mathematical form of data — is one of an ANN's strengths. ANNs with hidden layers are especially good at this.
- combining sigmoid (from combining decision bonds)
- would be nice to have high dimensional plots

### Universal Approximator
- Is there a limit to what kinds of functions a neural network can encode? Are all functions possible, or just certain ones?
- We can reduce the overall error even further if you place rectangles next to each other and adjust their heights. Rectangles are actually great function approximators.
- Any continuous function — a function without gaps or jumps — can be approximated by a series of rectangles to any precision.

### shape detector 2
- (nice case study) if pixels near the center of an image are dark, this ANN predicts that you drew a triangle. Of course, circles and squares are empty near the middle, but the hypotenuse of the triangle often crosses near the middle of the image.
- weight map
- add hidden layer
- At least one of the neurons in the hidden layer has learned to become a rudimentary symmetry detector to rule out squares and circles. During training, this ANN spontaneously learned that detecting symmetry helps it perform the classification better.
- more hidden neurons
- We have effectively removed the crutch used by the ANN with the five-neuron hidden layer to make near-perfect predictions.
- You may recall from the computer vision lesson that filters are used in computer vision for this very purpose. In a sense, this ANN has found a set of filters — all by itself — that help it classify shapes in this dataset.
- However, to get more improvement, we need to abandon the single-hidden-layer architecture of this ANN and replace it with a network that can exploit the spatial information that's encoded in the pixels.
- no CNN?

## Comments
### Interactive MLP
very good

### Digit recog interactive
amazing, how they made it

### Level of Math proficiency
what level are assumed, the intro to functions are not very obvious to non professionals but then why not make everyhing more formaal

## Suggestions
### Interactive MLP
no explanation on why more layers mean more power
### History of ANN

### More neural science
- lesson 3, difference in human and machine vision, maybe more about similarity

### Find My Key L4
hard to see how this relates to the learning strategy

### DB L5
should motivate them to think that the world is a robot then introduce probability

### L5-6
interresting intro with first bias only then weight

# LLM
## Contents (too short a lesson)
### Where are LLMs irl
- interesting interactive text generator

### n-grams
- Language models predict the next word by assigning a probability to each possible next word.
- more simple interactive text generator with bigram
- The bigram model only considers the last word, “question,” when making its prediction. It ignores the rest of the prompt. This is called the Markov assumption.

### n-gram prob with mini example
- 

### 
- The sky is… (maybe introduce joint prob and marginal and some )
- Temperature controls how random the output of a large language model is. (good intro to temperature, maybe  intuit about physics too)
- At temperature 0, the model eliminates all randomness from its predictions, so it chooses the most likely output every time. We call this type of model deterministic.

### epochs, loss and when to stop training

### Preprosessing
capitalization, punctuation, start token

### Tokenization
whitespace tokenization, affixes and punctuation, Byte-Pair Encoding


# Bayesian (great intro to info theory)
## Contents (using maximmally informative question as intuition)
### Guess Who
- Information theory, which is how to quantify and transmit information,
- Bayesian inference, which is how to update our beliefs in the face of new evidence, and
- causal Bayesian networks, which is how to infer causes from correlations.

We don’t know the answer to the question “Does the criminal have a yellow hat?”, but it's very likely that the answer is “no.” So, that question isn't very valuable, either. (hard for beginner to intuit, need more intuition on expectaion)

It seems a question's usefulness is somehow related to how much uncertainty we have about the answer. The most informative questions are the ones whose answer we are the most uncertain about.

- maximally informative questions
- maximal uncertainty
- some intuition about expectation/average

### Conterfeit Coin
4 coins, one might be fake, one reference coin, fewest tests to find the fake one.

weighing 2 and 2, Was this a good weighing scheme to pick first?

We can judge it by quantifying how many hypotheses are still possible, on average, after we get the answer. We'd like to make that number as low as possible because we need to try to eliminate possibilities using as few questions as possible.

we're looking for a weighing that splits the hypotheses into three groups of equal size.

### Language and Information
- information per syllable
- information per second
- universality of information transition speed with human languages

### Measuring uncertainty (!so good at explaining Shannon information!)
we could count how many maximally informative questions it would take to resolve our lack of knowledge. This is called information.

At the beginning, there's a 50% chance that the criminal is a triangle and there's a 50% chance that they're striped.

When we find out that the criminal is striped, we don't learn anything about whether they're a triangle — that probability is still 50%, the same as before. This means the questions are independent of each other: knowing the answer to one gives you no information about the other.

log rule of adding questions to resolve uncertanitty

### Unequal outcomes (very good)
So far, we’ve discussed how to quantify uncertainty in the case where there are several possibilities and we think they’re all equally likely. In reality, this is rarely the case.

Though there might technically be many possibilities, there are only a few that are very likely.

### Entropy (good intuition on non integer bits of info)
what it means to ask less than one question for biased coin?

more flips converge to true information and then divide by number of times which is exactly how you get thermo entropy. 

By trying to predict the result of two consecutive coin flips instead of just one coin flip, Alice can get closer to asking maximally informative questions.

For the most part, she's accomplished that, but the third question was forced to be one that wasn't very informative.

That formula tells us the number of maximally informative questions we'd need to ask, and that's why we fell short — it's not always possible to ask maximally informative questions.

 if you have some source of uncertainty like the words someone is about to say and you want to quantify how much uncertainty each word has, then there are two ways to go about it:

you could ask “yes” or “no” questions about each word separately, or

you could try to guess the whole thing at once.

The first way is wildly inefficient, but the second way leads to significant savings in the number of questions asked.

This kind of thinking has real applications — e.g. in the compression of files on your computer (not just text files).

After Shannon, we realized that information is so fundamental that its laws are respected by everything from physical objects to language.

### Information compression
The size of the file is how many yes/no questions the computer needs to ask before it knows exactly how the image should look.

The reason we say a PNG file is compressed is that those questions are chosen carefully so that the number of answers needed to identify the image is small.

We are going to use 8 bits to narrow down the color that we want. The first question is

“Is the color in the left or right half of this scale?”

what information do we have about an image before we send it that can help us compress it? changes are gradual

when images follow the patterns we expect, we can find out what they are quite efficiently.

### Bayes (very good intuition building, though i never liked the medical examples)
How can we put a precise probability to a belief? For example, can you put a number to the chance that you'll move to Toronto, Canada sometime in the future?

Probably not, because there are so many considerations to take into account. On the other hand, it's easier to answer a question like “How much more likely are you to move to Toronto than to Montreal?” You might answer, “I'm 10 times more likely to move to Montreal than Toronto because of the superior poutine.”
# Crypto
## Contents
### History of currency
- bartering
- commodity monies. Early examples of money helped to meet basic needs independent of their currency status and therefore had inherent value. but they’re not always the most convenient things to carry around or store.
- Some solutions are to use a commodity that's more convenient without worrying if it can meet a basic need or to trade things that represent the commodities. 
- credit
- Cryptocurrencies offer another way to exchange money in a way that's fundamentally different from credit cards, bank transfers, and other common methods of exchange. Cryptocurrencies accomplish a monetary system that doesn't depend on trust in a central authority or the people you're transacting with. It requires trust in mathematics and certain algorithms.



### Cryptonia
- gold can be stolen->infallible benevolent dragon
- hard to trade->notes with face value
- still can be stolen->notes signed to a specific person
- might still be stolen (harder to monetize now), need a lot of them, transfer amount can be changed->need signiture of holder to authenticate and tamper resistance->enchantable wax note

### Cryptonia cont.
- outsiders->need to find mathematical replacements for the functions of DragonBucks. In particular, they need something to replace the dragon so that people can verify that a transaction is valid, and they need replacements for spells as personal identities.
- To make it easier to talk about these replacements, we can give names to each part of the system. Since a Cryptonian’s spellcasting ability is personal to them, it's called a secretKey. The visual spell effect is connected to this spellcasting ability but can be publicly shared, so it's publicKey. A transaction note is a message, and the enchanted wax seal is a signature since it's used to prove who sent a message.

The crucial step is being able to verify a signature while hiding the secretKey that generated it. In this lesson, you'll learn about a mathematical function that hides information and can help us toward this goal.

System 1
1. Everyone picks a number s for their secretKey which they don't reveal, but they share 5×s as their publicKey.
2. Each message is converted into a number m.
3. The person sending the message produces a signature to prove they're the one who sent it by calculating m×s.

Most ordinary functions don't hide their inputs very well — you can reverse addition with subtraction, division with multiplication, squaring with taking the square root, and so on.

Fortunately, there are some functions that can't be easily reversed. For example, if we share the remainder after dividing a secretkey by 17 (mod)

If we can use mod to verify a signature while hiding the secretKey that generated it, that will help us mathematize the DragonBucks system.

### [Dragon->Decentralize](https://brilliant.org/courses/cryptocurrency/introduction-101/decentralizing-dragonbucks/2/)
After a couple of generations of living with DragonBucks, the townspeople no longer cared about the gold backing and allowed the dragon to get rid of it, keeping the gold hoard for herself in exchange for maintaining the DragonBucks system.

The people trusted that DragonBucks would be recognized when doing business in the town, even if they couldn't be traded to the dragon for a set amount of gold.

Removing the gold backing freed the Dragon to “mint” new DragonBucks, since each DragonBuck no longer needed to correspond to a gold coin in her hoard.

CryptoniaCoin doesn’t depend on the dragon and, instead, it would aim to put a copy of the ledger in the hands of every Cryptonian

minting new CCs should be tied to the work of maintaining the currency and whoever does that work should receive the newly minted coins.
# Work
## Potential topics
### *Active Inference*

### Music Theory

### Science/Calculus History

### History
Asking whys. Motivating people to ask questions that naturally lead to history. e.g. israel, china, why DC is like rome, political philosophies. in general, how do we get here questions.

### *Advanced ML*

### Language

### *Linguistics*

### Neuroscience

### Learning, Understanding, Sensing, Thinking

## Questions
### Ontology
#### Being Light
- where expect people to go next (links or more topics)
- when expect people to use this
- 
### Graphics
https://brilliant.org/courses/math-history/introduction-77/math-stories/2/ how long it takes for that triangle binomial animation and the fractal pattern and the historical figures (do they plan to use it elsewhere)

### Comparisons
khan, coursera, traditional classroom, online youtube viideos, books, tiktok

### User Research
do people like this and do they like this compared to other platforms (khan, coursera, traditional classroom, MOOC, etc). How many ppl like it.

### Wiki
plan for brilliant wiki and compare to wikipedia

### Dev
#### Search engine
how long it took, did someone happen to have the experience or they deccide to learn and build from sccratcch

#### Monitoring
- what are being logged (right-wrong ansers, time, daily activity, copy paste,)


# Suggestions
## UI
### hyperlink and popup 

### Custom font size and background color
## 
the idea is for them to come up with the thing we are trying to teach, the problem, the thought process, some partial solutions. it's not always possible and rarely easy, but I believe one original idea is worth a book of given knowledge. At least we should motivate them to ask one question after each course and try to solve it themselves. Solution doesn't matter. Their problems will hopefully stick with them so that every time they learn something new, they will think of the problem and try to improve their thought process in light of new knowledge. When they have a set of their own problems prompted by all kinds of different disciplines, they will be forced to think about them constantly, try new ways to think and establish some thinking framework, and new things they learn will be quickly incorporated to their framework. 

##  
### 
There  should be a grand relearning of everything. It's not necessary but there should be. People should relearn numbers, basic operations, basic physics, all those pre-college stuff. This time as an intellectual curiosity and a way to underrstand life and universe instead of as tools or compulsory requierments. It's a shame that few people got the chance to start appreciating how wonderful and thought provocing those "basic" knowledge is. 

### 
When explaining things, there needs to be motion, or change of sensory inputs wrt time in addition to static graphics, because that's how the universe works, that's how nature teaches us what she is. We develop the idea of gravity because things **fall**, that's a motion. We know how to grab a pen because we know from experience where our hands will be as time goes by if we execute certain action. It's the big list of things happening one after another that taught us how the world operates. So we should do the same in a teaching website. I do not know how necessary is interaction. I think it helps people to experient with things they can't experiemnt in real life.

Also I believe humans have evolved more complex or fasater visual and auditory system than language ssystem, as it came later. So usiing animations can really speed up the understanding and when rertrieving the knowledge it's faster tto process. 

###
the point is to get one idea to stick, not many ideas to forget. Visual learning works better for me in that regard. 

### Universal primary education source

## 
### On historical approach
know exactly where to put each lesson in, avoid confusion

### On grand principal of life and universe
- life as part of universe
- pattern, pattern recog, and prediction

### On abstract examples
some examples are too made up when real life examples can clearly demonstrade the ideas better

### A Heuristic approach to education
method: have a few mmajor themes and include all courses under those themes overlapping is ok. each course should direct to as many other courses under the theme as possiible and no course path shall be followed. stuednts are free to advance any course at anytime and are encouraged to explore answers they have from one course at another.

potential connections: bayesian prob and search engine
## Vs Khan Academy
### Khan
more traditional and test oriented

### Friend or Foe
"Which is better, Khan or Brilliant" is a common google search, and will be more common when brilliant gets bigger. Should brilliant seek to replace Khan or work in parralel?

Should Brilliant add test oriented courses? Is that a divergence from the original goal of this website? I hope brilliant will be known for fostering scientific mind instead of a good tool for studying for school. But this goal will alawys be a minority goal bc people will still study for tests in forseable future.
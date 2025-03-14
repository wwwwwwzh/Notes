# Puppets on String
least actiion

boltzmann distribution

# Associatiion

# Shadows in Cave

# Patterns

## Patterns in Space

## Patterns in Time

## Does God Play Dice
> Nature has established patterns originating in the return of events, but only for the most part.

# Science Primer
## Patterns
### Intro
You've proly seen this word in many settings,
pattern is more than finding the next number in a seriies of numbers or your carpet,
It could be claimed that pattern is why we are alive
### 
Before unswering why pattern is important or even define what it really is, let's see why we want patterns, even though  you proly not aware of it. If we seek something, then that thing is proly important

ancient gods, soothsayer, astrology

today, everyday life pattern

psychology of persistency. eg queen elithabeth

so why this thing I haven't defined but by now you proly have an intuition of, called pattern, is important? questions

we can foresee what is not available to us, in both space and time. we know that by tasting water to be salty we  ARE near ocean, we know that a dark cloud means there WILL BE rain. In terms of time, we often say patterns give us the ability to predict.

now we know why it's good to have it, is it bad to not have it? questions

the world descends into chaos. the pattern that washing machines don't run around eatiing people is now gone, the pattern that sun rises everyday is now gone, the pattern that your friend is a nice guy is none gone. 





## Plato's Cave
what is real/truth
levels of abstraction
truth in geometry and numbers
math
numbers and pebbles (real)->written symbols->symbol as ideas->are ideas real

## Does God Play Dice
truth in probability

# Machine Learning
why do we learn, why we evolved the ability to learn->find patterns (a snake means run away)->simple reflexes->blocks of tool nature/evolution gave us->neurons as association machines->associationism->functiions->blocks of tool we gave ourselves

what does a reflex really mean->how do we associate two things->why they should be associated->they happen one by one/together->

## What is Learning
Machine learning is about letting machines to learn, and people jump straight ahead to explain how to make that happen. What's missing is to explain what is learning. What do we mean when we, as humans, say we learned something.

### Build a List
Think about a simple scenario when you said you learned something, say, you learned that Newton was born in 1642. What does that mean. You probably mean that you can now answer the question "in what year was Newton born"[,= or that when people talk about Newton, you can jump in and say "he was born in 1642".] If you were a robot, then compared to before learning, now you can do exactly 1 more thing: to respond to the phrase "in what year was Newton born". 

Now let's discuss further what this simple person, which I'll call Alex, is capable of. First, it somehow stores a big list of things, each thing composed of two items. Whenever it encounters the first item it executes the second. The first item could be auditory or visual or any senses. The second could be anything a normal person can actively perform (speaking, moving, etc). Learning is just adding couples of items to this list. It's scary to think that you may just be this Alex. Think of something you can't do with such a list. At 7 A.M., you HEAR the clock, then you execute "get up". When you FEEL you are in standing position, you execute "go to bathroom". Jumping ahead, when you SEE a friend on the street, you execute "nod and smile". When you HEAR your friend say "have a brilliant day", you execute "say 'you too'". [question about what can't be done with Alex]

### What is a List
You'll see that I like to ask you these kinds of nonsense questions. But these are essential questions that lead to true understanding. 

What is a list? No trick. A list could be items written in pencil on a piecce of paper. It could be names inscribed on a stone. It could be an excel file. You can call many things lists. But can you define what a list is? You could build a collection of everything that can be called a list and define list to be a thing from that collection. You could also use our vague human language to write a dictionary definition, but then kids will attack your definition with qusetions like "can I eat a list" or "am I a list", to which you can't really have a confident answer. Without going deep into the philosophical background, you should keep in mind that there's this idea of a list and there are many things "in real life" that are instantiations of this idea of a list. 

> Plato's cave and theory of form.

Why am I talking about this? Our goal is to first understand what learning is and then try to "build it", following Feynmann's "what I cannot build, I do not understand". Now we have the idea of what learning could be. We have the idea that some kind of lists with some operations can mimic learning. How do we build it? By building I mean making something physical that can behave in ways we described above. 

All ideas can be converrted to mathematiical language (See Projection & Language). A list is an idea, therefore we can mathematically define a list and operations we descirbed for Alex. Once you have your ideas in math language, it turns our there is something called a computer that make math alive. People rarely associate a computer with its ability to compute. To sum up, once you have ideas recorded in math, someone can put these maths into a computer and make your ideas tangible. 

### Function
There are many physical insttantiations of a list. There are also many mathematical representations of a list. If you know some progamming, you know you can just use a class called list. But the representation we'll be using is a function. 

Remember what our list does. Given one item it gives some other item. That's exactly what a function is. If Alex wants to give exactly what is given, we can represent the list Alex keeps as a simple y=x function. You are proabbly wondering how we could rerpresent things like hearing the alarm go or say hello as numbers that could be used in functions, but as I said, all ideas can be converted to math. You could just represent english letters with 1 to 26 and hard code something like "say hello" to a bunch of numbers. That's a crude way, but I'm just showing that abstract ideas like behaviors and senses can really be representes as numbers. 

The reason we use function to represent a list is to save space. For the case where Alex wants to give exactly what is given, and say there are one million things that could be given, an excel like list will contain one million entries or 2 million items. But our function representation only needs y=x. This is an extreme case. You usually need more complex functions like y=2x1+3x2^3+x3*x4^2... No matter how complex your function is, it usually sstill saves more spacce than a regular list.

### Build a Web
Let's go back to the Newton example. Again, you learned that he was born in 1642. If you were Alex, you mean exactly that you added one thing to your list. A problem quickly emerges when you realize you were not Alex. You can do much more when you learned that Newton was born in 1642. For example, when discussing the year 1642 with a friend for whatever nerdy reason, you can say "Newton was born that year!", or when introducing Newton to a friend, you can begin with "born in 1642, ...". 

[question: If we try to make Alex capable of doing these new things, what is the main problem]

Aftering learning one simple sentence, Alex needs to add a bazillion thinngs to his list. It's possible that humans are doing this and it's possible to build a machine that worrks this way, but can we have something better than a big list?

How about a web? Just like the spider web. There are nodes and nodes are connected to other nodes in the web. Let's try to use a web and understand how Bob learns. 

When Bob learned that "Newton was born in 1642", he creates 3 nodes: Newton, born, and 1642. He then connects each one to all others (in this case it's a triangle). Sensing each node activates all nodes connected to it. So in the simplist version, hearining "Newton" will give "born 1642", hearing "1642" will give "Newton born", hearing "born" wiill give "Newton 1642". Not the best grammar but it makes sense. Notice how space perserving this is. If Bob learned 100 people born in the year 1642, 102 nodes and 201 connections are created [drawing needed]. To have the same function as perrson two (one word gives the other 2), Alex would need 300 couples of items in that list. [optional, about speed improvement]

### Funcctional
In Alex example we went practical and tried to repressent the list alex uses as a function. Now we want to do the same with Bob. 

Bob uses a web. A web, like a list, is an idea, and can be represented by many physical and mathematical things. The one we'll be using is called functional. 

A functional F works like this: if I give Newton to F, then instead of giving out a single y=1642, it gives a function f. If you then give 1642 to f, it outputs 1. If you give born to f, it also outputs 1. [image needed]. This might be confusing at the moment, especially the outputs of f which seems to mean nothing, but we'll explore one more thing about learning and see how those outputs, which curretly are all 1s, can be exploiited.

### Does God Play Dice
Think about "apple". What are you thinking of. You probably traversed through more than just one idea. You probably first imagined an image of an apple, perhaps then an apple of slightly different shape of color, maybe you also thought of the brand Apple. The point is, you have associated apple with many things, and when you see the word apple, these things come up in an order. In additoin, if I ask you 

How is this order determiined? Why are you first thinking about a fruit then the brand or vise versa? It's a deeply philosophical question discussed in consciousness and free will, but we'll try to oversimplfy it. 

Have you heard of determinism? Basiically it says everything in the future has been determined by the status of the world now. Let's add probablistic to this. Probablistic determinism. Fancy word. It measn that although yout don't know what number you'll get for your next dice throw, you know, deterministicly, that the chance of landing on any number is 1/6. The odds are determined, not the real outcomes. If you don't really understand this, don't worry.

We'll model the order in which ideas come up with this Probablistic determinism. 

### Summruy
We have seen that one way to understand huamn learniing is to imagine that there's a big web in our braiins and behaviors like reacting to certain senses and learning can be adequately expalined with this model. We have also seen that this web, together with its operations, can be represented as a functional. In the next chapter, instead of explaining how this functional can be actually progarmmed in a computer, we'll try to introduce learning from a whole different perspective and arrive at the same conclusions we reached here.

### Deep Web
We introduced Bob because . Now let's see what else you can do. Again back to the Newton problem. After learning that fact, which I believe you are confident that you have, what would you say in response to the following questions: "name a person born in 17th century", "give a birthdate of a famous person", "a british scentist". You probably have something to say to each of these phrases. But notice that we never talked about "a person", "17th century", "birthdate", "famous", nor "british scentist". We somehow automatically connected new facts to things we already know. 


### An Association Machine
The arguemnts so far has hopefully led you to believe that learning could be understood as association between things. This is by no means the best understanding of learrning and hopefully you'll discover somethinig else in the future or even better, an understanding of your own.



## Why do we Learn
We have tried to explain "how do we learn" and arrived at an abstract mechanism of how we might learn. Now let's ask "why do we learn" and you'll see that somehow it's necessary to have a learning mechanism like ours for us to be alive.

### Patterns
You've probably seen this word in many settings: patterns of a wall or carpet, patterns of numbers, patterns on a batterfly wing, patterns of someone's behavior, etc. 

What is pattern? Pattern is more than finding the next number in a series of numbers or finding repeated shapes on your carpet. Patterns exist everywhere and go much beyond daily objects and logic practices. It could even be claimed that pattern is why we are alive.

### Why we seek patterns
Before explaining why pattern is important or even define what it really is, let's see why we want patterns, even though you are proly not aware of it. If we seek something, then that thing is proly important

From ancient times we have been trying to find something regular out of this chaotic world, to predict things out of randomness. That's basically how ancient gods work. In many religions there's a god for each object, like river or sky or even doors. People tried to build patterns that goes something like "river is dry because river god is angry" and "river god likes kids". With this pattern they also claim the ability to predict things, like "giving kids to the river god will make river flood again".  
ancient gods, soothsayer, astrology

today, everyday life pattern

psychology of persistency. eg queen elithabeth

so why this thing I haven't defined but by now you proly have an intuition of, called pattern, is important? questions

we can foresee what is not available to us, in both space and time. we know that if water from this river is salty then we ARE near ocean, we know that a dark cloud means there WILL BE rain. In terms of time, we often say patterns give us the ability to predict. [more examples, sunshine after rain means rainbow, bookshelves labeled with A,B,C measn next one is labeled with D, your girlfriend says she's fine which means she's not fine]

now we know why it's good to have it, is it bad to not have it? questions

the world descends into chaos. the pattern that washing machines don't run around eatiing people is now gone, the pattern that sun rises everyday is now gone, the pattern that your friend is a nice guy is none gone. 

### Our Universe Speaks in Patterns

### Recognize Patterns

### Connecting
early ways involve mechanical robots that physcially connect things, https://cyberneticzoo.com/mechanical-elephants-horses-and-other-walking-animals/
early modern ways to build machines thaat minic human learning involve electro-mechanical robots that learn by physically switching and moving electric components. Big names like Alan Turing and Claude Shannon have all tried tto build such robots and you will be amazed by how these simple, mechanical robots can do.
https://cyberneticzoo.com/robots/1937-professor-arcadius-durand-descamps-french/

using matchbox to play tic-tac-toe
## Going Deeper
### Names
There are three people on earth called Andrew, Alice, and Giovanni. Without knowing anything about them, which two of them do you think are related? 

You probably chose Andrew and Alice, unless you have relatives who happen to have 2 of the names above. This seems like a very basic ability, but it's in fact one the most amazing things about learning.

How did you do that? You implicitly understand that Giovanni is proabbly an Italian name while the other two are probably not Italian. Your brain automatically associates names with a bunch of useful things like oriigni, sex, is that someone you know, etc. 

Without  this ability,  if I ask you again which two are likely related, you would either guess randomly or learn it by going through a list of names of every person on earth and see how many times 2 of the names are actually related. 
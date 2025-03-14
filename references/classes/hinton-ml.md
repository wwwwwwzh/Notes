https://www.cs.toronto.edu/~hinton/HintonMumbai.pdf

I think the whole history of AI might have been quite different if the two major figures who believed in neural nets in the 1950's had not died before their time. One was Alan Turing and the other was John von Neumann. Neither of them could be accused of being ignorant of logic, but they were both convinced that it was not the way to understand how the brain computed.

The rejection of neural networks was even more vociferous in the school of linguistics led by Noam Chomsky. I remember watching a TV program called Nova about linguistics. One after another, the leading linguists said that ... language ... is not learned.

https://www.youtube.com/watch?v=cbeTc-Urqak&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=1
1. motivation: object recog, image recog, new program, speech recog
2. neuroscience basics
3. **models of neurons** (philosophy of idealization and math). 
    - Linear neuron y=Σxw+b 
    - Binary threshold (McCulloch-Pitts), activation as truth value of proposition (note the problem of non-probabilistic intepretation of thoughts): y=I(y>0)
    - Rectified Linear (ReLU): 
    - Sgmoid (logistic unit)
    - Stochastic binary
    - Stochastic relu (y is poisson rate)
4. example of digit recog with simple pattern learning
5. supervised (regression vs classification), unsupervised (high-dim input typically live near one or more low-dim manifold, PCA assumes one such planar manifold, clustering assumes one discrete feature) and RL. 
6. (2.1) architectures of NN: FFN, RNN, Symmetrically connected network (Hopfield net): ![](/images/symmetric-net.png)
7. perceptrons, Minsky and Papert. Training consists of adding (if incorrectly 0) or substracting (if incorrectly 1) the input to the weight vector
8. **geometric view of how perceptrons learn** ("to deal with hyperplanes in a 14-d space, visualize a 3-d space and say "14" to yourself very loudly"). Imagine a space of weights so each weight is a vector. Now the activation of a neuron is the dot product of a weight and a input vector. The plane normal to the input vector is the decision boundary where all weight vectors on the side of the plane WITH the input vector gives positive values, and the side WITHOUT the input vector gives negative values. **Cone of solutions** (of weight vectors). ![](/images/solution-cone.png) Has to be **convex** (two good weigths sum to good weight)
9. proof that adding input vector to current weight minimizes a distance to the cone of solutions
10. perceptrons can't learn XOR (with geometric proof). Group invariance theroem by Minsky. 
11. (3.1) instead of moving weights to good weights, move output closer to real output. This introduces the squared error measure and the chain rule supported updating rule **dE/dwᵢ=xᵢ(y_true-y)**. (evolutionally, this might be how certain central neurons emerge to have a better numeric measure of various over neurons). Note that this rule is the perceptron updating rule (adding or sub input vec) with residual error as "speed"
12. **error surface**. Imagine the aforementioned perceptron weight space with one extra dimension of error. The batch update rule in 11 is steepest descent on the error surface. ![](/images/error-surface.png)
13. derivative of logistic function: **$\frac{\partial y}{\partial w_i}=x_iy(1-y), \frac{\partial E}{\partial w_i}=x_iy(1-y)(y_{true}-y)$**
14. **Backprop**. Random evolutoinal perturbation of weights (inefficient) or the output of the neurons (still inefficient). 
15. tricks. mini-batch, learning rate adaptation, overfitting (intrinsic data noise, sampling bias that might lead to learning a bad distribution, Hinton calls it accidental regularity as opposed to "real regularity")
16. **[4.1]**(https://www.youtube.com/watch?v=ReUrmqStBd4&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9&index=16) **Family tree example** (as used in Nature): ![](/images/family-tree.png) we want to learn the relations proposition (eg. Colin hasMother Victoria). To learn all such relations involve iterating over all such triples. We use a network to directly learn these relationships. ![](/images/family-leanring.png)![](/images/family-leanring2.png) The 6 bars are the 6 neurons of distributed encoding of person 1 in previous figure. The 24 blocks are the activations of that neuron from the 24 inputs, ie, the 24 people, where top 12 are English and bottom 12 are Italian. Note that the row 1 col 2 neuron learns to differentiate *nationality*. Row 2 col 2 neuron learns *generation*. Row 3 col 1 learns *gender*.
17. Debate of concept as vector or relation. Distributed representation: ![](/images/concept-debate.png)
18. **Softmax** and cross entropy loss
19. Example of speech recog (ambiguity in acoustic signal to words: recognize speech vs wreck a nice beach). Trigram algorithm and its limitation of only accounting for previous 2 words. Hinton wants a feature representation of words. **Bengio** (worse than trigram): ![](/images/bengio-next-word.png)
20. Because the approach above requires a large number of logits for each word (the zs before applying softmax), change it so the input is 3 words where 3rd word is candidate and output is a single logit. Then fix 2 input and try all candidate and get all logits for one training run. Hinton also uses a direct 2 input one output approach and get the output word from a tree structure. Another approach aims to learn just the word code by checking if a middle word is right among 10 context words. **t-SNE** of word code: 
21. (5.1) Why **object recog** is hard: segmentation, lighting, deformation, human centered (a chair is something to sit on and lacks a distinct physical description), viewpoint
22. viewpoint invariance: redundant feature (i think this is used very often in human and might have origins in allocentric place cells), normalize box (bad), replicated feature detectors (might also be extensively used in human especially in vision system and can handle small variation in viewpoints)
23. **CNN** for digit. replicated feature detectors
24. CNN for image. AlexNet, arch and tricks (random crop, dropout)
25. （6.1）**Stochastic gradient descent** (data are redundant so gradient from a portion is the same as the whole)
26. tricks for SGD
27. momentum method
28. adaptive learning rate
29. rmsprop
30. (7.1) **Sequence modeling** intro. Semisupervised learning (motivated by the problem that input sequence and output sequence are different in domain, so we use the input itself as target signal). Motivation of RNN from standard hidden state dynamical models (where a state evolves probablistically according to its internal dynamcis, is influenced by exterior influences, and produces observations): linear dynamical systems, Kalman filtering, Hidden Markov model (Hinton says hidden units are so called because he got the word from HMM). HMM is limited by its discrete state space which grows exponentially with information needed to turn state to prediction/observation. RNN uses distrbuted state encoding to overcome the HMM state problem and is non linear to overcome the LDS problem. "think of the hidden states of RNN as encoding the prob dist over the hidden states of LDS or HMM"
31. Backprop through time. RNN as MLP with same weights across layers
32. binary addition example
33. 
34. 
35. Hessian free method. Conjuugate Gradient


Body of notes should be moved to appropriate category specific paper notes ASAP

# 2023
## Nov
### 10
- [ROME]: 1) Causal Tracing of Factual Associations. "we posit a specific mechanism for storage of factual associations: each mid-layer MLP module accepts inputs that encode a subject, then produces outputs that recall memorized properties about that subject. Middle layer MLP outputs accumulate information, then the summed information is copied to the last token by attention at high layers." 2) Intervention by updating W as Key-Value storage approximation
### 12
- [Synaptic Plasticity]: Homeostatic plasticity (normalization). A thin line lies between synaptic activity eliciting a potentiation vs a depression
- Synaptic Plasticity Forms and Functions: ![](/images/SP-review-1.png)
### 14
- [Attractor](http://www.scholarpedia.org/article/Attractor_network): Stable, persistent activity has been thought to be important for neural computation at least since Hebb (1949). Amit (1989), following work on attractors in artificial neural networks, suggested that persistent neural activity in biological networks is a result of dynamical attractors in the state space of recurrent biological networks.
- [Neural Computation of Head Direction]: Ring attractor network for head direction and biological substrates in mammal and insects
- How Flies See Motion: algorithms for motion detection and how flies implement them

### 15
- https://news.mit.edu/2012/conjuring-memories-artificially-0322
- Feynman 330: movement of center, hallucination, seeing back of head with accurate finger movements
- Dream: 
- https://www.rockefeller.edu/news/33790-scientists-discover-brain-region-linking-short-term-to-long-term-memory/: anterior thalamus appears to referee memory-consolidating interactions between the hippocampus and the cortex

### 16
- Neural Circuits for Emotions: ![](/images/emotion.png)
- https://news.mit.edu/2017/neuroscientists-discover-brain-circuit-retrieving-memories-0817: Summary: recalling a memory requires subiculum, formation requires CA1. Experiment: In one group of mice, inhibited neurons of the subiculum as the mice underwent fear conditioning, can recall. In another group, inhibited subiculum neurons after fear conditioning had occurred, cannot recall. Other experiments revealed that the direct circuit from CA1 to the entorhinal cortex is not necessary for memory recall, but is required for memory formation.
- https://news.mit.edu/2017/neuroscientists-identify-brain-circuit-necessary-memory-formation-0406: memories are stored in both the hippocampus and the prefrontal cortex. However, the engram cells in the prefrontal cortex were “silent”. When prefrontal engram becomes active, hippocampal engram cells became silent. However, reactivating those cells with light still prompted the animals to freeze. In the basolateral amygdala, once memories were formed, the engram cells remained unchanged. Others: Kitamura says he believes that some trace of memory may stay in the hippocampus indefinitely, storing details that are retrieved only occasionally. “To discriminate two similar episodes, this silent engram may reactivate and people can retrieve the detailed episodic memory, even at very remote time points. ![](/images/memory-formation.png)
- https://news.mit.edu/2017/neuroscientists-build-case-new-theory-memory-formation-1023: Summary: plasticity, while necessary for a memory to be initially encoded, is not necessary for its subsequent long-term storage. Experiment: fear conditioning on mice; inhibited the synthesis of cellular proteins immediately after the training; can't recall with natural cues, can be reactivated artificially; treating the mice with PAK1 was enough to grow new synapses between engram cells and can recall naturally after days.

### 17
https://www.reddit.com/r/explainlikeimfive/comments/3mnpio/eli5why_do_we_feel_a_strange_sensation_when/

### 18
- Brain and Behavioral Asymmetry: Asymmetry in motor (escape, rotational swim), perceptual (foraging, social, mating)
- https://news.mit.edu/2011/face-perception-0109: left fusiform gyrus first (?) process face features, right have consistent pattern of activation for genuine face versus face like images.
- https://web.mit.edu/sinhalab/Papers/Transformation_generalization2020.pdf:  Summary: invariant representations strengthen as the
number of transformed categories in the training set is increased. This is much
more prominent with local transformations such as blurring and high-pass filtering,
compared to geometric transformations. Thought: natural convergence?
- [Autism as a disorder of prediction](https://www.pnas.org/doi/epdf/10.1073/pnas.1416797111): With compromised predictions, an individual with autism inhabits a magical wherein events occur unexpectedly and without cause. temporally unfolding Markov systems. Examples: 1. Insistence on Sameness. 2. Sensory Hypersensitivities 3. dynamic object 4. theory of mind 5. island of proficiency

### 20
- [Navigate Cities with Vector Based Navigation](https://news.mit.edu/2021/how-brain-navigates-cities-1018): Instead of calculating minimal distances, we minimize angular displacement — pointing directly toward the destination as much as possible.
- [Vision Transformer Quadrupedal Locomotion 2021](https://arxiv.org/pdf/2107.03996.pdf): See Robotics

### 22
- [Movie reconstruction MRI 2011](https://www.youtube.com/watch?v=nsjDnYxJ0bo)
- 

### 23 
- [Hebbian CNN](https://link.springer.com/chapter/10.1007/978-3-030-30642-7_29)
- Neural Decoding of Visual Imagery During Sleep 2013: machine-learning models predict the contents of visual imagery during the sleep-onset period 
- Neural Correlates of Dream Lucidity 2012: bilateral precuneus, cuneus, parietal lobules, and prefrontal and occipito-temporal cortices activated strongly. ![](/images/lucid-dream.png)
- [Diffusion MRI decoding 2022](https://doi.org/10.1101/2022.11.18.517004): ![](/images/diffusion-mri.png)![](/images/diffusion-mri-2.png)

### 24
- Markov Chain: transient and recurrent state, steady state as equilibrium
- Statistical Methods: MAP, MLE, MSE
- Ice age: a good story doesn't need to show all moral implications all at once, reflections should naturally unfold with the story

### 25
- Six Easy Pieces: Feynman has an amazing ability to associate the most general aspects of daily life to physics such that abstract concepts quickly connects to familiar memories and imaginations.
- [CBMM Deep learning theory](https://youtu.be/pad023JIXVA?si=LAT_LpyvbAjPb3j7): Why DNN converge: large parameter space vs small gradient space of Lz ![](/images/why-convereg.png)

### 26
- Electrophysiology reveals that intuitive physics guides visual tracking and working memory 2023: EEG evidence of how visual tracking can be interrupted and restored by violation of expectation and explanation![](/images/EEG-intuitive-phys.png)
- [Intuitive physics learning in a deep-learning model inspired by developmental psychology 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9489531/pdf/41562_2022_Article_1394.pdf): object centered (object segmented autoencoder) and LSTM to predict next frame. Calculate VOE by error between prediction and actual. ![](/images/ml-voe.png)
- [Offline Learning](https://www.youtube.com/watch?v=k08N5a0gG0A): See offline learning of RL
- Offline Reinforcement Learning as One Big Sequence Modeling Problem 2021: See [Robotics](/CS/ML/Robotics.md)
- [FiLM](https://arxiv.org/pdf/1709.07871.pdf): method to embed text tokens to image network so image network output is conditioned on text input
- [Token Learner](https://arxiv.org/pdf/2106.11297.pdf): 
- RT-1 2022: See [Robotics](/CS/ML/Robotics.md)

### 27
- [PaLI](https://arxiv.org/pdf/2209.06794.pdf): Text+Image->Text with ViT and encoder decoder ![](/images/PaLI.png)
- PaLM: A LLM with hardware training advancement
- RT-2 2023: See [Robotics](/CS/ML/Robotics.md)
- GATO 2022: See [Robotics](/CS/ML/Robotics.md)

### 29
- [Visual MAE 2021](https://arxiv.org/pdf/2111.06377.pdf):![](/images/vmae.png)![](/images/vmae-2.png)
- [Segment Anything 2023](https://arxiv.org/pdf/2304.02643.pdf):![](/images/sa.png)
![](/images/sa-1.png)

### 30
- [CoDi](): ![](/images/codi.png)
- [Real-World Robot Learning with Masked Visual Pre-training 2022](https://arxiv.org/pdf/2210.03109.pdf) See [Robotics](/CS/ML/Robotics.md)
- [OVRL-V2 2023](https://arxiv.org/pdf/2303.07798.pdf) See [Robotics](/CS/ML/Robotics.md)
- [Masked World Models for Visual Control 2022](https://proceedings.mlr.press/v205/seo23a/seo23a.pdf) See [Robotics](/CS/ML/Robotics.md)
- [Transformer NEXT-FRAME](https://arxiv.org/pdf/2108.08224.pdf): frames->next frame on MNIST videos
- [Sparse Transformer 2019](https://openai.com/research/sparse-transformer)
- [VQGAN](https://arxiv.org/pdf/2012.09841.pdf) ![](/images/vqgan.png)
- [VQVAE](https://arxiv.org/pdf/1711.00937.pdf) Try https://github.com/airalcorn2/vqvae-pytorch
- [Dreamer 2019](https://arxiv.org/pdf/1912.01603.pdf): See [Robotics](/CS/ML/Robotics.md)
- [VideoGPT 2021](https://wilson1yan.github.io/videogpt/index.html): See [Video/590](/CS/ML/Video/590.md)
- [OpenAI VPT Minecraft 2022](https://openai.com/research/vpt): See [Robotics](/CS/ML/Robotics.md)

## Dec
### 11
- Lottery Ticket Hypothesis
- Early Bird Ticket
- Grokking:
- ROME
- Learning and Education

### 13
- MaskGIT: Summary: generative transformer beats GANs with iterative masked modeling instead of autoregressive. ![](/images/maskgit-1.png)![](/images/maskgit-2.png)

# 2024
## Jan
### 20
[Pleasure systems in the brain](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4425246/)
- In a sense, pleasure can be thought of as evolution’s boldest trick, serving to motivate an individual to pursue rewards necessary for fitness. 
- rewards involve a composite of several psychological components: liking (core reactions to hedonic impact), wanting (motivation process of incentive salience), and learning (Pavlovian or instrumental associations and cognitive representations) 
- The basic sensorimotor circuitry of these affective expressions resides in the brainstem, but such affective expressions are not mere brainstem reflexes, but rather are hierarchically controlled by forebrain structures. loss of dopamine doesn’t necessarily reduce pleasure after all

[Neural correlates of long-term intense romantic love](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3277362)
- early-stage romantic love and long-term romantic love: right VTA and posterior caudate body; bilateral anterior caudate body, mid-insula and posterior hippocampus; and left cerebellum. The right amygdala showed deactivation in early-stage love, while the left amygdala showed activation for the long-term love group.
- maternal love and long-term romantic love: right VTA/SN, PAG and hypothalamus; bilateral SN, anterior caudate, putamen, posterior GP, thalamus, mid-insula, dorsal Raphe and posterior cingulate; the left anterior cingulate and insular cortex.
- maternal, early-stage and long-term love: VTA, bilateral anterior caudate body and middle insula.

### 25
[The Neural Basis of Timing: Distributed Mechanisms for Diverse Functions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5962026/): Time and space might be similar in brain. The passage of "physical time" corresponds to "physical progression" of events. So a simple timed task could just rely on environmental inputs. *In fact, sometimes we count by periods of background noise*. / taxonomy of time: requiring a precise internal clock or not (simultaneity, temporal order vs Duration discrimination, reproduction, production); sensory or motor;

pacemaker-accumulator models, Weber’s law (standard deviation of the response time across trials increases linearly with the mean time of the responses)

> When the world is better than expected, phasic increases in dopamine neuron activity may act to slow striatal population dynamics, either by causing a net decrease in the excitatory drive to the striatal network or by altering the dynamics of synaptic plasticity. Such an effect may underlie common observations that fearful or pleasurable experiences can have opposites effects on perceived duration 

Space time is perceived because they are. Spatial and temporal patterns of the "real world" should remain when processed. All our sensory modality captures both space and time.
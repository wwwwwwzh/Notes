# Arguments
## AI related
- when people say LLM is stochastic parrots, remind them that many people behave even more like stochastic parrots in certain situations.
- the repetition in LLM can be seen in humans as repeating same melody or typo like activativation. 
- people who argue for the extreme form for object invariance (humans recognize an object from every angle), they don't consider for example being at the same place but with different emotional context (but maybe it's just week memory or complex environemnt cue), or for example knowing describe but can't figure out what scribere is when learning latin.
- LLM is like combined intelligence of the swarm, but it's possible that some humans are smarter than all humans combined. They use a distribution of thought that's not present in any major distribution of the training set and can generate ideas that would take LLM forever to sample. 

## Politics
- Saying Mao has predicted things in his essays and is therefore god is same as thinking Da Vinci is knows everything because of his notebook or Freud as god because he can explain everything
- 禁止不利于社会和谐的言论，让每个人都觉得自己在正确的道路上；由国家宏观调控个人价值观
- counterargument to chinese who think chinese history makes china great: science can be carried along by a few people, but politics is controlled by every person, and it's impossible that everyone learns politics. Thus no matter what history taught us, and no matter how smart the historians and leaders are, history must repeat itself. (Note that a requirement for all is destined to fail while a requirement of existence (in the mathematical sense) is almost surely to win, as a consequence of probability theory)
- 历史书第一课应该强调“以美国，欧盟为首的希腊-罗马文明，以中国为首的东亚文明，以印度为首的印度文明，和以阿拉伯，伊朗为首的中亚文明，都是同样古老且延续的文明”。此举意在弱化国家概念在文明比较中的影响，其他类似于四大文明古国的概念应在大学期间，学习完现代国家概念后引入。
- Are the pursuit of Capitalism and Communism different? Capitalism is more natural and the whole historic progression towards private property, resulting eventually in America, is so natural that people hardly question it. Private property is one the natural drive. So  Communism seemed very strange at the time. However, group is also a natural drive as ancient as private. So in this light, the difference is a result of social influence when one grows up. 

## Others
- people who try and learn from failures are like off policy and those who think before they do are on policy. The former updates their behavior only after some significant events while the later constantly reinforce their plan and avoid large changes

# Finance
- whether double touch bottom can reverse depend on small traders


# Others
- the lagrange euler has solution because p  and q are foundamentally connected and this property is used when saying delta p is d(delta q)/dt
- my experience with deadline and money is that you must have constraint to develop certain features, and the way people do it is to explore a magnitude more options when they have the consrtaint.


- in winter i can do goal directed behavior and can be activated by human interaction otherwise i'm drowsy especially when thinking hard theory problems. (need to document effect on physical exercise)


# Project proposals
## Small
- [ ] graphic proof of why delta function is sum of all freqeuncies by showing: given any theta not equal to 0, we can make all those e^iwt+theta cancel out
- [ ] gpt2 MLP value vectors antivalue
- [ ] transcoder
    - [ ] fully linear MLPs end to end usiing exisitng layers
    - [ ] end to end linear MLPs training
- since attn pattern uses softmax, contribtion of the output at a token position from all previous tokens should concentrate on just one or two previous tokens. So a information flow diagram can be automatically created for each forward pass. 

## Big
### Agent collab
- when multiple agents are powerful, you might want to copy one's answer to another to ccross-validate. is there an efficient way for many chatbots to converse?

### Computer Tool (currently framed under AI agent)
- (this can now be built on codes like browser use) universal human memory enhancement on computer, take in all user info and organize them and generates a tree like structure based on time and topic. For example, every websites i visited these days or books i read or messages i sent should be summarized and organized to provide easily accessible memory tool (i can ask what i learned yesterday or what are my thoughts for a certain topic)
- online annotator where instead of highlighting most highlighted sentences or comments, use AI to summarize annotations so people can search if they don't understand sth (should also work on things like Piazza)

### Social
- an online wild chicken university where everything is setup other than the campus. Find actual phd students who want to teach weird shit like cat management or toilet cleaning. Classes are formalized and everything is just like a university class. Give certificates of courses so they can share on social media. When it gets popular there will be acctual intellectiual contents and it essentially becomes a non standard light weight MOOC. 

# Might study
- should check behavior of pretrained model but give pairs like "Paris is beautiful" and "Paris is not beautiful" and see what happens. This might indirectly leads to invariance.
- we can not only steer concept vectors in networks to influence the words that got out, we can also steer word we use to influence what concept we can possibly use. For example, market communism or democratic authoritarianism might not be concepts most people have, but by moving the words themselves we now "create" new concepts.
- we can model NN as a differential system and describe the phase space trajectory of different inputs.
- it might be interestig to study the distributiion of rewards in human population. For example, some people get more reward from romantic relation or money or wisdom  or power etc

## Neuro
- when studying understanding of physical laws, it's important to study why those laws disappear in dreams. (however, emotions still exist so it appears our learned understansing of the world doesn't affect emotions)


# Reflections
- 2025.3.1. On the MATS application experience. I corresponded with Andy on 2.16 and noticed Neel's applciation the next day after joining ARENA slack. I started learning through the transformer module immediately for a week (2.18-21) and started looking into deepseek on 22nd (Saturday). Didn't understand because modern LLM use RL so started ARENA RL module and learned all PPO RLHF and GRPO stuff on 23rd. I started working on code the next Monday (24th). First 2 days were not productive since I never coded on LLM before. Initial insights were gained on Wednesday about prompting. Most work were done Thursday and Friday. Learned about the value updating paper late Thursday and mixed it to my work Friday so it's possible. 

# Bug Fix
## ML
### R1-QW project
if you see `ValueError: not enough values to unpack (expected 2, got 1) after patching`, it's because `hidden_states, self_attn_weights = self.self_attn()` requires 2 return values so in your hook just return a tuple with the second element set to output[1] or sth else if output_attentions is True. 
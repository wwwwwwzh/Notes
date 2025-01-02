# Util/Tools
## System Setup
### Longleaf
Basic:
- ssh zhw@longleaf.unc.edu
- cd /nas/longleaf/home/zhw
- store files at /work/users/z/h/zhw/ for high throughput io

SLURM:
- salloc --mem=4g --ntasks=1 --time=02:00:00
- srun --partition=interactive --nodes=1 --ntasks=1 --mem=4G --time=02:00:00 --pty bash
- view jobs: squeue -u zhw
- scancel job_id
- scancel -u zhw
- detailed info: scontrol show job job_id
- job history: sacct -u zhw

GPU: 
- 1080 8G: srun --partition=gpu --gres=gpu:1 --time=02:00:00 --qos=gpu_access --pty bash
- V100 16G: srun --partition=volta-gpu --gres=gpu:4 --time=02:00:00 --qos=gpu_access --pty bash

CUDA:
- view cudas: module avail cuda
- module load cuda/12.5
- check cuda version: nvcc --version

Jupiter:
- jupyter notebook --no-browser --ip=0.0.0.0 --port=8080
- ON LOCAL MACHINE: ssh -L 8080:c1121:8080 zhw@longleaf.unc.edu
- lsof -i :8080
- kill -9 <id>
- VSCODE: see vscode section

### UNC Computers
- AD means onyen
- AD needs internet access
- 
### General Troubleshooting
Step 1: Follow the below guide
Step 2: Use ChatGPT
Step 36: Go do something else 
#### Conda
see conda troubleshoot
#### module/command not found: 
- is your library in system path in ~/.bashrc or ~/.bash_profile
- can you run the command in terminal? If yes, then 1) check if there are package specific path loaction 2) are there multiple versions of a package. If no, 1) have you downloaded the right thing 2) have you linked it in system path

use for checking python path:
```
import sys
print(sys.executable)
```

#### Python
https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/#How-Python-locates-packages
- there are multiple pythons in your computer. Your conda environment (including base) has a copy of a version of python. Your system also have its own python version. Also check your PATH to see which pythons are seen. Use 'which python' to see where current python is.

### Package Not Installing
- Check python version
- copy paste the whole error message to chatgpt
- --no-build-isolation

### General Bash Commands 
- source ~/.bashrc or ~/.bash_profile
- df -h: view storage devices
- du -sh: view directory size
- pstree / ps aux: show running processes

- screen -S "12917.tdnerf_baseline" -X sessionname "newname"

- watch -n 0.5 nvidia-smi 	# shows the GPU usage
- htop				# shows CPU usage

- scp -r /path/to/directory zhw@hires-gpu1.cs.unc.edu:/playpen1/wzh/files/: copies the directory itself into files folder
- cp -r ~/folder1/. ~/new_folder1: copies contents of folder1 to a new folder (will create if not exist)

### Tensorboard
- tensorboard --logdir log; ssh -L 16006:127.0.0.1:6006 zhw@hires-gpu1.cs.unc.edu then go to http://127.0.0.1:16006: tensor board on ssh

### Jupyter Notebook
- jupyter notebook --no-browser --port=8080; ssh -L 8081:localhost:8081 zhw@hires-gpu1.cs.unc.edu

#### Troubleshooting
- Module not found: check if you can use the module in terminal, if yes, install jupyter in your current env. If no, 
- Restart terminal
- 

### Conda
#### Installation
follow codes here https://docs.anaconda.com/miniconda/#quick-command-line-install 

- conda create -n your_env_name
- conda activate your_env_name
- conda env list
- conda list

#### Removal
https://docs.anaconda.com/anaconda/install/uninstall/
On macbook pro my miniconda is in home directory

#### Export Environment 
- conda env export > environment_gp.yml
#### Troubleshoot
- solve environment forever (making new env should not take more than 2 minutes and installing a package should not solve for more than 1 minute): remove and reinstall conda


### Git
https://learngitbranching.js.org/
- git clone

- git init: initialize current directory
- git add .
- git commit -m "initial"
- go to github.com and create repo, or use gh command 
- git remote add origin git@github.com:wwwwwwzh/binder-manim.git
- git push -u origin main
- password is the ssh private key in keys.txt file alternatively it's in slack

- git branch branchName
- git checkout branchName
- git checkout -b branchName
- git merge branchName
- git rebase branchName

#### ssh
The process is as follows: you run a git clone command with an SSH URL; Git starts ssh to connect to the github.com host as git user; ssh connects and successfully authenticates by the 1st keypair; GitHub recognizes that it's the user that has access to the repository so it accepts the request at the Git protocol level

- create new key for github: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- add key to github: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- multiple keys for multiple github accounts: https://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config


#### Relative 
- git log
- git checkout commitHash
- git checkout branchName^
- git checkout HEAD^

- git reset --hard commitHash
- git reset HEAD~1
- git revert HEAD: new commit with content as previous commit. Use with pushed commits.

### Node
- upgrading node by first 'brew upgrade node' then 'brew link --overwrite --dry-run node' then 'brew link --overwrite node'

### cuda
- export PATH=/usr/local/cuda-11.1/bin:$PATH: change cuda version

> https://docs.google.com/document/d/1S8PU4EbigzlvSx4x_Ay835hMAjB8bCpouoWcNIyvTbc/edit

### Tools
- CMake: https://askubuntu.com/questions/829310/how-to-upgrade-cmake-in-ubuntu

## App Shortcuts
### PyCharm
select next occurrence: control + G 
deselect previous occurrence: shift + control + G 
copy line done: command + D

### VSCode
copy line done/up: shift + opt + arrow
select next occurrence: command + D

- setup remote developing: https://code.visualstudio.com/docs/remote/ssh
- remote jupiter notebook: run salloc and srun, THEN activate conda env and run jupiter, in vscode, add kernel to be the one in jupiter output (like http://c1123.ll.unc.edu) use 'import sys; print(sys.executable)' to check which env conda is using.

## Code
### Torch
```py
rearrange(x, "b (h c) x y -> b h c (x y)", h=heads) # from [b, c, x, y] to [b, h, c/h, x*y]
einsum("b h d i, b h d j -> b h i j", q, k) # if index is in result (b h i j), it's element to element; if index not in result: same index appear in both input matrices (d here): Einstein sum along that dimension (Σq[d]*k[d])
einsum("b h i j, b h d j -> b h i d", attn, v) 
```

# Reference
## People
### Science
- [multidiscplinary education guy](https://www.youtube.com/@physicsforthebirds)

## Websites
### ML
#### HuggingFace
https://huggingface.co/transformers/v2.9.1/pretrained_models.html: model name and size

### Language
- https://fluent-forever.com/product/fluent-forever-pronunciation-trainer/
- [Alphabet: The origin of every letter](https://www.youtube.com/watch?v=CYqqFqoLnnk)
- [Cyrillic Alphabet](https://www.youtube.com/watch?v=5kDpO9T-z60)

### Blog/Notes/Writing
- Interactive blog: https://idyll-lang.org/docs example: https://github.com/mathisonian/trig/blob/master/etymology/index.idl

### Others
- music: https://www.letras.com/shakira/1657452/

### Math
- Laplace transform visualization: https://www.youtube.com/watch?v=n2y7n6jw5d0


----------------------------------------------------------

# Logs
## 12.19
### sherical harmonic 

<img width="200" alt="Screen Shot 2022-12-19 at 4 43 09 PM" src="https://user-images.githubusercontent.com/36484215/208555184-85d131f8-bfdd-402f-924f-b145467e3f6e.png">

ω = (sinθ*cosφ,sinθ*sinφ,cosθ)

basically a basis for sherical functions like fourier basis

### projection matrix (reviewing Roni's slides)
<img width="300" alt="Screen Shot 2022-12-19 at 5 24 44 PM" src="https://user-images.githubusercontent.com/36484215/208559444-a1df7cd3-3423-4590-8fa1-64dd07c854de.png">

Note that image plane doesn't change size

<img width="300" alt="focal length and ratio" src="https://user-images.githubusercontent.com/36484215/208560712-78b6cd10-949e-446a-8d1b-c3646280e610.jpg">

Note that when f→∞, this becomes orthographical projection and ratio will be 2.

## 12.20-22 (reading pbr book)
### BRDF
### Others
- [Mach bands](https://en.wikipedia.org/wiki/Mach_bands)
- Thor 4 is really bad. 
- Beam search in translation (balance between greedy search and resource constraint)
- Log is a really interesting function. When x is too big, it makes x grow slower. When x is too small, it makes x shrink slower. Everything is within a more controllable range. 

## 12.24-25
### Think
- Kanzi the ape
- koko the gorilla
- “The primate vocal tract is ‘speech ready,’ but ... most species don’t have the neural control to make the complex sounds that comprise human speech,” Dunn writes for The Conversation.
- Deaf people think in sign language or imagined sounds or visual stuff
- Blind people: echolocation, spatial understanding, other sensory information
- https://waitbutwhy.com/table/person-with-no-senses
- criticacl period for language (or really intelligence) development. Nervous system stops growing (real brain learning?)

Sensory or external stimuli is needed to start things. Curiosity and other premitive desires (survival, imitation, some are uniqu to individuals, some learned) to drive internal processing. Memory?
https://www.youtube.com/watch?v=mFP_AjJeP-M

#### Short term memory
- motivation1: when we see a particular shape for a long time, we might see everything as that shape. CNN analogy is every pass also keeps a weighted average of activation so if a particular activation shows up many times, a small activation there can be very big so it sees every image as containing that shape. 
- RNN: rnn is really that CNN analogy with trained retaining activation. Previous activations are kept alive when new input comes. 

#### Long term memory
- Motivation1: long term memeory should be stored to "empty new space", be queried with trained (possibly refinable) network. 
- KVQ query system. multiple Q what is this, is this dangerous, is this beautiful...
- google seems like a good memory system
- continuous refinement of memory by asking questions and creating new connections.

## 12.26-29
### Eating
Not eating after 12.25 dinner makes me starve early in the morning and feel bad throughout the day. Ate at 12.26 but still not good after 12.27 breakfast. Took a walk and ate lunch much better. Slept and all good. Ran short late afternoon. 28 morning stomach feeling funny 2p. 29 morning better 2p.  Ran afternoon.

## 23.7.14-20
Ate salmon 7.14, diarrhea 7.15 but generally feel good. 7.16 went out and all good ate few for dinner. 7.17 very hungry in the morning and hungry though the day. 7.18 played badminton feel good and ate a lot. 7.19 feel good. 7.20 a little nervous and don't feel like eating breakfast but good throughout day.

## 23.10.27-30
Sunny and T-shirt. Halloween rush on Saturday

## 23.11.22-23
Door to door in Cary bad food expensive 8 ppl. 23. jade palace

## 24
### 1.6
scz 2000 + wzh 1600 robinhood

### 1.16 
dzy amd

### 3.6
dzy super trump

### 3.11-13
getting up with less than 6 hours of sleep, heartache, bad stomoch feeling after breakfast. well after lunch in Liming and walk Duke garden. 

sleep better 13 and all good

### 3.13
started transforming all mathematical ideas to visual experience (starting with linear algebra)

### 3.16 
very sleepy in the afternoon, had dinner with wzh last night probably infected but no sign. also very tired when trying running

### 5.4
btc from 58000 to 64000 in two days, major altcoins not moving, major meme coins and new shitcoins rise fast

### 5.8
major altcoins rising fast after trump made statements about being fine with crypto

### 5.10 
semester summury on trading/gambling. It's aweful. should not have entered but valuable lesson gained. Never do things you don't know about with great risk and no fantasy when you have flat prior. It's terrible to fall into gambler's mindset where you are destined to lose everything.

### 5.10
Totoro and book of trump rug pull. they do 2 pumps at 2 threshold and there are 2 major spikes. Best to buy after at the dip after first pump and sell immediately or 10 minutes after 2nd pump. ATH/5 is where to buy again and sell at double. No fantasy afterwards.

### 5.11
Extreme loneliness after graduation ceremony. Always feel this when coming from one place to another. Domescrolling doesn't work. Reading seems like only thing conforting.

### 5.14
Long flight is terrible, 7h east to west then 15h to xiamen. 

### 5.15 
hair. one year of long hair seems to make head vulnerable to cold air. after cutting, head is constantly slightly cold, wind sound is big.

### 5.12-7.12
Recovery from the psychological crisis. It's interesting that things follow similar patterns. For a bad stock to rise, you have to wait until it fully reached the bottom. The test is to see the reccovery response after artificially induced dips. After the final dip, it will settle for a short while then begin to rise. Also interesting how psychological trauma is. I developed a unconscious fear for phones after the experience. Also how state of mind can be manipulated and state has much power to determine behavior.

### 7.12
It occured to me that what I'm learning now of electromegnetism is but what I learned in AP physics 5 years ago. How did I answer all those questions? If my state of mind at that time solved the problems. How can I be sure that my state of mind rn is better? How interesting it is that I didn't know anything about calculus when I entered college and spent weeks trying to understand first page of differential equations. 

###  8.15
An account of an interesting recent change in mental state. After the crypto incident or perhaps earlier, possibly as early as end of 2023, I began to develop constant fatigue, especially in the afternoons. The primary symptoms are: fatigue of the body, shortness of involuntary breath, brain fog in the morning and early afternoon, drowsiness in whole afternoon even after napping. Interestingly, the following activities eradicacte the symptoms: talking to friends, including heavy texting; mentally talk about something I'm very interested about; imagining as I did as teenager (this can only be done when not drowsy). 

The weridest part is how instatnly can my mental state change between teh good and bad. There's an intereting dynamic between a constant drag to sleeping and ativities and oppose the drag by either creating a countering force or increasing mental inertia. 

Note that unlike pure psychological down state, I actually feel sleepy more often regardless of activities. Even when doing my favoritte activities, I feel sleepy earlier than I used to. Night sleep time qaulity is not controlled and I might use my watch to monitor it.

### 8.16
It seems that after a long flight, tired and hungry, my spirit is still high, albeit unstable (easy to collapse). The time is 6am in France and 12am in China. It's around 5 hours after stopping to sleep. In any case, it should be my drowsy time. But I'm not tired. Although intelligence is low. Reading in advanced physics is hard. Pictorial thinking intact. Conversation and imaginaiton of cconversation intact. 

At 9am france or 3pm china, sppirit is very stable. I can do anything except that hunger keeps physical work difficcult. THere's slight diziness when moving too much.

Met unc classmate who might infect me

### 8.18
Feelig like fever without fever. 

### 8.19
FDOC. Feeling  great, audited schocastic process, so many chinese. Went to gym

### 8.20
infected a friend (symptoms: mucus, no fever) gym again. Embasy event (haoge). Ran for 30 minutes after dinner.

### 8.21 
gym

### 8.22 
coughing hard and extremely sleepy in evening, friend worse

### 8.24
completely recovered, running nose. Night talked too much and coughiing again

### 8.25 
gym

### 8.28 
gym

### 9.2
megaman feeling extremely great, run

### 9.3
tried wawter placebo, not as good as yesterday.

### 9.5
setting up desktops in lab

### 9.6
friend still ill. Computers connected ethernet can ping each other

### 9.9
Lab meeting about some attention tasks on humans and testing some eeg region of interest. Some graphs of alpha and beta activities as function of time. Tried nfblab selflooping which was successful on both computers. LSL still no luck.

### 9.10
friend went to hospital but nothing abnormal.
Tried directly using socket to send keyboard events and worked. But lsl not working. Tried various firewall settings including inbound rules and closing firewall, also changed ip to 192.168.1.1. Not working. Grinding some basic networking. https://cs.lmu.edu/~ray/notes/netsandinets/. socket is the os level tool for networking

### 9.11
Now multicast directly can work. At first  ports from 224.0.0.0-224.0.0.255 are shown on wireshark as red and the receiver script not working. If firewall is disabled, this would work and netsh would show ethernet has joined the group ip. lsl still not working btw computers and no wireshark nor netsh signal. checking lsl library. The whole time vr is connected to internet.

Trying on macbook: 1) manual creation of multicast followiing https://stackoverflow.com/questions/603852/how-do-you-udp-multicast-in-python first shows a *[7	440.985751	152.23.129.132	224.0.0.183	IGMPv2	46	Membership Report group 224.0.0.183]* packet in wireshark, each transmission is a *[8	447.728175	152.23.129.132	224.0.0.183	UDP	45	64907 → 5007 Len=3]* packet. This UDP packet is shown on wireshark regardless of reception. 2) using lsl https://github.com/labstreaminglayer/pylsl/blob/master/pylsl/examples, now changed to wireshark to see all loopback data. sender showed nothing by itself. When listener starts, a udp and tcp server are setup with info data and then tcp is used for transmission. Switching to all interfaces, it seems udp and tcp are both transmitting. Again sender alone does nothing on udp tcp level. (dst net 224.0.0.0/4 or host 255.255.255.255). 

The IGMPv2 is seen only once and maybe it's not leaving membership so have to wait till reopen computer. 

### 9.12
Cleaning mac storage memory disk. Library is 11G, System is 13G, usr is 10G, yuwawng is 114G so next time just target that directly. Library under yuwang is 50G. Removed /Users/yuwang/Library/Developer/CoreSimulator which took 10G

### 9.13
ON 9.11 the computer can't access internet. It's solved by resetting IP. It was 192.168 IP. Luckily I stored the original IP on Wrike.

Following up on the wireshark tests. Selecting all interfaces and set filter to "dst net 224.0.0.0/4 or host 255.255.255.255". The VR computer which is connected to UNC Guest showed IGMPv3 join and leave group packet for LSLsender script. MulticastReceiver showed similar join packets.

### 9.16
downloaded psychopy on stiimulus computer, great componentized development and easy to use UI. Created a conda env called psy, py=3.8 with psychopy as required and installed matplotlib=2.2.4 then nfblab. 

### 9.17
finally working as I used my own computer and tested back and forth. But should have tested my computer with the school computer as well. Combining source code reading, it seems that the outlet creates several UDP and TCP servers and listens for requests. [check who joined mmulticast group] Then the inlet sends request [to the multicast group?] and establishes connection with server. Latency seems to be within millisecond range. Got photodiode

Met the other sttudent freshman in comp and neuro, prominent backgroud in tech and health care. Done some ECE projects and real project with Duke professor on preprocessing LFP data on mice and ships. 

In retrospect, I should have tested my computer with VR tthe first week because that's what I know. By playing around with the firewall and network stuff I was venturing into unfamiliar territory, whist not having tested every known option. The logic is that people in this field are not likely to know network stuff and are likely to have compuuters with similar restrictiive setup. If they have no problem using LSL directly, the first solution is to change computer. But this is nevertheless a very valuable experience iin network. I've almost forgotten my network stuff but now it's hands on refreshment.  

### 9.18
The complet network behavior of LSL: 
1. receiver (joins multicast group? and) sends session request to multiple multicast/broadcast/unicast ports from both ipv4 and v6 interfaces, the request contains a short info with name and type 
2. sender joins multicast groups and listens for requests
3. upon getting short info, sender sends long info (host info). (seen as udp packages of length around 683)
4. upon receiving host info, receiver starts TCP connection. 
5. After connection is esttablished, sender sends LSL::stream feed with data chunks

Format of psychopy: 
- Main function:
```py
expInfo = showExpInfoDlg(expInfo=expInfo)
thisExp = setupData(expInfo=expInfo)
logFile = setupLogging(filename=thisExp.dataFileName)
# this is the screen showing attemping to get frame rate and saved to expInfo['frameRate']
win = setupWindow(expInfo=expInfo)
setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
run(
    expInfo=expInfo, 
    thisExp=thisExp, 
    win=win,
    globalClock='float'
)
saveData(thisExp=thisExp)
quit(thisExp=thisExp, win=win)
```
1. First 34 import lines are reserved
2. Run **'before experiment'** code from [names of code blocks that are assigned as before experiment following builder flow order]
3. setup global variables: create 'deviceManager' and _thisDir = os.path.dirname(os.path.abspath(__file__)), expInfo, _fullScr, _winSize, filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
4. run()
    1. Start Code - component code to be run after the window creation:
    For each Routine in flow order, 2 initializations will be done, first is block initialization like texts or keyboard, second is to run **'Begin Experiment'** code
    2. timers
    3. For each Routine:
        1. Prepare to start routine [routine]
        2. **Run 'Begin Routine' code**
        3. Run Routine [first routine]
        4. End Routine
    4. endExperiment()
5. saveData and quit


Gradcpt outline:
1. d
2. run()
    1. inits
    2. here is gradcpt saving and stimuli processing functions
    3. trial variables are here
    4. dom_key/key to press when city, random assignment
    5. estimate_frame_rate Routine: transition_steps = round(refresh_rate * transition_time) # Hz*0.8
    6. welcome: text and listen for key press
    7. gradcpt_prep: more text and another key press wait
    8. thisExp.addLoop(blocks: {nReps:N_blocks})
        1. block_start: press space and assign city key
        2. text: image appearing in 5 seconds
        starting 1435: 
        ```py
        probe_count = 0
        frame_count = 0
        transition_step = 0
        next_es_trial = round(random.uniform(next_es_min, next_es_max))
        gradcpt_trial = 0
        es_trial = 0
        gradcpt_data = []
        es_gradcpt_data = []
        do_es = False

        routine_start = datetime.now()
        
        # stim_set is list of images, conditions is list of strings of either 'dom' or 'nondom'
        stim_set, conditions = create_stim_sequence(dom_stim, nondom_stim, N_dom, N_nondom)
        
        transition_current = np.linspace(np.zeros((256, 256)), # Grey
                                  stim_set[gradcpt_trial], # Image 1
                                  transition_steps)
        transition_next = np.linspace(stim_set[gradcpt_trial], # Image 1
                                  stim_set[gradcpt_trial+1], # Image 2
                                  transition_steps)
        
        
        trial_start_time = datetime.now()
        ```
        3.  thisExp.addLoop(blocks: {nReps:N_trials*2})
            1. gradcpt_stim: kb=Keyboard.Keyboard(); Run **Each Frame** code from stim_code
            ```py
            # if end of trial
            if (transition_step == transition_steps):
                if (gradcpt_trial == N_trials):
                #end routine
                elif gradcpt_trial == next_es_trial:
                    #do the 6 questions/es
                else:
                    # Update stimulus set
            img = transition_current[transition_step]
            frame_count += 1
            transition_step += 1
            if key pressed:
                gradcpt_data.append(save_gradcpt_data(rt, key))
            ```

        4. block_rest

```py
def save_gradcpt_data(rt, key):
    # Calling vars beyond the local scope of the function
    out = {
        'total_runtime_mins': (datetime.now() - experiment_start_time).total_seconds() / 60,
        # Start trial counter at one
        'gradcpt_trial': gradcpt_trial+1,
        'frame_count': frame_count,
        'transition_step': transition_step,
        'coherence': transition_step / transition_steps,
        'condition': conditions[gradcpt_trial],
        'resp_key': key,
        'rt': rt
    }
    return out
```

es is experience sample

### 9.19
an extra frame, test these tommorow:
1. change time to 400 and then to 17
2. add a print for each win.flip() and count
3. check the other frame and counter variables and see if and when they match

added the square, one frame alternation if too quick, still using 0, 400ms per trial.

An interesting phenomenon when discussing GRE vocab with friend. It seems that he's incapable of decomposing a word into its part and thus his memorization of english words is one to one, the least efficient, which kinda contradiicts my hypothesis of innate abstractoin. However, this is a valuable venue of research to compare L1 and L2 acctivation patterns to see how innate and acquired abstraction differ. I believe that there's a critical peroid of innate and acquired can be gradually transfered to iinnate by trimming the physical connections. The same phenomena applies to any field where you see gifted people compared to learned people. Arts and music and literature and investment can be good examples.

### 9.20
Catching the extra "frame". setting to 0.017s results in 1 frame per image and the ending time is exactly 0.167s. 0.8 or 1s per image results in approxiamtely 0.017s extra per image. 5s, or 300 frames per image, results in 5.0838s per image. Thus the extra frame is actually a precision overflow or frame drop. Consider using a high precision timer to ennforce the 0.8s transition time.

Forked the gradcpt repo and now working on git.

Now testing lsl. The first problem is my macbook can't initizlaze ioHub used by psychopy. This is solved by enabling psychopy in input monitorinig and accessibility in security & safety settings.

LSL or NDFlab uses XDF which is mostly used by electrophisiological data. Basically a custom xml.

---
On the research side, Danniel talks about left right asymetry in affective component (approach-avoidance in left and right prefrontal cortex). A stereotype was from lesion study. then EEG  alpha asymetry, greater relative left prefrontal activation reported higher levels of BAS strength, greater  right prefrontal activation reported higher levels of BIS strength (Behavioral Approach and Inhibition System (BAS and BIS))

Daniel's theory of sword and shield model was that people attack with dominant hand and defend with non-dominant hand. Which he then uses to propose modificatoin to tDCs treatment: identify the approach hemisphere first (tDCs assumes activating approach hemisphere makes you happy)

### 9.21
Now it's decided by me that frame doesn't matter, only time matters. So I'll modify the code such that everythiing is relative to current time. 

Wow I didn't expect this to take me soo long. First Psychopy just freezes when a bug happens so the debugging procdure becomes tedious. Later it was found that by killing a process (we know the port) the app defreeze. It's caused by index out of range and should have been tested easily with a simple test script. 

Now transition step is calculated by current time and next trial decision is still by this calculated step. The saved data show that for 4 trials, time elapsed is 3202ms which is good (800.5ms/trial). Actual frames during that 4 trials is 196 (supposed to be around 280). So this seems like a universal solution since we can't control frame drops.

Next is to study NFBLab:
- saving happens at next_protocol() in experiment.py, dir+experiment_data.h5 Using h5py to view it. No good graphical viewer found. Refer to https://nfb-lab.readthedocs.io/en/latest/experiment_results_file.html. Data in protocol0
- experiment is composed of sequences of blocks or block groups specificed in Protocals sequence. Block groups are composed of several blocks specificed in Protocal groups. A protocal is a block. A typical experiment has baseline, rest, and feedback blocks.
- A block ends when sample number (duration * sample rate/nominal_srate in stream info) is reached. Click the replay button enables you to run the block again and data will be saved in protocol1

['channels', 'fs', 'protocol0', 'protocol1', 'settings.xml', 'stream_info.xml']

### 9.22
Work on what exactly to transmit. Here are the questions:
- allow multiple presses within trial? what to do with extra presses?
- what should be transmitted when mountain appear and ppt either responded or didn't, or should we also assign a key for mountain? (if we don't do anything then ppt can just keep pressing whenever image changes)
- what should sampling frequecy be and if it's higher than image freq, then what should be recorded during the blanks

Matlab integration (ask gpt how do i incorporate mathlab scripts into python with matlab engine or pymatlab)

### 9.24
It seems that the only thing needs is rt and dom/nondom. The later can be sent at before trial starts along with trial numbers keys and transition time. rt should be sent on every press. The algorithm should be as follows:
1. create a list of rts of size N_trials
2. anything wihtin first 800*1.7ms is assigned to trial 1, rts[0]=data
3. 

### 9.25-27
R code for response assignment:
1. if rt==0, assign timeout, else if rt < unambig_low, assign previous trial, else if rt > unambig_high, assign current trial, else it's ambibugous. So ambiguous iff unambig_low < rt < unambig_high. At this step, trialcode1 is a list of length presses and contains either "timeout", a trial number or "ambiguous"
2. for ambiguous trials, check if there is response on current and previous trials. If exactly one of them is empty, assign to that trial. If both empty, assign to the current trial if current trial is dom otherwise to previous trial. If both trials are  assigned, assign it as duplicate to current trial. At this step, trialcode2 is a list of length number of presses, not number of trials. It contains either "timeout" or a trial number.
3. remove duplicates and timeout. Seems like no comparison of rt is made but might be implied in the logic. Need to check more.

It's so great that VSCode can integrate (show helps and run code directly) both matlab and R so no need to open up those gigantic apps. 

Since I have changed the transition step assignment to align with time, it's probably best to use rt directly in the r code.

The analysis suite contains bunch of behanioral data statistics, read https://phonetics.linguistics.ucla.edu/facilities/statistics/discrim.htm and [d-prime](https://phonetics.linguistics.ucla.edu/facilities/statistics/dprime.htm) 

Gradcpt-GP:
- note that x is onset time, y is rt interpolated. This assumption looks good (a quick rt followed by slow rt means rt might be rising for time in between)
1. log-transform and z-transform RT
2. linear detrend
3. use the last 2 minutes as test data

Potential changes:
- why log transform


Results:
- rbf+per:
![](/images/rbf-per.png)
- rbf:
![](/images/rbf.png)

### 9.28
Sleep data is disasterous, changing room layout (didn't do).

### 9.30
VSCode with ssh is amazing. Now using longleaf and vscode and jupiter notebook. Setup every time takes less than 1 min. See vscode references for implementation.

### 10.1
VR is 3080 ti. But longleaf is ok for Gaussian models for now. Strange problems with Gaussian regressor, need to read book

### 10.2
It's decided that I should watch the Khan economics series and study some technical analysis/financial time series processing. Therefore the main focus now has increased to 2: deterministic systems (linear and non-linear) and stochastic systems (history of statistics and time series forecasting)

### 10.4
Matlab eeglab basic eeg hands on on dummy, I think I've known the basic procedure for related studies.

Khan economics, damn Adam Smith said the exact thing I thought about (by promoting self interest the public interest fares better)

### 10.5
Economics is the study of human behavior when they have to reason about value of something. This reasoning of value should be fundamentally based on associationism, where each thing is associatetd to a representation of value when a decision needs to be made. The complex thing is that there are many interacting agents. Association can still account for value representation under more variables. Statistical physics has already established frameworks for such studies. 

Microeconomics is the study of decision making likely with “value” as a main influence on the association  process. Value is not a number, but a universal construct. It could be number, it could be an equivalence with something physical or abstract, it could be the concept of very big or very small. Normal decision making usually doesn’t involve such high level mental consctruct. This kind of study, being a decision process, fits stochastic process the best. 

Macroeconomics studies the result of many such decision making processes, which is exactly like study of many molecules. 

All of statistical studies, as always, exhibit phenomena that in the long term give a boost to the agent(s), in a Darwinian sense. In physical words, economics behaviors minimize entropy. 

### 10.6
Applied FFT on gradcpt data and some worded remarkebly well. Agnieszka is suprised about the results. Maybe explore more timeseries forecasting. 

I'd say this is helped by reading Simon's biography that same weekend and I'm growing more and more intreesred in signals and statistiacal analysis of signals.

### 10.8
Hinton and Hopsfield awarded Nobel Prize in Physcis! Physics students are very upset. 

- Hinton graduated college at 23 with Bachelor in experimental psychology after switching btween natural sciences, history of art, and philosophy. 
- He completed PhD in 31 (1978) at the University of Edinburgh in artificial intelligence supervised by Christopher Longuet-Higgins. This was at a time of AI winter when perceptron model (1958) was proven limited (1968). Higgins switched to symbolic AI and but was tolerant with Hinton who insisted on neural network research. 
- In 1985, Hinton co-invented Boltzmann machines with David Ackley and Terry Sejnowski. In 1986, while a postdoc at UC San Diego, David E. Rumelhart and Hinton and Ronald J. Williams applied the backpropagation algorithm to multi-layer neural networks.
- Hinton said he didn't like math once he learned functions because they meant little to him. He reformed his thinking once he learned about functions in programming. (another proof that a general non definition based pre-college teaching is harder than thought because different people are able to successfully associate to different ways of introducing a topic)

### 10.9
Starting chaos and statistics. Getting an understanding that statistics and probability can indeed be separated. eg your height or population of a country are statistics, deterministic. They chance we say of somthing happening is probabilistiic. But usually to measure and analyse statistics you need laws of probability. That's also how probability emerged. 

This offers a new perspective of projection. Projection is nature's statistics. We observe statistics of the world and infer or analyze this statistics. This view even adds to the original projection formulation. The forward and backward projection are now probabilistic, meaning that there are mathematical ways to better understand these two non deterministic mechanisms. 

### 10.10
Interestingly, the Feynman radiation chapters are now understandable possibly bc I have since learned electromagnetism and trignometry. The method to add 2 trig waves of same freq is explored in 29-7 which was expected.

### 10.11
It's interesting that music notes just look like stock data showing trends and periods and other things

Finally understood convolution after reading Feymann's chapter on EM wave. Inpulse response is indeed good for understanding this. Thnk of as input * impulse response=output. If there's a way to  normalize the signals, then can also think as input * pattern=match response

### 10.12
Probability means uncertainty. Statistics deal with numbers. Your height is a statistic, your number of outings with friends in a year is statistic, your schools budget is statistic. These numbers have certain structures. The framework to study these structure involves randomness. Thus in a sense, proabbility deals with microscopic uncertainties that give rise to structured behaviors, usually through large quantity or time, the numbers given by these behaviors is studied through statistics. One way to differetiate these is probability deals with distributiions and statistiics deals with numbers. As always, when you have a model/structure, you can predict. 

> In the Brownian motion problem and all its variants, one deals with a phenomenon that is the outcome of many unpredictable and sometimes unobservable events, which individually contribute a negligible amount to the observed phenomenon, but collectively lead to an observable effect. The individual events cannot sensibly be treated in detail, but their statistical properties may be known, and, in the end, it is these that determine the observed macroscopic behavior.

### 10.13
- Read some papers on ML enabled EEG classification. Impressive eeg to image or text results.  See reference/neuro/eeg/classification
- Read about PCA, ICA, IC and dipole fitting (similar in principle to COLMAP)
- Read Feymann. Now pausing this endeaver since I missed too much on light chapters. Should read these to get a fuller understanding of waves before doing quantum.

### 10.14
- now understood ICA, a good paper is worth everything. It's literally INDEPENDENT COMPONENT. The interesting thing is how you can get independent variables. Amazing how CLT is the key here. Also interesting how kurtosis and negentropy can be used to define "non-gaussianity".
- finally beginnning to understand MGF. From characteristic functions which is just FT. The moments are generated because fourier transform near 0 gives more global information and Taylor expansion can be used to prove how the moments are generated.
- Also with this understanding of MGF, CLT can be proven with ease. Though still confused why the multiplication won't collapse gaussian FT to delta.

### 10.17
- trying wavelets. very hard math and not many clear tutorials. 

### 10.18
- Reviewing Howl's moving castle orchestration, it's interesting how many DOF is involved. A simple strength or timing difference makes the sound much better. I wonder if machines can identify these
- Also makes me wonder if the brain is an orchestra. You have many instruments playing according to certain rules and results in harmony. Is harmony ini brain activity necessary from first principle? Would inharmonic rythms be synchronized or cause utter dysfunction? Can we somehow "listen" to this harmony? https://www.youtube.com/watch?v=X6s6YKlTpfw. Are neurons more like this or the view of people on a busy business center?
- [eeg to music GT](https://brainmusiclab.gatech.edu/publications/); [columbia neuroscientist eeg music](http://sites.music.columbia.edu/brad/brainwave-project/); [seizure rapsody](https://datadrivendj.com/tracks/brain/); [imapact of music on brain](https://pmc.ncbi.nlm.nih.gov/articles/PMC6130927/)

### 10.22
- 2 datasets both with pupil but diffeernt format. (original boston one actually don't have pupil)
- tubingen data unprocessed but could supposedly be easy to do with analysis suite (unfortunately data is messy). pupil maybe should process with the code there. not eveerey subject has both behavioral and pupil data
- original data need to understand the pupil index (no this is random data so not useful)
- really want image type data. 
- muse electrogel still no alpha peak trying the website when i got time

### 10.23
- there seems to be many gradcpt datasets. Now understanding how important qualitied data are
- reading https://phonetics.linguistics.ucla.edu/facilities/statistics/discrim.htm not much useful so just wiki and chatgpt: d prime and criterion score.
- tubingen dataset different format than esterman. also it seems that matlab people use ambiguous short abbreviations and inconsistent naming formats. no wonder why python prevailed.
- finally beginneing to understand chaos. interesting how chaos exhibit fractal order.

### 10.24
- got original tubingen code that geenrate aforementioned data. now things can be converted 
- working on a method to orgnaize the growing number of python notebooks:
    - should have a data processing notebook with just functions and variables so other nottebooks can use it with %run MyOtherNotebook.ipynb. 
    - then also a visualization function that takes arguments and produce graphs. need to be easy to call

### 10.25
- got tubingen original codes and now understood what they are, but it seems they don't exactly use the code bc some data that should defintiely be genrated by the code is not in the actual data
- experimenting with muse again with ble dongle, muselsl and eeg-notebooks. settign up environment took some time bc with the dongle on Mac you need to explicitly provide the bluetooth interface address (can be found with ls /dev/tty.* ). You might get the stupid BleakError("Bluetooth device is turned off") which means your bluetooth is turned off. Tried muselsl first and that's quite easy. eeg-notebooks have some bugs include the above and not getting data although muselab can show it. Solution  was to restart computer.  Now fianlly ran the whole n170. also tested SSVEP
- eeg-notebook: The class for eeg device is EEG which is a wrapper for **muselsl** and brainflow. Experiments are run with subclass of BaseExperiment class which ennforces preparestimulus() presentstimulus() setup() and run(). UI is done with **psychopy**. Analysis is done with **mne**
- mne: analysis functions used by eeg-notebook is in mne->io->base.py. of which compute_psd calls initialzer of Spectrum class which computes psd with Welch's method

### 10.26
Great experience at reality fest and very profesional organization. 

Looks like 67.5 hz signal is recorded. It seems that in jupyter notebook psychopy window can't quit naturally.
Structure: 
```py
ssvep = VisualSSVEP(duration=record_duration, eeg=eeg_device, save_fn=save_fn)
ssvep.run() # run calls setup, which calls load_stimulus and show_instructions, and calls self.eeg.start() and starts trial loop
```
run trials loop:
```py
start = time()
current_trial = current_trial_end = -1
current_trial_begin = None

# Current trial being rendered
rendering_trial = -1
while (time() - start) < self.record_duration:

    current_experiment_seconds = time() - start
    # Do not present stimulus until current trial begins(Adhere to inter-trial interval).
    if current_trial_end < current_experiment_seconds:
        current_trial += 1
        current_trial_begin = current_experiment_seconds + iti_with_jitter()
        current_trial_end = current_trial_begin + self.soa

    # Do not present stimulus after trial has ended(stimulus on arrival interval).
    elif current_trial_begin < current_experiment_seconds:

        # if current trial number changed get new choice of image.
        if rendering_trial < current_trial:
            # Some form of presenting the stimulus - sometimes order changed in lower files like ssvep
            # Stimulus presentation overwritten by specific experiment
            self.__draw(lambda: self.present_stimulus(current_trial, current_trial))
            rendering_trial = current_trial
    else:
        self.__draw(lambda: self.window.flip())
```
inside ssvep experiment:
```py
# self.trials has columns parameter and timestamp. parameter is 0 or 1 randomly drawn to represent the 2 frequencies.

def present_stimulus(self, idx, trial):
        
    # Select stimulus frequency
    ind = self.trials["parameter"].iloc[idx] # 0 or 1

    # Push sample
    timestamp = time()
    marker = [self.markernames[ind]] # 1 or 2 as defined by experiment base class setup()
    self.eeg.push_sample(marker=marker, timestamp=timestamp)

    # Present flickering stim
    for _ in range(int(self.stim_patterns[ind]["n_cycles"])):
        # array of 2 each has {"cycle": cycle, "freq": stim_freq, "n_cycles": n_cycles}
        for _ in range(int(self.stim_patterns[ind]["cycle"][0])):
            if self.use_vr:
                tracking_state = self.window.getTrackingState()
                self.window.calcEyePoses(tracking_state.headPose.thePose)
                self.window.setDefaultView()
            self.grating.draw()
            self.fixation.draw()
            self.window.flip()

        for _ in range(self.stim_patterns[ind]["cycle"][1]):
            if self.use_vr:
                tracking_state = self.window.getTrackingState()
                self.window.calcEyePoses(tracking_state.headPose.thePose)
                self.window.setDefaultView()
            self.grating_neg.draw()
            self.fixation.draw()
            self.window.flip()
    pass
```

mirabile dictu, I recorded muse without ble. wasted that ble dongle?

### 10.27
- funny as it sounds the problem of predicting next instant vtc is no problem at all because you can just follow a trend. That's why a most basic network with only current vtc as input gives almost perfect results. Experimenting with long distance forecasting failed as expected. 
![](/images/fl-vtc-pred-transformer-test.png)
- also the smooth vtc is given which contains future information. Should redo the data processor so it generates smooth vtc at current time or don't use smooth at all. need to make sure what is being evaluated. maybe a good idea to start tacs first.
- try fft with rnn?
- also should do the muse thing in real time. the experiment class started the lsl stream so you ccan just write a custom receiver in a nontebook and do a moving window fft.

### 10.28
- discussion about stimulation threshold and duration with Agnieszka.
- need to see how the 4 types of response directly affect rt. 1. is commision error recorded as rt? (anser is no, all errors don't contribute to rt, they are 0ed) 2. what is shown in rt on ommision error (city no response) (same as above, no rt here) then also 1. when mountain is presented, how will real time rt go? 2. when user didn't respond how should that count towards vtc since it indicates something.

### 10.29
- using cursor.com shame they can't do ssh below is account used: wzh@unc.edu; 

### 10.30
- processing tubingen data. note that onset in original dataset is onset of stimuli so it increments 800ms. I'm creating an onset this way for tubingen but they also have actual press time so i added a press_onset column
- I'm still doing one big file in accordance with original structure with id and run columns
- ppt 15 has run 0
- found very interesting correlation btw pupil size and vtc turns out to be 0.3 overall is it good?
- while reviewing latin: is there education efforts to teach people many languages at once? Can we find the most efficient structure of language and meanings? can we use LLM to find etymological connections?
- also language, what does the entropy theory do with different languages? are languages linear? this lead to the reinforcement of the idea that the "linear space" of ffeatures are mutally indicative or have low conditional entropy. Knowing lux means knowing light. But this is a fake argument in that feature can be found this way (or is it?). There has to be some extra constraint.
- DOGE wormwhole on sol. doubled in one hour upon announcement. I don't understand how price works so can't risk too much. This is the kind of opportunity that can be combined with knowledge to create giant gain for certainty.

### 11.2
- From Neuron to Brain has a chapter 18 that has introductory circutory information about leach. 

### 11.9
- A realization of a derailmemnt from the imagined track of life. It seems that reality has finally presented itself. 
- Berkshire house no light, roommate is good. bus is 15 min to MEJ
- Sudden temperature drop. ate the second day megaman and feels exited until around 11 when it's still increasing. (cold feet for the whole time) Feels fainting or nauseus after pooping until lunch where I ate little or otherwise want to throwup. At berkshire nice talk and everything normal except ffeels numb and fainting after talking too long. PPee a lot. Feels better after dinner and talking is normal but still faitning if laugh too much. After hot bath finally normal again.

### 11.10
- btc breaks 80k after trump victory from below 70k a week ago. ether to 3200 from 2400
- Formulating the closed loop: 


### 11.12
- ppt 22 of tubingen data has weird 1st run data and is not processed. ppt 36 is not included bc run 3 and 4 are invalid in behavioral data, this is done in pupil_behavioral_all()

### 11.14
- Meeting with prof easterman. New idea of having more zones with pupil and vtc. Looking at some pupil literature  and hopefully can devise a usefull derivative of pupil to be used with vtc. 
- should experiment with directly categorizing zones with vtc and pupil and see if same statistical significance remain. Also need a measure of those 4 parameters.
- Regretting not selling doge? It seems that after the initial send, there aren't more impetus for more infflow and the k-line can't tell you everything. However, memes like pnut and moodeng are also without such impetus but were still sending waves after waves. Maybe it's because those SOL coins were sending while the general market was sending, but the rise of DOGE coincided with the first moderate correction of BTC after election pump. DOGE has been established as a mainstream elon based focus and I expect exciting news from elon in the upcoming days. The team is legit. So I'm holding. But it IS important to decide when to sell next. This is like venture capitalists who only do pre-IPOs, they take profits no matter the outlook after IPO. It's also confirming that SOL is a very volatile market. You have pnut and ACT sending within weeks of creation but most coins that look legit will shrink in the order of 10s in market backset. So in a expected bull rise, it's wise to invest some little portions to such "little coins" but sol money always rotate back to the big ones like popcat and ponke. Luce and Ban also look promising but luce may be too religious to be listed on binance. Ponke might be listed spot soon. 

### 11.15
- found some "a very short introduction" series books. got probability nothing and consciousness. Hopefully will be good casual reads
- doing muse  again. Let's get the protocol right: 1. turn on bluetooth and (optional) plug in ble-dongle. 2. check for settings bluetooth permission on whatever is starting the connection. 3. open muse app to check connections 4. close muse app so connection is not sent to phone. 

### 11.16
- Muse experiemnts are running. N170 is clear but ssvep is still problematic since my computer has not fixed refresh rate. Also changing UI to be pygame based. 
- For analysis, studying mne. The basic data structure is a mne.io.RawArray and this explain the basic:
```py
data = np.random.randn(10, 1000)
sfreq = 100  # Sampling frequency in Hz
ch_names = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10']
ch_types = ['eeg'] * 10  # All channels are EEG

info = mne.create_info(ch_names, sfreq, ch_types)

raw = mne.io.RawArray(data, info)
```

### 11.17
I was extremely tireless after dinner last night and tired this morning even after day1 megaman, is my attentional resource depleted? now at night energetic again

### 11.18
so the closed loop thing is a bang-bang controller. The validity of the stimulation procedure should only be statistically verified by existing data. It's yet clear if the final hypothesis is just about a control that improved attention or if we need to chain it to the claim that stimulations happen at real "out zones". Current protocol is to directly stimulate 20s every time it went out and because the average number of times it went out is consistent it should work (except that the constant 20s is now blocking some otherwise short transitions)
- Should try a rnn that pinalize numberr of switches. 
- rnn directly predicting if next 20 seconds should stimulate? transformer with one output?
- greek personification might led to science because they are studying/analysing forms instead of instantiations.

### 11.21
- met with Conner and Agnieszka and introduced the project. Learned that tES is usually just to find a certain phase on a certain frequency and see what happens. Flavio was involved in early works that proved tACS can treat depression. 
- (to be transfered elsewhere) After several days of thinking about the language/feature entropy problem, as started from the art-language-math problem, new insights from within natural language differences are included (latin-english-chinese) and this paragraph aims to provide a comprehensive update. [shannon english entropy](https://languagelog.ldc.upenn.edu/myl/Shannon1950.pdf)


### 11.24
- [aeneid](https://youtu.be/QH6tVkxeGM8): iliad, Virgil's Aeneid to merge Romans to Greek universe, Aeneas filial piety (Octavian to Caesar and patriarchy), merging all founding stories (Romos, Romulus and Remus, Evander, Aeneas -> iulus/Julius), Dido, Dante, 


### 12.1
- idea 1: the art-language-math problem may be formulated using expected entropy of symbols of that language (in the general sense), denoting as E[H]. E[H] should also imply somthing about the geometry of the symbols. A high E[H] means directions are highly dependent and you may not find orthogonal directions in information/representaion space.
- idea 2: when thinking, there's a spectrum of difficulty of a thought. For example, a math problem is harder to think about than something you like to imagine. There's also the power of control spectrum, where when you're about to go to sleep it's weekest. When it's week, you can observe that thinking about hard problems requires a mental capacity/modality different from easy problems. Also thinkign about easy things lead to sleep. Relatedly, these 2 modalities can coexsist. eg. when counting but start visual imagination when sleeping. 
- https://www.youtube.com/@manshi_math https://lr32768.github.io/
- working on gradCPT EEG data. downloading from dropbox using the link and wget and got a zip file but it was corrupted for some reason (zip bomb). Used UNZIP_DISABLE_ZIPBOMB_DETECTION=TRUE unzip fixed_eeg_data.zip. Also it's stored in /work/users/z/h/zhw/FL/projects/gradCPT-combined/gradCPT_Tubingen/data/eeg/ because that's where it's recommended to store large working file with 10TB storage. /nas/longleaf/home/zhw has only 50GB.

### 12.2
- pupil and behavioral seems to show some significance, tested mixed effect and trynig to understand it. 
- talked with Conner about Magdeburg dataset problem was behaviral data is absent. 
- Magdelena said the EEG is 10-20 64 channels will try mne standard model.

### 12.3
- mixed effect example (students learn more and get worse grade->add class and its the opposiite effect) only ce show combined significance
- tubingen pupil is  processed by unkown guy so menalli redid the processing from the raw csv files, which is already processed online by the camera to remove artifcats, to txt files and I converted them back tto the subjectid/subject_run.txt structure to be read by pupil_behavioral_all
- oh no pupil doesn't have time data. Well the time data is actually made up in the old processed pupil data. But Menalli's data now has extra time so need to figure that out (give this prompt: i have a pupil_folder string and inside are files like 007_run1.txt i need to restructure the folder so that there are folders like 007 and inside it file smoothed_participant_008_run_1.txt there are invalid files where it's all 0 but should check first 5 lines and if it's all 0.000000 then this file should not be included)
- consider saving the dicts by get_data() since the loading pipeline is more stable now. 

### 12.4
- got conner setup everything on longlead took 80min which is good. Nice to have all the instructiions at hand but still some missed simple things like installing VSCode extensions (remote explorer and jupyter) and also the ssh has to be done exactly as in github manneul. note that permission denied problem was solved by adding:
Host sc.unc.edu
    HostName sc.unc.edu
    User git
    IdentityFile ~/.ssh/gitlab
to config file under ~/.ssh/


### 12.6
use matlab dirrecctly in python with matlab engnine:
1. matlab is stored in /nas/longleaf/rhel8/apps/matlab/2024a
2. in .bashrc add 
    ```
    export PATH="/nas/longleaf/rhel8/apps/matlab/2024a/bin:$PATH"
    export LD_LIBRARY_PATH="/nas/longleaf/rhel8/apps/matlab/2024a/bin/glnxa64:$LD_LIBRARY_PATH"
    ```
3. if python version is incompatible with matlab, do conda install python=3.11
4. find compatiple matlabengine on https://pypi.org/project/matlabengine (mine is pip install matlabengine==24.1.2)

### 12.7
- to use scripts as packages add the project root path to bashrc and create __init__.py files. then all folders from root are modules
- converted some key notebooks to python scripts: jupyter nbconvert visual.ipynb --to python
- new error pushing: fatal: unable to access 'https://sc.unc.edu/frohlichlab/gradCPT-TuebingenEEG.git/': error setting certificate file: /etc/ssl/certs/ca-certificates.crt 
- this might be caused by the numerous path and dynamic link variables change. Temporary solution was to use git config --global http.sslCAInfo /etc/ssl/certs/ca-bundle.crt

- on observing many people going out of stadium: the randomness of walking comes from the fact that if the left side if fully parked people had to go right. All "random" processes should be understood as a basic necessity that if one side (of an elementary binary "coin") is chosen too much, then they have to begin choosing more of the other side.


### 12.19
- btc crashes following fed less cut 2025 105k to 95k eth 4k to 3.3k
- the gradCPT task paradiam can all be infered in response and ttt. ttt is just number of trials by nummber of frames per trial. The press onset minus rt in response will equal its corresponding ttt starting time (column 1). It's found that Magdeburg trial time is 1.2s instead of 1.3. 
- a good way of teaching might be to left some key calculations or graphs out so students have to come up themselves

### 12.20
- Hopfield on consciousness: he said the human brain is completely governed by classical dynamics and the complexity comes from complex system with 10^14 parts instead of quantum mechanics ("the physics of complex system is at least as badly understood as the physics of phase coherence in quantum mechanics" https://www.youtube.com/watch?v=KrdZ46MfNrM)
- L=T-V finally explained https://www.youtube.com/watch?v=Q10_srZ-pbs
- [body language](https://www.youtube.com/watch?v=VHUrdELKjDw), it's verifying how associationism works: your body gestures and other cues are all presenting information and for visual viewers these might actually convery more memorable information
- [LLM actually generalize, tested by creating many ability grouped dataset and learn on subset of them](https://www.youtube.com/watch?v=fTMMsreAqX0)
- to be watched Hopfield https://www.youtube.com/watch?v=7dplBHOq-yY
- Feynman actually introduced the visual system better than any neuroscientist
- And I realized that if one reads through that chapter, one will understand why people in mirrors look farther apart! So it takes 36 chapters to answer my middle school question.

### 12.21
- [critical brain hypothesis](https://www.youtube.com/watch?v=hjGFp7lMi9A)

### 12.22
 data processing procedure for Magdeburg
- fs36 is invalid

- problem of importing error: check if other variables can be imported and if only old var do, restart jupiter.

### 12.23
- Thomas Mazzoni's quantitive finance has actually a very good intro on prob theory with examples. An application based prob class could be built on this. The linear algebra intro is also superb but requires some prior training

### 12.24
- since i'm using music to excite myself nowadays, I wonder if it's a replacement to other sensory excitement. I used to be excited so much by people and visual stuff, now this kind of stimuli is just fading. Maybe auditory stimuli was not exploited too much before so I can still use them. But in the future this too might lose potency.
- [“网赌”平台Polymarket，如何暴打全球玩家](https://www.bilibili.com/video/BV1askGYYET3/?share_source=copy_web&vd_source=3bec0bb565604586cf0a7846abb0a768) an very interesting mentioned is why polymarket is a "real" use of blockchain. Things like NFT are inspired from art collection market but arts are tangible. Knowledge however, is inherently metaphysical. Recall the view that math exists outside of the physical world, and that computers are instantiations of these metaphysical objects to our physical world. Therefore, it's best to run a metaphysical object on computers. So pure ideas are best aligned with blockchain. Of course, to succeed the pure ideas you want to put on chain have to be connected back to the real world. They have to be interesting. The problem for Polymarket is how oligarchs might control it.

### 12.25
- sleep idea: processing of uncertainty in brain with example of myself and 阿诺, focusing on the marvelous creation of the word "荒燥". Extended examples include kids and people with psychiatric disorders.
    - hypothesis
    - information theoretic model: a creative/ambiguous agent assigns both inputs and outputs with distributions of high entropy, ie, there is a high randomness in its thought behavior. We further assume that such observation implies an underlying high entropy input-output information flow. 
    - experiment: We model AN with a LLM, adjusting output temperature as an indirect mean to control output entropy.
        - input: [阿诺文学 在油的光彩里微笑](https://www.bilibili.com/video/BV1G9qrYBEXk/?share_source=copy_web&vd_source=3bec0bb565604586cf0a7846abb0a768) "主播脸怎么油油的，（说明有光彩啊），脸不油，怎么能有光彩呢？你们谁看到哪个人那个脸上是，是那个，比较那个。啊。脸上油是好事，难道你脸上是（荒的），（荒燥的）"
    - result: 

### 12.26
- on nap: interesting feeling sometimes when you want to wake up but cannot, and have to struggle to do it, accompanied by very strong sensory inputs, today music specifiically, likely due to whole morning of loud classic music playing. maybe the motor system is shut out and some executive parts also not fully functional because the "wanting" to wake up definitely feels not as when awake.
- stochastic calculus: 
- lol the if you put all sorts of financial charts together it looks like EEG data

# Log Summary
## September 2024
### 2-8

### 9-15

### 16-22

### 23-30
## October 2024
3 focus now, is it possible? 
- foundations of classical mechanics and control (differential equation and signal processing)
- stochastic processes (brownian physics, quantum, theory of probability, laws of statistics, stochastic differential equations)
- statistical mechanics (entropy models, physical and computational models)

## Dec 2024
- when moving out, had dinner for consecutive nights with friends and lots of physical activity while moving out. there was brief periods of normality coming back at night when i feel everything is good and exciting, so it's in fact important to talk in person with groups of people, as this is me. This actually happened last time beginning of semester but it's interesting I can't remember it vividly. By vivid memory, I mean the desire to recall it and the accompanying happiness that's usually associated with all memory. My last vivid memory seems to be Siggraph. So it's likely that beginning of 2024 events did impact the memory structure. I also proved that memory can in fact be eliminated or altered after extremely strong emotional manipulation. The M+2 effect is still there. Also the music stimulation works stochastically so would be interesting to see how exactly stimullting music "resonate" with brain.

# Tracks
## Economics
- finiancial intro (mathematical finance, Paul Wilmott on quantitative finance)
- modeling (brownian motion calculus)

## Statistics
### Traditional
- naked statistics

### 
## Programming

## AI
- RL
- Hinton Youtube class
- cs229 notes (traditional methods)

## Computational Neuroscience
- dynamics (after Chaos book, read we are electric, rythms of brain (if problems, read also system dynamics), Neurodynamics)
- 

## Physics
- Feynman
- Taylor Hamilton chapter and profoundphysics book
- relativity (einstein and einstein book)


# Periodiciity
- 10.15 (2): ate before sleep 10:30, had phone call with lhl.
- 10.16 (3, 4.56-0.54): energetic, watched, back workout, run aborted due to cold air
- 10.17 (4 Fall break, 5.41-1.11): very drowsy, m, late lunch, feels like there's a diminished part of brain constantly operating but not very efficiient, can't easily stop it either, loss of motivation at all things
- 10.18 (5, 6.41-0.44): very concentrated, wet feet, not sleepy throughout day but tired in the afternoon. Did some workout but didn't run much due to dry air. Ate at night 9:35
- 10.24 (4, m, chase): feeling good
- 10.25 (5, milk and sqm): tired for no obvious reason
- 10.26 (6, reality fest, milk and sqm): sleep late and extremely tired after coming back
- 10.27 (7, m, cold): not well even with mega and m late afternoon feel better  afterwards
- 10.28 


# Ideas
## School Related
### Course Plan
- Literary Arts: Cicero

HS CI BN GL

math for physics: https://www.youtube.com/watch?v=m_SbJnpMDD8

### Interested
- ECON 231 Economic History of Western Europe
- ECON 234 Survey of the History of Economic Thought

- ARTH 151 History of Western Art I

- NSCI 222 - LEARNING
- NSCI 423 - NEUROTECHNOLOGY
- NSCI 421 - PRINCIPLES OF BRAIN CIRCUITS
- [NSCI 434 - COGNITIVE NEUROSCIENCE]

- Hist 158 Early Modern Europe
- HIST 266 history of warfare
- HIST 315 NATION BUILDING LATIN AMERICA
- HIST 340 ETHICS AND BUSINESS IN AFRICA
- HIST 538 MIDDLE EAST & THE WEST
- MUSC 120 Foundations in Music
- PWAD 490

## Psychology
### Visual and Auditory Logic
- maybe people who use linguistic logic better are aided by music or sound, and those who use visual logic are aided by light, or other visual stumuli. This could explain why I feel scattered in rainy days. This could also explain the old days in school where Chinese schools have very bright lights (need to verify).
 

## Projects
### Talk to make a world
basically auto game engine with ML to code stuff from what people tell them to do. everyone wants to create a world of their own and rule everything. dumb people can benefit from ML: engine ask conditions to make them exhaustive so ppl don't have to think of every cases.

### ML for Education
Find salient feature of things to teach. e.g. ni language, what's different and what's the same across and inter languages. Find easiest to remember and most important feature of the material.

### Universal Linker
Just like how brain links information from different modalities, note taking should focus on relations. e.g. drag a page on pdf to become a link just like url, everything on any software should have a unique location marker for reference.

### Spirited Away Train


## AI and Brain
### On Knowledge
> 20 years ago SVD (invented 1873) wasn't in linear algebra and 100 years ago no one use linear algebra.
Were they actively looking for and discovered ancient technics when they need more math to solve problems? How could they discover it? Did they use to know everything?

#### Knowledge Map
It's useful to connect everything to everything else but that requires n^2 computaion. Even future AI can't do it. But in the case of scenary information, we know how every location relates to every other location and we know how to go from anywhere to anywhere with little thinking. It's because we have a map that gives us overall view of everything. Manifold learning is thus important.

### On What is Learning When ML is Just An Optimizer
To fit a function as complex as a DNN, some properties in the middle of the network have to emerge. If they are human understandable then it "learned" something. This is also the thought of Hinton and what he convinced the Nature reviewer with.

### On Consciousness, Evolution and Optimization
We do a lot of amazing things, but animals can also do most of them. It's important to identify things that truly make us superior. I think I'll just define those properties as "high consciousness". Through evolution, animals began to have interesting traits and behaviors that offer evolutional advantages. Through kin selection and corporation they can even naturally develop behaviors that optimize complex games like war and social hierarchy. To empower these actions, animal brains must be powerful. We can see animals perform human like behaviors like doing chores and trade. These are not consciousness though. Currently I think language and symbolic thinking is key to consciousness as they establish a clear information flow inside brain (see quotes from The Story of My Life). 

https://www.perkins.org/laura-bridgman/

### Reading The Story of My Life (Helen Keller)
- > At first, when my teacher told me about a new thing I asked very few questions. My ideas were vague, and my vocabulary was inadequate; but as my knowledge of things grew, and I learned more and more words, my field of inquiry broadened, and I would return again and again to the same subject, eager for further information. Sometimes a new word revived an image that some earlier experience had engraved on my brain.

### On Logical and Natural Optimization/Why Our Logical Strategies Coincide Natural Phenomena
We see tit for tat in animals even when this is also deduced from human analytical thinking. We see learning algorithms reach local minima when human also reach local minima with the exact logic i.e. it looks good from where I came from and without an external nudge this will always be the best solution I can see. This is because systems have to follow the same physical laws and their high level behaviors have to sometimes follow patterns to satisfy those laws.

### On local minima
Humans are prone to local minima. The physical configuration of human body admits infinite behaviors. Behaviors lead to consequences within their context. There are only finite context one will encounter. Thus many configurations will fit these seen contexts and people with "bad" configurations will believe they are smart such that they can solve problems they have seen. ML might be able to exhaust the data and learn a "true" good configuration (Greco-Roman+bad time?). 

### Learning from examples is superficial
Related to previous idea.

Create "inductive bias" as teaching more low level principles one at a time so it really understands things. Like in nerf where knowing geometry makes color optimization easier.

If we can "train a complete adult" model it will fulfill half of the quest. The problem is it's difficult to train. We need layered structure and train them one by one with appropriate tasks

### Early Neural Network Success
- 1989: Backpropagation applied to handwritten zip code recognition
- 1989: minimizing the number of free parameters in neural networks can enhance the generalization ability of neural networks
- 1996: Neural Network-Based Face Detection

> even though the problem (zip code) is linearly separable, single-layer networks exhibited poor generalization capabilities. When using shift-invariant feature detectors on a multi-layered, constrained network, the model could perform very well. He believed that these results proved that minimizing the number of free parameters in the neural network could enhance the generalization ability of the neural network.

### Misc
- artistic training during childhood change structure of brain forever and can't be done in adulthood?
- Neuron plasticity inspired SOM might work on very small tasks where all layers before are frozen and provide a solid inductive bias
- A brain should distinguish "self" from everything else. Emergent property of complex network?

## Advanced AI and Brain
### What Counts as Output (Consciousness)
Since we don't know how consciousness arises,we don't know if it's the spatial or temporal activations of certain neurons or a certain pattern of transmission of potentials that matters as desired output of a network.

### Modeling Relationship Between Interesting Neurons
We can find certain neurons that's activated by certain things but we don't know connections between these neurons. To study how information is processed, we must either identify all connection strength between neurons of interest or build statistic models to measure how different "metaneurons" relate to each other.

### Function of Hippocampus as Associative Center


### Infinite Memory
If "one memory" corresponds to a pattern of activations of certain neurons, then given infinite connection complexity, different inputs (senses) can leads to (recall) 2^n memories. 

#### Problem of Null Memory
If recalling of memory means reading from a certain groups of neurons, then attempting to recall when given non recallable inputs should theoretically be still possible and would yield some random memory. But this didn't happen. For example, reading books read before gives some feeling of knowing stuff ahead but reading new books doesn't, though some activities have to be happening at the same region activated in the former event.

### Misc
- We can sometimes remember if we have recalled a memory or not 
- What happens in dream can be as influential as reality and thus more powerful than imagination

### Recurrent Connections
Two way information processing means two way learning (e.g. an image -> an idea + the idea -> the image)

### Horizontal Connections
Recurrent horizontal connections can be converted to hopfield network

## On Projection
### The World as Projection of an Underlying Structure and Every Natural Science as Projection Problem

### Logic as an Infallible Structure of the World

### Math as THE structure / Language of the Universe

Math provides language for the structure of things. When we see things happen, we first try to reason abstractly the underlying force that drives the happening. This is abstract. To prove something to be true, a language infinitely precise is needed. With this language can we really say this force produced such results.

See "Math and Physics" for whether math itself provides the structure.

### Math and Physics
It seems that primitive math emerges everywhere out of basic needs and grows as economy of the region. However, once physics is born, math becomes tool of physics. 

However, in a different lens, math is a desire to precision, and it inevitably leads to reduction to some extremely primitive and precise/self evident postulates. This is similar to physics's attempt to find something basic that explains everything complex. It also follows from these postulates that 

### The Middle Way and Projection
We often find theories uniting existing conflicting theories or find a solution mixing several more extreme solutions better. This is just how inverse engineering works. When you have modal specific information/projection, you can only construct a part of it, that's also called bias. When many people see different projections, first of all they are likely all right because a projection is a projection no matter from which angle it is from, the collective knowledge obtained by combining all their reconstruction result will give a better approximation. In terms of partial projection where everyone receives shadow of part of the object, collective knowledge reveals the whole. 

### P-NP

## Metaphysics
### Components of Philosophy
1. Eternity: At some point in life, we ask what's our purpose. By association, we have the natural concept of cause and effect. Further by the behaviorist education methods powered by our existing reward mechanism, we learn to associate everything with purpose. We ask the purpose what we do now and get an answer. We then ask the purpose of whatever that answer is. This can be repeated indefinitely, leading to the concept of eternity. Philosophy is thus the search for eternity. Another way to lead to the thought of eternity might be the search for durable material, similar to Russel's idea. How to build things that last forever. Most study of eternity before enlightenment had focused on Form since form was considered eternal. Religion also has a big component of eternity, and many religious arguments are also inspired from backward tracing (infinite regress) of purpose which leads to logical existence of God.

1.5. Death and happiness: We are driven by happiness and we want happy moments to last longer. As long as we are happy we don't worry about death and [it seems that happiness for life is an ideal goal for human]. 

2. Sceptic: What we see and hear gives association of ideas. And by associating repeating events we have the concept of universal. But association is not universal. One event doesn't always lead to another. We thus acquired an association from everything to a question about universality. The impetus to always ask question forms the the most obvious way to do philosophy: ask and ask more. In asking we break up vague sentences into concepts. We also formalize rules to operate concepts called logic. This relates to eternity because these rules need to be eternal because based on our experience of change, changing rules gives changing observations and one thing cannot be both is and is not. 

### On Logic
Since I feel Plato's idea of form is nonsense, I was trying to prove how every idea is derived from senses. It's easy to see that numbers have some clear physical meanings: two object normally result in two complete contours; two sounds are separated or differentiated naturally. However, logic seems more mysterious. Logic like parallel line postulate doesn't correspond to physical things that have clear boundaries. It is from some precise definitions that live on their own. Processing of them doesn't elicit sense memories but is a byproduct of some functions of brain. It's also possible that the most primitive logic are indeed generalizations of senses. For example:
![](/images/common-notions.png)
These are completely from senses. And from such generalizations we can build prepositional logic and others. So are also for numbers like: 1-A unit is that by virtue of which each of the things that exist is called one. 2-A number is a multitude composed of units.

![](/images/postulates.png)



### Ontology
#### Existence of Idea
I have an idea of a car because I've seen and rode a car and sensed it with all my sense organs. But does the idea exist by its own, i.e. If there are no humans, do cars exist?

Some people believe that these physical things, these "matter" are always real regardless of observation. However, a more difficult case would be something like this: a program exists because I have written it and run it, but I know there are infinitely many programs that "exist" but are yet to be written. We might solve this by having different levels of existence (exist now, past, future). 

But what about pure ideas? What about the relationship between a circle and its radius? The relationship never changes. But does it exist without being discovered?

## History
### Assumptions
- What happens if Medieval is skipped (Rome conquered all of Europe and slavs)

### Comparative
- Why Muslin golden age didn't produce Enlightenment and Scientific Revolution
- Different paths Mediterranean and China took in ancient times
- Compare China with Europe after Rome before Modern Era
- What exactly powered the train of Renaissance to Industrial Revolution
- What's lacking in Chinese and Islamic science compared to European science.
- How is communism different from "good" colonialism.

### 
- Why didn't Rome continue Greek legacy

## General
### 
- The language of literature is too full of emotions and experience that only looking back at the words as your own memories can you truly understand; the language of political philosophy is too full of hate and beliefs, understanding them is thus to become a cult; only the language of science is impartial, it stands above feelings and senses. 
- People don't have a sense of time yet they care about ideas like "recently" "not long ago" "long time ago" "ancient". As long as they are not born at that time, it doesn't matter to them if you describe a time period as 10 years, 100 years, or 1000 years ago. Lack of historical integrity.
- Number 3 is very interesting. When we see things the second time, we are excited because we can recognize it, but when we see it the third time, we sense a pattern. Also Taoism says everything is from 3. Also the cocktail treatment use combination of 3 drugs. Triangle has 3 sides and is most stable...

## Pedagogy
### Why Learn Everything with History
It is most natural to learn things from historical perspective. True learning comes from answering questions asked by oneself. The questions arise naturally given historical context since it's that exact same context that prompted people to ask the question that leads to the solution we are trying to learn. The answers also lock tightly with the historical question since we are all humans having essentially similar processes of innate minds.

Time is totally ordered. Any other categorization is set and by partially ordered.


## Movies to Watch
- The Last of the Mohicans
- Indiana Jones
- battle of algiers


## Quotes
### Books
#### Feynman
- On meaning of physical laws: Although it is interesting and worth while to study the physical laws simply because they help us to understand and to use nature, one ought to stop every once in a while and think, "What do they really mean?" The meaning of any statement is a subject that has interested and troubled philosophers from time immemorial, and the meaning of physical laws is even more interesting, because it is generally believed that these laws represent some kind of real knowledge. The meaning of knowledge is a deep problem in philosophy, and it is always important to ask, "What does it mean?"
- "science is the belief in the ignorance of experts"
#### Heisenberg
- On physics and philosophy: My mind was formed by studying philosophy, Plato and that sort of thing". "Modern physics has definitely decided in favor of Plato. In fact the smallest units of matter are not physical objects in the ordinary sense; they are forms, ideas which can be expressed unambiguously only in mathematical language"

#### Da Vinci
- On flight (not really from him): When once you have tasted flight, you will forever walk the earth with your eyes turned skyward. For there you have been, and there you will always long to return

#### Einstein
- On physics (from evolution of physics): Physical concepts are free creations of the human mind, and are not, however it may seem, uniquely determined by the external world.
- His love of algebra and geometry was so great that at twelve, he was already confident that nature could be understood as a "mathematical structure".

#### Archimedes
- On love for pure ideas (Plutarch): Archimedes possessed so high a spirit, so profound a soul, and such treasures of scientific knowledge, that though these inventions had now obtained him the renown of more than human sagacity, he yet would not deign to leave behind him any commentary or writing on such subjects; but, repudiating as sordid and ignoble the whole trade of engineering, and every sort of art that lends itself to mere use and profit, he placed his whole affection and ambition in those purer speculations where there can be no reference to the vulgar needs of life.
- On his proof of area of circle equals triangle of height r and base Q (circumference) (Plutarch): No amount of investigation of yours would succeed in attaining the proof, and yet, once seen, you immediately believe you would have discovered it.

#### J. R. R. Tolkien.
- I love not the sword for it's sharpness, nor the arrow for it's swiftness, nor the warrior for his glory, I love only that which they defend.

#### Others
- On Joseph II of the Holy Roman Empire: "Everything for the people, nothing by the people"



### Talks
#### Ivan Sutherland
- On research: ”So projects can be wonderful fun. In fact, I have the attitude that if research is not fun, why are you doing it? Are you exploring the unknown, and why in the world would you bother doing that? You cannot do it for rewards, because you do not know what the rewards are. You do not know what you will find, so you do it because it is an adventure, because the spirit and the camaraderie of a research group is one of the things that makes research worth doing. I think that is important. An important thing to know about research is that **if the researchers are not happy, there probably is not much research going on. It is hard enough wrestling with nature that you do not want also to have to wrestle with management.**”

#### Alan Kay
- On David Evans: Dave's way was to make something like a garden, and tend that garden so that many things would have many chance to grow by themselves. His idea was to just do good deeds everywhere and every time you can without any hope of return. And much of the time the angelic side of humans will nudge other humans to start helping themselves.

#### Hinton
- On intuition and knowledge distillation: you need to put in a lot of hard work to get sufficient experience in a domain and then you need to trust your intuitions. 
- On politics and science: I grew up in Britain in the 1950's and 60's and a major puzzle at the time was to understand how civilized and well-educated Germans could have allowed Hitler to gain power. Recent events in the US have made that seem a lot less puzzling. ... I believe that highly selected and extremely well-educated students like yourselves have **a moral duty to stand up for the truth in the face of political attempts to suppress it.**

#### Dirac
- On art: The aim of science is to make difficult things understandable in a simpler way; the aim of poetry is to state simple things in an incomprehensible way. The two are incompatible.

### Movies
#### Oppenheimer
- "When you speak they hear a prophet, when Straus speaks they hear themselves", "They'll listen to the prophet", "The prophet can't be wrong, not once."

#### The Green Book
- You? Mr. Big Shot. You live on top of a castle. Traveling around the world doing concerts for rich people.  I live on the streets. You sit on a throne. 
- The world's full of lonely people afraid to make the first move



### Forbes
- Bernard Arnault: I see myself as an ambassador of French heritage and French culture. What we create is emblematic. It's linked to Versailles, to Marie Antoinette.
- Elon Musk: I operate on the physics approach to analysis. You boil things down to the first principles or fundamental truths in a particular area and then you reason up from there.
- Jeff Bezos: I didn't think I'd regret trying and failing. And I suspected I would always be haunted by a decision to not try at all.
- Larry Ellison: When people start telling you that you're crazy, you just might be on to the most important innovation in your life.
- Bill Gates: Money has no utility to me beyond a certain point. Its utility is entirely in building an organization and getting the resources out to the poorest in the world.
- Carlos Slim Helu: When you live for others' opinions, you are dead. I don't want to live thinking about how I'll be remembered.
- Larry Page: You never lose a dream; it just incubates as a hobby.
- Sergey Brin: Obviously everyone wants to be successful, but I want to be looked back on as being very innovative, very trusted and ethical and ultimately making a big difference in the world.

### LATIN
- VIVAMUS MORIENDUM EST
- FORTIS FORTUNA ADIUVAT
- NIHIL SUB SOLE NOVUM
- SI VIS PACEM PARA BELLUM
- PER ASPERA AD ASTRA
- DUM SPIRO SPERO
- DUM VIVIMUS VIVAMUS
- ERRARE EST HUMANUM
- COGITO ERGO SUM
- CUI BONO
- ALEA LACTA EST
- dimidium facti, qui coepit, habet; sapere aude, incipe (He who has begun is half done; dare to know; begin!)
- novus ordo seclorum
- annuit coeptis/deo faventi
- invia virtuti nulla est via
- seu dea tu praesens, seu dis gratissima, numinis instar eris semper mihi

### Internet
- On Merry go around life: it makes you miss a life you never had
- On Miyazaki's answer of who No Face is: I was always wondering who no face was, little did I knew, I was the no face all along
- "The battle make a man a hero... Death makes the hero a legend... Time makes the legend a myth... ...and that myth inspire a man.

## Good Music
### Classical
- Shostakovitch - Waltz no.2
- VIVALDI - The Four Seasons, Concerto No. 2 "Summer": III. Presto
- DVORAK - Symphony No. 9 in E Minor, "From the New World": IV. Allegro con fuoco
- Brahms - Hungarian Dance No. 1 in G minor. Allegro molto 
- Jenkins - Concerto Grosso for Strings "Palladio": I. Allegretto


## Recent Thoughts
- 9.13: reading Dreaming and the brain: from phenomenology to neurophysiology, Building machines that learn and think like people. Consciousness, CNN and k-nn, other inputs coming from working and long term memory to fine tune boundary cases with imagination. Memory of internal thoughts and why are they transient, how are they related to dreams. 
- 9.29: I've successfully connected a brain thought while waking up in middle of night to "note taking" and remembered it once I saw this app

# Reviews
### Brilliant.org
Very good visual and interactive interface. Sequences are good as long as you know what they want to teach you. But for beginners, lack overarching insights are what users are being taught. Consider promoting more reflections from the user instead of old style multiple choice questions.

Gets interesting starting at Light and Quantum in Physics module. Best intro to this subject I've seen so far.

# 
91.79K
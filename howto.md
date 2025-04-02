# Util/Tools
## Longleaf
- loginL ssh zhw@longleaf.unc.edu
- work directory: cd /nas/longleaf/home/zhw
- storage directory (conda, data): /work/users/z/h/zhw/ for high throughput io

## SLURM
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

## Jupiter
- jupyter notebook --no-browser --ip=0.0.0.0 --port=8080
- ON LOCAL MACHINE: ssh -L 8080:c1121:8080 zhw@longleaf.unc.edu
- lsof -i :8080
- kill -9 <id>
- VSCODE: see vscode section
- forward to local browser: jupyter notebook --no-browser --port=8080; ssh -L 8081:localhost:8081 zhw@hires-gpu1.cs.unc.edu

### Troubleshooting
- Module not found: 1) if python file check interpreter setting 2) if notebook: check if you can use the module in terminal, if yes, install jupyter in your current env. If no, in command line "pip show pkg_name" and add the path to code 
```
import sys
sys.path.append('/nas/longleaf/home/zhw/miniconda3/envs/scrap/lib/python3.11/site-packages')
```
- check which version of a package is used, if version is wrong, change the kernel inside jupiter notebook UI, select another kernel->Python environments
```
import bs4, sys

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("bs4 module path:", bs4.__file__)
```
- Restart terminal


## UNC Computers
- AD means onyen
- AD needs internet access


## Tensorboard
- tensorboard --logdir log; ssh -L 16006:127.0.0.1:6006 zhw@hires-gpu1.cs.unc.edu then go to http://127.0.0.1:16006: tensor board on ssh




## Git
### Create Repo
https://learngitbranching.js.org/
clone
- git clone

create new
- git init: initialize current directory
- git add .
- git commit -m "initial"
- go to github.com and create repo, or use gh command 
- git remote add origin git@github.com:wwwwwwzh/code-mapper.git
- if added readme: 
    - git branch --set-upstream-to=origin/main main
    - git pull --allow-unrelated-histories
    - i to type message and esc and :wq
- git push -u origin main
- password is the ssh private key in keys.txt file alternatively it's in slack

- git branch branchName
- git checkout branchName
- git checkout -b branchName
- git merge branchName
- git rebase branchName

### ssh
The process is as follows: you run a git clone command with an SSH URL; Git starts ssh to connect to the github.com host as git user; ssh connects and successfully authenticates by the 1st keypair; GitHub recognizes that it's the user that has access to the repository so it accepts the request at the Git protocol level

- create new key for github: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- add key to github: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- multiple keys for multiple github accounts: https://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config


### Relative 
- git log
- git checkout commitHash
- git checkout branchName^
- git checkout HEAD^

- git reset --hard commitHash
- git reset HEAD~1
- git revert HEAD: new commit with content as previous commit. Use with pushed commits.

## Node
- upgrading node by first 'brew upgrade node' then 'brew link --overwrite --dry-run node' then 'brew link --overwrite node'

## C
- CMake: https://askubuntu.com/questions/829310/how-to-upgrade-cmake-in-ubuntu

## Vim
- insert: i
- esc
- :wq (w is save, q is quit)

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

### matplotlib
export PDF
- pdf makes components easy to change
- `plt.savefig("path.pdf", format='pdf')` before plt.show()

boxplot with scatter points
```py
bp = plt.boxplot(
    all_runs,
    vert=True,
    positions=[0, 1, 2],
    widths=0.2,
    whis=[5, 95],
    showfliers=False,
)

for median in bp['medians']:
    median.set_color('orange')

x_jitter = np.random.normal(i, 0.04, size=len(filtered_data))
plt.scatter(
    x_jitter, 
    filtered_data,
    color='gray',
    alpha=0.8,
    s=80,  # Large points
    zorder=0  # Draw behind boxplots
)

plt.axhline(y=0, color='red', linestyle='--', linewidth=1)
plt.xlim(-0.5, 2.5)
plt.xticks([0, 1, 2], ['Run 1', 'Run 2', 'Run 3'], fontsize=14)
plt.ylabel('Correlation', fontsize=20)
plt.yticks(fontsize=20)
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
plt.grid(True, alpha=0.3)
plt.tight_layout()
```

## Inkspace
- when import pdf select substitude missing fonts

# Linux
## General Bash Commands 
- source ~/.bashrc or ~/.bash_profile
- df -h: view storage devices
- du -sh: view directory size
- pstree / ps aux: show running processes

- screen -S "12917.tdnerf_baseline" -X sessionname "newname"

- watch -n 0.5 nvidia-smi 	# shows the GPU usage
- htop				# shows CPU usage

- scp -r /path/to/directory zhw@hires-gpu1.cs.unc.edu:/playpen1/wzh/files/: copies the directory itself into files folder
- cp -r ~/folder1/. ~/new_folder1: copies contents of folder1 to a new folder (will create if not exist)

## Package
### Build package without sudo
case study:
ask deepseek:
(base) [zhw@longleaf-login2 ~]$ curl --version
curl 7.61.1 (x86_64-redhat-linux-gnu) libcurl/8.4.0 OpenSSL/3.0.12 zlib/1.2.11 libssh2/1.11.0
i don't have sudo how can i download a new curl and link to libcurl/8.4.0

## Module




## cuda/torch download
- cuda version, nvcc version and torch version must match
- when compiling custom c++ packages into pip package using cuda sometimes you run into gcc incompatibility. check with `gcc --version` and `module avail gcc` and try `module load gcc/{version_number}`
> https://docs.google.com/document/d/1S8PU4EbigzlvSx4x_Ay835hMAjB8bCpouoWcNIyvTbc/edit



## General Troubleshooting
Step 1: Follow the below guide
Step 2: Use ChatGPT
Step n: Go do something else 

### Conda
see conda troubleshoot

### module/command not found: 
- is your library in system path in ~/.bashrc or ~/.bash_profile
- a command run in terminal should be in $PATH. If you used pip install they are in conda env which are not supposed to be run as terminal command. Use the full path to the pip package.
- are there multiple packages. use `pip show pkg_name` or `which pkg_name`. if there are multiple use `echo $PATH` and see which path takes precedence. delete accordingly. 
- can you run the command in terminal? If yes, then 1) check if there are package specific path loaction 2) are there multiple versions of a package. If no, 1) have you downloaded the right thing 2) have you linked it in system path

use for checking python path:
```
import sys
print(sys.executable)
```

### Python
https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/#How-Python-locates-packages
- there are multiple pythons in your computer. Your conda environment (including base) has a copy of a version of python. Your system also have its own python version. Also check your PATH to see which pythons are seen. Use 'which python' to see where current python is.

### Package Not Installing
- Check python version
- copy paste the whole error message to chatgpt
- --no-build-isolation

## Others
### Download from google drive
- rclone config
- rclone copy "gdrive:" /nas/longleaf/home/zhw/personal/gs/data --drive-root-folder-id 1nUNWrFLKmK2g-ClJ4Nd9OGuxhYeu6Sv7 -P


# Huggingface
```py
import os
from huggingface_hub import login

os.environ["HF_AUTH_TOKEN"] = x # x is "token"
login(x)
```
- for some gated model, request access and all your API keys will have access

# conda
## Basics
### Conda cli
note that sometimes installing packages will fail with conda install. First update base conda (conda package manager itself is in the base environment):
`conda update -n base -c defaults conda -y` 

### Mamba
- conda install -n base -c conda-forge mamba -y 
> install only once to base env
- mamba create -n colmap-env -y
- mamba install -c conda-forge cmake libuv -y
> -y means yes to all prompts

### Installation
follow codes here https://docs.anaconda.com/miniconda/#quick-command-line-install 

- conda create -n your_env_name
- conda activate your_env_name
- conda env list
- conda list

> sometimes you need to manually do `conda install anaconda::pip` and make sure `which pip` points to current env, otherwise pip installed packages will go to user local locations.


### Removal
https://docs.anaconda.com/anaconda/install/uninstall/
On macbook pro my miniconda is in home directory

### Export Environment 
- conda env export > environment_gp.yml

## Troubleshooting
- `which pip` should output `miniconda3/envs/env_name/bin/pip`, if not do `conda install pip`
sometimes you can do `pip cache purge`
- solve environment forever (making new env should not take more than 2 minutes and installing a package should not solve for more than 1 minute): remove and reinstall conda

## Move conda
### Download new
1. do not export environment files 
2. download conda at new location
3. unset PATHONHOME and PYTHONPATH
4. reset PATH
5. conda init
6. create environemnts with the files. 

### Move Env/pkg

### Save New env to new location


## Specific Downloads
### build gaussian splatt cuda libraries
before running `pip install -e submodules/depth-diff-gaussian-rasterization`
- module avail cuda
- pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{version}
> cuda and torch version must match
- export CUDA_ROOT=/nas/longleaf/rhel8/apps/cuda/11.8
- export CUDA_PATH=/nas/longleaf/rhel8/apps/cuda/11.8
- export CPATH="/nas/longleaf/rhel8/apps/cuda/11.8/includee"

### Colmap
- **mamba install conda-forge::colmap**


FAILED (no root user, cuda compile)
- git clone https://github.com/colmap/colmap.git
- cd colmap
- mkdir build
- cd build
- mamba install -c conda-forge cmake libuv ninja boost-cpp eigen ceres-solver gflags glog freeimage suitesparse metis cuda-compiler flann cgal mesa-libgl-devel-cos7-x86_64 glew
- check where is cuda toolkit: which nvcc 
- ls /nas/longleaf/rhel8/apps/cuda/11.8/lib64/libcurand*
- cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/colmap-install \
    -DCUDA_TOOLKIT_ROOT_DIR=/nas/longleaf/rhel8/apps/cuda/11.8 \
    -DCMAKE_LIBRARY_PATH=/nas/longleaf/rhel8/apps/cuda/11.8/lib64 \
    -DCUDA_curand_LIBRARY=/nas/longleaf/rhel8/apps/cuda/11.8/lib64/libcurand.so \
    -DCMAKE_PREFIX_PATH="$CONDA_PREFIX" \
    -DCUDA_ENABLED=ON
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/colmap-install \
    -DCMAKE_C_COMPILER=/nas/longleaf/rhel8/apps/gcc/11.2.0/bin/gcc \
    -DCMAKE_CXX_COMPILER=/nas/longleaf/rhel8/apps/gcc/11.2.0/bin/g++ \
    -DCMAKE_CUDA_FLAGS="-ccbin=/nas/longleaf/rhel8/apps/gcc/11.2.0/bin/gcc" \
    -DCMAKE_PREFIX_PATH="$CONDA_PREFIX" \
    -DCUDA_ENABLED=ON
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/colmap-install \ 
    -DCMAKE_PREFIX_PATH=$CONDA_PREFIX \ 
    -DCUDA_ENABLED=OFF  

- make -j32 (use `lscpu` to see how many cores and `ulimit -a` to see memory size)
- optional if failed: make clean
- make install
in bash: 
```
export PATH="$HOME/colmap-install/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/colmap-install/lib:$LD_LIBRARY_PATH"
export C_INCLUDE_PATH="$HOME/colmap-install/include:$C_INCLUDE_PATH"
export colmap_DIR="$HOME/colmap-install/share/colmap"
```
- source ~/.bashrc
- colmap -h


# Conventions
## Naming Convention
### Variable
general
- postfix by type
    - i
    - f
    - b
    - v
        - vi: vector of ints
    - v2

### Function


# Harware
## Network
### Connect 2 PC trough ethernet
1. control panel->network and sharing->click ethernet->properties->IPv4->properties->change IP to 192.168.1.1, musk to 255.255.255.0 router to 192.168.1.1
2. on the other PC change IP to 192.168.1.2, musk to 255.255.255.0 router to 192.168.1.1
3. ping each other


# Mac
### Strike through shortcuts
https://discussions.apple.com/thread/7154458?sortBy=rank



# Server setup
## Longleaf
on local machine terminal 1
1. ssh zhw@longleaf.unc.edu
2. srun --partition=volta-gpu --gres=gpu:1 --time=04:00:00 --qos=gpu_access --pty bash
3. conda activate agent
4. cd 
5. python api.py

on local machine terminal 2
1. ssh -N -L 5000:g181103:5000 zhw@longleaf.unc.edu
2. go to localhost:6001/?key=abc
> `sudo lsof -i :6001` to view which process is using a port. `kill -9 id` to kill.

# UNC
## SSO
if cookie issue: 1) go to connect carolina and login, 2) delete browsing history containing sso and unc and any website that required unc sso login (eg parchment)

# Prompt
## Chatbot
### GPT
- when building something complex: don't assume, when in doubt ask me for clarification.
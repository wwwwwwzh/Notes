# Quick Notes
## Summary
1. manual entry point
2. 1st scan: ast for each file for each function to register all internal functions 
3. 2nd scan: for each registered function, give the raw and meta to LLM for description and component segmentation
4. 3rd scan: for each function, use CallAnalyzer to find calls, then register segments to the function, then to components.
5. upload to database
6. for each function build a RAG index

## bugs
### Parser
- call in the syntax of with and with call as

### Tree Nav
- click function should scroll the custom functions
## Plan
### Func Tree
interactive tree that shows all function and all calls so user can click one and all this functions will highlight 

### Viewer (use monaco?)
- within function variable tracking, vscode like highlight and cmd click
- cmd+click to see caller and update nav tree (change the search function section to custom entry panel), this can only select one caller, see below for inverse tree
- the current approach has a function as root and its calls as nodes, need to also build inverse tree, where a function is root but its CALLERS are nodes
- a file persistence system as in vscode to navigate btw open files

### RAG
- the paper, the readme, and a call chain should be incorporated when building index for a function
  - baseline: 

### Function Tester
For each function, store sample input output and make the code viewer be able to also run code.

Or just setup the venv for each repo so users can directly run the code online


### Read
- https://github.com/anthropics/anthropic-cookbook/tree/main?tab=readme-ov-file




# Project structure
## Processing
### Repo Control
summary
- the url is hashed as a key to repos
- repos are stored directly in the project folder 

plan
- database?

3.30
- the url is hashed as a key to repos
- repos are stored directly in the project folder 

### Code Analyzer
summary
- llm analyzes readme and find the entry points
- entry functions: entry file is parsed with ast and all of its function names and codes are returned
- function snapshot: each function is analzed by llm to create a short summary text and detailed description
- function workflow: 

workflow
- only look at function calls first
- 

plan


3.30
- llm analyzes readme and find the entry file
- entry file is parsed with ast and all of its function names and codes are stored
- each function is analzed by llm to create a short summary text and detailed description
- (plan) under the repo the output at each analyzer step should also be stored
- (plan) the ast should also give all variables and function calls inside functions 

3.31
- entry file analyzer input is the file tree and the input (first summarized by a small hf model)
- entries are lists of structure that include file name and function name
- the entries are used to build ast
- ast nodes now has two types, internal call and code literal. internal calls have child nodes. 
- (plan) the whole tree should be built and the user will either see a default tree at a depth or they can type in what they want to focus on and see a new tree that omit unimportant parts (search 2 levels, find potential nodes (increasing number?) at first level and recurse). 
- note that we exclude the following top level files/folders: [docs, benchmark, assets, LICENSE]

## Presentation


## Notes
### Line Number
The basic component is function. Also, functions are sent to LLM for analysis. We have the function start line number (def line) given by ast, which is the actual code editor style line number (starting from 1). So if def is at line 1, then when you read the whole file you need to read the function from lineno-1, and the list of lines will have def at index 0. 

- lineno starts at 1
- endline is not the line after endline, so one line will have start and end the same

At scan project, 




ast_parser.py:698 - INFO - analysis={'short_description': 'Softsplat forward pass', 'input_output_description': 'Takes three inputs (tenInput, tenFlow, tenMetric) and returns one output.', 'long_description': 'This function performs the forward pass of the Softsplat module, utilizing the provided input, flow, and metric tensors.', 'components': [{'start_line': 1, 'end_line': 1, 'short_description': 'Function definition', 'long_description': 'Defines the forward function with three parameters: tenInput, tenFlow, and tenMetric.'}, {'start_line': 2, 'end_line': 2, 'short_description': 'Return statement', 'long_description': 'Calls FunctionSoftsplat with the provided inputs and self.strType, returning the result.'}], 'function_name': 'softsplat.ModuleSoftsplat.forward'}
ast_parser.py:707 - INFO - comp={'start_line': 1, 'end_line': 1, 'short_description': 'Function definition', 'long_description': 'Defines the forward function with three parameters: tenInput, tenFlow, and tenMetric.'}
ast_parser.py:707 - INFO - comp={'start_line': 2, 'end_line': 2, 'short_description': 'Return statement', 'long_description': 'Calls FunctionSoftsplat with the provided inputs and self.strType, returning the result.'}
ast_parser.py:690 - INFO - func_60, {'id': 'func_60', 'name': '__init__', 'full_name': 'Q_Slerp.quaternion.__init__', 'simple_name': 'Q_Slerp.__init__', 'module': 'Q_Slerp', 'class_name': 'quaternion', 'file_path': '/tmp/code_tree_pxej4h7g/D2RF/Q_Slerp.py', 'lineno': 30, 'end_lineno': 50, 'callers': [], 'callees': [], 'segments': []}
llm_function_analyzer.py:94 - INFO - Analyzing function: Q_Slerp.quaternion.__init__ using groq
llm_function_analyzer.py:287 - INFO - Successfully received response from Groq API
llm_function_analyzer.py:109 - INFO - Analysis received
llm_function_analyzer.py:119 - WARNING - Attempt 1/1 failed: 'components' must end at last line of function
Error analyzing function Q_Slerp.quaternion.__init__ with LLM: 'components' must end at last line of function
Traceback (most recent call last):
  File "/home/webadmin/projects/code/app/utils/ast_parser.py", line 697, in scan_project
    analysis = analyze_function(func_content, func_info['full_name'], provider="groq")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/webadmin/projects/code/app/utils/llm_function_analyzer.py", line 114, in analyze_function
    validate_slots(func_length, analysis)
  File "/home/webadmin/projects/code/app/utils/llm_function_analyzer.py", line 384, in validate_slots
    raise SlotFillingError("'components' must end at last line of function")
app.utils.llm_function_analyzer.SlotFillingError: 'components' must end at last line of function


Error analyzing function render_utils.DSKnet.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function render_utils.DSKnet.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.PNetLin.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.PNetLin.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.ScalingLayer.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.ScalingLayer.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.NetLinLayer.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.Dist2LogitLayer.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.Dist2LogitLayer.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.BCERankingLoss.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.BCERankingLoss.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.FakeNet.__init__: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.L2.forward: unexpected indent (<unknown>, line 1)
Error analyzing function models.networks_basic.DSSIM.forward: unexpected indent (<unknown>, line 1)



needs to update prompt to tell LLM how to extract component
# Libraries
## AST
- python only
### Nodes
Expression Nodes
- Call
- Expr
- BoolOp (And, Or)
- NamedExpr (Walrus operator :=)
- BinOp
...

Statement Nodes
- FunctionDef
- AsyncFunctionDef
- ClassDef
- Return
- Delete
- For
- While
- If
...

Fields
- lineno: The line number where the node appears in the source code
- col_offset: The column offset (starting from 0) where the node begins
- end_lineno: The ending line number (Python 3.8+, not always present)
- end_col_offset: The ending column offset (Python 3.8+, not always present)
- FuncDef{
    'name': str,           # Function name
    'args': arguments,      # Arguments object
    'body': list[node],     # Function body
    'decorator_list': list, # Decorators
    'returns': expr,        # Return annotation
    'lineno': int,
    'col_offset': int
}
- ClassDef{
    'name': str,            # Class name
    'bases': list[expr],    # Base classes
    'keywords': list,       # Keyword args for bases
    'body': list[node],     # Class body
    'decorator_list': list, # Decorators
    'lineno': int,
    'col_offset': int
}
- Call{
    'func': expr,           # Function being called
    'args': list[expr],     # Positional arguments
    'keywords': list,       # Keyword arguments
    'lineno': int,
    'col_offset': int
}


### NodeVisitor
```py
class FunctionCounter(ast.NodeVisitor):
    def __init__(self):
        self.function_count = 0
        self.class_count = 0
    
    def visit_FunctionDef(self, node):

tree = ast.parse(code)
analyzer = FunctionCounter()
analyzer.visit(tree)
```
# Code Structure
## Building database
### Remote_tree_builder
repo_hash = build_and_store_code_tree(
            args.repo_url, args.entry_points, args.db_uri, args.verbose
        )
- git_manager.clone(repo_url)
- registry = scan_project(repo_path)
  - for every .py file, find the module name, then build an ast for the file, then use **FunctionScanner** to visit the tree, 
    - self.registry.add_function(
            self.module_name, 
            node.name, 
            self.file_path,
            lineno,
            end_lineno,
            self.current_class
        )
  - then for every function, build its segments


  util not registered



# Hosting
### Digital Ocean
- there's referal program but strict non bot check (can't open multiple account with one person's cards). so use other's referal link when you create account

## Linux Setup
### Basic setup
ssh
- cat ~/.ssh/id_rsa.pub

login
- ssh root@159.223.132.83
- ssh webadmin@159.223.132.83

system setup
- apt update && apt upgrade -y
- sudo apt install -y git curl wget htop unzip
- sudo apt-get install -y build-essential
- sudo apt-get install -y libpq-dev


new user
- adduser webadmin (asd)
- usermod -aG sudo webadmin
- mkdir -p /home/webadmin/.ssh
- chmod 700 /home/webadmin/.ssh
- cp ~/.ssh/authorized_keys /home/webadmin/.ssh/
- chown -R webadmin:webadmin /home/webadmin/.ssh
- chmod 600 /home/webadmin/.ssh/authorized_keys

firewall
- ufw allow OpenSSH
- ufw allow 80/tcp
- ufw allow 443/tcp
- ufw enable

change sshd (ssh daemon) config
- nano /etc/ssh/sshd_config
- systemctl restart ssh

nginx
- sudo apt install -y nginx

node
- https://nodejs.org/en/download

other downloads
- npm install -g pm2

### Basic system management/monitoring
- view memory: free -h 
- view memory live with UI: htop
- view top mem using process: ps aux --sort=-%mem | head -10

add swap mem
- sudo fallocate -l 2G /swapfile (swapfile is a name of your choice)
- sudo chmod 600 /swapfile
- sudo mkswap /swapfile
- sudo swapon /swapfile
- echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab


## App Framework
### Node app
test webapp
- sudo mkdir -p /var/www/myapp
- sudo chown webadmin:webadmin /var/www/myapp
- cd /var/www/myapp
- npm init -y
- npm install express

- pm2 start app.js --name "myapp"
- pm2 save
- pm2 startup

- sudo nano /etc/nginx/sites-available/myapp
```
server {
    listen 80;
    server_name _;  # or domain or ip

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
- sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
- sudo rm /etc/nginx/sites-enabled/default  # Remove the default config
- sudo nginx -t
- sudo systemctl restart nginx

end app
- pm2 stop myapp (pm2 delete myapp)
- sudo rm /etc/nginx/sites-enabled/myapp
- sudo systemctl restart nginx



encryption
- sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com (Saving debug log to /var/log/letsencrypt/letsencrypt.log Enter email address (used for urgent renewal and security notices)  (Enter 'c' to cancel): 2642503302@qq.com)

### Python app
- sudo apt-get install python3-venv
- python3 -m venv venv
- source venv/bin/activate

- pip install psycopg2
- sudo systemctl start postgresql
- sudo systemctl enable postgresql

## Postgres
### Basics
sudo -i -u postgres
psql -d code

### Creating database
CREATE USER codeuser WITH PASSWORD 'asdasd11';
CREATE DATABASE code OWNER codeuser;


### Priviliages
GRANT CONNECT ON DATABASE code TO codeuser;
GRANT USAGE, CREATE ON SCHEMA public TO codeuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO codeuser;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO codeuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO codeuser;
GRANT ALL PRIVILEGES ON SCHEMA public TO codeuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO codeuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO codeuser;

### Allowing connection
- sudo nano /etc/postgresql/*/main/postgresql.conf
- sudo nano /etc/postgresql/16/main/pg_hba.conf
- sudo systemctl restart postgresql

### Lifecycle
- sudo systemctl status postgresql@16-main

### Remote 
python new/app/remote_tree_builder.py --verbose \
  --db-host 159.223.132.83 \
  --db-user codeuser \
  --db-pass asdasd11 \
  --db-name code \
  --save-tree output.txt \
  https://github.com/xianrui-luo/D2RF.git \
  run_nerf.py:__main__

python new/app/remote_tree_builder.py --verbose --display-tree \
  --db-host 159.223.132.83 \
  --db-user codeuser \
  --db-pass asdasd11 \
  --db-name code \
  --save-tree output.txt \
  https://github.com/wwwwwwzh/demo-repo.git \
  main.py:__main__ \
  --update-if-exists


## Apache
- sudo apt install -y apache2 apache2-dev libapache2-mod-wsgi-py3

### Congifuration
```
sudo cp code_mapper.conf /etc/apache2/sites-available/
sudo a2ensite code_mapper.conf
sudo systemctl restart apache2
sudo tail -f /var/log/apache2/code_mapper_error.log
```

## Celery
- sudo apt install -y redis-server

### Configuration
sudo nano /etc/systemd/system/code-mapper-celery.service
```
[Unit]
Description=Celery Service for Code Mapper
After=network.target

[Service]
User=webadmin
Group=webadmin
WorkingDirectory=/var/www/code_mapper
Environment="PATH=/var/www/code_mapper/venv/bin"
ExecStart=/var/www/code_mapper/venv/bin/celery -A app.celery worker --loglevel=info

[Install]
WantedBy=multi-user.target
```
sudo systemctl start code-mapper-celery

## Privacy
- sudo apt-get update
- sudo apt-get install acl
- sudo setfacl -R -m u:webadmin:rwx,u:www-data:rwx /home/webadmin/projects/code
- sudo setfacl -R -d -m u:webadmin:rwx,u:www-data:rwx /home/webadmin/projects/code




# 
## Sample Questions
- how does rgb convert to sh
- what is the structure and vars of cam_transforms sh_utils->RGB2SH
- how is time incorporated to model 
    - render->viewpoint_camera.time->pc._deformation(...,time), FourDGSdataset uses
```py
Camera(colmap_id=index,R=R,T=T,FoVx=FovX,FoVy=FovY,image=image,gt_alpha_mask=None,
       image_name=f"{index}",uid=index,data_device=torch.device("cuda"),time=time,
       mask=mask) 
CameraInfo(uid=uid, R=R, T=T, FovY=FovY, FovX=FovX, image=image,
    image_path=image_path, image_name=image_name, width=width,height=height,
    time = float(idx/len(cam_extrinsics)), mask=None)
```




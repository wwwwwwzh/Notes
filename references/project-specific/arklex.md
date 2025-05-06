# Tasks
1: Read this general AI Agent tutorial from my Intro NLP class:
https://lnkd.in/ewwScx3J

2: Watch the more advanced research talk on AI Agents Beyond ChatGPT:
Video: https://lnkd.in/eM8QAtwK


3: Play with arklex open-source AI Agents framework that efficiently orchestrates AI Agents to complete various tasks, such as customer service, sales, and meeting scheduling:
Watch Video: https://lnkd.in/eJjRxcmN
Join the open-source: https://lnkd.in/eDavUGu3

4: Join the Discord group to follow a tutorial and homework design to build your agents:
https://lnkd.in/eKb-6amK

5: Email me your experience of the current framework and what research or engineering efforts could improve the agent's performance or make building agents easier after completing the homework introduced on discord.

# Summary
## Running

```
python run.py --input-dir ./examples/repo_agent3/

python model_api.py  --input-dir ./examples/repo_agent3_arklex
python eval.py  --model_api http://127.0.0.1:8000/eval/chat  --config ./examples/repo_agent3_config.json  --documents_dir ./examples/repo_agent3_arklex  --output-dir ./examples/repo_agent3_arklex
```


# Background On Automation
## History
### LLM+Tool
This approach is actually rooted in intelligence theory. We have a central thinking machine and allocate specific work to specific units of computation. Of course, the central unit can also perform those tasks, but due to the specificity generality tradeoff it might not perform fast or well. The contrary is also true. The specific units can also adopt this central unit-specific units architecture. 

Crewai uses its own [toolkit](https://docs.crewai.com/concepts/tools#available-crewai-tools) and from [langchain](https://python.langchain.com/docs/integrations/tools/)

### Task Graph
langGraph
- conditional DAG

### Swarm
crew.ai
- role-based design. eg, researcher, data collector, reporter.
- https://youtu.be/ONKOXwucLvE
- agent, task, crew, flow
    - agent
        - role: Defines the agent's function within the crew.
        - goal: Specifies the agent's objective.
        - tools: Lists the tools the agent can utilize.
        - allow_delegation: can the agent delegate tasks to other agents?
        - memory: Controls whether the agent maintains memory of interactions.
```py
ai_team = Crew(
    agents=[researcher, writer],
    tasks=[data_collection, content_creation],
    process='sequential',
    manager_llm='gpt-4',
    verbose=True
)
```
- short-term (RAG), long-term (SQLite3), and contextual memory with Human-in-the-Loop



openai swarm

Microsoft Autogen



### Computer Interaction 
some tasks might require the agent to give input to the computer or browser instead of just reading from them. 


### Specifics
- creating agent: function parameter to config file
- boilerplate: creates codes from cli call

## Other Agents
### Replit (Also see Reference.md->engineering->ai agent)
procedure


demo:
![](/images/replit-1.png)
![](/images/replit-2.png)


## Arklex Feature
- Mixed-Control:  balance user objectives with builder-defined goals
- Task Graph: ensures agents follow predefined workflows while minimizing unpredictable reasoning. If a task cannot be completed through such a graph, the framework will then call the dynamic AI agent planning flow on the fly. If the agent can complete the task under the requirement, then the system will autonomously incorporate this trajectory into the task graph
- Task Composition: allows AI agents to dynamically switch between different workflows based on semantic meaning. For example one complex task can be broken down to several smaller tasks (workers). 
- Arklex includes a human intervention function that automatically determines when to seek human input


# Architecture
## Creating Agent
```py
def generate_taskgraph(args):
    generator = Generator(args, args.config, model, args.output_dir)
    taskgraph_filepath = generator.generate()
    task_graph = json.load(open(os.path.join(os.path.dirname(__file__), taskgraph_filepath)))
    task_graph["nluapi"] = ""
    task_graph["slotfillapi"] = ""
    with open(taskgraph_filepath, "w") as f:
        json.dump(task_graph, f, indent=4)


def init_worker(args):
    ## TODO: Need to customized based on different use cases
    config = json.load(open(args.config))
    workers = config["workers"]
    worker_names = set([worker["name"] for worker in workers])
    if "FaissRAGWorker" in worker_names:
        logger.info("Initializing FaissRAGWorker...")
        build_rag(args.output_dir, config["rag_docs"])        

    elif any(node in worker_names for node in ("DataBaseWorker", "search_show", "book_show", "check_booking", "cancel_booking")):
        logger.info("Initializing DataBaseWorker...")
        build_database(args.output_dir)
```
### Generator
```py
def generate(self):
    self._load_docs()  # Loads crawled documents
    self._generate_tasks()  # Creates initial tasks
    best_practices = [self._generate_best_practice(task) for task]
    app = TaskEditorApp(tasks)  # Human refinement
    finetuned_best_practices = self._finetune_best_practice(steps)
    return self._format_task_graph(practices)  # Final JSON structure
```
Actual code
```py
def generate(self):

    # Step 0: Load the docs
    self._load_docs()
    
    # Step 1: Generate the tasks
    if not self.tasks:
        self._generate_tasks()
        logger.info(f"Generated tasks: {self.tasks}")
    else:
        self._format_tasks()
        logger.info(f"Formatted tasks: {self.tasks}")

    # Step 2: Generate the task planning
    best_practices = []
    for idx, task in progress_bar(enumerate(self.tasks), total=len(self.tasks)):
        logger.info(f"Generating best practice for task {idx}: {task}")
        best_practice = self._generate_best_practice(task)
        logger.info(f"Generated best practice for task {idx}: {best_practice}")
        best_practices.append(best_practice)

    # Step 3: iterate with user
    format_tasks = []
    for best_practice, task in zip(best_practices, self.tasks):
        try:
            task_name = task['task']
            steps = [bp["task"] for bp in best_practice]
        except Exception as e:
            logger.error(f"Error in format task {task}")
            logger.error(e)
            continue
        format_tasks.append({"task_name": task_name, "steps": steps})
    app = TaskEditorApp(format_tasks)
    hitl_result = app.run()
    task_planning_filepath = os.path.join(self.output_dir, f'taskplanning.json')
    json.dump(hitl_result, open(task_planning_filepath, "w"), indent=4)

    # Step 4: Pair task with worker
    finetuned_best_practices = []
    for idx_t, task in enumerate(hitl_result):
        steps = task["steps"]
        format_steps = []
        for idx_s, step in enumerate(steps):
            format_steps.append({
                "step": idx_s + 1,
                "task": step
            })
        finetuned_best_practice = self._finetune_best_practice(format_steps)
        logger.info(f"Finetuned best practice for task {idx_t}: {finetuned_best_practice}")
        finetuned_best_practices.append(finetuned_best_practice)

    # Step 5: Format the task graph
    task_graph = self._format_task_graph(finetuned_best_practices)

    # Step 6: Save the task graph
    taskgraph_filepath = os.path.join(self.output_dir, f'taskgraph.json')
    with open(taskgraph_filepath, "w") as f:
        json.dump(task_graph, f, indent=4)

    return taskgraph_filepath
```
![](/images/ark-1.png)
The user selection menu at step  3
```c++
[03/24/2025 21:46:51] {generator.py:_generate_tasks} INFO - Generated tasks: [
    {'intent': 'User wants product information', 'task': 'Provide detailed information about Richtech Robotics products and their features'}, 
    {'intent': 'User has an inquiry about purchasing options', 'task': 'Assist with inquiries related to purchasing, including rental options and pricing'}, 
    {'intent': 'User seeks support for product installation or operation', 'task': 'Provide support for product installation, operation, and troubleshooting'}, 
    {'intent': 'User wants to know about delivery times and logistics', 'task': 'Inform about delivery times and logistics for different robots'}, 
    {'intent': 'User is interested in robot integration into business operations', 'task': 'Advise on the integration of robots into existing business operations'}, 
    {'intent': "User requests information about ClouTea and ADAM's capabilities", 'task': "Provide information about ClouTea and ADAM's beverage-making capabilities"}, 
    {'intent': 'User asks about maintenance and service plans', 'task': 'Offer information on maintenance and service plans available for robots'}, 
    {'intent': 'User requires assistance with a transaction or policy inquiry', 'task': 'Assist with transaction-related inquiries and provide policy information'}]
[03/24/2025 21:46:54] {generator.py:_generate_best_practice} INFO - Best practice detection: Reasoning: The task is to provide detailed information about Richtech Robotics products and their features. This task can involve multiple aspects, such as accessing internal documentation to gather comprehensive information about various products and their features, and possibly answering follow-up questions that the user might have. The FaissRAGWorker can be utilized to retrieve information from the companys internal documentation, which is essential for this task. However, since the task specifies providing detailed information, it might also involve real-time updates or comparisons that could be addressed by the SearchWorker. Additionally, the MessageWorker would be necessary to communicate with the user, delivering the information in an understandable way, and possibly asking clarifying questions if needed.Given the complexity of the task, which might require gathering and synthesizing information from multiple sources and effectively communicating it, this task is not a singular action and cannot be handled by a single resource alone. It requires coordination between multiple resources (FaissRAGWorker for documentation, possibly SearchWorker for real-time data, and MessageWorker for user interaction), indicating that the task should be decomposed into smaller sub-tasks that can be managed more efficiently.

[03/24/2025 21:48:02] {generator.py:429} INFO - Generated best practice for task 7: [{'step': 1, 'task': "Use the MessageWorker to acknowledge the user's inquiry and ask for clarification if necessary, to determine if the inquiry is transaction-related or policy-related."}, 
{'step': 2, 'task': 'If the inquiry is transaction-related, use the DefaultWorker to guide the user through the transaction process, addressing any specific issues they might be encountering.'}, 
{'step': 3, 'task': "If the inquiry is policy-related, use the FaissRAGWorker to retrieve relevant policy information from the company's internal documentation, such as FAQs or policy documents."}, 
{'step': 4, 'task': 'Deliver the retrieved information or assistance to the user via the MessageWorker, ensuring clarity and completeness of the response.'}, 
{'step': 5, 'task': 'Ask if the user needs further assistance or information, to ensure their inquiry is fully resolved.'}]
[03/24/2025 21:50:29] {generator.py:459} INFO - Finetuned best practice for task 7: [{'step': 1, 'task': "Use the MessageWorker to acknowledge the user's inquiry and ask for clarification if necessary, to determine if the inquiry is transaction-related or policy-related.", 'resource': 'MessageWorker', 'example_response': 'Thank you for reaching out. Could you please provide more details about your inquiry? Is it related to a transaction or a policy?', 'resource_id': '26bb6634-3bee-417d-ad75-23269ac17bc3'},
{'step': 2, 'task': 'If the inquiry is transaction-related, use the DefaultWorker to guide the user through the transaction process, addressing any specific issues they might be encountering.', 'resource': 'DefaultWorker', 'example_response': "Let's go through the transaction process together. Please let me know what specific issue you are encountering.", 'resource_id': 'default_worker'}, 
{'step': 3, 'task': "If the inquiry is policy-related, use the FaissRAGWorker to retrieve relevant policy information from the company's internal documentation, such as FAQs or policy documents.", 'resource': 'FaissRAGWorker', 'example_response': '', 'resource_id': '9aa47724-0b77-4752-9528-cf4b06a46915'}, 
{'step': 4, 'task': 'Deliver the retrieved information or assistance to the user via the MessageWorker, ensuring clarity and completeness of the response.', 'resource': 'MessageWorker', 'example_response': 'Here is the information you requested regarding our policy: [insert policy details]. Please let me know if this answers your question.', 'resource_id': '26bb6634-3bee-417d-ad75-23269ac17bc3'}, 
{'step': 5, 'task': 'Ask if the user needs further assistance or information, to ensure their inquiry is fully resolved.', 'resource': 'MessageWorker', 'example_response': 'Is there anything else I can assist you with today?', 'resource_id': '26bb6634-3bee-417d-ad75-23269ac17bc3'}]
[03/24/2025 21:50:30] {create.py:45} INFO - Initializing FaissRAGWorker...
[03/24/2025 21:50:30] {build_rag.py:20} WARNING - Loading existing documents from ./examples/customer_service/documents.pkl! If you want to recrawl, please delete the file or specify a new --output-dir when initiate Generator.
[03/24/2025 21:50:30] {build_rag.py:30} INFO - CRAWLED URLS: ['https://www.richtechrobotics.com', 'https://www.richtechrobotics.com/about', 'https://www.richtechrobotics.com/blog', 'https://www.richtechrobotics.com/blog/adam-at-gtc', 'https://www.richtechrobotics.com/blog/adams-stellar-showcase-at-the-specialty-coffee-expo', 'https://www.richtechrobotics.com/blog/fime-2024', 'https://www.richtechrobotics.com/blog/mac-usa-partnership', 'https://www.richtechrobotics.com/blog/richtech-robotics-at-ces-2023', 'https://www.richtechrobotics.com/blog/robot-beer', 'https://www.richtechrobotics.com/blog/roth-conference', 'https://www.richtechrobotics.com/blog/smart-hotel-technology-trends', 'https://www.richtechrobotics.com/blog/zipphaus-joint-venture', 'https://www.richtechrobotics.com/medbot', 'https://www.richtechrobotics.com/media', 'https://www.richtechrobotics.com/media?6495208d_page=2', 'https://www.richtechrobotics.com/privacy-policy', 'https://www.richtechrobotics.com/richie', 'https://www.richtechrobotics.com/skylark', 'https://www.richtechrobotics.com/titan', 'https://www.richtechrobotics.com/titan-auto']
[03/24/2025 21:50:30] {loader.py:225} INFO - Skip url: https://www.richtechrobotics.com/blog/mac-usa-partnership because of error or no content

```
## Running Agent
```py
# run.py
config = json.load(open(os.path.join(args.input_dir, "taskgraph.json")))
env = Env(
    tools = config.get("tools", []),
    workers = config.get("workers", []),
    slotsfillapi = config["slotfillapi"]
)
history = [{"role": "assistant", "content": "first node's start_message"}]
params = {}
while True:
    output, params, hitl = get_api_bot_response(args, history, user_text=input("You: "), params, env)
    history.append({"role": user_prefix, "content": user_text})
    history.append({"role": worker_prefix, "content": output})

def get_api_bot_response(args, history, user_text, parameters, env):
    data = {"text": user_text, 'chat_history': history, 'parameters': parameters}
    orchestrator = AgentOrg(config=os.path.join(args.input_dir, "taskgraph.json"), env=env)
    result = orchestrator.get_response(data)
    return result['answer'], result['parameters'], result['human-in-the-loop']

    
```

```py
get_response(self, inputs: dict)
    text = inputs["text"]
    chat_history = inputs["chat_history"]
    params = inputs["parameters"]

    taskgraph_chain = RunnableLambda(self.task_graph.get_node) | RunnableLambda(self.task_graph.postprocess_node)
    node_info, params = taskgraph_chain.invoke(taskgraph_inputs)

    message_state = MessageState(
        sys_instruct=sys_instruct, 
        bot_config=bot_config,
        user_message=user_message, 
        orchestrator_message=orchestrator_message, 
        trajectory=params["history"], 
        message_flow=params.get("worker_response", {}).get("message_flow", ""), 
        slots=params.get("dialog_states"),
        metadata=params.get("metadata"),
        is_stream=True if stream_type is not None else False,
        message_queue=message_queue
    )
    response_state, params = self.env.step(node_info["id"], message_state, params)

    # ReAct
    while:
        if response_state["trajectory"] last role is "assistant" and last content exists: 
            response_state["response"] = response_state["trajectory"][-1]["content"]
            break

        node_info, params = taskgraph_chain.invoke(taskgraph_inputs)
        message_state["orchestrator_message"] = OrchestratorMessage(message=node_info["attribute"]["value"], attribute=node_info["attribute"])

        if node not in tool nor in worker:
            action, response_state, msg_history = self.env.planner.execute(message_state, params["history"])
        else:
            message_state["response"] = "" # clear the response cache generated from the previous steps in the same turn
            response_state, params = self.env.step(self.env.name2id[action], message_state, params)
            tool_response = params.get("metadata", {}).get("tool_response", {})

    output = {
            "answer": response_state.get("response", ""),
            "parameters": params,
            "human-in-the-loop": params['metadata'].get('hitl', None),
        }
    return output

Env.step(self, id, message_state, params):
    if tool
        tool: Tool = self.tools[id]["execute"]()
        tool.init_slotfilling(self.slotfillapi)
        response_state = tool.execute(message_state, **self.tools[id]["fixed_args"])
        

    if worker:
        worker: BaseWorker = self.workers[id]["execute"]()
        if hasattr(worker, "init_slotfilling"):
            worker.init_slotfilling(self.slotfillapi)
        response_state = worker.execute(message_state)
    
    params["history"] 
    params["dialog_states"]
    params["node_status"][current_node]

    return response_state, params

Tool._execute(state: MessageState, **fixed_args)
    self._init_slots(state)
    chat_history_str = format_chat_history(state["trajectory"])
    slots : list[Slot] = self.slotfillapi.execute(self.slots, chat_history_str, state["metadata"])
    # slotfillapi.execute uses LLM to fill in the slots
    if slot.value is not empty for all slots, and all the slots has been verified:
        kwargs = {slot.name: slot.value for slot in slots}
        combined_kwargs = {**kwargs, **fixed_args}
        response = self.func(**combined_kwargs)
        state["trajectory"].append({
            'content': None, 
            'role': 'assistant', 
            'tool_calls': [
                {
                    'function': {
                        'arguments': json.dumps(kwargs), 
                        'name': self.name
                    }, 
                    'id': call_id, 
                    'type': 'function'
                }
            ], 
            'function_call': None
        })
        state["trajectory"].append({
            "role": "tool",
            "tool_call_id": call_id,
            "name": self.name,
            "content": response
        })
    return state
```

### Env
```py
def __init__(self, tools, workers, slotsfillapi, resource_inizializer: Optional[BaseResourceInitializer] = None):
    if resource_inizializer is None:
        resource_inizializer = DefaulResourceInitializer()
    self.tools = resource_inizializer.init_tools(tools)
    self.workers = resource_inizializer.init_workers(workers)
    self.slotfillapi = self.initialize_slotfillapi(slotsfillapi)
```

### Orchestrator
```py
class AgentOrg:
    def __init__(self, config, env: Env, **kwargs):
        if isinstance(config, dict):
            self.product_kwargs = config
        else:
            self.product_kwargs = json.load(open(config))
        self.user_prefix = "user"
        self.worker_prefix = "assistant"
        self.environment_prefix = "tool"
        self.task_graph = TaskGraph("taskgraph", self.product_kwargs)
        self.env = env

    def generate_next_step(
        self, messages: List[Dict[str, Any]], text:str
    ) -> Tuple[Dict[str, Any], str, float]:
        if MODEL['llm_provider'] != 'openai':
            messages[0]['role'] = 'user'
       
        res = llm.invoke(messages)        
        message = aimessage_to_dict(res)
        action_str = message['content'].split("Action:")[-1].strip()
        try:
            action_parsed = json.loads(action_str)
        except json.JSONDecodeError:
            # this is a hack
            logger.warning(f"Failed to parse action: {action_str}, choose respond action")
            action_parsed = {
                "name": RESPOND_ACTION_NAME,
                "arguments": {RESPOND_ACTION_FIELD_NAME: action_str},
            }
        if action_parsed.get("name"):
            action = action_parsed["name"]
        else:
            logger.warning(f"Failed to parse action: {action_str}, choose respond action")
            action = RESPOND_ACTION_NAME
        # issues with getting response_cost using langchain, set to 0.0 for now
        return message, action, 0.0


    def get_response(self, inputs: dict, stream_type: StreamType = None, message_queue: janus.SyncQueue = None) -> Dict[str, Any]:
        
```



### Inter Task Communication
in the customer service example, a FaissRAGWorker is always used to first retrieve relavant information from the files generated at agent creation `docs = FaissRetrieverExecutor.load_docs(database_path=os.environ.get("./examples/customer_service"))`

in the booking system, the DataBaseWorker is responsible for interactively adding and retrieving information to a local sqlite database initialized duriing agent creation.

msg_state: MessageState
- 

## Evaluation
```
python model_api.py  --input-dir ./examples/repo_agent3_arklex/

python eval.py \
 --model_api http://127.0.0.1:8000/eval/chat \
 --config ./examples/repo_agent3_config.json \
 --documents_dir ./examples/repo_agent3_arklex \
 --output-dir ./examples/repo_agent3_arklex
```






## Sample Tasks
Note that most tasks require using a predefined procedure, but this procudure is defined after exploration. We need to see if we want to start with the exploration or directly witht the procedure

### Common tasks
- custom news feed
- stock tracker
- customer service bot (like those floating window chatbox in some websites)
- calender

### My Examples
interactive historical map
- need a good source, possibly many, each for each region and period
- the agent need to think up of a program architecture and refine it and start iterating the program by building small and evaluate it, possibly with human feedback. 


paper map/interactive book maker
- a website book that introduce a line of work starting from prerequisite, using a history approach and mostly chronological order.
- ai can generate new content on the fly for each user since everyone knows something different.

code map
- read in a repo and starting from readme and the functions it describes to all calls they used and build a tree like interactive map of how the flow runs, especially need to specify important variables' dimensions

job finder
- simulate my dad's job finding strategy




need to understand the workers



# Opinions
### Browser
gradio


### Presenting Data/Information
Current AI agents are good at getting and processing data. They can find data and create arbitary representations of them. But we don't currently have a efficient data delivery/presentation method. Most agents, like Chatbots, can only present text. This is expected since natural language communication is also the most used among huamns. But various modern visual presentation techniques are arguably better suited for many tasks. For example, a user might want to see various charts of sales data, or a workflow graph of a program or a project.

We already have a powerful and versatile visual delivery method, which happens to be easily customizable: the browser. Modern web frameworks have made it easy to create arbitary representations of data from formal languages (codes), which LLMs are good at. Therefore, a web page/app should be the default place for presenting data.

Thus I propose a general platform, or a default component of the exisiting agent creation workflow. Like the default RAG system for data retrieval and the message worker for textual data delivery, there should be a web app component and various default workers to build webpages on the fly. An added benefit is that Arklex can become a hosting service. 


### Self aware agent builder
the agent should know how it's built, it should have it's own source code so unexpected behaviors can be handled directly by itself.

```
You: what's the intent, i want to analyze the repo
getAPIBotResponse Time: 3.7887990474700928
("Bot: It seems like you're trying to analyze a GitHub repository, but I'm "
 'unable to directly access external URLs or analyze specific repositories. '
 'However, I can guide you on how to analyze the repository on your own. If '
 'you have specific questions about the repository or need help with a '
 'particular part of it, feel free to share more details or code snippets, and '
 "I'll do my best to assist you!")
You: you have a code worker that can download and parse the code
getAPIBotResponse Time: 3.5383245944976807
("Bot: I'm sorry for any confusion, but I don't have the capability to "
 'directly download or parse code from external URLs or repositories. However, '
 'I can certainly help guide you through the process of analyzing a repository '
 'on your own. If you have specific questions or need help with a particular '
 'part of the repository, feel free to share more details or code snippets '
 "here, and I'll do my best to assist you!")
```




### Bugs
- .rstrip(".py") to .removesuffix(".py") otherwise tools/workers ending in y will not be registered
- `message_state["response"] = ""` in orchestrator makes the message worker not able to retain any information from previous workers. in `response_state, params = self.env.step(node_info["id"], message_state, params)`, params is not modifiable by workers. response_state is returned from worker.execute. params will be outputed by the big function and get into next loop where 

# repo reader
- current implementation takes whole files in RAG, retriever gets top 2. Needs  to truncate.



## Sample
```
("Bot: Hello! I'm your GitHub Repository Analyzer. I can download GitHub "
 'repositories, index their content, and help you search through them. What '
 'would you like to do today?')
Main loop


You: what repos i currently have
getAPIBotResponse Time: 5.987802982330322
('Bot: Here are the repositories you currently have indexed:\n'
 '\n'
 '1. **Repository**: [D2RF-mini](https://github.com/wwwwwwzh/D2RF-mini)  \n'
 '   **Indexed**: April 19, 2025  \n'
 '   **Files**: 139\n'
 '\n'
 '2. **Repository**: '
 '[demo-repo-mini](https://github.com/wwwwwwzh/demo-repo-mini)  \n'
 '   **Indexed**: April 14, 2025  \n'
 '   **Files**: 1\n'
 '\n'
 '3. **Repository**: [demo-repo](https://github.com/wwwwwwzh/demo-repo)  \n'
 '   **Indexed**: April 14, 2025  \n'
 '   **Files**: 10\n'
 '\n'
 "Is there anything else you'd like to know about GitHub repositories? I can "
 'download new repositories, search existing ones, or manage your repository '
 'database.')
Main loop


You: what's the D2RF-mini repo about
getAPIBotResponse Time: 15.435706615447998
('Bot: The D2RF-mini repository appears to be related to neural rendering or '
 'neural radiance fields (NeRF), which is a method in computer graphics and '
 'machine learning for synthesizing novel views of complex 3D scenes. The code '
 'provided includes portions of two classes, `NeRF` and `Rigid_NeRF`, which '
 'are part of this approach.\n'
 '\n'
 '### Understanding the Code\n'
 '\n'
 '1. **Class Definitions:**\n'
 '\n'
 '   The code provides two `__init__` methods for different classes: `NeRF` '
 'and `Rigid_NeRF`. These are likely neural network models used to process 3D '
 'scene data and generate new views.\n'
 '\n'
 '2. **Parameters:**\n'
 '\n'
 '   Both classes have the following parameters:\n'
 '   \n'
 '   - `D`: Depth of the network, indicating the number of layers.\n'
 '   - `W`: Width of each layer, specifying the number of neurons per layer.\n'
 '   - `input_ch`: Number of input channels for points, typically representing '
 '3D coordinates.\n'
 '   - `input_ch_views`: Number of input channels for view directions, often '
 'used for encoding camera angles.\n'
 '   - `output_ch`: Number of output channels, usually representing RGB colors '
 'and possibly alpha (opacity).\n'
 '   - `skips`: Layers where skip connections are applied, which facilitate '
 'gradient flow and improve learning.\n'
 '   - `use_viewdirs`: Boolean indicating whether view direction data is used, '
 'allowing for view-dependent effects.\n'
 '\n'
 '3. **Network Architecture:**\n'
 '\n'
 '   - **Points Linear Layers (`pts_linears`):** These layers process the '
 'input 3D points. The architecture includes a series of linear layers, with '
 'optional skip connections that concatenate input features to intermediate '
 'layers, enhancing model capacity.\n'
 '   \n'
 '   - **Views Linear Layers (`views_linears`):** These layers process the '
 'input view directions, combined with features from the point processing '
 'layers.\n'
 '\n'
 '   - **Conditional Layers:**\n'
 '     - If `use_viewdirs` is `True`, additional layers are defined for '
 'processing features (`feature_linear`), predicting alpha values '
 '(`alpha_linear`), and predicting RGB values (`rgb_linear`).\n'
 '     - If `use_viewdirs` is `False`, a single output layer (`output_linear`) '
 'is used.\n'
 '\n'
 '4. **Additional Components:**\n'
 '\n'
 '   - `sf_linear` and `prob_linear` in the `NeRF` class: These layers suggest '
 'the network might also predict additional properties such as scene flow '
 '(changes in the scene) and probabilities, respectively.\n'
 '   \n'
 '   - `w_linear` in the `Rigid_NeRF` class: This layer might be used for '
 'predicting weights or confidence values related to the neural rendering '
 'process.\n'
 '\n'
 '5. **Purpose and Functionality:**\n'
 '\n'
 '   The purpose of these classes is to define neural network architectures '
 'for synthesizing images from 3D scenes. The `NeRF` class includes components '
 'for potentially handling dynamic scenes or additional tasks (like scene '
 'flow), while the `Rigid_NeRF` class seems to focus on simpler or more '
 'constrained scenarios, potentially assuming rigidity (no deformation).\n'
 '\n'
 '6. **Optimization Placeholder:**\n'
 '\n'
 '   The method `optimize_parameters()` is a placeholder, indicating that the '
 'actual optimization logic (e.g., backpropagation, gradient descent) is '
 'defined elsewhere in the repository.\n'
 '\n'
 '### Conclusion\n'
 '\n'
 "The D2RF-mini repository's code suggests a focus on neural rendering, "
 'potentially involving both static and dynamic scenes. The classes define '
 'neural network architectures capable of processing 3D point data and view '
 'directions to generate novel views, with considerations for scene dynamics '
 'in the `NeRF` class. The repository likely builds on the core principles of '
 'NeRF, enhancing them for specific applications or research goals.')
Main loop


You: give a workflow of the demo-repo
getAPIBotResponse Time: 10.900551080703735
('Bot: Based on the provided code from the `demo-repo`, the workflow of the '
 'application can be broken down into several key steps. The code seems to '
 'implement a straightforward data processing pipeline, with defined stages '
 "from setup to report generation. Here's a detailed breakdown of the "
 'workflow:\n'
 '\n'
 '### Main Workflow\n'
 '\n'
 'The entry point of the application is the `main()` function. The workflow '
 'within this function is structured as follows:\n'
 '\n'
 '1. **Starting the Application**:\n'
 '   ```python\n'
 '   print("Starting demo application...")\n'
 '   ```\n'
 "   This marks the beginning of the application's execution.\n"
 '\n'
 '2. **Setup Environment**:\n'
 '   ```python\n'
 '   config = setup_environment()\n'
 '   ```\n'
 '   The application sets up the environment by calling the '
 '`setup_environment()` function, which returns a configuration dictionary. '
 'This dictionary includes parameters like `temp_dir`, `log_level`, and '
 '`max_threads`.\n'
 '\n'
 '3. **Input and Output Paths**:\n'
 '   ```python\n'
 '   input_path = "data/input.json"\n'
 '   output_path = f"{config[\'temp_dir\']}/output.json"\n'
 '   ```\n'
 '   The application defines paths for input and output data. The output path '
 'uses a temporary directory specified in the configuration.\n'
 '\n'
 '4. **Input Validation**:\n'
 '   ```python\n'
 '   if validate_input(input_path):\n'
 '   ```\n'
 '   The application validates the input data using the `validate_input()` '
 'function. If the input is not valid, the application exits with an error '
 'message.\n'
 '\n'
 '5. **Data Loading**:\n'
 '   ```python\n'
 '   data = load_data(input_path)\n'
 '   ```\n'
 '   If the input is valid, the data is loaded from the specified input path '
 'using the `load_data()` function.\n'
 '\n'
 '6. **Data Transformation**:\n'
 '   ```python\n'
 '   transformed_data = transform_data(data)\n'
 '   ```\n'
 '   The loaded data is transformed using the `transform_data()` function, '
 'preparing it for further processing.\n'
 '\n'
 '7. **Batch Processing**:\n'
 '   ```python\n'
 '   processed_data = process_batch(transformed_data, config["max_threads"])\n'
 '   ```\n'
 '   The transformed data is processed in batches using multiple threads, as '
 'specified in the configuration (`max_threads`).\n'
 '\n'
 '8. **Saving Results**:\n'
 '   ```python\n'
 '   if save_results(processed_data, output_path):\n'
 '       print("Results saved successfully!")\n'
 '   ```\n'
 '   The processed data is saved to the output path. If successful, a '
 'confirmation message is printed.\n'
 '\n'
 '9. **Displaying Summary**:\n'
 '   ```python\n'
 '   display_summary(processed_data)\n'
 '   ```\n'
 '   A summary of the processed data is displayed using the '
 '`display_summary()` function.\n'
 '\n'
 '10. **Report Generation**:\n'
 '    ```python\n'
 '    report = generate_report(processed_data)\n'
 '    print(f"Report generated: {report}")\n'
 '    ```\n'
 '    Finally, a report is generated based on the processed data using the '
 '`generate_report()` function, and it is printed to the console.\n'
 '\n'
 '11. **Completion Message**:\n'
 '    ```python\n'
 '    print("Demo application completed.")\n'
 '    ```\n'
 '    The application prints a completion message indicating the end of the '
 'workflow.\n'
 '\n'
 '### Supporting Functions\n'
 '\n'
 '- **`setup_environment()`**: Configures the environment settings for the '
 'application. Returns a dictionary with configuration details.\n'
 '  \n'
 '- **`display_summary(data)`**: Displays a summary of the processed data, '
 'including status, number of items processed, and timestamp. The function '
 'also formats the data for display.\n'
 '\n'
 '- **`generate_report(data)`**: Generates a report based on the processed '
 'data, including details like data status and items processed. The report '
 'includes a timestamp of when it was generated.\n'
 '\n'
 'Each of these functions plays a specific role in the data processing '
 'pipeline, ensuring that the input data is validated, transformed, processed, '
 'and reported efficiently.\n'
 '\n'
 'This workflow provides a clear structure for handling data from start to '
 'finish, making it a useful template for similar data processing '
 'applications.')
Main loop


You: i want to analyze https://github.com/arklexai/Agent-First-Organization
getAPIBotResponse Time: 16.405592918395996
("Bot: I've successfully downloaded and indexed the GitHub repository: "
 'https://github.com/arklexai/Agent-First-Organization\n'
 '\n'
 'Repository Hash: c9c1296f794eb18d09c2508b271142aa\n'
 'Files Indexed: 483\n'
 '\n'
 'The repository is now available for querying. You can ask questions about it '
 'by specifying the repository hash or URL.')
Main loop


You: how does https://github.com/arklexai/Agent-First-Organization create taskgraph
getAPIBotResponse Time: 14.691633224487305
('Bot: The `Agent-First-Organization` repository creates a task graph using a '
 'combination of configuration files, models, and resource initializers. '
 "Here's a breakdown of the relevant parts of the code that demonstrate how "
 'the task graph is created:\n'
 '\n'
 '1. **Function Definition**: \n'
 '   The main function responsible for creating the task graph is '
 '`generate_taskgraph`. There are two versions of this function, but they '
 'essentially perform similar tasks with slightly different implementations.\n'
 '\n'
 '2. **Model Initialization**:\n'
 '   ```python\n'
 "   model = PROVIDER_MAP.get(MODEL['llm_provider'], "
 'ChatOpenAI)(model=MODEL["model_type_or_path"], timeout=30000)\n'
 '   ```\n'
 '   Here, a language model is initialized using a provider map to get the '
 "appropriate model based on a configuration (`MODEL['llm_provider']`). If no "
 'provider is found, it defaults to `ChatOpenAI`.\n'
 '\n'
 '3. **Generator Creation**:\n'
 '   ```python\n'
 '   generator = Generator(args, config_file, model, output_dir, '
 'resource_initializer)\n'
 '   ```\n'
 '   A `Generator` object is created, which appears to be responsible for the '
 'task graph generation. It takes several parameters including arguments, a '
 'configuration file, a model, an output directory, and a resource '
 'initializer.\n'
 '\n'
 '4. **Task Graph Generation**:\n'
 '   ```python\n'
 '   taskgraph_filepath = generator.generate()\n'
 '   ```\n'
 '   The `generate` method of the `Generator` object is called, which '
 'generates the task graph and returns the file path where the task graph is '
 'stored.\n'
 '\n'
 '5. **Task Graph Modification**:\n'
 '   ```python\n'
 '   task_graph = json.load(open(os.path.join(os.path.dirname(__file__), '
 'taskgraph_filepath)))\n'
 '   task_graph["nluapi"] = ""\n'
 '   task_graph["slotfillapi"] = ""\n'
 '   with open(taskgraph_filepath, "w") as f:\n'
 '       json.dump(task_graph, f, indent=4)\n'
 '   ```\n'
 '   After generating the task graph, the script opens the file and updates it '
 'by adding or modifying the API URLs (`nluapi` and `slotfillapi`). It then '
 'saves the modified task graph back to the file.\n'
 '\n'
 '6. **Formatting the Task Graph**:\n'
 '   The `_format_task_graph` method is used to format the task graph, which '
 'includes creating nodes and edges based on tasks and best practices. This '
 'method constructs a detailed graph representation with nodes and edges.\n'
 '\n'
 '   - **Nodes and Edges**: \n'
 '     Each node in the graph represents a task or step in a task, and edges '
 'connect these nodes to represent the flow or dependency between tasks.\n'
 '   \n'
 '   - **Start Node**:\n'
 '     A special start node is added to the graph, which is initialized with a '
 'message generated using a prompt template and a model.\n'
 '\n'
 '7. **Initialization**:\n'
 '   The constructor `__init__` for the class that likely contains these '
 'methods initializes the task graph environment using a resource initializer '
 '(`TauBenchResourceInitializer`) and sets up the environment with tools, '
 'workers, and other necessary components.\n'
 '\n'
 'In summary, the task graph is created by initializing necessary components '
 'such as a model and a resource initializer, generating the graph using a '
 '`Generator` object, and then modifying and formatting the graph to include '
 'necessary attributes and API endpoints. The graph is structured with nodes '
 'and edges to represent tasks and their dependencies, and a start node is '
 'included to initiate the task sequence.')
Main loop


You: How does it run an agent
getAPIBotResponse Time: 15.724620819091797
("Bot: The repository you've referenced appears to manage the execution of an "
 'agent through a combination of functions and an orchestrator class called '
 "`AgentOrg`. Let's break down the relevant parts of the code to understand "
 'how this execution and management works.\n'
 '\n'
 '### Key Functions\n'
 '\n'
 '1. **`get_api_bot_response` Function**\n'
 '\n'
 '   ```python\n'
 '   def get_api_bot_response(args, history, user_text, parameters, env):\n'
 '       data = {"text": user_text, \'chat_history\': history, \'parameters\': '
 'parameters}\n'
 '       orchestrator = AgentOrg(config=os.path.join(args.input_dir, '
 '"taskgraph.json"), env=env)\n'
 '       result = orchestrator.get_response(data)\n'
 '\n'
 "       return result['answer'], result['parameters'], "
 "result['human_in_the_loop']\n"
 '   ```\n'
 '\n'
 '   This function is a central piece in managing the execution of an agent. '
 "Here's a breakdown of its components:\n"
 '\n'
 '   - **Inputs**: The function takes in several parameters, including `args`, '
 '`history`, `user_text`, `parameters`, and `env`.\n'
 '   - **Data Preparation**: It creates a dictionary `data` that contains '
 "`text` (the user's input), `chat_history` (the conversation history), and "
 '`parameters` (additional parameters for the agent).\n'
 '   - **Orchestrator Initialization**: An instance of `AgentOrg` is created '
 'with a configuration file (`taskgraph.json`) and an environment variable '
 '(`env`).\n'
 '   - **Response Handling**: The `orchestrator.get_response(data)` method is '
 "called to get the agent's response. This function returns the response's "
 '`answer`, updated `parameters`, and a flag `human_in_the_loop`.\n'
 '\n'
 '2. **`interact` Function**\n'
 '\n'
 '   ```python\n'
 '   def interact(intent_path, summary, model_api, model_params, client):\n'
 '       history = []\n'
 "       instructional_prompt = 'Replicate the behavior of a human customer. "
 'You are interacting with customer service chatbot for the following company: '
 "' + summary\n"
 '       start_text = "Begin the conversation as a human customer with the '
 'following intent: " + intent_path[0]\n'
 "       history.append({'role': 'system','content': instructional_prompt})\n"
 "       history.append({'role': 'user', 'content': start_text})\n"
 '       for i in range(len(intent_path)):\n'
 '           intent = intent_path[i]\n'
 '           output = chatgpt_chatbot(history, client) \n'
 "           history.append({'role': 'assistant', 'content': output, 'intent': "
 'intent})\n'
 '           response_data = query_chatbot(model_api, filter_convo(history), '
 'model_params)\n'
 '           answer = response_data["answer"]\n'
 "           answer = answer.replace('\\n', ' ')\n"
 '           model_params = response_data.get("parameters", model_params)\n'
 '           if i < len(intent_path) - 1:\n'
 '               intent = intent_path[i+1]\n'
 "           history.append({'role': 'user', 'content': answer + '\\nRespond "
 "to this utterance with the following intent: ' + intent + '\\nMake sure your "
 'response is natural and follows the flow of the conversation. For example, '
 "if the bot asks you a question make sure you answer it.'})\n"
 '       return history\n'
 '   ```\n'
 '\n'
 '   This function simulates interaction with an agent as a human user in a '
 'customer service scenario. Key points include:\n'
 '\n'
 '   - **Conversation Initialization**: It starts by setting up an initial '
 'conversation prompt and adding it to the `history`.\n'
 '   - **Iterative Interaction**: For each intent in `intent_path`, it '
 'simulates interaction with a chatbot (`chatgpt_chatbot`) and queries another '
 'model (`query_chatbot`) for a response.\n'
 '   - **Response Management**: The response is processed, and the '
 'conversation history is updated with the intent and the response.\n'
 '   \n'
 '### Execution Management\n'
 '\n'
 'The execution of the agent is primarily managed through the `AgentOrg` '
 'class, specifically through the `get_response` method. This method is '
 "responsible for processing the input data and returning the agent's "
 "response. The configuration for the agent's behavior and tasks is specified "
 'in a configuration file (`taskgraph.json`), which is loaded during the '
 'initialization of the `AgentOrg` instance.\n'
 '\n'
 '### Conclusion\n'
 '\n'
 'The repository uses a combination of functions and an orchestrator class to '
 'manage the execution of an agent. The `get_api_bot_response` function is key '
 "to orchestrating the agent's response based on user input and conversation "
 'history, while the `interact` function simulates a customer service '
 'interaction with the agent. The `AgentOrg` class, with its '
 "configuration-driven approach, is central to the agent's execution and "
 'behavior management.')
```

Tool: An abstract syntax tree based parser to build function based rag
Workers:
- github_repo_worker: downloading GitHub repositories and creating FAISS indexes for them
- repo_database_worker: managing the repository database
- repo_query_worker: querying indexed GitHub repositories using FAISS



Improvements:
1. The message system is too complicated and thus hard to debug. I'm not familiar with the literature on this but intuitively, a centralized data bus with various access rights (eg. between tools or taskgraph nodes) would be manageable. 
2. I'm not sure if it's a good idea to make workers hardcoded. If workers are to be agents, the framework should help choose tools for them and build the action garph for them based on the agents' descriptions. This makes tools the atomic parts of the framework and the only hardcoded components. In addition, the workers currently have only one action graph (those actions can be conditional). Might consider lettng each worker have a set of graphs or routines which can be seen as sub-tasks.
3. The taskgraph is interesting but automating the process of making good taskgraphs should be better investigated. 

Suggestions:
1. I've been thinking about a self-understanding agent creation framework which also produces self-understanding agents. The codebase itself should be fed into the framework when creating agents so agent makers can better debug. The agent produced should know how it was produced so to give useful insights when it sucks on a task. This means every agent is by default a code chat bot about its own source code. A simple workflow is to detect if a response is about an error and if yes, run the response and source code to detect the problem 
2. This might be too futuristic but I believe there's a component missing from the current overal agent creation picture. The agents are good at getting and processing data, but not at presenting them. Most agents are still conversation based, which is understandable since humans also primarily use written communications. It would be nice to have workers dedicated to presenting data. Currently people use markdown as an improvement from plain text. But ultimately I believe they will use web apps, with more flexibity and the crucial addition of interactivity with users. A web app producing agent could, for example, build a text reader and whiteboard where users can draw or highlight, in addition to only giving textual input. A code analyzing worker should create a website that interactively guides users through the code base (see my recently built http://159.223.132.83/code for an example)
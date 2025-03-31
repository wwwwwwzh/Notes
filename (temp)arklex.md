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




# Background On Automation
## History
### LLM+Tool
This approach is actually rooted in intelligence theory. We have a central thinking machine and allocate specific work to specific units of computation. Of course, the central unit can also perform those tasks, but due to the specificity generality tradeoff it might not perform fast or well. The contrary is also true. The specific units can also adopt this central unit-specific units architecture. 

Crewai uses its own [toolkit](https://docs.crewai.com/concepts/tools#available-crewai-tools) and from [langchain](https://python.langchain.com/docs/integrations/tools/)

### Swarm
crew.ai
- https://youtu.be/ONKOXwucLvE
- agent, task, crew, flow: 

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


## Architecture
```py
def generate(self):
    self._load_docs()  # Loads crawled documents
    self._generate_tasks()  # Creates initial tasks
    best_practices = [self._generate_best_practice(task) for task]
    app = TaskEditorApp(tasks)  # Human refinement
    finetuned_best_practices = self._finetune_best_practice(steps)
    return self._format_task_graph(practices)  # Final JSON structure


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

## Sample Tasks
Note that most tasks require using a predefined procedure, but this procudure is defined after exploration. We need to see if we want to start with the exploration or directly witht the procedure

### Common tasks
- custom news feed
- stock tracker
- customer service bot (like those floating window chatbox in some websites)
- 

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

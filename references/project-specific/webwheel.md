
# summary
## Sum

## Plan


## To Read
https://discord.com/channels/1303749220842340412/1310029356839473192/1356986678375350412

https://discord.com/channels/1303749220842340412/1355959799426060398/1355994657984741577



# ----- Traditional----- 







# ----- Agentic ----- 


# Structure
- the user enters a prompt
- optional starts -- 
- agent searches google with the prompt
- the page is parsed and with the prompt goes to LLM, LLM returns 1 to 3 websites to click
- for each chosen website, agent enters the website, all text are scrapped and sent to LLM. A summary of background information (200 tokens) about the task and a plan (150 tokens) is returned. If more than one website, previous returns are sent as input. 
- The final summary and plan are stored in taskKnowledge cache and agent returns to original starting website.
- optional ends -- 
- For each step, `enhancedKnowledge = taskState.taskKnowledge + '\n\nCurrent page DOM elements:\n' + domData.clickableElements` is sent to LLM. `{ stepInstruction, elementToClick, isComplete } = parseAIResponse(aiResponse)`
- > ClickableElement: `[${index}]<${tag} ${id} ${className} ${type}>${text}</${tag}>`

### Extension Communication
background
- content script handles the current webpage
- background 

### Task State
- startTask
- getNextStep
- endTask
- reportUIState
- setApiKey
- elementClicked


## Plans
- the highlighter needs to be more consppicuous
- DONE the ClickableElement is not uniquely identifiable in the DOM tree. Need to apply my method.
- some buttons have embded div with text inside



# Dim
$
\begin{table}[htbp]
\centering
\caption{Dimensions of Computer Interface Tools}
\begin{tabular}{|p{2.5cm}|p{3cm}|p{3.5cm}|p{3cm}|p{3cm}|}
\hline
\textbf{Tool} & \textbf{Workflow Creation} & \textbf{Action Type} & \textbf{Supported Platform} & \textbf{Orientation} \\
\hline
Open Computer Use & AI-driven & Native API actions (keyboard, mouse, shell commands) & Linux (cloud-based) & Task-oriented: performs direct actions on behalf of users \\
\hline
Browser-Use & AI-driven & DOM manipulation, browser actions & Cross-platform browsers & Task-oriented: performs web-specific tasks with memory capabilities \\
\hline
Automa & Manual (block-based) & Browser actions, data manipulation & Chrome, Firefox browsers & Task-oriented: user-defined automation sequences \\
\hline
Torta & Demonstration-based & Visual tutorial + validation scripts & macOS, primarily for command-line and GUI apps & Learning-oriented: creates mixed-media tutorials with step validation \\
\hline
PPTutorial & Demonstration-based & In-app highlighting + contextual instructions & General GUI applications & Learning-oriented: focuses on navigating visual complexity \\
\hline
Vega & Demonstration-based & Visual tutorial + in-app highlights + validation & Web browsers & Learning-oriented: provides both GUI and CLI tutorial views \\
\hline
OmniParser & AI-driven (vision-based) & Visual overlays + action generation & Cross-platform, application-agnostic & Task-oriented: enhances AI's ability to interact with interfaces \\
\hline
\end{tabular}
\end{table}
$
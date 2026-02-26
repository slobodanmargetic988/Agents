<thread-id> identificator of a thread used ot acess it through cli has to match the value in filename and in first message in thread file
<starting-timestamp> for sanity make it before the moment when thread spawning is initiated.
<current-working-directory> informative but important to make sure agent knows what folder it is working in. very usefull for worstation setup.
<originator-descriptor> default  "Codex Desktop"  MUST BE "Codex Desktop" to be visible in the UI
will research other valid values maybe we can use custom "Thread spawner for developer"
<source> default "vscode" MUST BE "vscode" to be visible in the UI

<core-base-instructions> Descriptive text that sets the attitude of the entire thread its behavior, personality and way of working. i believe we can make the custom agents much better by setting their descriptions inside this instead of insde user instructions. also by setting this manually in here we can save a huge amount of tokens which are used every time when orchestrator reads custom agents to prepare a message for custom instructions. by setting custom agent here through a skill we can avoid a few heavy turns for each agent instantiation.
<initial-commit-hash> sets the git state agent should expect when he starts working. usefull signal for agent to know if hes in a clean workstation or not. 
<initial-branch-name> same as comit hash but for branch 
<repository-url> link to repo url where origin branches are reachable

<permissions-set>has 2 possible values as far as i know but appears it can be set to custom values as well. default value for when in full acess is :
        """<permissions instructions>\nFilesystem sandboxing defines which files can be read or written. `sandbox_mode` is `danger-full-access`: No filesystem sandboxing - all commands are permitted. Network access is enabled.\nApproval policy is currently never. Do not provide the `sandbox_permissions` for any reason, commands will be rejected.\n</permissions instructions>"""

<application-context> Description of where the thread resides. (codex desktop app for example) and what are the limitations of that environment. teaches the thread how to get the best out of the UI for its environment. 
<user-personalization> this is the first set of user input the thread gets and it sets users preferences. if we were to edit only this it wouls still be a big win cause orchestrators would not need to find all teh content for this and set if on thread initialiization every time.
<environment_context>  in this format environment context shows the thread where it is now. for this template it makes perfect sence to leave  this as is and only adapt curent-working-dir to match desired value.
                        defualt value :  """<environment_context>\n  <cwd><current-working-directory-up-to-date></cwd>\n  <shell>zsh</shell>\n</environment_context>"""         
                                                                        <current-working-directory-up-to-date>=<current-working-directory> already defined
<collaboration-mode> this is something i would not touch because it can be colaboration mode or plan mode and plan mode is interactive. users should use plan mode in the app in the regular wy not using thread spawned manualy. and if they want a thread spawned manualy they can manualy switch it to plan mode in the UI.
I should maybe edit the part in the colaboration mode description where it says you are stronly discouraged to ask questions to be more strict so it never asks questions for worker threads.
<turn-identifier> some has turn id might be important to change this for all threads spawned
<first-actual-user-message> first request made by user
<first-actual-AI-response> going to have to put some place holdeer here so it looks like a regular turn completed. or maybe i can not put anithing and just give it another user propmpt to answer the previous prompt or make it so the response was "all start working on this as soon as you say start" or something like that.

<tools-descriptions-and-when-to-use> this is the actual preparation for the task 




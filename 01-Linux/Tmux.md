Tmux is a [[Terminals]] multiplexor. ![[tmux-working-diagram-4174023875.jpg]]

"Mux" comes from the word "multiplexor" which means that Tmux creates a server from which many sessions can be spawned. Within a same session, the user can spawn many new windows or pane representations of the same variable environment.
Sessions are persistent, which means that you can reattach to a closed session and even share sessions.
##Basic Usage:
- Ctrl+b is the default leader key
- Down in your window you can see [0] 0:bash, which means you are at window 0 connected to the bash shell. 
- To create a new window press leader+c
- To detach from a session leader+d
- To list the tmux sessions leader+s
- tmux attach to attach to previous session or tmux ls from the terminal.
- You can kill a server by typing tmux kill-server
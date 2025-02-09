Environment variables are variables which are defined on your shell. These are accesible by programs to find and use resources from the system.

```
env
```

You can use the command `env` to see which variables are defined on your shell. 

#### PATH:
A very important variable that many programs are designed to look for is the PATH variable. If you want to see its contents you can write:

```
echo $PATH
```

This will print a list separated by `:` , which shows the directory where your shell looks for programs when you execute a command. If the system doesn't find your command in those folders as an executable, it will just print: `command not found` .
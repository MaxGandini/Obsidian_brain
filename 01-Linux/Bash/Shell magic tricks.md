This is a note with tips gotten from the video:

https://www.youtube.com/watch?v=PRm6tYo8nGY

Example: if you forgot to 'sudo' a command, you can type:

```bash
missed command
```

```bash
sudo !!
```

"!!" is a std in for the previous command.
If you want to add something just:

```bash
sudo !!addsmth
```

```
```you can press:
- ctrl+l to clear the terminal screen 
- ctrl+a to go to beggining of line
- ctrl+e to get to end
- ctrl+k to delete rest of line
- ctrl+w to delete before cursor
```

I enabled vi mode for my terminal so these are obsolete and I don't have to remember them.

``` bash
!cd 
```

you can find the last cd command. It finds the last command that matches the pattern.

If you want to access previous arguments, like a long directory:

```
!:0 
!:1 
!:2
```

If you want to replace a previous command you can :

```bash
^fuzzy^fzf
```

This replaces fuzzy with fzf. 



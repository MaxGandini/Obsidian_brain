While working on a local branch (IE:`local_main`), if you want to push the changes to the main branch on [[Git remote]] you can use the command:

``` command
git push origin local_main
```

While working on a local branch, and finding an "un-updated" repo you can use: 

``` command 
git fetch origin
```

Or git pull:

``` command
git pull <remote> <branch>
git pull origin main
```

What it does:

Fetches the latest changes from the specified remote and branch.
Merges those changes into your current local branch (same as running git fetch + git merge).
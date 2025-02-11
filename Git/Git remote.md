When creating another file version of a repository, like a fork, you can add a pointer to the origin. (In the case of a fork, the origin is already added)

``` command
git remote add origin https://github.com/your-username/webflyx.git
```

This command is how you add an origin to a git repo. If you messed up and want to change the url :

``` command
git remote set-url origin <correct-url>
```

the correct url can be a path to a directory, like `../web` (.. signifies the previous directory out of your local repo)

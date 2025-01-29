pyenv is a program that lets you manage different versions of python and access them without changing you whole system's python version.

```
pyenv install 3.11
```

to create a specific python version for a project, go to you project folder (I recommend you create and activate your environment here so it's all nice and contained, but I'm no expert, maybe it's a bad practice that works for me) and type : 

```
pyenv local <version>
```

this will create a .python-version file which you will see activated if you activated and ran your local env.

In my case, using `starship` I see it as:

![[pyenv.png]]
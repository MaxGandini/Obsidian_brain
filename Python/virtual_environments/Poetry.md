```
pipx install poetry
```

This is not completely necessary, you can also install it with pip in your [[venv]] .

To create a .toml file, you can run :
```
poetry init
```

and it will walk you through the steps. Bear in mind that when it asks for the version of the python interpreter, you need to have it installed by some other program, like for example [[pyenv]].
In my first try, I wanted to have python 3.11 installed for my venv, but I needed any 3.11.xx to work. So my TOML file was: 
```toml
[project]
name = "llmenv"
version = "0.1.0"
description = "An environment for llm engineering"
authors = [
    {name = "MaxGandini",email = "maximiliano.gandini.27@gmail.com"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

```


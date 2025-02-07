Jupyter uses kernels to run code, and these kernels can be created easily from pre-existing virtual environments made with programs such as [[venv]].
To do this, go to your virtual environment and type:

```
ipython kernel install --user --name=myenv
```

```
python -m ipykernel install --user --name=myenv
```

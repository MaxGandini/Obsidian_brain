It's an open source framework that provides tools and APIs for downloading and training models for deep learning based on the [[Transformers]] architecture. 

To use the API one needs to create a token and login:

```python
from transformers import login
login()
```

Once logged, you can train, predict, etc.
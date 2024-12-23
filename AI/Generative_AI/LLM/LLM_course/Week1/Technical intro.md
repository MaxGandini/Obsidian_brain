
The number of parameters and weights in an LLM is daunting and far beyond what you see in a typical data science model:

- GPT-1 had 117 Million weights. (2018)
- GPT-4 has 1.76 Trillion weights... (2023)
- The number of weights of the latest frontier models are undisclosed.

#### Tokens:

In the past, neural networks were trained to predict the next character. The demands of this information from the model is huge, there is less predictability with just taking into account the next character. So the training phase would be too demanding. 
Some went to the other extreme, and made models to take individual words and tried to infer the meaning. The problem with these models is that the vocabulary needed was insane, and it couldn't handle unknown or rare words.

The optimal solution was found in the form of tokens. Which are chunks of words, much like syllables in spanish but not quite. The advantage of this is that almost all words are put on the same level of importance, for example, handling proper names like any other word.

![[token.png]]

Something to bear in mind is that some words in the example are broken down into bits which can capture the meaning. In the case of "masterers" we have an invented word, but it's meaning is isolated through the master token. 

##### We are going to explore different tokenizers as there is not a single approach to the problem.

## Context window:

It measures the amount of tokens that a model can consider when generating a new token. 

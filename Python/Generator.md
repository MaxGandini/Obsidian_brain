A generator is an [[Iterable]] that you can only iterate over once.
In python an generator is an object that when propped, returns a value from a pre-set sequence, but it generates these values as it is propped. IE:

```
for i in range(5):
```

range(5) is an generator, which sums 1 each time it's propped externally.
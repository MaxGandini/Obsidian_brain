To do a while loop, you can use the syntax:
```
x=1
while [ $x -le 5]
do
	x=$(( $x + 1 ))
done
```

So, this loops while x is less than five, and you define an x variable that you use to run through the loop. 
For boolean operators between variables or numbers, you can use :

```
-lt, -le, -gt , -ge , -eq, -ne
```


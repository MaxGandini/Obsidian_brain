Permissions are visually represented as a 10-character string. 
```
drwxrwxrwx
```

### First character:

It's always a `d` (directory) or a `-` (file) .

### positions 2-3-4:

`rwx` read write execute

This is applied to the owner of the file, this usually means the creator, but it can be changed.

If this were `r-x` it means the owner can read and execute but not write.

### positions 5 to 10:

The following 3 (5 to 7) apply to a group, and the rest applies to others.
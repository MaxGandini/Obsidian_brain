Using the command `git config` one can access many configuration options for a repository.
The hierarchy is as follows:

![[e4S7M9u.png]]

This traces out a hierarchy where the more specific location overrides the more general one (makes sense).

If you want to see your current git configuration:

``` command
git config --list --local
```

The output of this, is the local keys which are set for the project. But if you want to get some particular key:

``` command
git config --get <key>
git config --add 
git config --add webflyx.ceo "Warren"
```

The second command adds a key which makes no sense, but It's an useful template.
If you want to unset a key, or unset all keys which share some property:

``` command
git config --unset <key>
git config --unset-all example.key
git config --remove-section section
```

In the last command I remove a section, which in the case of the previous example.key, would be `section=example` .


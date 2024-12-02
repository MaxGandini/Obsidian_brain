A good shortcut is ctrl+r for reverse fuzzy find.
``` bash
ctrl+r
```

You can ask bash for your PID and your last PID:

``` bash
echo $$
echo $_
```

For example, if you want to go back a folder while cding, you can type:

```bash
cd $_
```

Note that for this to make sense, you can check with echo `$_` .
It's easier to go to the previours with :

```bash
cd -
```

a way to remove some file in a certain position when you ls:

```bash
rm file[14]
```

This will remove a file named file followed by 1 or 4.


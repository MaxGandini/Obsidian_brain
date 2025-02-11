Git branches are like pointers to specific versions of the main or master branch. Instead of putting your hands on a well curated repository that is working, you [[fork]] it , work on the changed separately and then make a [[pull]] request. 

### Merge:

If you want to merge a branch to main, you switch to the main branch and use the command:

``` command
 git merge update_titles
 git branch -d update_titles #deletes it
```

### Rebase :

No better way to explain what a rebase is, than with this graph:

##### initially:
```
A - B - C    main
   \
    D - E    feature_branch
```

```
git rebase main
```
##### after:
```
A - B - C         main
         \
          D - E   feature_branch
```
 
 ##### IE:
 
 To use rebase to bring changes from main onto a current branch (let’s pretend we’re on one called jdsl), we would run this while on the jdsl branch:

```
git rebase main
```

This will do the following:

- Checkout the latest commit from main into a temporary location
- Replay each commit from jdsl one at a time onto this temporary location
- Update the jdsl branch to point to the last replayed commit in the temporary location, making this the new permanent jdsl.
- The rebase does not affect the main branch; jdsl now includes all changes from main.

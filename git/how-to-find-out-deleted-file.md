# How to find out files that are deleted

I met a problem this morning. Some guy in my team deleted some database migration files by accident a few days ago. And I can't remember the files's contents.

I searched the problem in StackOverflow and in this thread https://stackoverflow.com/questions/6839398/find-when-a-file-was-deleted-in-git I found the answer.

```shell
git log --full-history -- [file path]
```
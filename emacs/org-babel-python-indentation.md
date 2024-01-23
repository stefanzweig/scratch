# Indentation for Python in Babel Block

I am using org mode for note taking. Sometimes I write python code in babel block. 

However the indentation goes mess if the depth increases. I checked the org mode manual and there is an answer. 

The following statement is inserted into the config file to make it work.

```lisp
(setq org-src-preserve-indentation 4)
```

To edit the block in the mini buffer, the shortcut is `C-c '`.

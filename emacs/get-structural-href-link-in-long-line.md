# How to get a link in a long line

I saw a table in a page in which a link is in a column of each row. I need to snap all the links. What I did is as the following.

- In Chrome Devtool I got the text of the table.
- Pasted the text into `emacs` I use.
- Set the buffer to `sgml-mode`, which can read the markup tags.
- Run command `sgml-pretty-print` to render the buffer into a structural text. One tag at each line.
- Move the cursor to the very beginning of buffer, run the command `delete-non-matching-lines`. The result of the command shows the lines I need, like 

```      
     score.html?d=20220522
```
- Run some rectangle command to add the prefix to each line, stripping the whitespaces around.

The final result looks like `https://www.nhk.or.jp/goshogi/igo/score.html?d=20220522`. I save the bunch of links alike to a list file. I can get the page contents from the list file then.
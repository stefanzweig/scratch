# how to make field with " into numeric one

In a CSV file, if a column contains numbers with commas (e.g., "1,000"), and the quote marks, I am using `emacs` to covert it into a recognizable numeric format.

Sample:

```csv
2023-12-31,CNY,"-1,200.00",cmbchine,WeChat Pay
```

1. copy the contents into `emacs`
2. run `M-x org-table-convert-region`,  the text turns into the following:
```org
| 2023-12-31 | CNY | -1,200.00 | cmbchine | WeChat Pay |
```
3. replace "," with empty string
4. replace "|" with comma ","
5. delete every comma in the end of each line
6. save the `csv` file. done.

Then the `csv` file can be inserted into a `sqlite` file using the command 

```sh
sqlite-utils insert cmb.db fund_flow cmb2024.csv --csv
```

The schema can be checked with the command

```sh
sqlite-utils schema cmb.db
```

The output should be the following, which `Amount` can be seen in the float format.

```sql
CREATE TABLE "fund_flow" (
   [Date] TEXT,
   [Currency] TEXT,
   [Amount] FLOAT,
   [Description] TEXT,
   [Information] TEXT
);
```


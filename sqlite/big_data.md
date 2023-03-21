# How to handle the big data with sqlite and pandas

SQLite with memory can be used to handled the big data in csv format.

```python
import pandas as pd
import sqlite3

db = sqlite3.connect(':memory:')

with db:
    c = db.cursor()
    f = 'taxi.csv'
    df = pd.read_csv(f, sep=',')
    df.to_sql('tempdata', db, if_exists='replace', index=False)

df.info()
```
# SQLite-Utils Insert Files into database

### Basic Usage

I want to insert all the csv files in the folder into the tabel **mytable**.

```shell
sqlite-utils insert-files karls.db mytable *.csv \
    -c name:name \
    -c content:content \
    -c content_hash:sha256 \
    -c created:ctime_iso \
    -c modified:mtime_iso \
    -c size:size \
    --upsert  \
    --alter \
    --pk name%
```

At the same time, I want to insert all csv data into the **brand** table.

```shell
#!/bin/bash
for i in `find . -type f -name "*.csv"`
do
    ls -l $i
    sqlite-utils insert karls.db brand $i --csv --alter
done
```

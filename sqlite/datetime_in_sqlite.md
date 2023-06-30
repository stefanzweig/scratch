# DateTime in SQLite

Function `date` can add some offsets in query statement.

```sql
select * from records where datetime <= date(:date_end, '+1 day')
```

In the statement above the argument date_end is in the  format like "2023-06-30", without the time, so one day is added if the query wants to include this date.
# Learn to Use Datasette Dashboard

### Installation

```shell
pip3 install datasette-dashboards
```

### Configurations

In metadata.yml,

```yaml
  datasette-dashboards:
    stats:
      title: My Data
      description: My Personal Data
      settings:
        allow_fullscreen: true
        autorefresh: 0
      layout:
        - [daily-line]
      filters:
        date_start:
          name: Date Start
          type: date
          default: "2023-04-01"
        date_end:
          name: Date End
          type: date
          default: "2023-04-30"
      charts:
        daily-line:
          title: daily data line 
          db: blood
          query: >-
            select
                strftime("%m-%d", datetime) as day,
                strftime("%H:00", datetime) as time,
                value
            from
              blood
            where
              strftime("%M", datetime) < '05' 
              [[ AND datetime >= :date_start ]] 
              [[ AND datetime <= date(:date_end, '+1 day') ]]
            order by
              day
          library: vega-lite
          display:
            mark: { type: line, tooltip: true }
            encoding:
              x: { field: time, type: ordinal, bin: false }
              y: { field: value, type: quantitative, bin: false }
              color: {field: day, type: nominal}
```

#### SQL Statement Writing

The big importance of SQL statement is `query: >-`

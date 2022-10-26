# Use SQLite-Utils Analyzing the Data in Table

### Basic Usage

Curl the link and get the data, passing it to the `sqlite-utils` with `memory -` option to analyse data, following a sql statement.

```shell
$ curl -s 'https://api.github.com/users/dogsheep/repos' \
  | sqlite-utils memory - '
      select full_name, forks_count, stargazers_count as stars
      from stdin order by stars desc limit 3
    ' -t
```

The result looks like

```
full_name                     forks_count    stars
--------------------------  -------------  -------
dogsheep/twitter-to-sqlite             12      225
dogsheep/github-to-sqlite              14      139
dogsheep/dogsheep-photos                5      116
```

`-t` option decides the format of result to table. The documentation of the tool is https://sqlite-utils.datasette.io/en/stable/
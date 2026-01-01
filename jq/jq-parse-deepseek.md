# How to parse deepseek archive in JSON format

`Deepseek` supplies archive file in JSON format. It contains data in list at the top level.

I flattened the data via `jq` tool and the new flattened json list can be inserted into a `sqlite` data file.


Here is the command

```sh
jq '[.[] | {title, inserted_at, ask: .mapping["1"].message.fragments[0].content}]' conversations.json \
    | sqlite-utils insert deepseek.db questions -
```

The first part of the command makes the output like this.

```json
[
  {
    "title": "使用DeepSeek与LLM CLI教程",
    "inserted_at": "2025-12-25T21:24:43.696000+08:00",
    "ask": "llm cli (simon willison) 能使用deepseek"
  },
  {
    "title": "NE555芯片型号及功能解析",
    "inserted_at": "2025-12-25T22:56:41.219000+08:00",
    "ask": "型号：21AT68H NE555P是什么东西"
  },
  {
    "title": "请求分析GitHub日志工作流",
    "inserted_at": "2025-12-25T23:17:58.896000+08:00",
    "ask": "https://gistpreview.github.io/?6e07c54db7bb8ed8aa0eccfe4a384679 分析一下这份日志，厘清工作流"
  },
  {
    "title": "DeepSeek安装与使用指南",
    "inserted_at": "2025-12-26T08:20:06.034000+08:00",
    "ask": "llm-deepseek 怎么安装"
  }
]
```


# Tasks in xmake

My xmake's version is `xmake v2.9.8+20250321`, which runs in the ubuntu 20.04.

Here is an example of `xmake.lua`. There are some highlights.

```lua
add_rules("mode.debug", "mode.release")

task("my_task")
    on_run(function()
        print("✅ Task is running!")
    end)

target("hello")
    set_kind("binary")
    add_files("src/*.c")
    after_build(function()
        print("Build finished, running task...")
        print("task.run(my_task)")
        import("core.project.task")
        task.run("my_task")
    end)

target("default")
    set_kind("phony")
    on_build(function()
        import("core.project.task")
        task.run("my_task")
    end)
```

In target `default` the kind is set to "phony", which means none of file artifacts will be produced.

At the same time, statement of `import("core.project.task")` is needed to make sure the plugin `task` is introduced.
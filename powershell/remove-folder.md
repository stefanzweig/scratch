# How to remove the folder recursively

To remove the folder, use the following statements:

```powershell
Remove-Item $folderPath -Force  -Recurse -ErrorAction SilentlyContinue
```

Where `$folderPath` is the folder path. For example:

```powershell
Remove-Item .\spdlog\ -Force  -Recurse -ErrorAction SilentlyContinue
```

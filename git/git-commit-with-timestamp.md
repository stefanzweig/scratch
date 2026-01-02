# How to commit with timestamp in message

In PowerShell,
```powershell
git commit -am "$(Get-Date -Format 'MM-dd HH:mm') Fix bug"
```

In bash or zsh,
```sh
git commit -am "$(date '+%m-%d %H:%M') 修复bug"
```


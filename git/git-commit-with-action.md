# How to git commit automatically

Especially in `Github Actions` with generated artifacts.

```sh
git config user.name "Automated" 
git config user.email "actions@users.noreply.github.com" 
git add -A timestamp=$(date -u) 
git commit -m "${timestamp}" || exit 0 
git pull --rebase 
git push
```
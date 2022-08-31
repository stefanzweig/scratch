# The command for the github actions.

I copied it from simon willision's til build.yaml file. 

```
- name: Commit and push if README changed
    run: |-
    cd main
    git diff
    git config --global user.email "readme-bot@example.com"
    git config --global user.name "README-bot"
    git diff --quiet || (git add README.md && git commit -m "Updated README")
    git push
```
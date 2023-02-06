# How to configure the gitlab-runner in both user and root mode

We install the gitlab-runner on ubuntu server.

```shell
sudo apt install gitlab-runner
```

Then we need register the runner.
```shell
gitlab-runner register
```
It is better to register the gitlab-runner in user mode, or some folder permission troubles would be met.

I the final step of registration, a choice shoule be made which way the runner runs. Typically `shell` is used.

Cool. The registration is done. At last the gitlab-runner should run in a user mode with the command:

```shell
gitlab-runner run &
```

It runs and immediately is put in the background.
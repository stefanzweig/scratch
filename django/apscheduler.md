# Django-Apscheduler schedule a job

I need to run the job at several time points in the day. The solution is comma-split string in the `register_job` decorator.

```python
@register_job(scheduler, "cron", hour='0,6,12,18')
def pending_block_activity_notification():
    print("pending_block_activity_notification Job started")
```
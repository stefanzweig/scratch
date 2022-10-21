# Bulk Create

Bulk create the data at a time.

```python
bulk = []
for dev in data:
    bulk.append(Device(sn=dev.sn))
objs = Device.objects.bulk_create(bulk)
```
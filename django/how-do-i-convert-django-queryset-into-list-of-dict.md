# How do I convert django queryset into list of dictionary

link: https://stackoverflow.com/questions/7811556/

Solution #1:

```python
from django.forms.models import model_to_dict

def queryset_to_list(qs,fields=None, exclude=None):
    my_list=[]
    for x in qs:
        my_list.append(model_to_dict(x,fields=fields,exclude=exclude))
    return my_list
```

Solution #2:

```python
>>> Blog.objects.values()
[{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}],
>>> Blog.objects.values('id', 'name')
[{'id': 1, 'name': 'Beatles Blog'}]
```

Solution #1 is my favorite.
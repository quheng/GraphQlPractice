


## notes
1. missed this dependency
```
pip install django-graphiql
```
Second missed add installed app in settings.py
```
INSTALLED_APPS = [
    # ...
    'django_graphiql',
    # ...
]
```

2. In GraphQL, underline will be replaced by capital. For example, if you want to get the field of source_url, you can use sourceUrl.

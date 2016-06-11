## aim
use these project to practice GraphQL

## usage
todo

## dependency
You can use
```
pip install -r requirements.txt
```
to install all of dependencies


## test
You can use
```
py.test unit_test.py
```
to do some unit tests

## notes
1. In this [https://data.crunchbase.com/docs/2013-snapshot](https://data.crunchbase.com/docs/2013-snapshot) just provide advanced account register. If you want to register a basic account, should go to [https://data.crunchbase.com/page/basic-access-form](https://data.crunchbase.com/page/basic-access-form). Further, better use Gmail to register account. If you use another e-mail, you may lose their reply.
2. I can not visited [http://graphql.org](http://graphql.org), but I get their source code from [here](https://github.com/graphql/graphql.github.io). I read their documents and example from this.
3. First, I try to use flask. The example of flask-graphql provide by graphene is discarded and did not work well. I get the right usage from [here](https://github.com/graphql-python/flask-graphql). Then I find there is no usable example of flask so that I decided to use Django.
4. When I use Django, the documents of graphene still have some mistakes.
First missed this dependency
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
5. In GraphQL, underline will be replaced by capital. For example, if you want to get the field of source_url, you can use sourceUrl.

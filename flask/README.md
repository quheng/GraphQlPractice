## aim
use these project to practice GraphQL

## usage
I do not finish this.
I can not find any useful documents and work examples.
DO NOT USE THIS

## BUGS
1. can not return
```
session.query(Obj).all()
```
2. the method provided by official documents
```
node = relay.NodeField(Employee)
all_employees = SQLAlchemyConnectionField(Employee)
all_roles = SQLAlchemyConnectionField(Role)
role = relay.NodeField(Role)
```
some fields do not show

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

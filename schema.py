# coding=utf8
# Author: quheng

import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode
from graphene.contrib.sqlalchemy import SQLAlchemyConnectionField


from database import Acquisitions as AcquisitionsModels


schema = graphene.Schema()


@schema.register
class Acquisitions(SQLAlchemyNode):
    class Meta:
        model = AcquisitionsModels


class Query(graphene.ObjectType):
    node = relay.NodeField()
    all_acquisitions = SQLAlchemyConnectionField(Acquisitions)


schema.query = Query

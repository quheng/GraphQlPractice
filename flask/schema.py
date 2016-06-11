# coding=utf8
# Author: quheng

import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode
from graphene.contrib.sqlalchemy import SQLAlchemyConnectionField

from database import session
from database import Acquisitions as AcquisitionsModels
from database import Degrees as DegreesModels
from database import FundingRounds as FundingRoundsModels
from database import Funds as FundsModels
from database import Investments as InvestmentsModels
from database import Ipos as IposModels
from database import Milesones as MilesonesModels
from database import Objects as ObjectsModels
from database import Offices as OfficesModels
from database import People as PeopleModels
from database import Relationships as RelationshipsModels

schema = graphene.Schema(session=session)


class AcquisitionsType(graphene.ObjectType):
    name = "acquisitions"
    id = graphene.Int()
    acquisition_id = graphene.Int()
    acquiring_object_id = graphene.String()
    acquired_object_id = graphene.String()
    term_code = graphene.String()
    price_amount = graphene.Float()
    price_currency_code = graphene.String()
    acquired_at = graphene.DateField()
    source_url = graphene.String()
    source_description = graphene.String()
    created_at = graphene.DateTimeField()
    updated_at = graphene.DateTimeField()

class Query(graphene.ObjectType):
    name = "query"

    acquisitions = graphene.Field(
        AcquisitionsType,
        id = graphene.String()
    )

    def resolve_acquisitions(self, args, info):
        id = args.get("id")
        return session.query(AcquisitionsModels).all()
        return CbAcquisitions.objects.get(id=id)

schema.query = Query

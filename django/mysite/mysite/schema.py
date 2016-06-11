# coding=utf8
# Author: quheng

import graphene


from models import CbAcquisitions
from models import CbObjects

class AcquisitionsType(graphene.ObjectType):
    id = graphene.Int()
    acquisition_id = graphene.Int()
    acquiring_object_id = graphene.String()
    acquired_object_id = graphene.String()
    term_code = graphene.String()
    price_amount = graphene.Float()
    price_currency_code = graphene.String()
    acquired_at = graphene.String()
    source_url = graphene.String()
    source_description = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

class ObjectType(graphene.ObjectType):
    id = graphene.String()
    entity_type = graphene.String()
    entity_id = graphene.String()
    parent_id = graphene.String()
    name = graphene.String()
    normalized_name = graphene.String()
    permalink = graphene.String()
    category_code = graphene.String()
    status = graphene.String()
    founded_at = graphene.String()
    closed_at = graphene.String()
    domain = graphene.String()
    homepage_url = graphene.String()
    twitter_username = graphene.String()
    logo_url = graphene.String()
    logo_width = graphene.String()
    logo_height = graphene.String()
    short_description = graphene.String()
    description = graphene.String()
    overview = graphene.String()
    tag_list = graphene.String()
    country_code = graphene.String()
    state_code = graphene.String()
    city = graphene.String()
    region = graphene.String()
    first_investment_at = graphene.String()
    last_investment_at = graphene.String()
    investment_rounds = graphene.String()
    invested_companies = graphene.String()
    first_funding_at = graphene.String()
    last_funding_at = graphene.String()
    funding_rounds = graphene.String()
    funding_total_usd = graphene.String()
    first_milestone_at = graphene.String()
    last_milestone_at = graphene.String()
    milestones = graphene.String()
    relationships = graphene.String()
    created_by = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()



class Query(graphene.ObjectType):
    name = "query"

    objects = graphene.List(
        ObjectType,
        id = graphene.String()
    )

    def resolve_objects(self, args, info):
        id = args.get("id")
        return CbObjects.objects.filter(entity_id__lt=10)

schema = graphene.Schema(
    query = Query
)

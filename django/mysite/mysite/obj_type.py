# coding=utf8
# Author: quheng

import graphene

from models import CbAcquisitions
from models import CbDegrees
from models import CbFundingRounds
from models import CbFunds
from models import CbInvestments
from models import CbIpos
from models import CbMilestones
from models import CbObjects
from models import CbOffices
from models import CbPeople
from models import CbRelationships
from obj_filter import *

class ObjectsType(graphene.ObjectType):
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

# finish
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
    acquiring = graphene.List(
        ObjectsType,
    )
    acquired = graphene.List(
        ObjectsType,
    )

    def resolve_acquiring(self, args, info):
        id = self.acquiring_object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

    def resolve_acquired(self, args, info):
        id = self.acquiring_object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

# finish
class DegreesType(graphene.ObjectType):
    id = graphene.String()
    object_id = graphene.String()
    degree_type = graphene.String()
    subject = graphene.String()
    institution = graphene.String()
    graduated_at = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

# finish
class PeopleType(graphene.ObjectType):
    id = graphene.String()
    object_id = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    birthplace = graphene.String()
    affiliation_name = graphene.String()
    degrees = graphene.List(
        DegreesType,
    )

    def resolve_degrees(self, args, info):
        id = self.object_id
        if id:
            cond = "object_id='" + id + "'"
        return degrees_filter(cond)

# finish
class FundingRoundsType(graphene.ObjectType):
    id = graphene.String()
    funding_round_id = graphene.String()
    object_id = graphene.String()
    funded_at = graphene.String()
    funding_round_type = graphene.String()
    funding_round_code = graphene.String()
    raised_amount_usd = graphene.String()
    raised_amount = graphene.String()
    raised_currency_code = graphene.String()
    pre_money_valuation_usd = graphene.String()
    pre_money_valuation = graphene.String()
    pre_money_currency_code = graphene.String()
    post_money_valuation_usd = graphene.String()
    post_money_valuation = graphene.String()
    post_money_currency_code = graphene.String()
    participants = graphene.String()
    is_first_round = graphene.String()
    is_last_round = graphene.String()
    source_url = graphene.String()
    source_description = graphene.String()
    created_by = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    company = graphene.List(
        ObjectsType,
    )

    def resolve_company(self, args, info):
        id = self.object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

# finish
class FundsType(graphene.ObjectType):
    id = graphene.String()
    fund_id = graphene.String()
    object_id = graphene.String()
    name = graphene.String()
    funded_at = graphene.String()
    raised_amount = graphene.String()
    raised_currency_code = graphene.String()
    source_url = graphene.String()
    source_description = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_investment(self, args, info):
        id = self.object_id
        if id:
            cond = "investor_object_id='" + id + "'"
        return objects_filter(cond)


class InvestmentsType(graphene.ObjectType):
    id = graphene.String()
    funding_round_id = graphene.String()
    funded_object_id = graphene.String()
    investor_object_id = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()


class IposType(graphene.ObjectType):
    id = graphene.String()
    ipo_id = graphene.String()
    object_id = graphene.String()
    valuation_amount = graphene.String()
    valuation_currency_code = graphene.String()
    raised_amount = graphene.String()
    raised_currency_code = graphene.String()
    public_at = graphene.String()
    stock_symbol = graphene.String()
    source_url = graphene.String()
    source_description = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    company = graphene.List(
        ObjectsType,
    )

    def resolve_company(self, args, info):
        id = self.object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)


class MilestonesType(graphene.ObjectType):
    id = graphene.String()
    object_id = graphene.String()
    milestone_at = graphene.String()
    milestone_code = graphene.String()
    description = graphene.String()
    source_url = graphene.String()
    source_description = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    company = graphene.List(
        ObjectsType,
    )

    def resolve_company(self, args, info):
        id = self.object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

class OfficesType(graphene.ObjectType):
    id = graphene.String()
    object_id = graphene.String()
    office_id = graphene.String()
    description = graphene.String()
    region = graphene.String()
    address1 = graphene.String()
    address2 = graphene.String()
    city = graphene.String()
    zip_code = graphene.String()
    state_code = graphene.String()
    country_code = graphene.String()
    latitude = graphene.String()
    longitude = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    company = graphene.List(
        ObjectsType,
    )

    def resolve_company(self, args, info):
        id = self.object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)


class RelationshipsType(graphene.ObjectType):
    id = graphene.String()
    relationship_id = graphene.String()
    person_object_id = graphene.String()
    relationship_object_id = graphene.String()
    start_at = graphene.String()
    end_at = graphene.String()
    is_past = graphene.String()
    sequence = graphene.String()
    title = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()

    company = graphene.List(
        ObjectsType,
    )

    def resolve_company(self, args, info):
        id = self.relationship_object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

    person = graphene.List(
        ObjectsType,
    )

    def resolve_person(self, args, info):
        id = self.person_object_id
        if id:
            cond = "id='" + id + "'"
        return objects_filter(cond)

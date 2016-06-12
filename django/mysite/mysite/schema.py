# coding=utf8
# Author: quheng

import graphene

from obj_type import *
from obj_gra import *
from obj_filter import *


class Query(graphene.ObjectType):
    name = "query"
    acquisitions = GraAcquisitions
    objects = GraObjects
    people = GraPeople
    fundingRounds = GraFundingRounds
    funds = GraFunds
    ipos = GraIpos
    milestones = GraMilestones
    offices = GraOffices
    relationships = GraRelationships
    people = GraPeople

    def resolve_acquisitions(self, args, info):
        return acquisitions_filter(args.get("where"))

    def resolve_objects(self, args, info):
        return objects_filter(args.get("where"))

    def resolve_people(self, args, info):
        return people_filter(args.get("where"))

    def resolve_fundingRounds(self, args, info):
        return funding_rounds_filter(args.get("where"))

    def resolve_funds(self, args, info):
        return funds_filter(args.get("where"))

    def resolve_ipos(self, args, info):
        return ipos_filter(args.get("where"))

    def resolve_milestones(self, args, info):
        return milestones_filter(args.get("where"))

    def resolve_offices(self, args, info):
        return offices_filter(args.get("where"))

    def resolve_relationships(self, args, info):
        return relationships_filter(args.get("where"))

schema = graphene.Schema(
    query = Query
)

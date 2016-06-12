# coding=utf8
# Author: quheng


from obj_type import *

GraAcquisitions = graphene.List(
    AcquisitionsType,
    where = graphene.String()
)
GraDegrees = graphene.List(
    DegreesType,
    where = graphene.String()
)
GraFundingRounds = graphene.List(
    FundingRoundsType,
    where = graphene.String()
)
GraFunds = graphene.List(
    FundsType,
    where = graphene.String()
)
GraInvestments = graphene.List(
    InvestmentsType,
    where = graphene.String()
)
GraIpos = graphene.List(
    IposType,
    where = graphene.String()
)
GraMilestones = graphene.List(
    MilestonesType,
    where = graphene.String()
)
GraObjects = graphene.List(
    ObjectsType,
    where = graphene.String()
)
GraOffices = graphene.List(
    OfficesType,
    where = graphene.String()
)
GraPeople = graphene.List(
    PeopleType,
    where = graphene.String()
)
GraRelationships = graphene.List(
    RelationshipsType,
    where = graphene.String()
)

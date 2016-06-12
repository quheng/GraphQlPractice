# coding=utf8
# Author: quheng

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

def condition_preprocess(condition):
    cond = condition.replace(' ', '')
    cond = cond.replace(">", "__gt=")
    cond = cond.replace("<", "__lt=")
    cond = cond.replace(">=", "__gte=")
    cond = cond.replace("<=", "__lte=")
    return cond


def acquisitions_filter(condition):
    if not condition:
        return CbAcquisitions.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbAcquisitions.objects.filter(" + condition + ")"
        return res

def objects_filter(condition):
    if not condition:
        return CbObjects.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbObjects.objects.filter(" + condition + ")"
        return res

def degrees_filter(condition):
    if not condition:
        return CbDegrees.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbDegrees.objects.filter(" + condition + ")"
        return res

def people_filter(condition):
    if not condition:
        return CbPeople.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbPeople.objects.filter(" + condition + ")"
        return res

def funding_rounds_filter(condition):
    if not condition:
        return CbFundingRounds.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbFundingRounds.objects.filter(" + condition + ")"
        return res

def funds_filter(condition):
    if not condition:
        return CbFunds.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbFunds.objects.filter(" + condition + ")"
        return res

def ipos_filter(condition):
    if not condition:
        return CbIpos.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbIpos.objects.filter(" + condition + ")"
        return res

def milestones_filter(condition):
    if not condition:
        return CbMilestones.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbMilestones.objects.filter(" + condition + ")"
        return res

def offices_filter(condition):
    if not condition:
        return CbOffices.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbOffices.objects.filter(" + condition + ")"
        return res

def relationships_filter(condition):
    if not condition:
        return CbRelationships.objects.all()
    else:
        condition = condition_preprocess(condition)
        exec "res = CbRelationships.objects.filter(" + condition + ")"
        return res

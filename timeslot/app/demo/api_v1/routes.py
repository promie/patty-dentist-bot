# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.dentists_did_timeslots import DentistsDidTimeslots
from .api.dentists_did_timeslots_tid_reserve import DentistsDidTimeslotsTidReserve
from .api.dentists_did_timeslots_tid_cancel import DentistsDidTimeslotsTidCancel


routes = [
    dict(resource=DentistsDidTimeslots, urls=['/dentists/<did>/timeslots'], endpoint='dentists_did_timeslots'),
    dict(resource=DentistsDidTimeslotsTidReserve, urls=['/dentists/<did>/timeslots/<tid>/reserve'], endpoint='dentists_did_timeslots_tid_reserve'),
    dict(resource=DentistsDidTimeslotsTidCancel, urls=['/dentists/<did>/timeslots/<tid>/cancel'], endpoint='dentists_did_timeslots_tid_cancel'),
]
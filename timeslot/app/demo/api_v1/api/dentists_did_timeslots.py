# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify, make_response

from . import Resource
from .. import schemas

from .helpers import read_from_file
class DentistsDidTimeslots(Resource):

    def get(self, did):

        dentist_name = did.title()

        try:
            timeslots = read_from_file()
            timeslot = timeslots[dentist_name]
            timeslot['id'] = dentist_name
            
            return make_response(jsonify(timeslot), 200) 
        except KeyError:
            return {}, 404
    
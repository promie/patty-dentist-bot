# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response,jsonify

from . import Resource
from .. import schemas
from .helpers import read_from_file, write_to_file, availability

class DentistsDidTimeslotsTidCancel(Resource):

    def put(self, did, tid):

        dentist_name = did.title()
        
        try:
            tid_transformed = tid.split(' ')
            tid_transformed[0] = tid_transformed[0].title()
            separator = ' '
            final_tid = separator.join(tid_transformed)

            if final_tid not in availability:
                return {}, 404
            else:
                timeslots = read_from_file()
                timeslots[dentist_name]['times'][final_tid] = 'available'
                write_to_file(timeslots)

                return make_response(jsonify({ 'message': f'Your cancellation with <span style="color: green"><strong>{dentist_name}</strong></span> for <span style="color: green"><strong>{tid}</strong></span> has been confirmed.'}))
        except KeyError:
            return {}, 404
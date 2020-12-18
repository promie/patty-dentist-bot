# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify, make_response

from . import Resource
from .. import schemas
from .helpers import read_from_file

class Dentists(Resource):

    def get(self):
        dentists = read_from_file()
        list_of_dentists = []

        for k, v in dentists.items():
            current_dentist = {"id": k, **v}
            list_of_dentists.append(current_dentist)

        return make_response(jsonify(list_of_dentists), 200)
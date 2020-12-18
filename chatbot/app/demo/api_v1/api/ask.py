# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from rivescript import RiveScript
from flask import request, g
import os

from . import Resource
from .. import schemas
from .patty import ask_patty


username = 'z5137192'
bot = RiveScript()
bot.load_directory(
    os.path.join(os.path.dirname(__file__), ".", "brain")
)
bot.sort_replies()
class Ask(Resource):

    def get(self):
        expression = g.args.get('expression')
        answer = ask_patty(bot.reply(username, expression), expression)

        return {'answer': answer}, 200, None
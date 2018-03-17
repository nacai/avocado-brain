# -*- coding: utf-8 -*-

from conversation.api import docomo

def get_reply(text):
    response = docomo.get_reply(text)
    return response

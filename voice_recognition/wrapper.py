# -*- coding: utf-8 -*-

from voice_recognition.api import docomo

def recog_start():
    voice_text = docomo.recog_start()
    return voice_text

#!env/bin/python
# -*- coding: utf-8 -*-

from tts import wrapper as tts
from conversation import wrapper as conv

def brain_start():
    while True:
        print('Input your voice:')
        input_voice = input()
        response = conv.get_reply(input_voice)
        print(response)
        tts.text_to_speech(response)

if __name__ == '__main__':
    brain_start()

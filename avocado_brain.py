#!env/bin/python
# -*- coding: utf-8 -*-

from tts import wrapper as tts

def brain_start():
    tts.text_to_speech('こんにちは')
    tts.text_to_speech('僕、アボカドです')

if __name__ == '__main__':
    brain_start()

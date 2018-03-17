# -*- coding: utf-8 -*-

from gtts import gTTS
from tempfile import NamedTemporaryFile
import pygame.mixer
import time

TEMP_VOICE_FILE_NAME='/tmp/temp.mp3'

def text_to_speech(text):
    tts = gTTS(text, lang='ja', slow=False)
    tts.save(TEMP_VOICE_FILE_NAME)
    time.sleep(0.1)
    pygame.mixer.init()
    pygame.mixer.music.load(TEMP_VOICE_FILE_NAME)
    pygame.mixer.music.play(1)
    while(pygame.mixer.music.get_busy()):
        time.sleep(0.1)
    pygame.mixer.music.stop()
    time.sleep(0.1)
    '''
    with NamedTemporaryFile() as f:
        tts.write_to_fp(f)
        pygame.mixer.init()
        print(f.name)
        pygame.mixer.music.load(f.name)
        pygame.mixer.music.play(1)
        time.sleep(1)
        while(pygame.mixer.music.get_busy()):
            print('busy')
            time.sleep(1)
        pygame.mixer.music.stop()
    '''
    

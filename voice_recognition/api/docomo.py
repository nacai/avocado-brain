from voice_recognition.api import docomo_api_key

import requests
import pyaudio
import json
import wave

KEY = docomo_api_key.KEY

URL = 'https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY=' + KEY

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 # Sampling rate depends on mic spec
RECORD_FILE_PATH = '/tmp/temp_voice.wav'
RECORD_SECONDS = 5

def recog_start():
    pa = pyaudio.PyAudio()

    input_device_index = 0

    stream = pa.open(format = FORMAT,
                     channels = CHANNELS,
                     rate = RATE,
                     input = True,
                     frames_per_buffer = chunk)
    
    all = []
    cnt = RECORD_SECONDS
    oneTime = int(RATE / chunk)
    for i in range(0, oneTime * int(RECORD_SECONDS)):
        if i % oneTime == 0:
            print(cnt)
            cnt = cnt - 1
        data = stream.read(chunk)
        all.append(data)

    stream.close()
    data = b''.join(all)
    out = wave.open(RECORD_FILE_PATH,'w')
    out.setnchannels(1) #mono
    out.setsampwidth(2) #16bits
    out.setframerate(RATE)
    out.writeframes(data)
    out.close()

    pa.terminate()
    print('Record end')
    
    payload = {'a': open(RECORD_FILE_PATH, 'rb'), 'v': 'on'}

    r = requests.post(URL, files=payload)
    recognized_voice = r.json()['text']

    print(recognized_voice)
    
    return recognized_voice


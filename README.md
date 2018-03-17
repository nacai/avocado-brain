# Avocado brain

## System Requirements
- Python 3.5 or later
- Python3-dev
- PortAudio
```
$ sudo apt install python3 python3-dev portaudio19-dev
```

## Environment Settings (for developers)
```
$ python3 -m venv env/
$ . env/bin/activate
$ pip install -e .[dev] -c constraints.txt
```

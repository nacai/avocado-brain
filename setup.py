from setuptools import setup
from version import __version__

requires = ['pyaudio']
extras = {'dev': ['pytest']}

setup(
    name='avocado_brain',
    version=__version__,
    install_requires=requires,
    dev_requires=extras['dev'],
    extras_require=extras,
)

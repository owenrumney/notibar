from setuptools import setup

APP = ['notibar/notibar.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'requests', 'keyring'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
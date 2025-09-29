from setuptools import setup

APP = ['notibar/notibar.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'logo.icns',
    'argv_emulation': False,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'requests', 'keyring'],
    'includes': ['log', 'github'],
    'excludes': ['tkinter', 'test', 'unittest', 'pydoc'],
    'optimize': 2,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
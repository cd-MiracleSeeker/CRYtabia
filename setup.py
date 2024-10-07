"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup



NAME = ['CRYtabia']
VERSION = ['0.7.1']
APP = ['main.py']
DATA_FILES = [
	'infolib.xlsx',
	'images'
]
OPTIONS = {
	"iconfile": "images/icon.icns",
	'argv_emulation': True,
	"packages": ['pandas','pygbif']
	
	}


if __name__=='__main__':
	setup(
	    app=APP,
	    data_files=DATA_FILES,
	    options={'py2app': OPTIONS},
	    setup_requires=['py2app'],
	)

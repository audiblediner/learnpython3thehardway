try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description: 'My Project',
	'author': 'Kelly C.'
	'url': 'URL to get at it.'
	'download_rul': 'Where to download it.',
	'author_email': 'audiblediner@fastmail.fm',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

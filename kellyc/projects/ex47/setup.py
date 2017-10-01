try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Kelly C.',
	'url': 'URL to get at it.',
	'download_rul': 'Where to download it.',
	'author_email': 'audiblediner@fastmail.fm',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'projectname'
}


# call setup with all arguments of config as if they had been
# passed as discrete arguments
# http://grokbase.com/t/python/python-list/125w91kxhr/setup-config-rookie
setup(**config)

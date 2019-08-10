#!/usr/bin/env python3.7

from setuptools import setup

with open('README.md', 'r') as f:
	readme = f.read()

setup(
	name='phosphorus',
	version='0.0.0',
	description='Basic regex-based WSGI framework',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='Dull Bananas',
	author_email='dull.bananas0@gmail.com',
	url='https://github.com/dullbananas/phosphorus',
	license='MIT',
	packages='phosphorus',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Internet :: WWW/HTTP :: WSGI',
	],
	python_requires='>=3.4',
	install_requires=[
	],
)

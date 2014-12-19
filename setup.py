from distutils.core import setup

version = '0.0.5'

setup(
	name='BoxOfficeMojo',
	version=version,
	install_requires=['BeautifulSoup4', 'vcrpy'],
	author='Justin Cano',
	author_email='jcano001@ucr.edu',
	packages=['bom', 'tests'],
	test_suite='tests',
	url='https://github.com/hyperbit/BoxOfficeMojoAPI',
	license='MIT License',
	description='Unofficial Python API for Box Office Mojo.',
	long_description='''\
Unofficial Python API for Box Office Mojo
http://boxofficemojo.com/
---------------------------------------------
Usage: https://github.com/hyperbit/BoxOfficeMojoAPI
''',
	classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
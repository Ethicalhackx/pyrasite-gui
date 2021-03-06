from setuptools import setup, find_packages

version = '2.0beta7'

f = open('README.rst')
long_description = f.read().split('split here')[1]
f.close()

setup(name='pyrasite-gui',
      version=version,
      description="A graphical interface for interacting with running Python processes",
      long_description=long_description,
      keywords='debugging injection runtime gtk',
      author='Luke Macken',
      author_email='lmacken@redhat.com',
      url='http://pyrasite.com',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "pyrasite",
        "meliae",
        "pycallgraph",
        "psutil",
      ],
      tests_require=['nose'],
      test_suite='nose.collector',
      entry_points="""
      [console_scripts]
      pyrasite-gui = pyrasite_gui.gui:main
      """,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Topic :: System :: Monitoring',
          'Topic :: Software Development :: Debuggers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ],
      )

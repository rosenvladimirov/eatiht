from setuptools import setup

def readme():
    with open('README.rst') as readmefile:
        return readmefile.read()

setup(name='eatiht',
      version='0.1.0',
      description='A featherweight tool used to extract an \
                  article\'s text in html documents.',
      keywords='extract extracted extracting extraction filter filtered \
               filtering out remove removed removing removal text \
               textbody body content contents sentence sentences \
               word words boilerplate boilerpipe delete tag tags \
               unsupervised classification machine learning algorithm \
               opening closing main article html hypertext \
               Rodrigo Palacios rodrigo palacios im-rodrigo im_rodrigo \
               rodricios',
      url='https://github.com/rodricios/eatiht',
      author='Rodrigo Palacios',
      author_email='rodrigopala91@gmail.com',
      license='MIT',
      packages=['eatiht'],
      install_requires=['lxml',],
      scripts=['bin/eatiht'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)

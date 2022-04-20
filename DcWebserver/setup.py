from setuptools import setup
from setuptools import find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Discord Bot Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='DcWebserver',
  version='0.0.1',
  description='A module to make your discord bots online 24/7',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abhinav Singh Rathore',
  author_email='sketchquicksilver@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Webserver', 
  packages=find_packages(),
  install_requires=['flask','threading'] )
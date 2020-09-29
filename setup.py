from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 

setup(
  name='asyncrequester',
  version='0.1.2',
  description='Basic async requester',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Abdulhamit Akaslan',
  author_email='hamtaksln@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='async', 
  packages=find_packages(),
  install_requires=['grequests'] 
)

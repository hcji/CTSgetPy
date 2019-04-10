from setuptools import setup, find_packages

setup(name='CTSgetPy',
      version='0.0.1',
      description="Python interface to Chemical Translation Service (CTS)",
      license='MIT',
      author='Hongchao Ji',
      author_email='ji.hongchao@foxmail.com',
      url='https://github.com/hcji/CTSgetPy',
	  long_description_content_type="text/markdown",
      packages=find_packages(),
	  install_requires=['requests'，'tqdm', 'bs4'],
	  classifiers=[
	  'Development Status :: 4 - Beta',
	  'Topic :: Software Development :: Chemistry'
	  'Programming Language :: Python :: 3.6',
	  ]
     )
from setuptools import setup, find_packages
tests_require = ["pytest"] 

setup(
    name='python-examples-for-beginners',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    description='Test Exponential Function Graph',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    author='Shashi Gharti',
    tests_require=tests_require,
    author_email='shashi.gharti@gmail.com'
)
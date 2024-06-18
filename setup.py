from setuptools import setup, find_packages

setup(
    name='myapp',
    description='my first python package',
    author='Zaitsu Shogo',
    packages=find_packages(),
    license='MIT'
)

print("This is setup.py.")
print(find_packages())
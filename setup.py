from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
        This function would return the list of requirements
    '''
    requirements = []
    with open(file_path) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author='Jatin',
    author_email='jatin.nandwani@gmail.com',
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
)

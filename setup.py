from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def getRequirements(filepath:str)->List[str]:
    """
    Read a requirment.txt and setup.py

    """
    requirements = []
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='mlproject',
author='Raanjith',
version='0.0.1',
packages=find_packages(),
install_requires=getRequirements('requirement.txt')    
)
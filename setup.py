from setuptools import find_packages,setup
from typing import List

HYPEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements
    '''
    print("file path",file_path)
    requirements=[]
    with open(file_path) as  file_obj:
        requirements = file_obj.readlines()
        requirements =[ req.replace("\n","") for req in requirements]
    if HYPEN_E in requirements:
        requirements.remove(HYPEN_E)

    return requirements
    

setup(
    name="computervisionproject",
    version='0.0.1',
    author="ravu",
    author_email="ravinikam00786@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
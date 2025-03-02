from setuptools import find_packages,setup
from typing import List

hyphen = "-e ."
print(List)
def get_requirements(file_path:str)->List[str]:
    ''' 
    This function will return list of requirement
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements
print(get_requirements("requirements.txt"))
setup(
name = 'mlprojrect',
version='0.0.1',
author = 'Prakhar',
author_email='kprakhar176@gmail.com',
packages=find_packages(),
install_requires =get_requirements('requirements.txt')

)

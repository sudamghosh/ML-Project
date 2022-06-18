from setuptools import find_packages, setup
from typing import List

#Declaring valriables below for setup function
PROJECT_NAME="housing-predictors"
PROJECT_VERSION="0.0.1"
AUTHOR="SUDAM GHOSH"
DESCRIPTION="THis is first House price prediction"

REQUIREMENT_FILE_NAME="requirements.txt"

#Requirement file name
def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention in
    requiremets.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    
setup(
name=PROJECT_NAME,
version=PROJECT_VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())
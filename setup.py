from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open (REQUIREMENT_FILE_NAME) as requirement_fie:
        requirement_list = requirement_fie.readlines()
        
    requirement_list = [i.replace("\n", "") for i in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list


setup(
    name="book_recommendations",
    version="0.0.2",
    author="Arpit_Trivedi",
    author_email="trivedi.virendra2685mmi@gmail.com",
    packages = ['book'],
    install_requires=get_requirements(),
)
#basic setup imports
import email
from logging import basicConfig
from setuptools import setup , find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    this function will return 
    list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
                  
                  #read lines from file
                  lines = file.readlines()

                  #process each line
                  for line in lines:
                    requirement = line.strip()

                  #ignore empty lines and -e.
                    if requirement and requirement != '-e .':
                        requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found") 

    return requirement_lst    

setup(
     name = "ETL_project",
     version = "1.0.0",
     author = "Rudra Tyagi",
     author_email = "rudratyagi777@gmail.com",
     packages = find_packages(),
     install_reqirements = get_requirements()
)

     




        

    
    
    
                    
                    
                  

                  





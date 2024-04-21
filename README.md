[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ktyD1gKg)
## Assignment 2 Formal Languages And Compilers (ST0270)

## Group Members:
**1.** Juan David Velásquez
**2.** Jhon Fredy Alzate

## System Information
- System Operating: Microsoft Windows 11
- Programming Language: Python
- Python Version: Python 3.12.2
- Tools Used: PyCharm


## instructions for executing the implementation:
**1.** In the github repository:
```bash
https://github.com/ssramirezr/assignment-2-assignamet2-teamss.git
```

You can download the main.py file or clone the repository

- Remember that you must have python installed on your operating system, or have a python iddle.

**2.** 

**2.1.** The easiest ways to run your code is to upload the file to the iddle and press the RUN button, or copy the code and paste it into an online iddle and press RUN.

**2.2.** Alternative, in the console you must access the folder where the main.py file is located, and use the commands to run the program:

     ```bash 
     python main.py
     ```
     
## Input
This is an example of what the input data looks like.

1                          number of examples

5 5                        number of productions of grammar    number of strings to analyze

S AB BA SS AC BD           grammar

C SB

D SA

A a

B b

aabbab                     string 1 to analyze

aabb                       string 2 to analyze

ab                         string 3 to analyze

aa                         string 4 to analyze

b                          string 5 to analyze


## Output
This is an example of what the output data looks like.

yes                        string 1 accepted

yes                        string 2 accepted

yes                        string 3 accepted

no                         string 4 rejected

no                         string 5 rejected


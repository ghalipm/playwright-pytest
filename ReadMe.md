1.	Windows PowerShell, go to pytest module directory
2.	pip install --upgrade pip setuptools  (to avoid working on old files)
3.	python -m venv venv
4.	venv\Scripts\activate
venv is green? Good (at this step it has to be green)
5.	pip install playwright
    playwright install
6.	playwright --version
Version 1.44.0? good
7.	pip install pytest
pytest 8.2.1? good
8.	pip install pytest selenium
9.	make sure your tests folder is at the same level as venv (otherwise a lot of problems!)

# to run two or more tests at the same time:
10.	pip install pytest-xdist
11.	pytest --numprocesses auto

# to get more detailed report, add -v for verbose report, then you see which tests ran:
12.	pytest --numprocesses auto -v

Ensure there is an __init__.py file in 
your tests directory. This file can be empty, 
but it allows Python to recognize 
the directory as a package.

Running Tests: Run your tests from the project root 
directory. This ensures that the root directory 
is in the Python path.

Adjust Imports: Use relative imports if necessary.
Ensure that your imports are correct.

Ensure Correct Directory Structure: Make sure 
your directory structure is correct. For example:

Project Directory Structure:

project_root/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_10_element_handle_find_elements.py
└── pytest.ini

tests/init.py: Make sure this file exists 
even if it's empty.
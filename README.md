# Tools

## selenium
https://www.selenium.dev

Python 3.7+

pip install selenium

webdrivers:
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/



## pytest
https://docs.pytest.org/en/7.2.x/

pytest requires: Python 3.7+ or PyPy3

pip install -U pytest

Check that you installed the correct version:

$ pytest --version
pytest 7.2.0



## pytest-xdist
https://pytest-xdist.readthedocs.io/en/latest/

Install the plugin with:
pip install pytest-xdist

To use psutil for detection of the number of CPUs available, install the psutil extra:
pip install pytest-xdist[psutil]



## pytest-html
https://pytest-html.readthedocs.io/en/latest/

pytest-html will work with Python >=3.6 or PyPy3.

To install pytest-html using pip:
$ pip install pytest-html



## openpyxl
https://openpyxl.readthedocs.io/en/stable/index.html

Python 3.6, 3.7, 3.8 and 3.9.

Installation
$ pip install openpyxl


## allure-pytest
https://docs.qameta.io/allure-report

$ pip install


# Directory structure

mkdir configurations logs pages reports screenshots tests test_data utilities

## turn into Python packages
touch pages/__init__.py tests/__init__.py utilities/__init__.py

## sample result structure
.
├── configurations
├── logs
├── pages
│   └── __init__.py
├── README.md
├── reports
├── requirements.txt
├── screenshots
├── test_data
├── tests
│   └── __init__.py
└── utilities
    └── __init__.py

# python -m venv myenv -to create a virtual environment files
# python.exe -m pip install --upgrade pip - to upgrade pip
# pip install pandas==1.4.4  -to download specific version of the pandas.
# verison environment are usually created to avoid version mismatched.

# PS C:\Users\HP\PycharmProjects\pythonProject> python
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pandas as pd
# >>> pd.__version__ #you can see the version of the pandas
# '1.5.3'
# >>> exit()
#Enter  >>virtualenv on command prompt to see more details about virtual environment.

# we will go used vs code for that cwh_42_old python series
# 9:14
'''To create a virtual environment we have to write
"python -m venv myenv" and enter on command prompt virtual environment will be created.'''

# If virtual environment is not activated then change the execution policy by admin login in command prompt.
# write "set-executionpolicy remotesigned" on  Admin(Command prompt) & Enter your execution policy will be changed.
#  (.\myenv\Scripts\activate) or (.\myenv\Scripts\Activate.ps1) ->Enter virtual environment will be activated.
# (import pandas as pd) -> To import pandas
# pip install pandas -> to install pandas module.
# pip install pandas==1.4.4 ->to install pandas specific version.
# to check pandas version:
# first write "import pandas"
# pandas.__version___
# first write "import pandas as pd"
# then write "pd.__version__" to check pandas version.
# "deactivate"-->Enter to deactivate virtual environment.
# to activate virtual environment on command prompt write (.\myenv\Scripts\activate) or (.\myenv\Scripts\Activate.ps1) ->Enter virtual environment will be activated.
import pandas as pd
print(pd.__version__)
print("Hello world")

# Others modules
#  pip install dateutils
#  pip install lxml
# pip install openpyxl

#  (pip freeze) -->show the list of all the modules that are installed in your system or if you are in the virtual environment then  it will also show the list of all the modules that are installed in  the virtual environment.

# Those command will create the respected files and store all the python module version.
# pip freeze > requirement.txt
# pip freeze > requirement.py

# Those command will create the respected files.
# pip > requiremenert.py
# pip > requiremenert.txt

# (pip install -r requirement.txt) --> To install all the modules stored in requirement.txt in your system.
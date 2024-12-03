"""
It is a build-in module.
Shutil is a Python module that provides a higher level interface for working with file
and directories. The name "shutil" is short for shell utility.It provides a convenient and
efficient way to automate tasks that are commonly performed on files and directories.In this repl,
we'll take a closer look at the shutil module and its various functions and how they can
be used in Python
"""
# print(__doc__)
import shutil
import os
# 1 6

# shutil.copy("main.py","main2.py")
# Just copy the file

shutil.copy2("main.py","main2.py")
# copy the and also copy the meta data that a file contain i.e. when the file was made ,it's date and time etc.

# shutil.copytree("myenv","waqrul")
# It copy the whole content in the specific folder.

# shutil.move("helo/world","wordtore")
# shutil.move("helo/yellow/lora","lassan")
# shutil.move("helo/yellow","iamfile")
# shutil.move("helo/yes.py","no")
# shutil.move("helo/ia m py.py","Itispythonfile.py")
# It can move the file/folder/pythonfile/othertypeoffile from 1 place to another place.

# It is used to delete the directory
# shutil.rmtree("directory")

# It is used to delete a file and shutil can't support deletion of a file
# os.remove("myt.txt")

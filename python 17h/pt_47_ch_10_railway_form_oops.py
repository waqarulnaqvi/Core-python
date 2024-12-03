# import pandas as pd
# pd.DataFrame()#DataFrame is a class..
# # ctrl +Hower DataFrame()+ right click on mouse to know more details about DataFrame class..
#  pip install flask ->to import user defined/external modules in python..
#  pip install panda ->to import user defined/external modules in python..
#  pip install --upgrade pip ->to upgrade pip
#  pip install --upgrade panda ->to upgrade panda
#  pip install --upgrade flask ->to upgrade flask
class Railway_Form:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


harrysApplciation=Railway_Form()
harrysApplciation.name="Harry"
harrysApplciation.train="Rajdhani Express"
harrysApplciation.printData()
# jab aap external module use kar rhe hote ho.. there is a high chance aap class import kar rhe hote ho..

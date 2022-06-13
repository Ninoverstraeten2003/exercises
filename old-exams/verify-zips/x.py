
from zipfile import ZipFile

data = "C:\\Users\\Rina\\Desktop\\School\\exercises\\old-exams\\verify-zips\\data\\sub000.zip"


print(ZipFile.getinfo(data))
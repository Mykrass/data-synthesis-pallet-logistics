import zipfile
import os
import sys

#Create folder for files
!mkdir ./SalesData
!mv ./*.csv ./SalesData

#zip folder
zipname = 'synthetic_sales_data'
def zipfolder(foldername, target_dir):
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

zipfolder(zipname, '/content/')
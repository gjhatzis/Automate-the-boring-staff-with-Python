# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:08:59 2020

@author: George Chatzis
"""


# import re,os,shutil

# date_pattern = re.compile(r"""
# ^(.*?) # all text before the date
# ((0|1)?\d)- # one or two digits for the month
# ((0|1|2|3)?\d)- # one or two digits for the day
# ((19|20)\d\d) # four digits for the year
# (.*?)$ # all text after the date
# """, re.VERBOSE)

# # Loop over the files in the working directory.

# for amerFilename in os.listdir('.'):
#     mo = date_pattern.search(amerFilename)
    
# # Skip files without a date.

#     if mo == None:
#         continue
    
#     # Get the different parts of the filename.
        
#     beforePart = mo.group(1)
#     monthPart = mo.group(2)
#     dayPart = mo.group(4)
#     yearPart = mo.group(6)
#     afterPart = mo.group(8)
    
# # Form the European-style filename.

# euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# # Get the full, absolute file paths.

# absWorkingDir = os.path.abspath('.')
# amerFilename = os.path.join(absWorkingDir,amerFilename)
# euroFilename = os.path.join(absWorkingDir,euroFilename)

# # Rename the files.

# print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
# #shutil.move(amerFilename, euroFilename) #uncomment after testing


import zipfile, os

def backupToZip(folder):
    
# Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute
    
# Figure out the filename this code should use based on what files already exist.
    
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

# Create the ZIP file.

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

# Walk the entire folder tree and compress the files in each folder.

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        
    # Add the current folder to the ZIP file.
    
        backupZip.write(foldername)
    
    # Add all the files in this folder to theZIP file.
    
    for filename in filenames:
        newBase / os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip')
            continue # don't backup the backup ZIP files
    backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done.')














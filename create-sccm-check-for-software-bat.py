import subprocess
import re
from datetime import datetime

# # generate a timestamp for the file
# now = datetime.now()
# str_now = now.strftime('%H-%M-%S_%a%b%m-%Y')

# find the correct drive letter and return it
def get_removable_disk_drive_leter():
    # get a list of all drives on the computer
    result = str(subprocess.run('wmic logicaldisk get deviceid, volumename, description', capture_output=1)) 

    # create a regular expression to find the correct drive letter fot the removable drive
    removable_disk_drive_leter_regular_expression = r'(?:Removable Disk\s*)([A-Z])(?::\s*MAC-address)'

    # find the drive letter
    removable_disk_drive_leter = re.search(removable_disk_drive_leter_regular_expression, result).group(1) 
    
    return removable_disk_drive_leter 

# generate the .bat file with the correct drive letter
drive_letter = get_removable_disk_drive_leter()

with open(f'{drive_letter}:\(drive-{drive_letter})sccm-check-for-software.bat', "w") as file:
    file.write(f'powershell.exe -executionpolicy bypass -File "{drive_letter}:\\sccm-check-for-software\\sccm-check-for-software.ps1"') 


from datetime import date

import shutil

def take_bkp(src_file_name, bkp_file_name = None, 

             src_file_loc
 = '', bkp_file_loc = ''):

    #source
 file name

    src_file
 = src_file_loc+src_file_name

    

    #fetching
 today's (current day) date

    today
 = date.today()

    date_format
 = today.strftime("%d_%b_%y_")

    #modified
 name of the backup file

    if
 bkp_file_name is None:

        bkp_file_name
 = src_file_name

        bkp_file
 = bkp_file_loc+date_format+bkp_file_name

    else:

        bkp_file
 = bkp_file_loc+date_format+bkp_file_name

    #creatime
 backup copy of the source file

    shutil.copy2(src_file,
 bkp_file)

    #Success

    print("Job
 is done")

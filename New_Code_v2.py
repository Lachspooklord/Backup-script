from datetime import date
import datetime
import shutil
import backupcfg
from pathlib import Path

date_format = datetime.datetime.utcnow().strftime("%Y%m%d-%H%I%S-UTC")

def take_bkp(src_path, dst_path):

    #source file name???
    p = Path(src_path)

    #fetching today's (current day) date
    #modified name of the backup file
    backupfilepath = dst_path + p.name + '-' + date_format   

    #creatime backup copy of the source file
    try:
        shutil.copy2(src_path, backupfilepath)
        #Success
        return { "code": 0, "text": "Job is done" }

    except Exception as e:
        return { "code": 1, "text": str(e) }

def log_outcome(outcome, function_name):

    log     = open(backupcfg.logfile, 'a+')
    log.write(outcome['text'] + ', ' + function_name + ', ' + date_format + "\n")
    log.close()

    if outcome['code'] > 0:
        pass

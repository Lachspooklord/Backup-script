from New_Code import take_bkp, log_outcome
import sys
import backupcfg

if len(sys.argv) == 2:
    script, job = sys.argv

    if job in backupcfg.jobs:

        src_path = backupcfg.jobs[job]['src']
        dst_path = backupcfg.jobs[job]['dst']
        outcome = take_bkp(src_path, dst_path)
        log_outcome(outcome, 'take_bkp')
      
    else:
        print("Job is invalid.")

else:
    print("Usage: python3 backup.py <job>")

from django.test import TestCase
from datetime import datetime, timezone
from fundcare.settings import  *
import sys
# Create your tests here.
LOGPATH = BASE_DIR +  "P_LOGS"
def WriteIntoLog(f_status, f_filename, f_message):
    try:
        dt = datetime.now()
        x = dt.strftime("%Y-%m-%d %H:%M:%S")
        logmessage = str(x) + ("             ") + f_status + ("             ") + f_filename + ("             ") + f_message + "\n"
        os.chdir(LOGPATH)
        strdate = datetime.now()
        Logfile = open(str(strdate.strftime("%d-%b-%Y")) + "_OpenApiBroadcast(python).Log","a+")
        os.chdir(LOGPATH)
        Logfile.write(logmessage)
        Logfile.close()
    except:
        print('\nError in Writing Logs!!!')
        sys.exit()
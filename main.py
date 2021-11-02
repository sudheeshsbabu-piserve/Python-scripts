import time
from datetime import datetime
import random
from pathlib import Path
from SMWinservice import SMWinservice
import sys
import servicemanager

startTime = datetime.now()
startTimeStamp = startTime.timestamp()
def WriteToFile():
    DIR = 'C:\\Users\\dell\\Documents\\projects\\python\\log.txt'
    with open(DIR, 'a+') as file:
        currentTime = datetime.now()
        file.write(currentTime.strftime("%Y-%m-%d %H:%M:%S")+'\n')

class PythonCornerExample(SMWinservice):
    _svc_name_ = "AaaaTestService1"
    _svc_display_name_ = "AAAA Python Corner's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            WriteToFile()
            time.sleep(60)

if __name__ == '__main__':
    '''
    Handle command line argument count issue, otherwise it will not work for executable.
    '''
    # PythonCornerExample.parse_command_line()
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonCornerExample)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        # win32serviceutil.HandleCommandLine(RouterService)
        PythonCornerExample.parse_command_line()
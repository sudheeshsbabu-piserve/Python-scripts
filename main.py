import time
from datetime import datetime
import random
from pathlib import Path
from SMWinservice import SMWinservice

def WriteToFile():
    DIR = 'C:\\Users\\dell\\Documents\\projects\\python\\log.txt'
    with open(DIR, 'a+') as file:
        file.write(str(datetime.now()))

class PythonCornerExample(SMWinservice):
    _svc_name_ = "AaaaTestService1"
    _svc_display_name_ = "AAAA Python Corner's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            WriteToFile()
            time.sleep(5)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import logging

logging.basicConfig(filename="service.log", level=logging.DEBUG)

class ExampleService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'AAExampleService'
    _svc_display_name_ = 'AAExample Service'
    _svc_description_ = 'AAExample Service Description'

    def __init__(self, args):
        #super().__init__(args) #
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                                servicemanager.PYS_SERVICE_STARTED,
                                (self._svc_name_, ''))
        self.main()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def main(self):
        logging.info('Service Main has started')

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ExampleService)
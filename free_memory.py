import win32serviceutil
import win32service
import win32event
import servicemanager
import psutil


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "Free_memory"
    _svc_display_name_ = "Free_memory"
    _svc_description_ = "Предупреждение о свободной памяти"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.hWaitResume = win32event.CreateEvent(None, 0, 0, None)
        self.timeout = 10000  # Пауза между выполнением основного цикла службы в миллисекундах
        self.resumeTimeout = 1000
        self._paused = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STOPPED,
                              (self._svc_name_, ''))

    def SvcPause(self):
        self.ReportServiceStatus(win32service.SERVICE_PAUSE_PENDING)
        self._paused = True
        self.ReportServiceStatus(win32service.SERVICE_PAUSED)
        servicemanager.LogInfoMsg(
            "The %s service has paused." % (self._svc_name_, ))

    def SvcContinue(self):
        self.ReportServiceStatus(win32service.SERVICE_CONTINUE_PENDING)
        win32event.SetEvent(self.hWaitResume)
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        servicemanager.LogInfoMsg(
            "The %s service has resumed." % (self._svc_name_, ))

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    # В этом методе реализовываем нашу службу
    def main(self):
  
        def main():

         # Здесь выполняем необходимые действия при старте службы
            servicemanager.LogInfoMsg("Hello! I'm a free_memory service.")
            while True:
                DISK = "C:"
                free = psutil.disk_usage(DISK).free/(1024*1024*1024)
                print(f"{free:.4} Gb free on disk {DISK}")

                DISK = "D:"

                free = psutil.disk_usage(DISK).free/(1024*1024*1024)
                print(f"{free:.4} Gb free on disk {DISK}")
                while free < 135:
                    print("Места не дофига")
                break
                # Здесь должен находиться основной код сервиса
                servicemanager.LogInfoMsg("I'm still here.")

                # Проверяем не поступила ли команда завершения работы службы
                rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
                if rc == win32event.WAIT_OBJECT_0:
                    # Здесь выполняем необходимые действия при остановке службы
                    servicemanager.LogInfoMsg("Bye!")
                    break
                
            # Здесь выполняем необходимые действия при приостановке службы
            if self._paused:
                servicemanager.LogInfoMsg("I'm paused... Keep waiting...")
            # Приостановка работы службы
            while self._paused:
                # Проверям не поступила ли команда возобновления работы службы
                rc = win32event.WaitForSingleObject(self.hWaitResume, self.resumeTimeout)
                if rc == win32event.WAIT_OBJECT_0:
                    self._paused = False
                    # Здесь выполняем необходимые действия при возобновлении работы службы
                    servicemanager.LogInfoMsg("Yeah! Let's continue!")
                    break

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
